from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]/'docs'
for name in ['index.html','deck-data.js','content.js','labs.js','.nojekyll']:
    assert (root/name).is_file(), f'Arquivo ausente: {name}'
for file in root.glob('*'):
    if file.suffix in ['.html','.js']:
        for asset in re.findall(r"assets/[A-Za-z0-9_.-]+",file.read_text()):
            assert (root/asset).is_file(), f'Asset ausente: {asset}'
assert re.search(r'<script src="labs\.js(?:\?[^"]*)?"></script>', (root/'index.html').read_text())
assert '<meta name="robots" content="noindex, nofollow, noimageindex">' in (root/'index.html').read_text()
print('PASS · página, scripts e imagens locais prontos para GitHub Pages')

import json
source=(root/'deck-data.js').read_text()
data=json.loads(source[source.index('['):].rstrip().rstrip(';'))
by_source={slide['source']:slide for slide in data}
for number,text in {3:'alta cilindrada',12:'indústria',21:'Qual é o componente principal',36:'cabem na memória disponível?',39:'não dá vazão',42:'do que há disponível',45:'distribuída uniformemente'}.items():
    assert text in by_source[number]['body'], (number,text)
assert '8% no GOMEMLIMIT' not in (root/'content.js').read_text()
assert 'A retenção é de 35% em todos os cenários.' in (root/'content.js').read_text()
print('PASS · correções de português e hipóteses de memória conferidas')
