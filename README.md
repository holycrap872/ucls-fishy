# Pong

This code is a partially done version of the game [fishy](https://freefishy.org/).
Your mission is to create a fully working version that:

1. Gives the user fish the ability to move up/down/left/right
2. Has the "dinner fish" moving from right to left or left to right
3. Has the "dinner fish" properly reset whenever they reach the opposite wall
4. Has the user fish grow whenever it eats a "dinner fish" that is smaller than it
5. Has the user fish die whenever it runs into a "dinner fish" that is bigger than it
6. Has a "score" variable that shows how many fish the user has eaten
7. Resets the game when the user runs out of lives

## Setup

The only thing that you _should_ need to do to get this project up and running
is:

### 0. Open the project's workspace

Open `vscode` and select `File` -> `Open Workspace from File`. Then, select the
`fishy.code-workspace` file within this project folder.

### 1. Install necessary extensions

On the left-most side of the `vscode` window, select the "Extensions" tab (four
small squares making a larger square) and install the following extensions:

- `Python`
- `Pylance` (auto installed with `Python` extension)
- `Black Formatter`
- `isort`

> Note: be careful to select only the "Microsoft approved" extensions.

### 2. Install necessary Python modules

Open the terminal window by selecting `Terminal` -> `New Terminal`. Then,
install all the required libraries by typing:

```
pip3 install pytest pygame
```

### 3. Verify it runs

You now should be able to run the program and see a white "user fish" and a red
"dinner fish" against a black background. Assuming you have that, move onto the
next task.

## Game Development

Now that everything is setup, you can start with developing the game. The file
you are editing is `src/fishy/main.py`.

## Read the Code

Look through the code and try and understand it. Pay particular attention to:

- The `User` class that has the ability to move in various direction, grow, and die
- The `Dinner` class that has the ability to move and reset
- The `is_colliding` function that tells you whether two fish are colliding
    - Note: It does this by using the "distance formula"
- How we create a `user_fish` and a single `other_fish` in our initialization
- How the `user_fish` can only move up (but not down)
- How the single `other_fish` can move across the screen

## Modify the Code

Now that you understand the code a little bit, work to accomplish each of the
following tasks in order:

1. Have the user fish move up/down/left/right
    - Hint: Look at how the `move_up()` function currently used
2. Have the "dinner fish" moving from right to left or left to right
    - Hint: You will need to put `other_fish[0].move()` in the right spot
3. Have the dinner fish properly reset whenever they reach the opposite wall
    - Hint: Look at how you determined if something was hitting the edge in Pong
    - Hint: You will need to add your own code to `reset()`
4. Have the user fish grow whenever it eats a dinner fish that is smaller than it
    - Hint: You will need to use the `is_colliding()` function
    - Hint: If the fish are colliding, you then need to compare their size
    - Hint: Use the `grow()` function
5. Have the user fish die whenever it runs into a dinner fish that is bigger than it
    - Hint: Use the `die()` function
6. Have a "score" variable that shows how many fish the user has eaten
    - Hint: You will need to create your own variable
7. Reset the game when the user runs out of lives
8. Instead of having one "dinner fish" have a a bunch of them
    - Hint: Add more fish to the `other_fishes` list
    - Hint: Use a loop to iterate through all the `other_fishes` and move them all

### Difficulties:

The hardest part of developing this game is to really understand what the `User`
and `Dinner` classes are for. Basically, they hold the bundle of data that is
required to represent a user or dinner fish. We then user "helper functions"
to make it easy to manipulate that data.

For example, rather than directly altering the dinner fish's `x` or `y`, we can
just say `move()` and it will handle itself. It's like how I can rely on a
vending machine to handle all the details itself: I only care about
`give_me_candy()`.

## Extend the Code

- Create "death fish" that will cause you to die no matter what size they are
- Use actual pictures of fish instead of circles
- Have a timer where the game ends when the clock hits 0
