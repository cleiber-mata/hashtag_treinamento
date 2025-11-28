<!-- Arquivo gerado pelo agente. Atualize com feedback do mantenedor. -->
# Instruções para agentes AI (Copilot / GPT)

Resumo rápido
- **Tipo de repositório**: exercícios/treinamentos em Python com notebooks e scripts pequenos.
- **Principais locais**: scripts em `preco_fase1/`, notebooks em `projeto_hashtag/`.

O que você precisa saber para ser produtivo
- **Arquitetura / Escopo**: não é um serviço ou pacote; são exercícios isolados. Alterações normalmente são:
  - corrigir/exemplificar código em `*.py` (ex.: `preco_fase1/lista_preco.py`);
  - atualizar ou fornecer versões explicadas de notebooks em `projeto_hashtag/`.
- **Fluxo de dados**: entradas e saídas são frequentemente impressões no console ou células de notebook (nenhum DB/serviço externo detectado).

Padrões e convenções do projeto
- **Código simples e imperativo**: scripts usam variáveis globais e `print()` para saída (veja `preco_fase1/lista_preco.py`).
- **Notebooks como fonte principal de conteúdo pedagógico**: não altere notebooks sem explicitar o objetivo — prefira criar uma versão derivada.
- **Sem dependências declaradas**: não há `requirements.txt`, `pyproject.toml` ou `setup.py` no repositório; trate o ambiente como Python padrão (>=3.8 recomendado).

Comandos úteis (PowerShell / Windows)
- Rodar um script simples:
  - `python .\preco_fase1\lista_preco.py`
- Abrir notebooks:
  - Use o VS Code (extensão Jupyter) ou `jupyter notebook` no diretório do repositório.

Como editar/contribuir como agente AI
- **Alterações em `.py`**: aplique mudanças pequenas e seguras — refatoramentos que mantêm a saída atual são preferíveis.
- **Alterações em notebooks**: gerar uma cópia com sufixo `-editado.ipynb` e documentar alterações na primeira célula; ofereça também uma versão `.py` exportada quando fizer transformações significativas.
- **Mensagens de commit / PR**: explique claramente a intenção pedagógica (ex.: "Melhora de legibilidade em `preco_fase1/lista_preco.py` — transforma loop para list comprehensions e adiciona asserts").

Exemplos concretos do repositório
- `preco_fase1/lista_preco.py`: uso de listas, laços `for` e `print()` para demonstrar cálculos de reajuste — ao modificar, mantenha as mensagens de saída semelhantes para preservação de exercícios.
- Notebooks: `projeto_hashtag/Arquivo Inicial - Aula 1.ipynb` e `Gabarito - Aula 1.ipynb` são materiais de aula — trate o conteúdo como referência de ensino.

Checagens rápidas que o agente deve fazer antes de propor mudanças
- Verifique se há arquivos de teste (nenhum detectado); se não houver, prefira mudanças que não requeiram infra de CI.
- Procure por `README.md` na raiz para contexto de projeto (resumo curto detectado).

Quando pedir orientação ao humano
- Se a modificação envolver reescrever notebooks, pergunte se prefere uma versão anotada, uma conversão para `.py`, ou um PR com a explicação pedagógica.

Feedback
- Se algo importante estiver faltando aqui, me diga quais áreas você quer que eu detalhe (ex.: dependências, formato de commits, fluxo de revisão).

-- Fim --
