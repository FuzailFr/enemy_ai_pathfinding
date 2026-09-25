import heapq

def heuristic(a, b):
    """Menghitung jarak Manhattan antara titik A dan B."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, goal):
    """
    Mencari jalur terpendek dari start ke goal menggunakan algoritma A*.
    Mengembalikan list koordinat jalur, atau None jika jalur tidak ditemukan.
    """
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            return path[::-1]

        x, y = current

        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        for neighbor in neighbors:
            nx, ny = neighbor

            if nx < 0 or ny < 0:
                continue

            if nx >= len(grid) or ny >= len(grid[0]):
                continue

            if grid[nx][ny] == 1:
                continue

            new_cost = cost[current] + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)

                heapq.heappush(
                    open_list,
                    (priority, neighbor)
                )

                came_from[neighbor] = current

    return None


def enemy_ai(enemy, player, grid, detection_range):
    """
    Mengontrol logika AI Enemy untuk mendeteksi dan mengejar Player
    berdasarkan jarak dan jalur dari A*.
    """
    distance = heuristic(enemy, player)

    if distance > detection_range:
        print("Player berada di luar jangkauan.")
        print("Enemy melakukan patroli.")
        return

    print("Player terdeteksi!")

    path = a_star(grid, enemy, player)

    if path:
        print("Jalur ditemukan:")
        print(path)

        for position in path:
            print("Enemy bergerak ke:", position)

        print("Enemy sudah Ketemu Player!")
    else:
        print("Jalur menuju Player tidak ditemukan.")


dungeon = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

enemy_position = (0, 0)
player_position = (4, 4)

enemy_ai(
    enemy_position,
    player_position,
    dungeon,
    detection_range=10
)
