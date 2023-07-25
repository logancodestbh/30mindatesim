import pygame

pygame.init()
window_width = 1152
window_height = 648
window = pygame.display.set_mode((window_width, window_height))

WHITE = (255, 255, 255)

background_image = pygame.image.load("home.png")
school_image = pygame.image.load("school.png")
school2_image = pygame.image.load("school2.png")
homeroom_image = pygame.image.load("homeroom.png")
classmate_image = pygame.image.load("classmate.png")
classmate2_image = pygame.image.load("classmate2.png")
end_image = pygame.image.load("end.png")
you_lose_image = pygame.image.load("you_lose.png")

font = pygame.font.Font(None, 36)

play_button_rect = pygame.Rect(window_width // 2 - 100, window_height // 2, 200, 50)
quit_button_rect = pygame.Rect(window_width // 2 - 100, window_height // 2 + 70, 200, 50)
pick_up_button_rect = pygame.Rect(window_width // 2 + 50, window_height // 2, 200, 50)
do_nothing_button_rect = pygame.Rect(window_width // 2 - 250, window_height // 2, 200, 50)

def draw_main_screen():
    window.blit(background_image, (0, 0))

    pygame.draw.rect(window, WHITE, play_button_rect)
    pygame.draw.rect(window, WHITE, quit_button_rect)

    play_text = font.render("Play", True, (0, 0, 0))
    quit_text = font.render("Quit", True, (0, 0, 0))

    play_text_rect = play_text.get_rect(center=play_button_rect.center)
    quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)

    window.blit(play_text, play_text_rect)
    window.blit(quit_text, quit_text_rect)

    pygame.display.flip()

def draw_continue_text():
    continue_text = font.render("Click to Continue", True, (255, 255, 255))
    continue_text_rect = continue_text.get_rect(bottomright=(window_width - 10, window_height - 10))
    window.blit(continue_text, continue_text_rect)

def draw_mom_text(game_state):
    if game_state == "school1":
        mom_text = "You walk out from your house, and your mom says goodbye."
        mom_text_surface = font.render(mom_text, True, (0, 0, 0))
        mom_text_rect = mom_text_surface.get_rect(midbottom=(window_width // 2, window_height - 30))
        pygame.draw.rect(window, WHITE, (mom_text_rect.left - 10, mom_text_rect.top - 5, mom_text_rect.width + 20, mom_text_rect.height + 10))
        window.blit(mom_text_surface, mom_text_rect)

def draw_classmate_text():
    classmate_text = "She looks at you and gets flustered when you notice."
    classmate_text_surface = font.render(classmate_text, True, (0, 0, 0))
    classmate_text_rect = classmate_text_surface.get_rect(midbottom=(window_width // 2, window_height - 30))
    pygame.draw.rect(window, WHITE, (classmate_text_rect.left - 10, classmate_text_rect.top - 5, classmate_text_rect.width + 20, classmate_text_rect.height + 10))
    window.blit(classmate_text_surface, classmate_text_rect)

def draw_classmate2_text():
    classmate2_text = "She drops her eraser. What do you do?"
    classmate2_text_surface = font.render(classmate2_text, True, (0, 0, 0))
    classmate2_text_rect = classmate2_text_surface.get_rect(midbottom=(window_width // 2, window_height - 30))
    pygame.draw.rect(window, WHITE, (classmate2_text_rect.left - 10, classmate2_text_rect.top - 5, classmate2_text_rect.width + 20, classmate2_text_rect.height + 10))
    window.blit(classmate2_text_surface, classmate2_text_rect)

    pygame.draw.rect(window, WHITE, pick_up_button_rect)
    pygame.draw.rect(window, WHITE, do_nothing_button_rect)

    pick_up_text = font.render("Pick up", True, (0, 0, 0))
    do_nothing_text = font.render("Do nothing", True, (0, 0, 0))

    pick_up_text_rect = pick_up_text.get_rect(center=pick_up_button_rect.center)
    do_nothing_text_rect = do_nothing_text.get_rect(center=do_nothing_button_rect.center)

    window.blit(pick_up_text, pick_up_text_rect)
    window.blit(do_nothing_text, do_nothing_text_rect)

def main():
    global play_button_rect, quit_button_rect
    game_state = "main_screen"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if game_state == "main_screen":
                    if play_button_rect.collidepoint(mouse_pos):
                        game_state = "school1"
                elif game_state == "school1":
                    game_state = "school2"
                elif game_state == "school2":
                    game_state = "homeroom"
                elif game_state == "homeroom":
                    game_state = "classmate"
                elif game_state == "classmate":
                    game_state = "classmate2"
                elif game_state == "classmate2":
                    if pick_up_button_rect.collidepoint(mouse_pos):
                        game_state = "end"
                    elif do_nothing_button_rect.collidepoint(mouse_pos):
                        game_state = "you_lose"

        if game_state == "main_screen":
            draw_main_screen()
        elif game_state == "school1":
            window.blit(school_image, (0, 0))
            draw_mom_text(game_state)
            draw_continue_text()
        elif game_state == "school2":
            window.blit(school2_image, (0, 0))
            draw_continue_text()
        elif game_state == "homeroom":
            window.blit(homeroom_image, (0, 0))
            draw_continue_text()
        elif game_state == "classmate":
            window.blit(classmate_image, (0, 0))
            draw_classmate_text()
            draw_continue_text()
        elif game_state == "classmate2":
            window.blit(classmate2_image, (0, 0))
            draw_classmate2_text()
            draw_continue_text()
        elif game_state == "you_lose":
            window.blit(you_lose_image, (0, 0))
            draw_continue_text()
        elif game_state == "end":
            window.blit(end_image, (0, 0))
            draw_continue_text()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
