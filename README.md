# OpenTelemetry em Produção · DevPira

Danrlei Souza e Ezequiel Barros

Apresentação interativa estática, pronta para GitHub Pages. Não exige instalação de dependências nem build.

## Publicar pela primeira vez

1. Crie um repositório no GitHub, por exemplo `otel-em-producao`. Para usar GitHub Pages com a conta gratuita, escolha um repositório público. Nesse caso, o código, as imagens e a apresentação ficam públicos.
2. Envie todo o conteúdo desta pasta para o repositório, incluindo `.github/workflows/pages.yml`. Não envie o ZIP como um único arquivo.
3. No repositório, abra **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Em **Actions → Publicar apresentação no GitHub Pages → Run workflow**, execute o workflow na branch `main`.
5. Quando terminar, abra o endereço mostrado no job ou em Settings → Pages. Normalmente será `https://SEU-USUARIO.github.io/otel-em-producao/`.

A pasta `.github` é oculta no Finder; Command + Shift + ponto permite vê-la. O envio por Git preserva essa pasta.

### Enviar pelo terminal

Dentro desta pasta, com Git e GitHub CLI instalados:

```sh
gh auth login -h github.com
git init -b main
git add .
git commit -m "Prepara apresentação para GitHub Pages"
gh repo create otel-em-producao --public --source=. --remote=origin --push
```

Depois faça a configuração de Pages descrita acima. Se esse nome já existir, escolha outro no comando `gh repo create`. Não inicialize outro repositório dentro de um clone existente.

## Atualizar a apresentação

Edite os arquivos dentro de `docs/` e envie as mudanças para `main`:

```sh
git add docs
git commit -m "Atualiza apresentação"
git push
```

O workflow publica automaticamente no mesmo endereço. Seu amigo precisa atualizar a página para carregar a nova versão; a sessão já aberta não recebe mudanças automaticamente. Após a publicação, se ainda aparecer a versão anterior, use Command + Shift + R ou Ctrl + Shift + R.

Este é o checkout local em `/Users/esbarros/projetos/otel-em-producao`. Para as próximas alterações neste chat, indique este repositório como fonte do projeto. Edite e versione `docs/`; não é necessário gerar um ZIP para publicar.

## Indexação

A apresentação inclui `meta robots` com `noindex, nofollow, noimageindex`. Isso orienta buscadores compatíveis a não indexarem a página. Não bloqueie o rastreamento da página em robots.txt, pois o buscador precisa ler a instrução noindex. Isso não torna o site ou o repositório privados nem impede acesso pelo link.

## Estrutura

- `docs/index.html`: estrutura e estilos.
- `docs/deck-data.js`: conteúdo das telas.
- `docs/content.js`: laboratórios e navegação.
- `docs/labs.js`: simulações.
- `docs/assets/`: imagens locais.
- `.github/workflows/pages.yml`: validação e publicação automática.
- `tools/verify.py`: verifica arquivos, imagens referenciadas e noindex.
- `tools/simulations.cjs`: testes dos quatro laboratórios e da sequência da apresentação.

## Testar localmente

```sh
python3 tools/verify.py
node tools/simulations.cjs
node --check docs/labs.js
node --check docs/content.js
node --check docs/deck-data.js
python3 -m http.server 8765 --directory docs
```

Abra `http://localhost:8765/`. As URLs dos assets são relativas, compatíveis com o caminho do repositório no GitHub Pages. Não há APIs, senhas, chaves ou backend para configurar. As simulações são didáticas e executam no navegador.

Documentação: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
