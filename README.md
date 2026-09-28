# Automação de Apresentação para TV

Projeto em Python para automatizar a exibição contínua de uma apresentação do PowerPoint e páginas de um relatório do Power BI em uma tela dedicada.

A aplicação alterna entre o PowerPoint Desktop e o Power BI aberto no Microsoft Edge, controlando a navegação entre slides, páginas do relatório, modo de tela cheia, atualização periódica e recuperação básica de falhas.

## Objetivo

O objetivo do projeto é manter uma tela exibindo continuamente:

- uma apresentação em PowerPoint;
- diferentes páginas de um relatório do Power BI.

A automação foi pensada para cenários em que uma apresentação e dashboards precisam permanecer visíveis durante o dia sem intervenção manual constante.

## Funcionamento

O ciclo principal funciona da seguinte forma:

```text
PowerPoint
    ↓
Exibe todos os slides
    ↓
Power BI
    ↓
Atualiza a página quando necessário
    ↓
Entra em tela cheia
    ↓
Dashboard 1
    ↓
Dashboard 2
    ↓
Sai da tela cheia
    ↓
Volta ao primeiro slide do PowerPoint
    ↓
Repete
```

A quantidade de slides do PowerPoint é identificada automaticamente pela aplicação.

## Horário de funcionamento

A aplicação foi projetada para permanecer em execução continuamente.

Por padrão, os ciclos automáticos são executados:

```text
Segunda a sexta-feira
07:00 às 17:00
```

Fora desse período, a aplicação permanece ativa em modo de espera e não executa novos ciclos de apresentação.

Exemplo de comportamento:

```text
17:00
→ conclui o ciclo atual
→ entra em espera

Durante a noite
→ permanece em execução
→ verifica periodicamente o horário

07:00 do próximo dia útil
→ retoma automaticamente os ciclos
```

Esse comportamento é especialmente útil em computadores que permanecem ligados continuamente.

As configurações de horário e dias permitidos podem ser alteradas em `config.py`.

Exemplo:

```python
START_TIME = time(7, 0)
END_TIME = time(17, 0)

OPERATING_WEEKDAYS = {0, 1, 2, 3, 4}
```

## Modo de teste

Durante o desenvolvimento é possível ignorar temporariamente as restrições de horário e dias permitidos.

Em `config.py`:

```python
TEST_MODE = True
```

Para uso normal:

```python
TEST_MODE = False
```

Quando o modo de teste está ativo, a automação pode executar ciclos independentemente do horário ou dia da semana.

## Atualização do Power BI

A atualização visual do relatório é realizada através do navegador utilizando:

```text
Ctrl + R
```

Esse procedimento recarrega a página do Power BI para buscar os dados mais recentes disponíveis no serviço.

A atualização da fonte de dados ocorre de forma independente desta aplicação.

O intervalo de recarregamento pode ser configurado em `config.py`.

Exemplo:

```python
POWERBI_REFRESH_INTERVAL = 75 * 60
```

O refresh só é executado quando necessário, evitando recarregamentos excessivos da página.

## Tecnologias utilizadas

- Python 3
- Microsoft PowerPoint Desktop
- Microsoft Power BI
- Microsoft Edge
- PyAutoGUI
- pywin32
- psutil
- Pillow
- Git

## Estrutura do projeto

