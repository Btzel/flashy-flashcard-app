# Flashy Language Learning App
A dynamic French-English vocabulary learning application built with Python using Tkinter and Pandas, featuring interactive flashcards with a scoring system.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data-red)
![Learning](https://img.shields.io/badge/Language-Learning-green)

## 🎯 Overview
This project creates an interactive learning environment where users:
1. View French vocabulary words
2. See English translations after delay
3. Choose correct/incorrect translations
4. Track learning progress
5. Build vocabulary through repetition

## 🎮 Application Features
### Interactive Elements
- Dynamic flashcard display
- Timed card flipping
- Right/wrong answer buttons
- Score tracking system
- Visual feedback system

### Data Management
- CSV-based vocabulary storage
- Random word selection
- Progress tracking
- Dynamic card updates

## 🔧 Technical Components
### Flashcard Management System
```python
def flashy_cards(self):
    french_word = self.random_row[0][0]
    self.right_english_word = self.random_row[0][1]
    wrong_english_word = self.random_row[1][1]
    self.english_word = random.choice([self.right_english_word,wrong_english_word])
    self.canvas_modifier(image_name="card_front",language="French",word=french_word)
    self.is_active_timer = self.window.after(2000,self.canvas_modifier,"card_back","English",self.english_word)
```

### Key Features
1. **Card Management**
   - Automatic card flipping
   - Random word selection
   - Translation display
   - Score tracking

2. **Learning System**
   - Instant feedback
   - Progress tracking
   - Random word pairs
   - Timed responses

3. **Data Processing**
   - CSV data handling
   - Word pair matching
   - Score calculation
   - Random selection

## 💻 Implementation Details
### Class Structure
- `Interface`: Core application and UI management
- Pandas DataFrame for vocabulary management
- Timer-based card flipping system

### Data Management
- French-English word pairs
- Random word selection
- Score tracking system
- Timer management

## 🚀 Usage
1. Install required packages:
```bash
pip install pandas
pip install tkinter
```

2. Run the application:
```bash
python main.py
```

3. Learn vocabulary:
   - View French word
   - Wait for English translation
   - Select right/wrong
   - Track your score

## 🎯 Learning Rules
1. Read the French word shown
2. Wait for card to flip (2 seconds)
3. Decide if translation is correct
4. Click ✓ for correct, X for incorrect
5. Track your progress via score

## 🛠️ Project Structure
```
flashy/
├── main.py              # Application core
├── data/
│   └── french_words.csv # Vocabulary database
└── images/
    ├── card_front.png   # Card templates
    ├── card_back.png
    ├── right.png        # Button images
    └── wrong.png
```

## 📊 Features
### Input Processing
- Timed card flips
- Button response handling
- Score calculation
- Random word selection

### Output Management
- Dynamic card display
- Score updates
- Visual feedback
- Progress tracking

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL