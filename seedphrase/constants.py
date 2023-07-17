LANGUAGES = {"en": "english",
             "zh": "chinese_simplified",
             "zh2": "chinese_traditional",
             "fr": "french",
             "it": "italian",
             "ja": "japanese",
             "ko": "korean",
             "es": "spanish"}

STRENGTHS = [128, 160, 192, 224, 256]

LENGTHS = [12, 15, 18, 21, 24]

LENGTH_STRENGTH = dict(zip(LENGTHS, STRENGTHS))