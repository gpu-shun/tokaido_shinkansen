import pygame

# Pygame の初期化
pygame.init()

# 画面サイズ設定
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("東海道新幹線 路線図")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 50, 50)

# 駅の座標データ（画面上の座標）
stations = {
    "Tokyo": (100, 300),
    "Shinagawa": (200, 300),
    "Shin-Yokohama": (300, 300),
    "Nagoya": (600, 300),
    "Kyoto": (800, 300),
    "Shin-Osaka": (900, 300)
}

# フォント設定
font = pygame.font.Font(None, 30)

# メインループ
running = True
while running:
    screen.fill(WHITE)  # 画面を白でクリア

    # 線路を描画（駅を結ぶ線）
    station_positions = list(stations.values())
    pygame.draw.lines(screen, BLACK, False, station_positions, 5)

    # 駅を描画
    for station, (x, y) in stations.items():
        pygame.draw.circle(screen, BLUE, (x, y), 10)  # 駅の丸
        text = font.render(station, True, BLACK)  # 駅名の描画
        screen.blit(text, (x - text.get_width() // 2, y + 15))

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # 画面更新

pygame.quit()
