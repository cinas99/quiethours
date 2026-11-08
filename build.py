#!/usr/bin/env python3
"""Builds the Quiet Hours Studio site (plain HTML for GitHub Pages).

Edit CONFIG and APPS below, then run:  python3 build.py
"""
import html
import pathlib

CONFIG = {
    "studio": "Quiet Hours Apps",
    "owner": "SOFTWARE DEVELOPER MARCIN KONIECZNY",
    "person": "Marcin Konieczny",
    "country_en": "Poland",
    "country_pl": "Polska",
    "email": "quiethours.apps@gmail.com",
    "address": "",  # optional, e.g. "ul. Przykładowa 1, 00-000 Miasto"
    "updated_en": "3 November 2026",
    "updated_pl": "3 listopada 2026",
}

APPS = [
    {
        "id": "snoozlet",
        "name": "Snoozlet",
        "tag_en": "Calming sounds for baby sleep",
        "tag_pl": "Spokojne dźwięki do usypiania dziecka",
        "desc_en": "White noise, shushing, heartbeat and lullabies with a gentle sleep timer. Works offline.",
        "desc_pl": "Biały szum, szum suszarki, bicie serca i kołysanki z łagodnym wyłącznikiem czasowym. Działa bez internetu.",
        "local_en": "your sound mixes, volume levels, timer and theme settings, language, and an optional sound file you choose yourself (for example a recording of your voice)",
        "local_pl": "twoje mieszanki dźwięków, poziomy głośności, ustawienia wyłącznika czasowego i motywu, język oraz opcjonalny plik dźwiękowy wybrany przez ciebie (np. nagranie twojego głosu)",
        "audience_en": "Snoozlet is meant for parents and caregivers. It is not directed at children and we do not knowingly collect data from children.",
        "audience_pl": "Snoozlet jest przeznaczony dla rodziców i opiekunów. Nie jest skierowany do dzieci i świadomie nie zbieramy danych od dzieci.",
    },
    {
        "id": "deepnook",
        "name": "Deepnook",
        "tag_en": "Focus sounds & Pomodoro timer",
        "tag_pl": "Dźwięki do nauki i timer Pomodoro",
        "desc_en": "Rain, café, brown noise, binaural beats and a Pomodoro timer for studying and deep work.",
        "desc_pl": "Deszcz, kawiarnia, szum brązowy, dudnienia binauralne i timer Pomodoro do nauki i pracy w skupieniu.",
        "local_en": "your sound mixes, timer mode, daily goal, focus history and streaks, the task names you type in, language and theme settings",
        "local_pl": "twoje mieszanki dźwięków, tryb timera, cel dzienny, historia sesji i serie dni, wpisywane nazwy zadań, język i motyw",
        "audience_en": "Deepnook is meant for users aged 13 and older. We do not knowingly collect data from children.",
        "audience_pl": "Deepnook jest przeznaczony dla użytkowników w wieku 13+. Świadomie nie zbieramy danych od dzieci.",
    },
]

CSS = """
:root{--bg:#0f1530;--bg2:#171f42;--card:#1c2550;--txt:#eef0ff;--muted:#a3abd6;--accent:#ffd27a;--mint:#7fe0c3;--line:#2c376a}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--txt);background:radial-gradient(ellipse at 50% -20%,#2b2f6b 0%,var(--bg) 60%) fixed}
a{color:var(--accent)}a:hover{opacity:.85}
.wrap{max-width:860px;margin:0 auto;padding:28px 20px 60px}
nav{display:flex;align-items:center;gap:12px;margin-bottom:40px}
nav .brand{display:flex;align-items:center;gap:10px;color:var(--txt);text-decoration:none;font-weight:800;font-size:18px}
nav .sp{flex:1}nav .lang{color:var(--muted);text-decoration:none;font-size:14px;border:1px solid var(--line);border-radius:99px;padding:4px 12px}
h1{font-size:40px;line-height:1.15;margin:0 0 12px;letter-spacing:-.5px}
h2{font-size:24px;margin:40px 0 12px}h3{font-size:18px;margin:28px 0 6px}
.lead{color:var(--muted);font-size:19px;max-width:620px;margin:0}
.apps{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:20px}
.app{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:20px;display:flex;flex-direction:column;gap:10px}
.app .top{display:flex;gap:14px;align-items:center}
.app img{width:64px;height:64px;border-radius:16px}
.app h3{margin:0;font-size:20px}.app .tag{color:var(--muted);font-size:14px;margin:0}
.app p{margin:0}.app .links{display:flex;gap:14px;flex-wrap:wrap;font-size:14px;margin-top:auto;padding-top:6px}
.badge{display:inline-block;font-size:12px;font-weight:700;color:#0f1530;background:var(--mint);border-radius:99px;padding:2px 10px}
.box{background:var(--bg2);border:1px solid var(--line);border-radius:16px;padding:18px 20px}
.legal{max-width:720px}.legal li{margin:4px 0}.legal p,.legal li{color:#dfe3ff}
.muted{color:var(--muted)}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:14px}
footer a{color:var(--muted)}
"""

