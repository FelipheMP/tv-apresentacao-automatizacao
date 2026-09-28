from datetime import time

# Horário de funcionamento da automação
START_TIME = time(7, 0)
END_TIME = time(17, 0)

# Segunda a sexta
OPERATING_WEEKDAYS = {0, 1, 2, 3, 4}

# Permite ignorar horário e dia útil durante testes.
TEST_MODE = False

# Tempo, em segundos, que cada slide ficará visível na TV
SLIDE_DURATION = 15

# Quantidade de slides do PowerPoint que possuem dashboards do Power BI embutidas.
SLIDES_DYNAMIC_POWERBI_PAGES = 2

# Tempo de exibição de cada página do Power BI
POWERBI_PAGE_DURATION = 45

# Tempo inicial para você colocar o PowerPoint em foco
# antes da automação começar
START_DELAY = 5

# Power BI - coordenadas da interface

# Posição neutra para esconder o cursor visualmente.
# Pode ser um canto da tela onde não atrapalhe o dashboard.
MOUSE_PARK_POSITION = (1919, 1079)

# Menu usado para abrir opções de exibição
POWERBI_VIEW_MENU = (1824, 209)

# Opção "Tela inteira"
POWERBI_FULLSCREEN_OPTION = (1822, 267)

# Menu inferior usado para trocar de página
POWERBI_PAGE_MENU = (354, 1133)

# Página "Prioridades"
POWERBI_PAGE_PRIORIDADES = (301, 1021)

# Página "A vencer em 3 dias"
POWERBI_PAGE_A_VENCER = (295, 1062)

# Tempo entre interações com a interface
POWERBI_UI_DELAY = 0.8

# Intervalo entre recarregamentos do Power BI.
# 75 minutos = 4500 segundos.
POWERBI_REFRESH_INTERVAL = 75 * 60

# Tempo de espera após Ctrl + R para o relatório carregar.
POWERBI_REFRESH_WAIT = 10