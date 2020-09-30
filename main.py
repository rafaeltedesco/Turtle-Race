import turtle, random, time, os

wn = turtle.Screen()
wn.bgcolor('white')
SIZE = WIDTH, HEIGHT = 800, 600
wn.setup(*SIZE)
DELAY = 0.1

dice = list(range(1, 7))

colors = ['red', 'green', 'blue', 'black', 'purple', 'orange']

winers = {}

class Player(turtle.Turtle):
    def __init__(self, x, y, id, color='black', shape='turtle'):
        super().__init__(shape)
        self.hideturtle()
        self.speed(0)
        self.id = id
        self.penup()
        self.color(color)
        self.setpos(x, y)
        self.showturtle()
        self.end_run = 0
        self.time_elapsed = 0

    def run(self):
      if not self.end_run:
        if random.choice([0, 1]):
            steps = random.choice(dice) * 20
            self.fd(steps)

    def check_win(self):
      if not self.end_run:
        if self.xcor() >= 300:
          self.time_elapsed = round(time.time() - start, 2)
          print(f'Turtle id: {self.id} finished at time {self.time_elapsed}!')
          winers[self.id] = self.time_elapsed
          self.end_run = 1

players = []
x = -300
y = 200

line = turtle.Turtle()
line.speed(0)
line.hideturtle()
line.color('gray')
line.penup()
line.goto(300, 300)
line.pensize(7)
line.pendown()
line.goto(300, -300)

for i in range(5):
    players.append(Player(x, y, i+1, color=random.choice(colors)))
    y -= 100

start = time.time()

race = True

while race:
    for p in players:
        p.run()
        p.check_win()
        time.sleep(DELAY)
        if len(winers) == len(players):
          race = False

os.system('cls' if os.name=='nt' else 'clear')

print('Race ends. See the position reached by ours players')

count = 1
for id, t in winers.items():
  print(f'#{count} - Turtle id: {id} - Time elapsed: {t}')
  count += 1
