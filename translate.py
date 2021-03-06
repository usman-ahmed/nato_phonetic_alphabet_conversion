# -*- coding: utf-8 -*-
import sys

alphabets_to_words =  {
        'A': 'Alfa',
        'B': 'Bravo',
        'C': 'Charlie',
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'India',
        'J': 'Juliett',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',        
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'X-ray	',
        'Y': 'Yankee',
        'Z': 'Zulu',

        '0': 'Zero, nadazero',
        '1': 'One, unaone',
        '2': 'Two, bissotwo',
        '3': 'Three, terrathree',
        '4': 'Four, kartefour',
        '5': 'Five, pantafive',
        '6': 'Six, soxisix',
        '7': 'Seven, setteseven',
        '8': 'Eight, oktoeight',
        '9': 'Nine, novenine',
        '.': 'Decimal, point',
        '-': 'Dash'
    }
for word in sys.argv[1:]:
  print("-----------------")
  print("\nTranslating to Nato Photentic Alphabets.....\n[ {} ]".format(
        word.upper()))
  for c in word:
    print("{} : {}".format(c.upper(), alphabets_to_words[c.upper()]))