import pygame
import sys
import heapq
import time


class Problem:
    def __init__(self):
        self.dosya = open("matrix.txt", "r", encoding="utf-8")
        self.oku = self.dosya.read()
        self.oku = self.oku.split('\n')
        for x in range(len(self.oku)):
            self.oku[x] = list(self.oku[x])
        for x in range(len(self.oku)):
            for y in range(len(self.oku[x])):
                if self.oku[x][y] == 'B':
                    self.oku[x][y] = '4'
                elif self.oku[x][y] == 'H':
                    self.oku[x][y] = '5'
                self.oku[x][y] = int(self.oku[x][y])
        print(self.oku)

        self.SWX = len(self.oku[0])
        self.SHY = len(self.oku)

        pygame.init()
        self.SW, self.SH = self.SWX * 50, self.SHY * 50

        self.BLOCK_SIZE = 50

        self.screen = pygame.display.set_mode((self.SW, self.SH))
        pygame.display.set_caption("Gezgin Robot")
        self.clock = pygame.time.Clock()

    def dijkstra(self, maze, start, end):
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
            for neighbor in self.get_neighbors(maze, current):
                if neighbor in visited:
                    continue
                if 0 < maze[neighbor[0]][neighbor[1]] < 4:
                    continue
                paths[neighbor] = paths[current] + [neighbor]
                heapq.heappush(heap, (cost + maze[neighbor[0]][neighbor[1]], neighbor))
        return (-1, [])

    def get_neighbors(self, maze, current):
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

    def shortest_path_coordinates(self, maze, start, finish):
        cost, path = self.dijkstra(maze, start, finish)
        return [p for p in path]

    def drawGrid(self):
        for x in range(0, self.SW, self.BLOCK_SIZE):
            for y in range(0, self.SH, self.BLOCK_SIZE):
                rect = pygame.Rect(x, y, self.BLOCK_SIZE, self.BLOCK_SIZE)
                pygame.draw.rect(self.screen, "#3c3c3b", rect, 1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("#c7c7c7")
            self.drawGrid()

            for x in range(self.SWX):
                for y in range(self.SHY):
                    # drawBarrier(x,y,oku)
                    if self.oku[x][y] == 4:
                        start_B = (x, y)
                        pygame.draw.rect(self.screen, "#00b300", [y * 50, x * 50, 50, 50])
                    elif self.oku[x][y] == 5:
                        end_H = (x, y)
                        pygame.draw.rect(self.screen, "#e60000", [y * 50, x * 50, 50, 50])
                    elif self.oku[x][y] == 1:
                        pygame.draw.rect(self.screen, "#3c3c3b", [y * 50, x * 50, 50, 50])
                    elif self.oku[x][y] == 2:
                        pygame.draw.rect(self.screen, "#3c3c3b", [y * 50, x * 50, 50, 50])
                    elif self.oku[x][y] == 3:
                        pygame.draw.rect(self.screen, "#3c3c3b", [y * 50, x * 50, 50, 50])

            print("Başlangıç: ", start_B, "\nBitiş: ", end_H)
            path = self.shortest_path_coordinates(self.oku, start_B, end_H)
            print("En kısa yolun uzunluğu:", len(path) - 1)
            print("En kısa yolun koordinatları:" + str(path))
            for p in path:
                time.sleep(0.5)
                pygame.draw.rect(self.screen, "#00b300", [p[1] * 50, p[0] * 50, 50, 50])
                pygame.display.update()

            pygame.display.update()
            self.clock.tick(10)

    pygame.quit()
    sys.exit()


