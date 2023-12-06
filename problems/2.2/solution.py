# <format> game id: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red
games = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        game_info, draws = line.replace('\n','').split(': ')
        id = int(game_info.split(' ')[1])
        
        game = { 'id': id, 'red': 0, 'blue': 0, 'green': 0 }
        for draw in draws.split('; '):
            choices = [choice.split(' ') for choice in draw.split(', ')]
            for num, color in choices:
                game[color] = max(game[color], int(num))
        games.append(game)

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
sum = 0
for game in games:
    sum += game['red'] * game['green'] * game['blue']
print(sum)

# <format> game id: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red