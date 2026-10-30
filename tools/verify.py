from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]/'docs'
for name in ['index.html','deck-data.js','content.js','labs.js','.nojekyll']:
    assert (root/name).is_file(), f'Arquivo ausente: {name}'
for file in root.glob('*'):
    if file.suffix in ['.html','.js']:
        for asset in re.findall(r"assets/[A-Za-z0-9_.-]+",file.read_text()):
            assert (root/asset).is_file(), f'Asset ausente: {asset}'
assert '<script src="labs.js"></script>' in (root/'index.html').read_text()
assert '<meta name="robots" content="noindex, nofollow, noimageindex">' in (root/'index.html').read_text()
print('PASS · página, scripts e imagens locais prontos para GitHub Pages')
