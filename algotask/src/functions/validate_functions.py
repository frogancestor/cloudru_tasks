# checks user input for containing only int and float
def validateUserInput(data: str) -> bool:
    for chunk in data.split(' '):
        try:
            if '.' in chunk:
                float(chunk)
            else:
                int(chunk)
        except ValueError as e:
            return False
    return True