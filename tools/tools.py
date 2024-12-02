def load_file(file_path:str) -> list[str]:
    with open(file_path, "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    return data
