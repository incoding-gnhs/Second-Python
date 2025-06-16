import random

def display_grid(grid):

    """2D 그리드 맵을 출력하는 함수"""

    for row in grid:

        print(" ".join(row))

    print("\n")

def move_robot(grid, robot_position, direction):

    """로봇을 특정 방향으로 이동시키는 함수"""

    x, y = robot_position

    grid[x][y] = "."  # 이전 위치를 초기화

    if direction == "W" and x > 0:  # UP

        x -= 1

    elif direction == "S" and x < len(grid) - 1:  # DOWN

        x += 1

    elif direction == "A" and y > 0:  # LEFT

        y -= 1

    elif direction == "D" and y < len(grid[0]) - 1:  # RIGHT

        y += 1

    else:

        print("🚧 이동할 수 없습니다. 방향을 다시 선택하세요.")

        return robot_position  # 위치 변경 없음

    # 장애물이나 함정 검사

    if grid[x][y] == "X":

        print("🚧 장애물이 있어 이동할 수 없습니다!")

        return robot_position  # 위치 변경 없음

    elif grid[x][y] == "T":

        print("💀 함정에 닿았습니다! 게임 오버!")

        exit()  # 프로그램 종료

    grid[x][y] = "R"  # 새로운 위치에 로봇 표시

    return (x, y)

def generate_obstacles(grid, num_obstacles, num_traps):

    """장애물과 함정을 랜덤하게 배치"""

    rows, cols = len(grid), len(grid[0])

    empty_cells = [(x, y) for x in range(rows) for y in range(cols) if grid[x][y] == "."]

    random.shuffle(empty_cells)

    # 장애물 배치

    for  in range(numobstacles):

        if empty_cells:

            x, y = empty_cells.pop()

            grid[x][y] = "X"

    # 함정 배치

    for  in range(numtraps):

        if empty_cells:

            x, y = empty_cells.pop()

            grid[x][y] = "T"

def main():

    # 5x5 그리드 생성

    grid = [["." for  in range(5)] for  in range(5)]

    # 로봇과 목표 위치 초기화

    robot_position = (0, 0)  # 시작점 (좌측 상단)

    goal_position = (4, 4)   # 목표점 (우측 하단)

    grid[robot_position[0]][robot_position[1]] = "R"

    grid[goal_position[0]][goal_position[1]] = "G"

    # 장애물과 함정을 생성

    generate_obstacles(grid, num_obstacles=5, num_traps=3)

    print("🤖 로봇 경로 탐색 프로그램에 오신 것을 환영합니다!")

    print("로봇(R)을 목표(G)로 이동시키세요!")

    print("명령: W(UP), A(LEFT), S(DOWN), D(RIGHT)\n")

    print("⚠️ 'X'는 장애물이고 'T'는 함정입니다. 함정에 닿으면 게임 오버입니다!\n")

    # 초기 그리드 출력

    display_grid(grid)

    while robot_position != goal_position:

        command = input("다음 이동 방향을 입력하세요 (W, A, S, D): ").strip().upper()

        # 이동 실행

        robot_position = move_robot(grid, robot_position, command)

        # 현재 상태 출력

        display_grid(grid)

        if robot_position == goal_position:

            print("🎉 목표에 도착했습니다! 게임을 클리어했습니다.")

if name == "__main__":

    main()

