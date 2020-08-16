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
    }
for word in sys.argv[1:]:
  print("-----------------")
  print("\nTranslating to Nato Photentic Alphabets.....\n[ {} ]".format(
        word.upper()))
  for c in word:
    print("{} : {}".format(c.upper(), alphabets_to_words[c.upper()]))