def get_limit():
    f = open("config.txt", 'r')
    for line in f.readlines():
        if 'limit' in line:
            data = line.split('=')
            f.close()
            return int(data[1])
    f.close()
    print("An error has occurred. Please check config.txt.")

def get_token():
    f = open("config.txt", 'r')
    for line in f.readlines():
        if 'token' in line:
            data = line.split('=')
            f.close()
            return data[1]
    f.close()
    print("An error has occurred. Please check config.txt.")

def get_channel_ids():
    f = open("channel_id.txt", 'r')
    ids = []
    for line in f.readlines():
        if line != '':
            ids.append(int(line))
    f.close()
    return ids

def reset_channel_ids():
    f = open("channel_id.txt", 'w')
    f.close()

def add_channel_ids(channel_id):
    f = open("channel_id.txt", 'a')
    f.write(channel_id + '\n')

def set_limit(value, token):
    f = open("config.txt", 'w')
    f.write('=========== AUTO CREATE CONFIG ==========\n')
    f.write('limit=' + str(value) + '\n')
    f.write('token=' + str(token))
    f.close()


