import pygame


def get_multiple_collisions(single_rect, rect_list=[]):
    collision_list = []
    for rect in rect_list:
        if single_rect.colliderect(rect):
            collision_list.append(rect)
    return collision_list
