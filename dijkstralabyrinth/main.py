import pygame
import sys
import heapq
import time
import random
from colorama import init


secenek = 1
if secenek == 1:
    dosya = open("matrix.txt", "r", encoding="utf-8")
    oku = dosya.read()
    oku = oku.split('\n')
    for x in range(len(oku)):
        oku[x] = list(oku[x])
elif secenek == 2:
    def surroundingCells(rand_wall):
        s_cells = 0
        if (oku[rand_wall[0] - 1][rand_wall[1]] == '0'):
            s_cells += 1
        if (oku[rand_wall[0] + 1][rand_wall[1]] == '0'):
            s_cells += 1
        if (oku[rand_wall[0]][rand_wall[1] - 1] == '0'):
            s_cells += 1
        if (oku[rand_wall[0]][rand_wall[1] + 1] == '0'):
            s_cells += 1
        return s_cells

    wall = '1'
    cell = '0'
    unvisited = '2'
    height = 15
    width = 15
    
    oku = []

    init()

    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        oku.append(line)

    starting_height = int(random.random() * height)
    starting_width = int(random.random() * width)
    if (starting_height == 0):
        starting_height += 1
    if (starting_height == height - 1):
        starting_height -= 1
    if (starting_width == 0):
        starting_width += 1
    if (starting_width == width - 1):
        starting_width -= 1

    oku[starting_height][starting_width] = cell
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    oku[starting_height - 1][starting_width] = '1'
    oku[starting_height][starting_width - 1] = '1'
    oku[starting_height][starting_width + 1] = '1'
    oku[starting_height + 1][starting_width] = '1'

    while (walls):
        rand_wall = walls[int(random.random() * len(walls)) - 1]
        if (rand_wall[1] != 0):
            if (oku[rand_wall[0]][rand_wall[1] - 1] == '2' and oku[rand_wall[0]][rand_wall[1] + 1] == '0'):
                s_cells = surroundingCells(rand_wall)

                if (s_cells < 2):
                    oku[rand_wall[0]][rand_wall[1]] = '0'

                    if (rand_wall[0] != 0):
                        if (oku[rand_wall[0] - 1][rand_wall[1]] != '0'):
                            oku[rand_wall[0] - 1][rand_wall[1]] = '1'
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    if (rand_wall[0] != height - 1):
                        if (oku[rand_wall[0] + 1][rand_wall[1]] != '0'):
                            oku[rand_wall[0] + 1][rand_wall[1]] = '1'
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    if (rand_wall[1] != 0):
                        if (oku[rand_wall[0]][rand_wall[1] - 1] != '0'):
                            oku[rand_wall[0]][rand_wall[1] - 1] = '1'
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)
                continue

        if (rand_wall[0] != 0):
            if (oku[rand_wall[0] - 1][rand_wall[1]] == '2' and oku[rand_wall[0] + 1][rand_wall[1]] == '0'):
                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    oku[rand_wall[0]][rand_wall[1]] = '0'
                    if (rand_wall[0] != 0):
                        if (oku[rand_wall[0] - 1][rand_wall[1]] != '0'):
                            oku[rand_wall[0] - 1][rand_wall[1]] = '1'
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (oku[rand_wall[0]][rand_wall[1] - 1] != '0'):
                            oku[rand_wall[0]][rand_wall[1] - 1] = '1'
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if (rand_wall[1] != width - 1):
                        if (oku[rand_wall[0]][rand_wall[1] + 1] != '0'):
                            oku[rand_wall[0]][rand_wall[1] + 1] = '1'
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)
                continue

        if (rand_wall[0] != height - 1):
            if (oku[rand_wall[0] + 1][rand_wall[1]] == '2' and oku[rand_wall[0] - 1][rand_wall[1]] == '0'):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    oku[rand_wall[0]][rand_wall[1]] = '0'
                    if (rand_wall[0] != height - 1):
                        if (oku[rand_wall[0] + 1][rand_wall[1]] != '0'):
                            oku[rand_wall[0] + 1][rand_wall[1]] = '1'
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (oku[rand_wall[0]][rand_wall[1] - 1] != '0'):
                            oku[rand_wall[0]][rand_wall[1] - 1] = '1'
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if (rand_wall[1] != width - 1):
                        if (oku[rand_wall[0]][rand_wall[1] + 1] != '0'):
                            oku[rand_wall[0]][rand_wall[1] + 1] = '1'
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)
                continue

        if (rand_wall[1] != width - 1):
            if (oku[rand_wall[0]][rand_wall[1] + 1] == '2' and oku[rand_wall[0]][rand_wall[1] - 1] == '0'):
                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    oku[rand_wall[0]][rand_wall[1]] = '0'
                    if (rand_wall[1] != width - 1):
                        if (oku[rand_wall[0]][rand_wall[1] + 1] != '0'):
                            oku[rand_wall[0]][rand_wall[1] + 1] = '1'
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])
                    if (rand_wall[0] != height - 1):
                        if (oku[rand_wall[0] + 1][rand_wall[1]] != '0'):
                            oku[rand_wall[0] + 1][rand_wall[1]] = '1'
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[0] != 0):
                        if (oku[rand_wall[0] - 1][rand_wall[1]] != '0'):
                            oku[rand_wall[0] - 1][rand_wall[1]] = '1'
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)
                continue

        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)
    for i in range(0, height):
        for j in range(0, width):
            if (oku[i][j] == '2'):
                oku[i][j] = '1'

    for i in range(0, width):
        if (oku[1][i] == '0'):
            oku[0][i] = '0'
            break

    for i in range(width - 1, 0, -1):
        if (oku[height - 2][i] == '0'):
            oku[height - 1][i] = '0'
            break