LOGO = ('<svg width="30" height="30" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="16" fill="#2b2f6b"/>'
        '<path d="M38 14a18 18 0 1 0 12 30A15 15 0 0 1 38 14z" fill="#ffd27a"/>'
        '<path d="M14 52q6-4 12 0t12 0t12 0" fill="none" stroke="#8fa6ff" stroke-width="3.5" stroke-linecap="round"/></svg>')

e = html.escape


def page(title, body, lang, alt_href, alt_label, root=""):
    c = CONFIG
    contact = f'<a href="mailto:{e(c["email"])}">{e(c["email"])}</a>'
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(c['studio'])} – calm, simple apps for sleep and focus.">
<link rel="icon" href="{root}assets/favicon.png"><link rel="stylesheet" href="{root}style.css"></head>
<body><div class="wrap">
<nav><a class="brand" href="{root}{'index.html' if lang=='en' else 'pl.html'}">{LOGO}{e(c['studio'])}</a><span class="sp"></span><a class="lang" href="{alt_href}">{alt_label}</a></nav>
{body}
<footer>© 2026 {e(c['studio'])} · {e(c['owner'])} · {e(c['country_en'] if lang=='en' else c['country_pl'])} · {contact}</footer>
</div></body></html>
"""


def home(lang):
    en = lang == "en"
    cards = []
    for a in APPS:
        priv = f"privacy/{a['id']}.html" + ("" if en else "#pl")
        cards.append(f"""<div class="app"><div class="top"><img src="assets/{a['id']}.png" alt="">
<div><h3>{a['name']}</h3><p class="tag">{e(a['tag_en'] if en else a['tag_pl'])}</p></div></div>
<p>{e(a['desc_en'] if en else a['desc_pl'])}</p>
<div><span class="badge">{'Coming soon to Google Play' if en else 'Wkrótce w Google Play'}</span></div>
<div class="links"><a href="{priv}">{'Privacy policy' if en else 'Polityka prywatności'}</a></div></div>""")
    c = CONFIG
    if en:
        body = f"""<h1>Calm, simple apps<br>for sleep and focus.</h1>
<p class="lead">{e(c['studio'])} makes small, quiet apps that do one thing well. No accounts, no ads, no clutter.</p>
<h2>Our apps</h2><div class="apps">{''.join(cards)}</div>
<h2>About</h2><div class="box"><p style="margin:0">{e(c['studio'])} is an independent app studio run by {e(c['person'])} ({e(c['owner'])}), {e(c['country_en'])}. Questions, feedback or support: <a href="mailto:{e(c['email'])}">{e(c['email'])}</a>.</p></div>"""
        return page(c["studio"], body, "en", "pl.html", "Polski")
    body = f"""<h1>Proste, spokojne aplikacje<br>do snu i skupienia.</h1>
<p class="lead">{e(c['studio'])} tworzy małe, ciche aplikacje, które robią jedną rzecz dobrze. Bez kont, bez reklam, bez rozpraszaczy.</p>
<h2>Nasze aplikacje</h2><div class="apps">{''.join(cards)}</div>
<h2>O nas</h2><div class="box"><p style="margin:0">{e(c['studio'])} to niezależne studio aplikacji prowadzone przez {e(c['person'])} ({e(c['owner'])}), {e(c['country_pl'])}. Pytania, opinie i pomoc: <a href="mailto:{e(c['email'])}">{e(c['email'])}</a>.</p></div>"""
    return page(c["studio"] + " – aplikacje do snu i skupienia", body, "pl", "index.html", "English")


def privacy(a):
    c = CONFIG
    mail = f'<a href="mailto:{e(c["email"])}">{e(c["email"])}</a>'
    addr = f", {e(c['address'])}" if c["address"] else ""
    n = a["name"]
    en = f"""<section class="legal" id="en">
