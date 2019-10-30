from sys import stdout, stdin

songs = []

n_songs, select_n = map(int, stdin.readline().split())

for i in range(1, n_songs + 1):
    plays, title = stdin.readline().split()

    songs.append((int(plays) * i, title))

songs.sort(key=lambda song: song[0], reverse=True)

for song in range(select_n):
    stdout.write(songs[song][1] + '\n')
