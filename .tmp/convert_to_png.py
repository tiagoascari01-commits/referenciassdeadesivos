from pathlib import Path
from PIL import Image

root = Path(r'c:\Users\Usuário\referenciassdeadesivos')
count = 0
for p in list(root.rglob('*.webp')):
    try:
        img = Image.open(p)
        png = p.with_suffix('.png')
        img.save(png, format='PNG')
        print(f'converted {p.name} -> {png.name}')
        count += 1
    except Exception as e:
        print(f'ERROR {p}: {e}')
print(f'TOTAL {count}')
