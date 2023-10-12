import time
import os

# nice result with the follwing cells:
# Enter cell coordinates (x, y): 2,1
# Enter cell coordinates (x, y): 2,3
# Enter cell coordinates (x, y): 2,5
# Enter cell coordinates (x, y): 2,2
# Enter cell coordinates (x, y): 4,3
# Enter cell coordinates (x, y): 3,2
# Enter cell coordinates (x, y): 3,3


# Function to create an empty grid
def create_empty_grid(rows, cols):
    return [[0] * cols for _ in range(rows)]


# Function to display the grid
def display_grid(grid):
    os.system('clear')  # Clear the console (for Unix-like systems)
    for row in grid:
        print(" ".join(["■" if cell else " " for cell in row]))


# Function to count live neighbors of a cell
def count_neighbors(grid, x, y):
    count = 0
    rows, cols = len(grid), len(grid[0])
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny]:
                count += 1
    return count


# Function to update the grid for the next generation
def update_grid(grid):
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            live_neighbors = count_neighbors(grid, i, j)
            if grid[i][j]:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid


# Function to set an initial pattern on the grid
def set_pattern(grid, pattern, x_offset, y_offset):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if 0 <= i + x_offset < len(grid) and 0 <= j + y_offset < len(grid[i]):
                grid[i + x_offset][j + y_offset] = pattern[i][j]


# Function to interactively set cells on the grid
def set_cells_interactively(grid):
    rows, cols = len(grid), len(grid[0])
    print("Select cells to make alive (x, y) or press 'Enter' to start the simulation.")

    while True:
        try:
            user_input = input("Enter cell coordinates (x, y): ")
            if user_input == "":
                break
            x, y = map(int, user_input.split(","))
            if 0 <= x < rows and 0 <= y < cols:
                grid[x][y] = 1
            else:
                print("Invalid coordinates. Please try again.")
        except ValueError:
            print("Invalid input. Please enter coordinates as 'x, y'.")


# Function to count the total live cells in the grid
def count_live_cells(grid):
    return sum(sum(row) for row in grid)


# Main function
def main():
    grid = create_empty_grid(20, 30) # or whatever you want

    # Interactive cell setup
    set_cells_interactively(grid)

    generation_count = 0
    while True:
        display_grid(grid)
        grid = update_grid(grid)
        generation_count += 1
        live_cell_count = count_live_cells(grid)
        print(f'You\'re at generation: {live_cell_count}')
        if live_cell_count == 0:
            print(f"All cells are dead after {generation_count} generations.")
            break
        time.sleep(0.9)  # Adjust the delay for the desired speed


if __name__ == "__main__":
    main()
