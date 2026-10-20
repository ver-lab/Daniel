(function () {
  'use strict';
  var current = 'ro';
  try { current = localStorage.getItem('daniel-language') === 'en' ? 'en' : 'ro'; } catch (e) {}
  var translations = {
    en: {
      welcomeTitle: "Hi, I'm Daniel. You're invited to my celebration!",
      open: "Let's celebrate!",
      inviteTitle: "You're warmly invited to my celebration!",
      paragraph1: "I can't wait to meet you! I'll bring sweet little eyes and giggles, and I'm looking forward to smiles, good cheer, and lovely conversations with you.",
      paragraph2: "My parents have told me stories about the old days: no tablets, but lively yards and plenty of mischief. I'd love for you to share a story from your childhood and take me, for a day, into the world of those memories.",
      paragraph3: "Together with my mommy and daddy, I'm looking forward to good music, delicious food, and a joyful celebration!",
      date: "Date", time: "Starting time", calendar: "Add to calendar", rsvpLink: "RSVP",
      location: "Location", rsvpTitle: "Will you celebrate with me?",
      first: "First name *", last: "Last name *", yes: "I'll be there", no: "I can't attend",
      adults: "Adults", children: "Children", note: "Note (optional)",
      placeholder: "Allergies, a message, a wish…", send: "Send RSVP",
      thanks: "Thank you for your reply!", again: "Send another reply",
      footer: "We look forward to sharing an unforgettable day with you.",
      mapLabel: "Open Casa din luncă, Trebujeni in Google Maps",
      required: "Please enter your first and last name.",
      offline: "The form isn't connected yet. Sorry — please try again later.",
      adultRequired: "Please select at least one adult.",
      sending: "Sending…",
      saveError: "We couldn't save your reply. Please try again.",
      connectionError: "We couldn't save your reply. Please check your connection.",
      welcomeAria: "Welcome page"
    },
    ro: {
      welcomeTitle: "Salut, sunt Daniel. Iar tu ești invitat la petrecerea mea!",
      open: "Hai să sărbătorim!",
      inviteTitle: "Te invit cu drag la cumătria mea!",
      paragraph1: "Abia aștept să ne cunoaștem! Eu vin cu ochișori dulci și chicoteli, iar pe voi vă aștept cu zâmbete, voie bună și chef de taifas.",
      paragraph2: "Părinții mi-au povestit despre vremurile voastre de altădată: fără tablete, dar cu ogrăzi pline de viață și năzbâtii cât cuprinde. Mi-ar plăcea să-mi dăruiți câte o poveste din copilăria voastră și să mă luați, pentru o zi, în lumea acelor amintiri.",
      paragraph3: "Împreună cu mami și tati, vă aștept cu muzică bună, bucate gustoase și o petrecere plină de veselie!",
      date: "Data", time: "Ora începerii", calendar: "Adaugă în calendar", rsvpLink: "Confirmă participarea",
      location: "Locația", rsvpTitle: "Veți fi alături de mine?",
      first: "Prenume *", last: "Nume *", yes: "Particip", no: "Nu pot participa",
      adults: "Adulți", children: "Copii", note: "Notă (opțional)",
      placeholder: "Alergii, un mesaj, o dorință...", send: "Trimite Răspuns",
      thanks: "Mulțumim pentru răspuns!", again: "Trimite alt răspuns",
      footer: "Vă așteptăm cu drag pentru o zi de neuitat.",
      mapLabel: "Deschide locația Casa din luncă, Trebujeni în Google Maps",
      required: "Te rugăm să completezi prenumele și numele.",
      offline: "Formularul nu este conectat încă. Ne pare rău, încearcă mai târziu.",
      adultRequired: "Alege cel puțin un adult.",
      sending: "Se trimite...",
      saveError: "Nu am putut salva răspunsul. Te rugăm să încerci din nou.",
      connectionError: "Nu am putut salva răspunsul. Verifică conexiunea.",
      welcomeAria: "Pagina de întâmpinare"
    }
  };
  function setText(el, value) { if (el) el.textContent = value; }
  function apply(lang) {
    current = lang === 'en' ? 'en' : 'ro';
    var t = translations[current];
    document.documentElement.lang = current;
    var title = document.querySelector('#welcome h1');
    setText(title, t.welcomeTitle);
    setText(document.getElementById('open'), t.open);
    setText(document.querySelector('#invitation .hero h2'), t.inviteTitle);
    var ps = document.querySelectorAll('#invitation .hero p.invitation-copy');
    setText(ps[0], t.paragraph1); setText(ps[1], t.paragraph2); setText(ps[2], t.paragraph3);
    var cards = document.querySelectorAll('#invitation .row2 .card small');
    setText(cards[0], t.date); setText(cards[1], t.time);
    setText(document.getElementById('ics'), t.calendar);
    setText(document.querySelector('#invitation .actions a[href="#rsvp"]'), t.rsvpLink);
    setText(document.querySelector('.signtxt small'), t.location);
    var map = document.querySelector('.map-link'); if (map) map.setAttribute('aria-label', t.mapLabel);
    setText(document.querySelector('#rsvp .title'), t.rsvpTitle);
    var labels = document.querySelectorAll('#rsvp label.f');
    if (labels[0]) labels[0].childNodes[0].textContent = t.first;
    if (labels[1]) labels[1].childNodes[0].textContent = t.last;
    if (labels[2]) labels[2].childNodes[0].textContent = t.adults;
    if (labels[3]) labels[3].childNodes[0].textContent = t.children;
    if (labels[4]) { labels[4].childNodes[0].textContent = t.note; var ta = labels[4].querySelector('textarea'); if (ta) ta.placeholder = t.placeholder; }
    var choices = document.querySelectorAll('#rsvp .choice');
    if (choices[0]) choices[0].lastChild.textContent = ' ' + t.yes;
    if (choices[1]) choices[1].lastChild.textContent = ' ' + t.no;
    setText(document.getElementById('send'), t.send);
    setText(document.querySelector('#done h3'), t.thanks);
    setText(document.getElementById('again'), t.again);
    setText(document.querySelector('footer'), t.footer);
    var welcome = document.getElementById('welcome'); if (welcome) welcome.setAttribute('aria-label', t.welcomeAria);
    var toggle = document.getElementById('languageToggle');
    if (toggle) {
      toggle.setAttribute('aria-label', current === 'ro' ? 'Switch language to English' : 'Schimbă limba în română');
      toggle.innerHTML = current === 'ro' ? '<span aria-current="true">RO</span><span class="lang-sep">|</span><span>EN</span>' : '<span>RO</span><span class="lang-sep">|</span><span aria-current="true">EN</span>';
    }
    try { localStorage.setItem('daniel-language', current); } catch (e) {}
  }
  function addToggle() {
    if (document.getElementById('languageToggle')) return;
    var style = document.createElement('style');
    style.textContent = '#languageToggle{position:fixed;z-index:1000;top:14px;right:14px;display:flex;align-items:center;gap:7px;padding:7px 10px;border:1px solid rgba(99,116,92,.35);border-radius:20px;background:rgba(255,250,240,.92);color:#63745c;font:500 12px/1 "Work Sans",system-ui,sans-serif;letter-spacing:.04em;cursor:pointer;box-shadow:0 2px 8px rgba(70,62,50,.06);backdrop-filter:blur(6px)}#languageToggle span[aria-current="true"]{font-weight:700;color:#51483e}#languageToggle .lang-sep{opacity:.45}#languageToggle:focus-visible{outline:2px solid #87977d;outline-offset:3px}@media(max-width:420px){#languageToggle{top:10px;right:10px;padding:7px 9px}}';
    document.head.appendChild(style);
    var button = document.createElement('button');
    button.id = 'languageToggle'; button.type = 'button';
    button.addEventListener('click', function () { apply(current === 'ro' ? 'en' : 'ro'); });
    document.body.appendChild(button);
    apply(current);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', addToggle);
  else addToggle();
  window.DanielLanguage = { apply: apply, getLanguage: function () { return current; }, translations: translations };
})();