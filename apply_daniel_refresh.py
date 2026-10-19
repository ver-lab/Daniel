from pathlib import Path
import shutil

path = Path("index.html")
if not path.exists():
    raise SystemExit("Rulează scriptul din rădăcina repository-ului Daniel; index.html nu a fost găsit.")

html = path.read_text(encoding="utf-8")
original = html

def once(old, new, label):
    global html
    count = html.count(old)
    if count != 1:
        raise SystemExit(f"Oprire în siguranță: «{label}» apare de {count} ori. Fișierul nu a fost modificat.")
    html = html.replace(old, new, 1)

css_anchor = ".hero .actions{margin-top:20px}\n.reveal{opacity:1}\n.js .reveal{opacity:0;transform:translateY(14px);transition:opacity .7s,transform .7s}\n"
css = r''' .hero .actions{margin-top:20px}
.reveal{opacity:1}
.js .reveal{opacity:0;transform:translateY(14px);transition:opacity .7s,transform .7s}
/* Opening surprise */
body.intro-pending #welcome,body.intro-pending #invitation{display:none}
#daisy-intro{min-height:100svh;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;padding:28px 20px;background:var(--cream);text-align:center}
#daisy-intro:before,#daisy-intro:after{content:"";position:absolute;width:260px;height:260px;border:1px solid rgba(113,128,106,.16);border-radius:50%;pointer-events:none}
#daisy-intro:after{width:340px;height:340px}
.intro-inner{position:relative;z-index:1;width:min(100%,520px)}
.intro-kicker{margin:0 0 8px;letter-spacing:.18em;text-transform:uppercase;font-size:.76rem}
.intro-flower{width:min(70vw,310px);aspect-ratio:1;margin:0 auto 18px;position:relative}
.intro-center{position:absolute;left:50%;top:50%;width:28%;aspect-ratio:1;transform:translate(-50%,-50%);border-radius:50%;background:#d6b36b;border:2px solid #b8923f;box-shadow:inset 0 0 0 5px rgba(255,250,240,.24)}
.intro-petal{position:absolute;left:50%;top:50%;width:13%;height:38%;margin-left:-6.5%;margin-top:-38%;transform-origin:50% 100%;border-radius:55% 55% 48% 48%;background:#fffdf6;border:1px solid #bdb29f;box-shadow:0 2px 5px rgba(70,62,50,.08);transform:rotate(var(--angle))}
.intro-petal:nth-child(1){--angle:0deg}.intro-petal:nth-child(2){--angle:30deg}.intro-petal:nth-child(3){--angle:60deg}.intro-petal:nth-child(4){--angle:90deg}.intro-petal:nth-child(5){--angle:120deg}.intro-petal:nth-child(6){--angle:150deg}.intro-petal:nth-child(7){--angle:180deg}.intro-petal:nth-child(8){--angle:210deg}.intro-petal:nth-child(9){--angle:240deg}.intro-petal:nth-child(10){--angle:270deg}.intro-petal:nth-child(11){--angle:300deg}.intro-petal:nth-child(12){--angle:330deg}
#daisy-intro.revealing .intro-petal{animation:petal-fall .95s cubic-bezier(.45,0,.8,.5) forwards;animation-delay:calc(var(--n, 0)*.13s)}
#daisy-intro.revealing .intro-petal:nth-child(1){--n:0}#daisy-intro.revealing .intro-petal:nth-child(2){--n:1}#daisy-intro.revealing .intro-petal:nth-child(3){--n:2}#daisy-intro.revealing .intro-petal:nth-child(4){--n:3}#daisy-intro.revealing .intro-petal:nth-child(5){--n:4}#daisy-intro.revealing .intro-petal:nth-child(6){--n:5}#daisy-intro.revealing .intro-petal:nth-child(7){--n:6}#daisy-intro.revealing .intro-petal:nth-child(8){--n:7}#daisy-intro.revealing .intro-petal:nth-child(9){--n:8}#daisy-intro.revealing .intro-petal:nth-child(10){--n:9}#daisy-intro.revealing .intro-petal:nth-child(11){--n:10}#daisy-intro.revealing .intro-petal:nth-child(12){--n:11}
@keyframes petal-fall{to{opacity:0;transform:translate(var(--drift,18px),150px) rotate(calc(var(--angle) + 100deg))}}
.intro-reveal{min-height:2.8em;margin:0 auto 18px;max-width:34ch;font-family:'Alegreya',Georgia,serif;font-size:clamp(1.6rem,6vw,2.2rem);opacity:0;transform:translateY(8px);transition:opacity .6s,transform .6s}
#daisy-intro.revealing .intro-reveal{opacity:1;transform:none}
#continue-invite{display:none}
#daisy-intro.revealing #continue-invite{display:inline-block}
#daisy-intro.revealing #reveal-petals{display:none}
.weave{height:12px;background:var(--sage)}
.weave svg{display:none}
.kicker,.date,.card small,.hero .name,.hero h2,.stage h1,h3.title,.card b,.signtxt small,.signtxt b,.lead,.stage p.sub,footer{color:var(--ink)}
.place{max-width:680px;gap:18px}
.signtxt small{font-size:.78rem;letter-spacing:.1em}
.signtxt b{font-size:clamp(1.2rem,3.4vw,1.65rem);line-height:1.25}
.pgarland{display:none}
.petals i{width:13px;height:19px;background:#fffdf6;border:1px solid #b7aa94;box-shadow:0 1px 3px rgba(70,62,50,.1)}
@media(prefers-reduced-motion:reduce){#daisy-intro.revealing .intro-petal{animation:none!important;opacity:0}#daisy-intro .intro-reveal{transition:none}}
'''
css = css.lstrip()
once(css_anchor, css, "CSS insertion")