<h1>{n} – Privacy Policy</h1><p class="muted">Last updated: {c['updated_en']} · <a href="#pl">Polska wersja</a></p>
<div class="box"><b>In short:</b> {n} works without an account. Your settings stay on your device. We do not sell data and we show no ads. Optional analytics and crash reports are used only if you agree.</div>
<h3>1. Who is responsible</h3>
<p>The data controller is {e(c['person'])}, running the business {e(c['owner'])}{addr}, {e(c['country_en'])}, publishing as {e(c['studio'])}. Contact: {mail}.</p>
<h3>2. Data kept only on your device</h3>
<p>{n} stores {e(a['local_en'])}. This data stays on your device, is never sent to us and is deleted when you uninstall the app or use “Reset” in the app.</p>
<h3>3. Purchases and subscriptions</h3>
<p>Payments are processed by Google Play. We never see your card or payment details. To check whether your subscription is active we use RevenueCat, which receives an anonymous app user ID, purchase receipts from Google Play and basic device information (model, OS version, app version, country). Legal basis: performance of the contract (Art. 6(1)(b) GDPR). <a href="https://www.revenuecat.com/privacy">RevenueCat privacy policy</a>.</p>
<h3>4. Analytics and crash reports (only with your consent)</h3>
<p>If you agree when the app asks, we use Google Firebase Analytics and Firebase Crashlytics to understand which features are used and to fix crashes. They receive usage events (for example “sound started”, “subscription screen shown”), device model, OS and app version, language, approximate country, a random app instance ID and crash details. We never collect your name, e-mail, contacts, location or recordings. You can withdraw consent at any time in the app settings. Legal basis: consent (Art. 6(1)(a) GDPR). <a href="https://firebase.google.com/support/privacy">Firebase privacy information</a>.</p>
<h3>5. Device permissions</h3>
<ul><li><b>Notifications</b> – to show playback controls while sounds play with the screen off.</li>
<li><b>Foreground service and wake lock</b> – to keep sounds playing in the background.</li>
<li>The app does <b>not</b> use the microphone, camera, location or contacts.</li></ul>
<h3>6. Children</h3><p>{e(a['audience_en'])}</p>
<h3>7. Retention</h3><p>Data on your device: until you uninstall the app or reset it. Analytics data: up to 14 months. Crash reports: up to 90 days. Subscription records: as long as required by tax and accounting law.</p>
<h3>8. Transfers outside the EEA</h3><p>Google and RevenueCat may process data in the United States. Such transfers rely on the EU–US Data Privacy Framework or Standard Contractual Clauses.</p>
<h3>9. Your rights</h3><p>Under the GDPR you may request access to, correction or deletion of your data, restriction of processing, data portability, and object to processing. Write to {mail}. You also have the right to lodge a complaint with the Polish supervisory authority (Prezes Urzędu Ochrony Danych Osobowych, uodo.gov.pl) or the authority in your country.</p>
<h3>10. Changes</h3><p>If this policy changes we will update it on this page and change the date above.</p>
</section>"""
    pl = f"""<section class="legal" id="pl" style="margin-top:64px">
