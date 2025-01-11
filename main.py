import random
import utils
from tqdm import tqdm
from PIL import Image

img = Image.new('RGB', (1920, 1080), color='white')
width, height = img.size
obj = img.load()

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

def test1(w, h):
  a = int((h * 100) / height)
  b = int((w * 100) / width)

  if a > 49:
    a = a - (a - (100 - a))
  if b > 49:
    b = b - (b - (100 - b))

  return random.choices([BLACK, WHITE], weights=[0 + a + b, 100 - a - b])[0]

def test2(w, h):
  a = int((h * 100) / height)
  b = int((w * 100) / width)

  if a > 49:
    a = a - (a - (100 - a))
  if b > 49:
    b = b - (b - (100 - b))

  return random.choices([BLACK, WHITE], weights=[0 + a - b, 100 - a + b])[0]

def test3(w, h):
  if utils.is_prime(w + h):
    return BLACK
  else:
    return WHITE

def test4(w, h):
  return random.choice([WHITE, BLACK])

def test5(w, h):
  return (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    255
  )


def main():
  print('''
  Available scenarios:
  1. Test #1
  2. Test #2
  3. Prime numbers
  4. White-black noise
  5. Noise
  ''')

  testname = input('Scenario number: ')
  testmap = { '1': test1, '2': test2, '3': test3, '4': test4, '5': test5 }

  if not testmap.get(testname):
    print('Invalid scenario number')
    return

  for h in tqdm(range(0, height)):
    for w in range(0, width):
      obj[w,h] = testmap[testname](w, h)

  img.show()
  img.save('test_{}.png'.format(testname), 'png')
  img.close()


if __name__ == '__main__':
  main()
