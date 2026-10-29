#!/usr/bin/env python3
"""Generate the lab's sample books: two EPUBs and a small comic series in CBZ.

All text is written for this lab. All art is drawn with PIL.
Everything lands in ./library next to this script.
"""
import io
import os
import zipfile

from PIL import Image, ImageDraw

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library")

PARAS = [
    "The garden behind the workshop had not been watered in nineteen years, "
    "and yet it bloomed. Mara found the first gear on a Tuesday, turning "
    "slowly in the soil where the beans should have been, ticking like a "
    "small patient heart.",
    "She dug with her fingers. Under the bean rows lay a shallow brass "
    "tray, and in the tray a hundred gears, each one turning the next, all "
    "of them fed by nothing she could see. At the centre of the tray a "
    "single flower opened and closed with the rhythm of a clock.",
    "By Friday the whole street knew. Neighbours leaned on the fence and "
    "offered theories the way neighbours do, generously and at length. "
    "Mara listened to all of them, thanked every one, and kept her own "
    "theory folded small in her apron pocket, next to the seed packets.",
]

PARAS2 = [
    "The boats were folded from old tide tables, which is why they always "
    "knew the way out of the harbour. Tomas made one every morning before "
    "the bakery opened, set it on the water, and watched it choose a "
    "direction the way other people read the weather.",
    "On the last morning of August, the boat came back. It had been gone "
    "eleven days, which was ten days longer than paper should last, and in "
    "its fold, dry as a pressed leaf, lay a stamp from a country that had "
    "never existed on any map Tomas owned.",
]


def make_epub(path, title, author, language, chapter_title, paras, ident):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    chapters = []
    body_template = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml"><head><title>%s</title></head>'
        "<body><h1>%s</h1>%s</body></html>"
    )
    # Split paragraphs across two chapters for a real table of contents.
    half = (len(paras) + 1) // 2
    groups = [paras[:half], paras[half:]] if len(paras) > 1 else [paras]
    manifest_items = []
    spine_items = []
    nav_points = []
    for i, group in enumerate(groups, start=1):
        ctitle = f"{chapter_title} {i}" if len(groups) > 1 else chapter_title
        paras_html = "".join(f"<p>{p}</p>" for p in group)
        chapters.append((f"chapter{i}.xhtml", body_template % (ctitle, ctitle, paras_html)))
        manifest_items.append(f'<item id="ch{i}" href="chapter{i}.xhtml" media-type="application/xhtml+xml"/>')
        spine_items.append(f'<itemref idref="ch{i}"/>')
        nav_points.append(
            f'<navPoint id="nav{i}" playOrder="{i}"><navLabel><text>{ctitle}</text></navLabel>'
            f'<content src="chapter{i}.xhtml"/></navPoint>'
        )
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="2.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:identifier id="BookId">{ident}</dc:identifier>
    <dc:title>{title}</dc:title>
    <dc:creator opf:role="aut">{author}</dc:creator>
    <dc:language>{language}</dc:language>
    <dc:description>A short book written for a reading-server lab.</dc:description>
    <meta name="cover" content="cover"/>
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="cover" href="cover.jpg" media-type="image/jpeg"/>
    {''.join(manifest_items)}
  </manifest>
  <spine toc="ncx">{''.join(spine_items)}</spine>
</package>
'''
    ncx = f'''<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head><meta name="dtb:uid" content="{ident}"/></head>
  <docTitle><text>{title}</text></docTitle>
  <navMap>{''.join(nav_points)}</navMap>
</ncx>
'''
    container = '''<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
'''
    cover = Image.new("RGB", (600, 900), (43, 84, 120))
    d = ImageDraw.Draw(cover)
    d.rectangle([40, 40, 560, 860], outline=(240, 230, 200), width=4)
    d.text((70, 380), title, fill=(255, 250, 230))
    d.text((70, 420), "by " + author, fill=(220, 220, 220))
    buf = io.BytesIO()
    cover.save(buf, "JPEG")

    with zipfile.ZipFile(path, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip",
                   compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/toc.ncx", ncx, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/cover.jpg", buf.getvalue(), compress_type=zipfile.ZIP_DEFLATED)
        for name, content in chapters:
            z.writestr(f"OEBPS/{name}", content, compress_type=zipfile.ZIP_DEFLATED)
    print("wrote", path, os.path.getsize(path), "bytes")


def make_page(number, label, hue):
    img = Image.new("RGB", (800, 1200), hue)
    d = ImageDraw.Draw(img)
    d.rectangle([30, 30, 770, 1170], outline=(255, 255, 255), width=5)
    d.rectangle([80, 120, 720, 500], outline=(255, 240, 200), width=3)
    d.ellipse([300, 200, 500, 400], outline=(255, 240, 200), width=3)
    d.text((90, 560), label, fill=(255, 255, 255))
    d.text((90, 600), f"Page {number}", fill=(255, 255, 255))
    d.text((90, 1050), "Drawn in the lab. No ferry was harmed.", fill=(230, 230, 230))
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return buf.getvalue()


COMICINFO = '''<?xml version="1.0" encoding="utf-8"?>
<ComicInfo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Title>Moon Post Office</Title>
  <Series>Moon Post Office</Series>
  <Number>1</Number>
  <Writer>Lab Author</Writer>
  <Summary>A one-shot about a post office that delivers letters to the moon, written and drawn for a reading-server lab.</Summary>
  <PageCount>4</PageCount>
</ComicInfo>
'''


def make_cbz(path, label, hue, pages=4, comicinfo=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for i in range(1, pages + 1):
            z.writestr(f"{i:03d}.png", make_page(i, label, hue))
        if comicinfo:
            z.writestr("ComicInfo.xml", comicinfo)
    print("wrote", path, os.path.getsize(path), "bytes")


def main():
    books = os.path.join(BASE, "Books")
    comics = os.path.join(BASE, "Comics")
    make_epub(
        os.path.join(books, "The Clockwork Garden", "The Clockwork Garden.epub"),
        "The Clockwork Garden", "Lab Author", "en", "Chapter", PARAS,
        "urn:lab:clockwork-garden",
    )
    make_epub(
        os.path.join(books, "Sea of Paper Boats", "Sea of Paper Boats.epub"),
        "Sea of Paper Boats", "Lab Author", "en", "Part", PARAS2,
        "urn:lab:sea-of-paper-boats",
    )
    ferry = os.path.join(comics, "Starlight Ferry")
    make_cbz(os.path.join(ferry, "Starlight Ferry v01.cbz"),
             "Starlight Ferry - Volume 1", (30, 60, 110))
    make_cbz(os.path.join(ferry, "Starlight Ferry v02.cbz"),
             "Starlight Ferry - Volume 2", (90, 40, 90))
    make_cbz(os.path.join(comics, "Moon Post Office", "Moon Post Office.cbz"),
             "Moon Post Office", (20, 90, 70), comicinfo=COMICINFO)


if __name__ == "__main__":
    main()
