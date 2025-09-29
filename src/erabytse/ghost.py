#!/usr/bin/env python3
"""
erabytse-ghost v0.1
An ethical companion for retiring digital accounts — not deletion, but closure.
"""

import json
import argparse
from pathlib import Path
from datetime import datetime

# Base de données publique (à étendre plus tard)
DELETION_GUIDES = {
    "github.com": {
        "url": "https://github.com/settings/admin",
        "steps": "Settings → Account → Delete account"
    },
    "twitter.com": {
        "url": "https://twitter.com/settings/deactivate",
        "steps": "Settings → Account → Deactivate"
    },
    "reddit.com": {
        "url": "https://www.reddit.com/settings",
        "steps": "User Settings → Disable account"
    },
    "facebook.com": {
        "url": "https://www.facebook.com/help/delete_account",
        "steps": "Settings → Your Facebook Information → Deactivation and deletion"
    }
}


def generate_death_certificate(email: str, services: list, output_dir: Path):
    now = datetime.now().strftime("%Y-%m-%d")
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>👻 Certificat de Décès Numérique</title>
    <style>
        body {{ font-family: serif; max-width: 600px; margin: 40px auto; line-height: 1.6; }}
        .seal {{ text-align: center; margin: 30px 0; color: #555; }}
        .service {{ margin: 8px 0; }}
    </style>
</head>
<body>
    <h1>👻 Certificat de Décès Numérique</h1>
    <div class="seal">❧</div>
    <p>Ce certificat atteste que le compte associé à l'adresse :</p>
    <p><strong>{email}</strong></p>
    <p>a été mis au repos le <strong>{now}</strong>.</p>

    <p>Services concernés :</p>
    <ul>
"""
    for svc in services:
        name = DELETION_GUIDES.get(svc, {}).get("name", svc)
        html += f'        <li class="service">{name} ({svc})</li>\n'

    html += """    </ul>

    <p>Merci pour les souvenirs. Que ta trace numérique repose en paix.</p>
    <hr>
    <p><em>Généré par <a href="https://github.com/takouzlo/erabytse-ghost">erabytse-ghost</a> — un acte de respect numérique.</em></p>
</body>
</html>"""

    cert_path = output_dir / "ghost_certificate.html"
    cert_path.write_text(html)
    return cert_path


def main():
    parser = argparse.ArgumentParser(
        description="👻 erabytse-ghost: an ethical companion for retiring digital accounts.",
        epilog="This is not deletion. This is closure with dignity."
    )
    parser.add_argument("--email", required=True, help="Email address to retire")
    parser.add_argument("--services", nargs="+", default=["github.com", "twitter.com"],
                        help="Services to include (e.g. github.com twitter.com)")
    parser.add_argument("--output", type=Path, default=Path("."), help="Output directory")

    args = parser.parse_args()

    print("👻 erabytse-ghost v0.1 — a ritual of digital closure")
    print(f"   Preparing retirement for: {args.email}\n")

    # Vérifie les services connus
    known_services = []
    unknown = []
    for svc in args.services:
        if svc in DELETION_GUIDES:
            known_services.append(svc)
        else:
            unknown.append(svc)

    if unknown:
        print(f"⚠️  Unknown services (no guide): {', '.join(unknown)}")

    print("📜 Deletion guides:")
    for svc in known_services:
        guide = DELETION_GUIDES[svc]
        print(f"   - {svc}: {guide['steps']}")
        print(f"     → {guide['url']}")

    # Génère le certificat
    cert_path = generate_death_certificate(args.email, known_services, args.output)
    print(f"\n🕊️  Certificate saved to: {cert_path}")


if __name__ == "__main__":
    main()