once('<main id="welcome" aria-label="Pagina de &#238;nt&#226;mpinare">',
'''<section id="daisy-intro" aria-label="Surpriză înainte de invitație"><div class="intro-inner"><p class="intro-kicker">O mică surpriză de la Daniel</p><div class="intro-flower" aria-hidden="true"><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-petal"></span><span class="intro-center"></span></div><p class="intro-reveal">Salut, sunt Daniel. Iar tu ești invitat la petrecerea mea!</p><button class="btn btn-primary" id="reveal-petals" type="button">Descoperă surpriza</button><button class="btn btn-primary" id="continue-invite" type="button">Deschide invitația</button></div></section>
<main id="welcome" aria-label="Pagina de &#238;nt&#226;mpinare">''', "intro insertion")

petal_anchor = '<i style="left:96%;animation-delay:-13.5s;animation-duration:18.8s"></i></div><img class="garland"'
extra = ''.join(f'<i style="left:{l}%;animation-delay:{d}s;animation-duration:{t}s"></i>' for l,d,t in [
(6,-5.7,15.2),(18,-8.4,19.1),(23,-1.7,13.8),(44,-12.1,17.4),(49,-6.6,20),(59,-9.2,16.7),
(71,-4.8,14.9),(78,-11.6,18.1),(91,-7.3,15.8),(14,-14.2,20.5),(68,-2.9,17),(32,-9.8,16.1)])
once(petal_anchor, '<i style="left:96%;animation-delay:-13.5s;animation-duration:18.8s"></i>'+extra+'</div><img class="garland"', "extra petals")

once('<div class="kicker">Daniel &middot; 12 iunie 2027</div>\n<h1>E&#537;ti invitat la petrecerea mea.</h1>\n<p class="sub">Un bobocel, c&#226;teva romani&#539;e &#537;i o zi frumoas&#259; &#238;n familie.</p>',
     '<h1>Salut, sunt Daniel. Iar tu ești invitat la petrecerea mea!</h1>', "page one copy")
once('<img class="pgarland" src="./ghirlanda.webp" width="900" height="259" alt="" aria-hidden="true"><img class="duck2"',
     '<img class="duck2"', "page two garland")
once('<div class="kicker">Cu drag, v&#259; invit&#259;m</div>\n<h2>Cum&#259;tria fiului nostru <span class="name">Daniel</span></h2>\n<p>Vreau s&#259; v&#259; sim&#539;i&#539;i ca acas&#259;, la o s&#259;rb&#259;toare &#238;n familie.</p>\n<div class="date">12 iunie 2027</div>\n<div class="row2"><div class="card"><small>Data</small><b>12 iunie 2027</b></div><div class="card"><small>Ora</small><b>14:00 &ndash; 22:00</b></div></div>',
     '<h2>Te invit oficial la Cum&#259;tria mea!</h2>\n<p>Abia a&#537;tept s&#259; ne cunoa&#537;tem &#537;i s&#259; s&#259;rb&#259;torim &#238;mpreun&#259; primul meu eveniment. Eu vin la pachet cu ochi&#537;ori dulci &#537;i chicoteli, iar pe voi v&#259; a&#537;tept&#259;m cu bun&#259; dispozi&#539;ie &#537;i pu&#537;i pe distrac&#539;ie!</p>\n<div class="date">12 iunie 2027</div>\n<div class="row2"><div class="card"><small>Ora de începere</small><b>13:00</b></div></div>', "page two copy")
once('<footer>Preg&#259;tit cu drag pentru o zi de neuitat.</footer>',
     '<footer>Vă așteptăm cu drag pentru o zi de neuitat. <span>(Vizitați această pagină mai aproape de eveniment pentru informații suplimentare referitoare la transport Mindrești - Trebujeni)</span></footer>', "footer")
once("'DTSTART:20270612T140000','DTEND:20270612T220000',", "'DTSTART:20270612T130000',", "calendar time")
once("var body=document.body;\nfunction route()", "var body=document.body;\nbody.classList.add('intro-pending');\nvar intro=$('daisy-intro');\n$('reveal-petals').onclick=function(){intro.classList.add('revealing')};\n$('continue-invite').onclick=function(){intro.style.display='none';body.classList.remove('intro-pending')};\nfunction route()", "intro interaction")

html = html.replace(">Trimite RSVP</button>", ">Trimite Răspuns</button>")
html = html.replace("b.textContent='Trimite RSVP';", "b.textContent='Trimite Răspuns';")

if html == original:
    raise SystemExit("Nicio modificare nu a fost aplicată.")
backup = path.with_suffix(".html.bak")
shutil.copy2(path, backup)
path.write_text(html, encoding="utf-8")
print(f"Actualizat: {path}")
print(f"Backup creat: {backup}")
print("Modificările sunt locale. Pentru publicare, verifică site-ul și apoi fă commit/push în GitHub.")