<h1>{n} – Polityka prywatności</h1><p class="muted">Ostatnia aktualizacja: {c['updated_pl']} · <a href="#en">English version</a></p>
<div class="box"><b>W skrócie:</b> {n} działa bez zakładania konta. Twoje ustawienia zostają na twoim telefonie. Nie sprzedajemy danych i nie wyświetlamy reklam. Opcjonalną analitykę i raporty błędów włączamy tylko za twoją zgodą.</div>
<h3>1. Kto jest administratorem</h3>
<p>Administratorem danych jest {e(c['person'])}, prowadzący działalność gospodarczą {e(c['owner'])}{addr}, {e(c['country_pl'])}, publikujący aplikacje jako {e(c['studio'])}. Kontakt: {mail}.</p>
<h3>2. Dane zapisywane tylko na twoim urządzeniu</h3>
<p>{n} zapisuje {e(a['local_pl'])}. Te dane zostają na twoim urządzeniu, nie są do nas wysyłane i znikają po odinstalowaniu aplikacji albo użyciu opcji „Resetuj”.</p>
<h3>3. Zakupy i subskrypcje</h3>
<p>Płatności obsługuje Google Play. Nie widzimy danych twojej karty ani płatności. Do sprawdzania, czy subskrypcja jest aktywna, używamy usługi RevenueCat, która otrzymuje anonimowy identyfikator użytkownika aplikacji, potwierdzenia zakupów z Google Play i podstawowe dane urządzenia (model, wersja systemu i aplikacji, kraj). Podstawa prawna: wykonanie umowy (art. 6 ust. 1 lit. b RODO). <a href="https://www.revenuecat.com/privacy">Polityka prywatności RevenueCat</a>.</p>
<h3>4. Analityka i raporty błędów (tylko za zgodą)</h3>
<p>Jeśli wyrazisz zgodę, gdy aplikacja o nią zapyta, używamy Google Firebase Analytics i Firebase Crashlytics, żeby wiedzieć, z których funkcji korzystają użytkownicy, i naprawiać awarie. Usługi te otrzymują zdarzenia z aplikacji (np. „włączono dźwięk”, „pokazano ekran subskrypcji”), model urządzenia, wersję systemu i aplikacji, język, przybliżony kraj, losowy identyfikator instalacji i szczegóły awarii. Nie zbieramy imienia, e-maila, kontaktów, lokalizacji ani nagrań. Zgodę możesz w każdej chwili wycofać w ustawieniach aplikacji. Podstawa prawna: zgoda (art. 6 ust. 1 lit. a RODO). <a href="https://firebase.google.com/support/privacy">Informacje o prywatności Firebase</a>.</p>
<h3>5. Uprawnienia</h3>
<ul><li><b>Powiadomienia</b> – żeby pokazać sterowanie odtwarzaniem, gdy dźwięki grają przy zgaszonym ekranie.</li>
<li><b>Usługa na pierwszym planie i blokada uśpienia</b> – żeby dźwięki grały w tle.</li>
<li>Aplikacja <b>nie</b> używa mikrofonu, aparatu, lokalizacji ani kontaktów.</li></ul>
<h3>6. Dzieci</h3><p>{e(a['audience_pl'])}</p>
<h3>7. Jak długo przechowujemy dane</h3><p>Dane na urządzeniu: do odinstalowania lub zresetowania aplikacji. Dane analityczne: do 14 miesięcy. Raporty błędów: do 90 dni. Dane o subskrypcjach: tak długo, jak wymagają tego przepisy podatkowe i rachunkowe.</p>
<h3>8. Przekazywanie danych poza EOG</h3><p>Google i RevenueCat mogą przetwarzać dane w Stanach Zjednoczonych. Podstawą takiego przekazania są ramy ochrony danych UE–USA (Data Privacy Framework) lub standardowe klauzule umowne.</p>
<h3>9. Twoje prawa</h3><p>Zgodnie z RODO masz prawo dostępu do danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przenoszenia oraz sprzeciwu. Napisz na {mail}. Masz też prawo złożyć skargę do Prezesa Urzędu Ochrony Danych Osobowych (uodo.gov.pl).</p>
<h3>10. Zmiany</h3><p>Jeśli polityka się zmieni, zaktualizujemy ją na tej stronie i zmienimy datę powyżej.</p>
</section>"""
    return page(f"{n} – Privacy Policy", en + pl, "en", "#pl", "Polski", root="../")


def main():
    out = pathlib.Path(__file__).parent
    (out / "style.css").write_text(CSS.strip() + "\n")
    (out / "index.html").write_text(home("en"))
    (out / "pl.html").write_text(home("pl"))
    (out / "privacy").mkdir(exist_ok=True)
    for a in APPS:
        (out / "privacy" / f"{a['id']}.html").write_text(privacy(a))
    (out / ".nojekyll").write_text("")
    print("built:", ", ".join(["index.html", "pl.html"] + [f"privacy/{a['id']}.html" for a in APPS]))


if __name__ == "__main__":
    main()
