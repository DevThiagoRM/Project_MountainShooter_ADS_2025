import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, K_BACKSLASH, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, C_GREEN, MENU_OPTION, C_WHITE
from code.DbProxy import DbProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans TypeWriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def save(self, game_mode: str, player_score: list[int]):
        # LOAD SCORE MUSIC
        pygame.mixer.music.load('./assets/Score.mp3')
        pygame.mixer.music.play(-1)  # Param to Loop music
        db_proxy = DbProxy('DbScore')
        name = ''
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, " YOU WIN!", C_GREEN, SCORE_POS['Title'])
            text = 'Enter Player 1 name (4 characters)'
            score = player_score[0]

            if game_mode == MENU_OPTION[0]:  # SINGLE PLAYER
                score = player_score[0]

            if game_mode == MENU_OPTION[1]:  # COOPERATIVE
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team Name (4 characters):'

            if game_mode == MENU_OPTION[2]:  # COMPETITIVE
                if player_score[0] > player_score[1]:  # PLAYER 1 WIN
                    score = player_score[0]
                elif player_score[0] < player_score[1]:  # PLAYER 2 WIN
                    score = player_score[1]

            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            # CHECK FOR ALL EVENTS
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:  # QUIT GAME
                        pygame.quit()
                        sys.exit()

                    case pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and len(name) == 4:  # KEY ENTER
                            db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                            self.show()
                            return

                        elif event.key == K_BACKSPACE: # KEY BACKSPACE
                            name = name[:-1]

                        elif len(name) < 4 and event.unicode.isalnum(): # NORMAL KEY (ONLY ALPHANUMERICS)
                            name += event.unicode.upper() # CONVERT TO UPPER



            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])

            # REFRESH DISPLAY
            pygame.display.flip()

    def show(self):
        # LOAD SCORE MUSIC
        pygame.mixer.music.load('./assets/Score.mp3')
        pygame.mixer.music.play(-1)  # Param to Loop music
        # DRAW IMAGES
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(50, "TOP 10 SCORE", C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE                     DATE      ', C_YELLOW, SCORE_POS['Label'])
        db_proxy = DbProxy('DbScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'   {name}        {score :05d}               {date}', C_YELLOW,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            # Check for all events
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    case pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            return

            # REFRESH DISPLAY
            pygame.display.flip()


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f'{current_time} - {current_date}'
