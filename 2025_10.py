def find_paths(x:int,y:int, size: int) -> int:
    if x + y == 2 * size: return 1

    paths = 0
    if x+1 <= size:
        paths += find_paths(x+1,y, size)
    if y+1 <= size:
        paths += find_paths(x,y+1,size)
    return paths

print(f"There are {find_paths(0,0,3)} ways to write BIGYHK<3")
