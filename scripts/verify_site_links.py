"""Check local links and media in the rendered site, including raw HTML attributes.

Run after mkdocs build. Network URLs remain covered by the source Lychee check.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from mkdocs.config import load_config


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for name, value in attrs
                         if name in {"href", "src", "poster"} and value)


def main():
    config = load_config()
    root = Path(config.site_dir).resolve()
    prefix = urlsplit(config.site_url).path
    errors = []
    count = 0
    pages = list(root.rglob("*.html"))
    if not pages:
        raise SystemExit("No built HTML found; run mkdocs build first")
    for page in pages:
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        for value in parser.urls:
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            path = unquote(url.path)
            if path.startswith("/"):
                if not path.startswith(prefix):
                    errors.append(f"{page.relative_to(root)}: outside site prefix: {value}")
                    continue
                target = root / path[len(prefix):]
            else:
                target = page.parent / path
            target = target.resolve()
            if target.is_dir():
                target /= "index.html"
            count += 1
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f"{page.relative_to(root)}: missing local target: {value}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {count} local references across {len(pages)} built pages")


if __name__ == "__main__":
    main()
