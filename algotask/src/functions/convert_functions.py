def handleUserInput(data: str) -> list:
    result = []
    for chunk in data.split(' '):
        if '.' in chunk:
            result.append(float(chunk))
        else:
            result.append(int(chunk))
    return result