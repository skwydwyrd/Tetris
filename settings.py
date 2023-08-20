# Define colors
BLACK = (0, 0, 0)
WHITE = (120, 120, 120)

CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

COLORS = [
	CYAN,
	YELLOW,
	MAGENTA,
	RED,
	GREEN,
	BLUE,
	ORANGE
]



# Set the width and height of the screen
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 520

# Set the dimensions of each block
BLOCK_SIZE = 20


# Define the board dimensions
COLS = WINDOW_WIDTH // BLOCK_SIZE
ROWS = WINDOW_HEIGHT // BLOCK_SIZE

# Set the initial position of the falling piece
INITIAL_POSITION = (COLS // 2 - 2, 0)

# Define the shapes of the Tetriminos
# SHAPES = [
#     [[1, 1, 1, 1]],	# I-Shape
#     [[1, 1], [1, 1]], # Block-Shape
#     [[1, 1, 0], [0, 1, 1]],	# S-Shape
#     [[0, 1, 1], [1, 1, 0]],	# Backwards S-Shape
#     [[1, 1, 1], [0, 1, 0]],	# T-Shape
#     [[1, 1, 1], [1, 0, 0]], # L-Shape
#     [[1, 1, 1], [0, 0, 1]], # J-Shape
# ]


# SHAPE_KEY = 'I-Shape'
# SHAPE_INDEX = random.choice()
COLORS = [(0,255,255),(255,0,255),(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# ishape = SHAPES[SHAPE_INDEX]['rotations'][0]

SHAPES = [
    {
        'key': 'I-Shape',
        'index': 0,
        'color': COLORS[0],
        'rotations': [
            [[1, 1, 1, 1]],
            [[1], [1], [1], [1]],
        ],
    },
    {
        'key': 'Block-Shape',
        'index': 0,
        'color': COLORS[1],
        'rotations': [
            [[1, 1],
             [1, 1]],
        ],
    },
    {
        'key': 'S-Shape',
        'index': 0,
        'color': COLORS[2],
        'rotations': [
            [[1, 1, 0],
             [0, 1, 1]],
            [[0, 1],
             [1, 1],
             [1, 0]],
        ],
    },
    {
        'key': 'Z-Shape',
        'index': 0,
        'color': COLORS[3],
        'rotations': [
            [[0, 1, 1],
             [1, 1, 0]],
            [[1, 0],
             [1, 1],
             [0, 1]],
        ],
    },
    {
        'key': 'T-Shape',
        'index': 0,
        'color': COLORS[4],
        'rotations': [
            [[1, 1, 1],
             [0, 1, 0]],
            [[0, 1],
             [1, 1],
             [0, 1]],
            [[0, 1, 0],
             [1, 1, 1]],
            [[1, 0],
             [1, 1],
             [1, 0]],
        ],
    },
    {
        'key': 'L-Shape',
        'index': 0,
        'color': COLORS[5],
        'rotations': [
            [[1, 1, 1],
             [1, 0, 0]],
            [[1, 1],
             [0, 1],
             [0, 1]],
            [[0, 0, 1],
             [1, 1, 1]],
            [[1, 0],
             [1, 0],
             [1, 1]],
        ],
    },
    {
        'key': 'J-Shape',
        'index': 0,
        'color': COLORS[6],
        'rotations': [
            [[1, 1, 1],
             [0, 0, 1]],
            [[0, 1],
             [0, 1],
             [1, 1]],
            [[0, 0, 1],
             [1, 1, 1]],
            [[1, 0],
             [1, 0],
             [1, 1]],
        ],
    },
]
