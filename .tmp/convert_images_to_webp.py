from pathlib import Path
import subprocess, sys, urllib.request
from io import BytesIO

root = Path(r'c:\Users\Usuário\referenciassdeadesivos')
images_dir = root / 'assets' / 'images'
images_dir.mkdir(parents=True, exist_ok=True)

try:
    from PIL import Image
except Exception:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    from PIL import Image

remotes = {
    'https://ibb.co/VcjqRcFT': 'mck.webp',
    'https://i.ibb.co/S4s3b4kB/mck.png': 'mck.webp',
    'https://ibb.co/9mddn4Bs': 'antes.webp',
    'https://i.ibb.co/0pzzq91h/5310db7c-0c13-4479-ba5f-e4257af11ce9.png': 'antes.webp',
    'https://ibb.co/YFnM2q7R': 'depois.webp',
    'https://i.ibb.co/Mxw4n3D2/e122db1b-1e41-4704-be9c-58a2877d0217.png': 'depois.webp',
    'https://ibb.co/1tYRMhdD': 'm20.webp',
    'https://i.ibb.co/jP93zBWc/m20.png': 'm20.webp',
    'https://ibb.co/pvNjZ2pK': 'm19.webp',
    'https://i.ibb.co/DDmfk4nM/m19.png': 'm19.webp',
    'https://ibb.co/wZPp5FNJ': 'm18.webp',
    'https://i.ibb.co/p6M4YBvW/m18.png': 'm18.webp',
    'https://ibb.co/yDZKWsg': 'm17.webp',
    'https://i.ibb.co/PRPJwC1/m17.png': 'm17.webp',
    'https://ibb.co/F4Y5b2ys': 'm16.webp',
    'https://i.ibb.co/zV2XhpB8/m16.png': 'm16.webp',
    'https://ibb.co/fdMWP163': 'm15.webp',
    'https://i.ibb.co/XxXPv20n/m15.png': 'm15.webp',
    'https://ibb.co/RTCjDp2S': 'm14.webp',
    'https://i.ibb.co/chNYrcJv/m14.png': 'm14.webp',
    'https://ibb.co/PZdPGq1W': 'm13.webp',
    'https://i.ibb.co/kgtw2NqD/m13.png': 'm13.webp',
    'https://ibb.co/JwL5Zhrx': 'm12.webp',
    'https://i.ibb.co/mVs6pxhv/m12.png': 'm12.webp',
    'https://ibb.co/Hp3Dk4N3': 'm11.webp',
    'https://i.ibb.co/DgTDSWGT/m11.png': 'm11.webp',
    'https://ibb.co/Nd5Phxrk': 'm10.webp',
    'https://i.ibb.co/KpdkZ6DQ/m10.png': 'm10.webp',
    'https://ibb.co/NvFbd2D': 'm9.webp',
    'https://i.ibb.co/J1cgwj6/m9.png': 'm9.webp',
    'https://ibb.co/4Rm5jT7p': 'm8.webp',
    'https://i.ibb.co/RTvVC09c/m8.png': 'm8.webp',
    'https://ibb.co/cK4DcBR9': 'm7.webp',
    'https://i.ibb.co/PsqwZLJy/m7.png': 'm7.webp',
    'https://ibb.co/mCwTft0G': 'm6.webp',
    'https://i.ibb.co/1f5QFKML/m6.png': 'm6.webp',
    'https://ibb.co/67zQ1rrS': 'm5.webp',
    'https://i.ibb.co/jPmtWbbY/m5.png': 'm5.webp',
    'https://ibb.co/zhxBmTKK': 'm4.webp',
    'https://i.ibb.co/nsmYwNhh/m4.png': 'm4.webp',
    'https://ibb.co/Lh6sJLzh': 'm3.webp',
    'https://i.ibb.co/JF2SyfRF/m3.png': 'm3.webp',
    'https://ibb.co/Wv9pDdpK': 'm2.webp',
    'https://i.ibb.co/8g34zR48/m2.png': 'm2.webp',
    'https://ibb.co/QvWc0spv': 'm1.webp',
    'https://i.ibb.co/b543tpQ5/m1.png': 'm1.webp',
}

for remote, file_name in remotes.items():
    if remote.startswith('https://i.ibb.co/'):
        target = images_dir / file_name
        if not target.exists():
            with urllib.request.urlopen(remote) as resp:
                data = resp.read()
            img = Image.open(BytesIO(data)).convert('RGBA')
            img.save(target, format='WEBP', quality=95)

html_path = root / 'index.html'
text = html_path.read_text(encoding='utf-8')
for remote, file_name in remotes.items():
    text = text.replace(remote, f'assets/images/{file_name}')
html_path.write_text(text, encoding='utf-8')

print(f'Converted {len(set(remotes.values()))} unique images to WebP in {images_dir}')
