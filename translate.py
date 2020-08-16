# -*- coding: utf-8 -*-
text = "sample"

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

print("-----------------")
print("\nTranslating '{}' to Nato Photentic Alphabets.....\n".format(text.upper()))
for c in text:
    print("{} : {}".format(c.upper(), alphabets_to_words[c.upper()]))