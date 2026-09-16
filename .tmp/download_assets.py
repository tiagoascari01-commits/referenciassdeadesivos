from pathlib import Path
import urllib.request

root = Path(r'c:\Users\Usuário\referenciassdeadesivos')
img_dir = root / 'assets' / 'images'
img_dir.mkdir(parents=True, exist_ok=True)

pairs = [
    ('https://i.ibb.co/bgMQCRMz/c3392ff669d25e03bb12-hero-mockup-cricut.webp', 'hero-mockup-cricut.webp'),
    ('https://i.ibb.co/jP93zBWc/m20.png', 'm20.png'),
    ('https://i.ibb.co/DDmfk4nM/m19.png', 'm19.png'),
    ('https://i.ibb.co/p6M4YBvW/m18.png', 'm18.png'),
    ('https://i.ibb.co/PRPJwC1/m17.png', 'm17.png'),
    ('https://i.ibb.co/zV2XhpB8/m16.png', 'm16.png'),
    ('https://i.ibb.co/XxXPv20n/m15.png', 'm15.png'),
    ('https://i.ibb.co/chNYrcJv/m14.png', 'm14.png'),
    ('https://i.ibb.co/kgtw2NqD/m13.png', 'm13.png'),
    ('https://i.ibb.co/mVs6pxhv/m12.png', 'm12.png'),
    ('https://i.ibb.co/DgTDSWGT/m11.png', 'm11.png'),
    ('https://i.ibb.co/KpdkZ6DQ/m10.png', 'm10.png'),
    ('https://i.ibb.co/J1cgwj6/m9.png', 'm9.png'),
    ('https://i.ibb.co/RTvVC09c/m8.png', 'm8.png'),
    ('https://i.ibb.co/PsqwZLJy/m7.png', 'm7.png'),
    ('https://i.ibb.co/1f5QFKML/m6.png', 'm6.png'),
    ('https://i.ibb.co/jPmtWbbY/m5.png', 'm5.png'),
    ('https://i.ibb.co/nsmYwNhh/m4.png', 'm4.png'),
    ('https://i.ibb.co/JF2SyfRF/m3.png', 'm3.png'),
    ('https://i.ibb.co/8g34zR48/m2.png', 'm2.png'),
    ('https://i.ibb.co/b543tpQ5/m1.png', 'm1.png'),
]

for url, name in pairs:
    target = img_dir / name
    if not target.exists():
        urllib.request.urlretrieve(url, str(target))

html_path = root / 'index.html'
text = html_path.read_text(encoding='utf-8')
for url, name in pairs:
    text = text.replace(url, f'assets/images/{name}')
for page_url, name in [
    ('https://ibb.co/HDfBbpfn', 'hero-mockup-cricut.webp'),
    ('https://ibb.co/1tYRMhdD', 'm20.png'),
    ('https://ibb.co/pvNjZ2pK', 'm19.png'),
    ('https://ibb.co/wZPp5FNJ', 'm18.png'),
    ('https://ibb.co/yDZKWsg', 'm17.png'),
    ('https://ibb.co/F4Y5b2ys', 'm16.png'),
    ('https://ibb.co/fdMWP163', 'm15.png'),
    ('https://ibb.co/RTCjDp2S', 'm14.png'),
    ('https://ibb.co/PZdPGq1W', 'm13.png'),
    ('https://ibb.co/JwL5Zhrx', 'm12.png'),
    ('https://ibb.co/Hp3Dk4N3', 'm11.png'),
    ('https://ibb.co/Nd5Phxrk', 'm10.png'),
    ('https://ibb.co/NvFbd2D', 'm9.png'),
    ('https://ibb.co/4Rm5jT7p', 'm8.png'),
    ('https://ibb.co/cK4DcBR9', 'm7.png'),
    ('https://ibb.co/mCwTft0G', 'm6.png'),
    ('https://ibb.co/67zQ1rrS', 'm5.png'),
    ('https://ibb.co/zhxBmTKK', 'm4.png'),
    ('https://ibb.co/Lh6sJLzh', 'm3.png'),
    ('https://ibb.co/Wv9pDdpK', 'm2.png'),
    ('https://ibb.co/QvWc0spv', 'm1.png'),
]:
    text = text.replace(page_url, f'assets/images/{name}')
html_path.write_text(text, encoding='utf-8')
print(f'Downloaded {len(pairs)} files to {img_dir}')
