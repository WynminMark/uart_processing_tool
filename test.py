def read_hex_frames(file_path):
    frames = []
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')  # 读取文件并去除换行符
        i = 0
        while i < len(data):
            # 查找帧的起始标志
            if data[i:i+4] == 'A55A':
                frame = data[i:i+20]  # 每帧包含16个字符（8个16进制数）
                frames.append(frame)
                i += 20  # 跳过当前帧
            else:
                i += 1  # 移动到下一个字符
    return frames

# 使用示例
file_path = 'path/to/your/file.txt'
hex_frames = read_hex_frames(file_path)
for frame in hex_frames:
    print(frame)