for x in range(len(oku)):
    for y in range(len(oku[x])):
        oku[x][y] = int(oku[x][y])
print(oku)

SWX = int(len(oku[0]))
SHY = int(len(oku))

SW, SH = SWX * 50, SHY * 50
BLOCK_SIZE = 50

pygame.init()
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Gezgin Robot")
clock = pygame.time.Clock()


def dijkstra(maze, start, end):
    heap = [(0, start)]
    visited = set()
    paths = {start: [start]}
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current in visited:
            continue
        if current == end:
            return (cost, paths[end])
        visited.add(current)
        for neighbor in get_neighbors(maze, current):
            if neighbor in visited:
                continue
            if 0 < maze[neighbor[0]][neighbor[1]] < 4:
                continue
            paths[neighbor] = paths[current] + [neighbor]
            heapq.heappush(heap, (cost + maze[neighbor[0]][neighbor[1]], neighbor))
    return (-1, [])


def get_neighbors(maze, current):
    n = len(maze)
    m = len(maze[0])
    row, col = current
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if row < n - 1:
        neighbors.append((row + 1, col))
    if col < m - 1:
        neighbors.append((row, col + 1))
    return neighbors


def shortest_path_coordinates(maze, start, finish):
    cost, path = dijkstra(maze, start, finish)
    return [p for p in path]


def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)


def problem():
    drawGrid()
    start_B = (0, 0)
    pygame.draw.rect(screen, "#00b300", [0, 0, 50, 50])
    end_H = (SWX - 1, SHY - 1)
    pygame.draw.rect(screen, "#e60000", [(SHY - 1) * 50, (SWX - 1) * 50, 50, 50])
    oku[0][0] = 0
    oku[SHY - 1][SWX - 1] = 0

    for x in range(SWX):
        for y in range(SHY):
            if oku[x][y] == 1:
                pygame.draw.rect(screen, "#3c3c3b", [y * 50, x * 50, 50, 50])
            elif oku[x][y] == 2:
                pygame.draw.rect(screen, "#3c3c3b", [y * 50, x * 50, 50, 50])
            elif oku[x][y] == 3:
                pygame.draw.rect(screen, "#3c3c3b", [y * 50, x * 50, 50, 50])

    print("Başlangıç: ", start_B, "\nBitiş: ", end_H)
    path = shortest_path_coordinates(oku, start_B, end_H)
    print("En kısa yolun uzunluğu:", len(path) - 1)
    print("En kısa yolun koordinatları:" + str(path))
    for p in path:
        time.sleep(0.5)
        pygame.display.update()
        pygame.draw.rect(screen, "#00b300", [p[1] * 50, p[0] * 50, 50, 50])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(10)
print(clock)
problem()

