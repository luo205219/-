import subprocess
import sys

import pygame

# 初始化pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 672
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("台球游戏")

# 颜色定义
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)

# 加载背景图
background = pygame.image.load("images/table.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# 按钮类
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("Microsoft YaHei", 40)  # 修改字体

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=10)

        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# 创建按钮
button_width = 200
button_height = 80
button_y = SCREEN_HEIGHT // 2 - button_height // 2

single_player_btn = Button(
    SCREEN_WIDTH // 2 - button_width - 20,
    button_y,
    button_width,
    button_height,
    "单人模式",
    GRAY,
    LIGHT_GRAY,
)

multi_player_btn = Button(
    SCREEN_WIDTH // 2 + 20,
    button_y,
    button_width,
    button_height,
    "双人模式",
    GRAY,
    LIGHT_GRAY,
)


# 主循环
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if single_player_btn.is_clicked(event.pos):
                    subprocess.Popen(["python", "game1.py"])
                    running = False
                elif multi_player_btn.is_clicked(event.pos):
                    subprocess.Popen(["python", "game2.py"])
                    running = False

        # 绘制界面
        screen.blit(background, (0, 0))
        single_player_btn.draw(screen)
        multi_player_btn.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