```text
tv-apresentacao-automatizacao/
│
├── main.py
├── config.py
├── powerpoint.py
├── powerbi.py
├── browser.py
├── window_utils.py
├── schedule.py
├── logger.py
├── mouse_position.py
│
├── start_tv_dashboard.bat
├── start_tv_dashboard_debug.bat
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Arquivos principais

### `main.py`

Ponto de entrada da aplicação.

Responsável por:

- iniciar os controladores;
- executar os ciclos;
- verificar o horário de funcionamento;
- manter a aplicação em espera fora do horário;
- controlar falhas consecutivas;
- executar procedimentos básicos de recuperação.

### `config.py`

Centraliza as principais configurações da aplicação, como:

- tempo de exibição dos slides;
- tempo de exibição das páginas do Power BI;
- intervalo de atualização;
- horário de funcionamento;
- dias da semana;
- coordenadas utilizadas pelo PyAutoGUI;
- tempos de espera;
- modo de teste.

### `powerpoint.py`

Responsável pelo controle do PowerPoint Desktop.

Utiliza a automação COM do Microsoft Office para:

- identificar uma apresentação em execução;
- obter a quantidade de slides;
- avançar e voltar slides;
- retornar ao primeiro slide;
- interagir com o modo de apresentação.

### `powerbi.py`

Responsável pela automação da interface do Power BI.

Controla:

- ativação do navegador;
- entrada e saída do modo tela cheia;
- navegação entre páginas do relatório;
- atualização através de `Ctrl + R`;
- interações com a interface utilizando PyAutoGUI.

### `browser.py`

Responsável por localizar e ativar a janela do Microsoft Edge.

### `window_utils.py`

Contém funções auxiliares para manipulação de janelas no Windows.

Utiliza APIs Win32 para trazer corretamente o PowerPoint ou o Edge para o primeiro plano.

### `schedule.py`

Responsável pelas regras de funcionamento da automação.

Controla:

- dias permitidos;
- horário inicial;
- horário final;
- modo de teste;
- espera até o próximo período de funcionamento.

### `logger.py`

Configura o sistema de logs.

Os registros são exibidos no terminal e também podem ser armazenados localmente em:

```text
logs/tv_dashboard.log
```

### `mouse_position.py`

Ferramenta auxiliar utilizada para descobrir coordenadas de elementos da interface.

Exemplo:

```powershell
python mouse_position.py
```

Posicione o cursor sobre o elemento desejado e anote as coordenadas apresentadas.

## Instalação

Clone o repositório:

```powershell
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```powershell
cd tv-apresentacao-automatizacao
```

Crie o ambiente virtual:

```powershell
py -m venv .venv
```

Ative:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## Dependências

As principais dependências utilizadas são:

```text
pyautogui
psutil
pillow
pywin32
```

As versões utilizadas podem ser consultadas em `requirements.txt`.

## Preparação antes da execução

Antes de iniciar a automação:

1. Abra o Microsoft PowerPoint Desktop.
2. Abra a apresentação desejada.
3. Inicie o modo apresentação.
4. Abra o Microsoft Edge.
5. Acesse o relatório desejado no Power BI.
6. Certifique-se de que a sessão esteja autenticada.
7. Mantenha PowerPoint e Edge abertos.
8. Inicie a automação.

## Execução manual

Com o ambiente virtual ativo:

```powershell
python main.py
```

Também é possível utilizar:

```text
start_tv_dashboard.bat
```

Esse arquivo:

- entra automaticamente na pasta do projeto;
- ativa o ambiente virtual;
- inicia a aplicação.

Como o processo permanece ativo fora do horário de funcionamento, não é necessário reiniciar a aplicação diariamente.

## Execução em modo de depuração

Para execução manual mantendo o terminal aberto após o encerramento:

```text
start_tv_dashboard_debug.bat
```

Esse modo é útil para testes e diagnóstico de erros.

## Inicialização automática

A aplicação pode ser iniciada manualmente através de:

```text
start_tv_dashboard.bat
```

Como o processo permanece ativo fora do horário de funcionamento, uma única execução pode permanecer ativa continuamente enquanto o computador estiver ligado e a sessão do usuário permanecer aberta.

Opcionalmente, em ambientes onde o computador pode reiniciar ou ocorrer logoff, pode ser configurada uma inicialização automática junto com a sessão do usuário do Windows.

Uma possibilidade é utilizar a pasta de inicialização do usuário:

```text
shell:startup
```

Essa configuração é opcional e não faz parte da aplicação em si.

## Configuração das coordenadas

Parte da automação do Power BI depende de coordenadas fixas da interface.

Essas coordenadas ficam centralizadas em `config.py`.

Exemplo:

```python
POWERBI_VIEW_MENU = (x, y)
POWERBI_FULLSCREEN_OPTION = (x, y)

POWERBI_PAGE_MENU = (x, y)
POWERBI_PAGE_1 = (x, y)
POWERBI_PAGE_2 = (x, y)
```

Para descobrir as coordenadas:

```powershell
python mouse_position.py
```

As coordenadas podem precisar de ajustes caso ocorram mudanças em:

- resolução da tela;
- escala do Windows;
- zoom do navegador;
- layout do Power BI;
- posição dos elementos da interface.

