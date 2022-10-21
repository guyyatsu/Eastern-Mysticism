#!/bin/python3
from random import randint

class iChing:

  def __init__(self):

    self.Diagrams = {

      # Zhao Huiqian's diagrammatic explanation of the Bagua.
      "Bagua Zhao Huiqian": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Bagua_Zhao_Huiqian.jpg",

      # Conversion of Hexagrams/Trigrams into binary.
      "Dualer Aufbau": "https://upload.wikimedia.org/wikipedia/commons/d/d3/DualerAufbau.JPG",

      # Derivation of the Bagua.
      "Xiantian Bagua": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Xiantianbagua.png",

      # The 64 Hexagrams, in color.
      "64 Hexagrams": "https://upload.wikimedia.org/wikipedia/commons/6/69/64_qu%E1%BA%BB.png",

      # The Shao-Yong Sequence, or the 'Earlier Heaven' model of interpretation.
      "Earlier Heaven": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Bagua-name-earlier.svg",

      # The King Wen, or 'Later Heaven' interpretation.
      "Later Heaven": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Bagua-name-later.svg",

      # An image of a turtle carrying the Bagua, the 12 Zodiac, and a smaller turtle carrying the Lo-Shu Square.
      "Tibetan Mystic Tablet": "https://upload.wikimedia.org/wikipedia/commons/2/27/Carus-p48-Mystic-table.jpg",
    }

  class Trigrams:
    def __init__(self):
      self.Qian = {
        "Figure": "☰",
        "Binary": '111',
        "Decimal": 7,
        "Character": "乾",
        "Name": "Qián",
        "Translation": "The Creative; Natural Force",
        "Image": ["Heaven", "Sky", "天"],
        "Phase": "Metal",
        "Later Direction": "North-West",
        "Later Equinox": None,
        "Earlier Direction": "South",
        "Earlier Equinox": "Summer Solstice",
        "Family Relationship": "Father",
        "Body Part": "Head",
        "Attributes": ["Strong", "Persisting"],
        "Stage/State": ["Creative"],
        "Animal": ["Horse", "馬"],
        "Obtained Images": ["Three Lines", "三連"],
      }

      self.Dui = { 
        "Figure": "☱",
        "Binary": '110',
        "Decimal": 6,
        "Character": "兌",
        "Name": "Duì",
        "Translation": "The Joyous, Open, Reflection",
        "Image": ["Lake", "Marsh", "澤"],
        "Phase": "Metal",
        "Later Direction": "West",
        "Later Equinox": "Fall Equinox",
        "Earlier Direction": "South-East",
        "Earlier Equinox": None,
        "Family Relationship": "Third Daughter",
        "Body Part": "Mouth",
        "Attributes": ["Pleasure"],
        "Stage/State": ["Tranquil", "Complete Devotion"],
        "Animal": ["Sheep", "Goat",  "羊"],
        "Obtained Images": ["Flawed Above","上缺"],
      }

      self.Li = { 
        "Figure": "☲",
        "Binary": '101',
        "Decimal": 5,
        "Character": "離",
        "Name": "Lí",
        "Translation": "The Clinging Radiance",
        "Image": ["Fire", "Glow", "火"],
        "Phase": "Fire",
        "Later Direction": "South",
        "Later Equinox": "Summer Solstice",
        "Earlier Direction": "East",
        "Earlier Equinox": "Spring Equinox",
        "Family Relationship": "Second Daughter",
        "Body Part": "Eye",
        "Attributes": ["Light-Giving", "Humane Dependence"],
        "Stage/State": ["Clinging", "Clarity", "Adaptable"],
        "Animal": ["Pheasant", "雉"],
        "Obtained Images": ["Hollow Middle", "中虛"],
      }

      self.Zhen = { 
        "Figure": "☳",
        "Binary": '100',
        "Decimal": 4,
        "Character": "震",
        "Name": "Zhèn",
        "Translation": "The Arousing Shake",
        "Image": ["Thunder", "雷"],
        "Phase": "Wood",
        "Later Direction": "East",
        "Later Equinox": "Spring Equinox",
        "Earlier Direction": "Nort-East",
        "Earlier Equinox": None,
        "Family Relationship": "First Son",
        "Body Part": "Foot",
        "Attributes": ["Inciting Movement"],
        "Stage/State": ["Initiative"],
        "Animal": ["Dragon", "龍"],
        "Obtained Images": ["Face-Up Jar", "仰盂"],
      }

      self.Xun = { 
        "Figure": "☴",
        "Binary": '011',
        "Decimal": 3,
        "Character": "巽",
        "Name": "Xùn",
        "Translation": "The Gentle Ground",
        "Image": ["Wind", "Air", "風"],
        "Phase": "Wood",
        "Later Direction": "South-East",
        "Later Equinox": None,
        "Earlier Direction": "South-West",
        "Earlier Equinox": None,
        "Family Relationship": "First Daughter",
        "Body Part": "Thigh",
        "Attributes": ["Penetrating"],
        "Stage/State": ["Gentle Entrance"],
        "Animal": ["Fowl",  "雞"],
        "Obtained Images": ["Broken Below", "下斷"],
      }

      self.Kan = { 
        "Figure": "☵",
        "Binary": '010',
        "Decimal": 2,
        "Character": "坎",
        "Name": "kǎn",
        "Translation": "The Abysmal Gorge",
        "Image": ["Water", "水"],
        "Phase": "Water",
        "Later Direction": "North",
        "Later Equinox": "Winter Solstice",
        "Earlier Direction": "West",
        "Earlier Equinox": "Fall Equinox",
        "Family Relationship": "Second Son",
        "Body Part": "Ear",
        "Attributes": ["Dangerous"],
        "Stage/State": ["In-Motion"],
        "Animal": ["Pig",  "豕"],
        "Obtained Images": ["Full Middle", "中滿"],
      }

      self.Gen = { 
        "Figure": "☶",
        "Binary": '001',
        "Decimal": 1,
        "Character": "艮",
        "Name": "Gèn",
        "Translation": "Keeping Still, Bound",
        "Image": ["Mountain", "山"],
        "Phase": "Earth",
        "Later Direction": "North-East",
        "Later Equinox": None,
        "Earlier Direction": "North-West",
        "Earlier Equinox": None,
        "Family Relationship": "Third Son",
        "Body Part": "Hand",
        "Attributes": ["Resting", "Standing Still"],
        "Stage/State": ["Completion"],
        "Animal": ["Dog",  "狗"],
        "Obtained Images": ["Face-Down Bowl", "覆碗"],
      }

      self.Kun = { 
        "Figure": "☷",
        "Binary": '000',
        "Decimal": 0,
        "Character": "坤",
        "Name": "Kūn",
        "Translation": "Rhe Receptive Field",
        "Image": ["Ground", "Earth", "地"],
        "Phase": "Earth",
        "Later Direction": "South-West",
        "Later Equinox": None,
        "Earlier Direction": "North",
        "Earlier Equinox": "Winter Solstice",
        "Family Relationship": "Mother",
        "Body Part": "Belly",
        "Attributes": ["Devoted", "Yeilding"],
        "Stage/State": ["Receptive"],
        "Animal": ["Cow",  "牛"],
        "Obtained Images": ["Six Fragments","六斷"],
      }

    def GenerateTrigram(self):

      first = randint(0,1)
      second = randint(0,1)
      third = randint(0,1)

      trigram = dict

      if first == 0:
  
        if second == 0:
          # 000
          if third == 0: trigram = self.Kun
          # 001
          else: trigram = self.Zhen
  
        else:
          # 010
          if third == 0: trigram =  self.Kan
          # 011
          else: trigram =  self.Dui
  
      else:
        if second == 0:
          # 100
          if third == 0: trigram =  self.Gen
          # 101
          else: trigram =  self.Li
  
        else:
          # 110
          if third == 0: trigram = self.Xun
          # 111
          else: trigram = self.Qian

      return trigram

  class Hexagrams:

    def __init__(self):

      self.Trigrams = Trigrams()

      # Qian-Based Hexagrams; 1, 6, 10, 12, 13, 25, 33, 44
      self.Qian = {
        "Number": 1,
        "Figure": "䷀ ",
        "Name": "Qián",
        "Character": "乾",
        "Translation": "Force",
        "Formation": [
          self.Trigrams.Qian,
          self.Trigrams.Qian
        ],
      }

      self.Lu = {
        "Number": 10,
        "Figure": "䷉ ",
        "Name": "Lǚ",
        "Character": "履",
        "Translation": "Treading",
        "Formation": [
          self.Trigrams.Qian,
          self.Trigrams.Dui
        ],
      }

      self.Tongren = {
        "Number": 13,
        "Figure": "䷌ ",
        "Name": "Tóngrén",
        "Character": "同人",
        "Translation": "Concording People",
        "Formation": [
          self.Trigrams.Qian,
          self.Trigrams.Li
        ],
      }

      self.Wuwang = {
        "Number": 25,
        "Figure": "䷘ ",
        "Name": "Wúwàng",
        "Character": "無妄",
        "Translation": "Innocence",
        "Formation": [
          self.Trigrams.Qian,
          self.Trigrams.Zhen
        ],
      }

      self.Gou = {
        "Number": 44,
        "Figure": "䷫ ",
        "Name": "Gòu",
        "Character": "姤",
        "Translation": "Coupling",
        "Formation": [
          self.Trigrams.Qian,
          self.Trigrams.Xun
        ],
      }

      self.Song = {
        "Number": 6,
        "Figure": "䷅ ",
        "Name": "Sòng",
        "Character": "訟",
        "Translation": "Arguing",
        "Formation": [
          self.Trigrams.Qian,
          self.Trigrams.Kan
        ],
      }

      self.Dun = {
        "Number": 33,
        "Figure": "䷠ ",
        "Name": "Dùn",
        "Character": "遯",
        "Translation": "Retiring",
        "Formation": [
          self.Trigrams.Qian,
          self.Trigrams.Gen
        ],
      }

      self.Pi = {
        "Number": 12,
        "Figure": "䷋ ",
        "Name": "Pǐ",
        "Character": "否",
        "Translation": "Obstruction",
        "Formation": [
          self.Trigrams.Qian,
          self.Trigrams.Kun
        ],
      }
      
      # Dui-Based Hexagrams; 17, 28, 31, 43, 45, 47, 49, 58
      self.Dui = {
        "Number": 58,
        "Figure": "䷹ ",
        "Name": "Duì",
        "Character": "兌",
        "Translation": "Open",
        "Formation": [
          self.Trigrams.Dui,
          self.Trigrams.Dui
        ],
      }

      self.Guai = {
        "Number": 43,
        "Figure": "䷪ ",
        "Name": "Guài",
        "Character": "夬",
        "Translation": "Displacement",
        "Formation": [
          self.Trigrams.Dui,
          self.Trigrams.Qian
        ],
      }

      self.Ge = {
        "Number": 49,
        "Figure": "䷰ ",
        "Name": "Gé",
        "Character": "革",
        "Translation": "Skinning",
        "Formation": [
          self.Trigrams.Dui,
          self.Trigrams.Li
        ],
      }

      self.Sui = {
        "Number": 17,
        "Figure": "䷐ ",
        "Name": "Suí",
        "Character": "隨",
        "Translation": "Following",
        "Formation": [
          self.Trigrams.Dui,
          self.Trigrams.Zhen
        ],
      }

      self.Daguo = {
        "Number": 28,
        "Figure": "䷛ ",
        "Name": "Dàguò",
        "Character": "大過",
        "Translation": "Great Exceeding",
        "Formation": [
          self.Trigrams.Dui,
          self.Trigrams.Xun
        ],
      }

      self.Kune = {
        "Number": 47,
        "Figure": "䷮ ",
        "Name": "Kùn",
        "Character": "困",
        "Translation": "Confining",
        "Formation": [
          self.Trigrams.Dui,
          self.Trigrams.Kan
        ],
      }

      self.Xian = {
        "Number": 31,
        "Figure": "䷞ ",
        "Name": "Xián",
        "Character": "咸",
        "Translation": "Conjoining",
        "Formation": [
          self.Trigrams.Dui,
          self.Trigrams.Gen
        ],
      }

      self.Cui = {
        "Number": 45,
        "Figure": "䷬ ",
        "Name": "Cuì",
        "Character": "萃",
        "Translation": "Clustering",
        "Formation": [
          self.Trigrams.Dui,
          self.Trigrams.Kun
        ],
      }

      # Li-Based Hexagrams; 14, 21, 30, 35, 38, 50, 56, 64

      self.Li = {
        "Number": 30,
        "Figure": "䷝ ",
        "Name": "Lì",
        "Character": "離",
        "Translation": "Radiance",
        "Formation": [
          self.Trigrams.Li,
          self.Trigrams.Li
        ],
      }

      self.Dayou = {
        "Number": 14,
        "Figure": "䷍ ",
        "Name": "Dàyǒu",
        "Character": "大有",
        "Translation": "Great Possessing",
        "Formation": [
          self.Trigrams.Li,
          self.Trigrams.Qian
        ],
      }

      self.Shihe = {
        "Number": 45,
        "Figure": "䷔ ",
        "Name": "Shìhé",
        "Character": "噬嗑",
        "Translation": "Gnawing Bite",
        "Formation": [
          self.Trigrams.Li,
          self.Trigrams.Zhen
        ],
      }

      # Zhen-Based Hexagrams;
      # Xun-Based Hexagrams; 
      # Kan-Based Hexagrams;
      # Gen-Based Hexagrams;
      # Kun-Based Hexagrams;
