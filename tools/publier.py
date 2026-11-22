"""Publie le prochain post VITRIZ en attente (a-publier/) sur la Page Facebook et la page LinkedIn VITRIZ.

Lancé par GitHub Actions. Pour chaque créneau : prend le plus ancien a-publier/<AAAA-MM-JJ>-<rubrique>.json
dont la date est aujourd'hui ou passée et dont le .html existe, rend l'image JPEG 1080x1350,
déplace les fichiers dans publiees/, pousse, puis appelle le webhook Make avec l'URL de l'image.
"""
import datetime as dt, glob, json, os, subprocess, sys, time, urllib.request
from zoneinfo import ZoneInfo

REPO = os.environ.get("GITHUB_REPOSITORY", "Minerve04/vitriz-social")
HOOK = os.environ["VITRIZ_WEBHOOK_URL"]
TOKEN = os.environ["VITRIZ_WEBHOOK_TOKEN"]
today = dt.datetime.now(ZoneInfo("Europe/Paris")).date().isoformat()


def sh(*a):
    print("+", " ".join(a)); subprocess.run(a, check=True)


cands = []
for j in sorted(glob.glob("a-publier/*.json")):
    slug = os.path.basename(j)[:-5]
    if slug[:10] <= today and os.path.exists(f"a-publier/{slug}.html"):
        cands.append(slug)
if not cands:
    print("Rien à publier aujourd'hui."); sys.exit(0)
slug = cands[0]
post = json.load(open(f"a-publier/{slug}.json", encoding="utf-8"))
for k in ("titre", "alt", "post_fb", "post_li"):
    assert post.get(k, "").strip(), f"champ manquant : {k}"
for ch in "()[]{}<>_*~|":
    assert ch not in post["post_li"], f"caractère interdit dans post_li : {ch}"

# Rendu
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.goto("file://" + os.path.abspath(f"a-publier/{slug}.html"))
    pg.wait_for_timeout(800)
    sz = pg.evaluate("[document.documentElement.scrollWidth, document.documentElement.scrollHeight]")
    assert sz[0] <= 1080 and sz[1] <= 1350, f"débordement {sz}"
    pg.screenshot(path=f"publiees/{slug}.jpg", type="jpeg", quality=90, clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
    b.close()

sh("git", "mv", f"a-publier/{slug}.json", f"publiees/{slug}.json")
sh("git", "mv", f"a-publier/{slug}.html", f"publiees/{slug}.html")
sh("git", "add", f"publiees/{slug}.jpg")
sh("git", "commit", "-m", f"Publication {slug}")
sh("git", "push")

img = f"https://raw.githubusercontent.com/{REPO}/main/publiees/{slug}.jpg"
for _ in range(30):
    try:
        if urllib.request.urlopen(img, timeout=20).status == 200:
            break
    except Exception:
        pass
    time.sleep(10)

payload = dict(token=TOKEN, titre=post["titre"], alt=post["alt"], post_fb=post["post_fb"], post_li=post["post_li"],
               image_url=img, fichier=f"{slug}.jpg")
req = urllib.request.Request(HOOK, data=json.dumps(payload).encode("utf-8"),
                             headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
res = urllib.request.urlopen(req, timeout=300).read().decode("utf-8", "replace")
print("Réponse Make :", res)
json.dump({"publie_le": dt.datetime.now(ZoneInfo("Europe/Paris")).isoformat(timespec="minutes"), "reponse": res},
          open(f"publiees/{slug}.resultat.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
sh("git", "add", f"publiees/{slug}.resultat.json")
sh("git", "commit", "-m", f"Résultat {slug}")
sh("git", "push")
if "ERREUR" in res or '"facebook":""' in res or '"linkedin":""' in res:
    print("::error::Publication incomplète : " + res); sys.exit(1)