## Controle do cursor

Após concluir uma interação com a interface, o cursor pode ser movido para uma posição discreta da tela para não permanecer sobre o conteúdo exibido.

Essa posição pode ser configurada em `config.py`.

## Logs

Os logs podem ser armazenados em:

```text
logs/tv_dashboard.log
```

Exemplo:

```text
2026-09-28 07:00:01 | INFO | Automação iniciada.
2026-09-28 07:00:02 | INFO | Iniciando ciclo.
2026-09-28 07:03:15 | INFO | Abrindo Power BI.
2026-09-28 07:05:04 | INFO | Ciclo concluído com sucesso.
```

A pasta `logs/` deve permanecer fora do controle de versão.

Exemplo de `.gitignore`:

```gitignore
logs/
*.log
```

## Recuperação de erros

A aplicação possui uma estratégia básica de recuperação.

Caso ocorra uma falha durante um ciclo:

1. o erro é registrado no log;
2. a aplicação tenta retornar a um estado conhecido;
3. tenta reposicionar o PowerPoint no primeiro slide;
4. aguarda alguns segundos;
5. inicia uma nova tentativa.

Existe também um limite configurável de falhas consecutivas.

Exemplo:

```python
MAX_CONSECUTIVE_ERRORS = 3
```

Ao atingir o limite, a aplicação é encerrada para evitar um loop infinito de erros.

## Watchdog

Antes de iniciar um ciclo, a aplicação pode verificar se:

- o PowerPoint está aberto;
- existe uma apresentação em modo Slide Show;
- o Microsoft Edge está aberto.

Caso algum desses componentes não esteja disponível, a execução do ciclo é interrompida e o mecanismo de recuperação é acionado.

## Git e desenvolvimento

O projeto utiliza branches por funcionalidade.

Exemplos:

```text
feat/powerbi-fullscreen
feat/powerbi-refresh
feat/operating-hours
feat/presentation-cycle
feat/logging-and-recovery
feat/watchdog
feat/persistent-schedule
```

Exemplo de fluxo:

```powershell
git switch -c feat/nova-funcionalidade
```

Após o desenvolvimento:

```powershell
git add .
git commit -m "feat: add nova funcionalidade"

git switch main
git merge feat/nova-funcionalidade
```

## Padrão de commits

O projeto segue um padrão simples inspirado em Conventional Commits.

```text
feat: nova funcionalidade
fix: correção de problema
refactor: reorganização do código
docs: alterações de documentação
chore: manutenção e configuração
test: testes
```

Exemplos:

```text
feat: add Power BI fullscreen navigation
feat: add periodic Power BI refresh
feat: add complete presentation cycle
fix: improve PowerPoint window focus
docs: update project README
```

## Boas práticas de segurança

Antes de publicar o repositório, verifique se não existem:

- URLs internas;
- IDs de relatórios, workspaces ou tenants;
- credenciais;
- tokens ou chaves de API;
- endereços de e-mail corporativos;
- nomes de pessoas;
- nomes de fornecedores;
- caminhos de rede;
- arquivos de log;
- dados ou capturas de tela de ambientes internos.

Arquivos com configurações específicas do ambiente podem ser mantidos fora do Git através do `.gitignore`.

## Limitações atuais

A automação do Power BI utiliza coordenadas fixas do PyAutoGUI.

Isso significa que alterações na interface podem exigir atualização manual das coordenadas.

A aplicação também depende de:

- sessão autenticada no Power BI;
- PowerPoint aberto;
- apresentação em modo Slide Show;
- Edge aberto;
- resolução e escala da tela permanecendo estáveis;
- sessão do usuário do Windows permanecendo ativa.

## Observações

O projeto foi desenvolvido para um computador dedicado à exibição contínua de apresentações e dashboards.

Algumas decisões priorizam simplicidade e previsibilidade, como o uso de coordenadas fixas para controlar elementos da interface do Power BI.

A automação não modifica o arquivo PowerPoint adicionando intervalos automáticos aos slides. A troca de slides é controlada pelo Python, permitindo que a mesma apresentação continue sendo utilizada normalmente em apresentações manuais.

Fora do horário configurado, a aplicação permanece em espera em vez de encerrar, permitindo que o funcionamento seja retomado automaticamente no próximo período válido.
