from pathlib import Path
from PIL import Image

root = Path(r'c:\Users\Usuário\referenciassdeadesivos')
img_dir = root / 'assets' / 'images'
img_dir.mkdir(parents=True, exist_ok=True)

colors = {
    'mck.webp': (255, 93, 43, 255),
    'antes.webp': (210, 60, 60, 255),
    'depois.webp': (32, 152, 74, 255),
}
for i in range(20, 0, -1):
    colors[f'm{i}.webp'] = (28, 42, 46, 255)

for name, color in colors.items():
    img = Image.new('RGBA', (1, 1), color)
    img.save(img_dir / name, format='WEBP', quality=95)
    print(f'created {name}')
