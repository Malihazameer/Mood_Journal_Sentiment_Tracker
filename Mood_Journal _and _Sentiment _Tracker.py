import datetime
# Mood Analyzer Function
def analyze_mood(text):
    text = text.lower()
    happy_keywords = ['happy', 'great', 'good', 'excited', 'joy']
    sad_keywords = ['sad', 'tired', 'bad', 'depressed', 'angry']

    for word in happy_keywords:
        if word in text:
            return "Happy 😊"
    for word in sad_keywords:
        if word in text:
            return "Sad 😞"
    return "Neutral 😐"

#creating user profile
class UserProfile:
  def __init__(self,name):
    self.name=name
    self.mood_entries= {}
    self.filename = f"{self.name.lower()}_journal.txt"
    self.load_journal()

#function for adding entries
  def add_entry(self):
     text = input("How are you feeling today?")
     if not text:
        print("Input cannot be empty.")
        return
     mood = analyze_mood(text)
     date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #with the help of this formate it return all the histroy of mood entries otherwise it overwrite and show only single because of the same date,
     self.mood_entries[date] = {'text': text, 'mood': mood}
     print(f"Your mood has been saved as: {mood}")
     self.save_journal() # also save all the mood sepeartely

#function to show all the entered history
  def show_history(self):
    if not self.mood_entries:
      print("No mood entries found.")
      return
    print("Mood History:")
    for date, entry in sorted(self.mood_entries.items()):
        print(f"\n🗓️ {date}")
        print(f"   Mood: {entry['mood']}")
        print(f"   Your Entry: {entry['text']}")
    #for date, entry in self.mood_entries.items():
      #print(f"{date}: {entry['mood']}")

#save all the entries
  def save_journal(self):
    if self.mood_entries:
      with open(self.filename, 'a', encoding='utf-8') as f:
        for date, entry in self.mood_entries.items():
          line = f"{date}|{entry['mood']}|{entry['text']}\n"
          f.write(line)
      print("Journal saved successfully.")
    else:
      print("No mood entries to save.")

#load journal when executed
  def load_journal(self):
    try:
      with open(self.filename, 'r',encoding='utf-8') as f:
        for line in f:
          parts = line.strip().split('|')
          if len(parts) == 3:
            date, mood, text = parts
            self.mood_entries[date] = {'mood': mood, 'text': text}
      print("Journal loaded successfully.")
    except FileNotFoundError:
        print("No previous journal found. Starting fresh.")

  #additional part tp erase all journal entries
  def clear_journal(self):
    confirm = input("Are you sure you want to erase all mood entries? (yes/no): ").strip().lower()
    if confirm == 'yes':
        self.mood_entries.clear()  # Clear in-memory data
        # Overwrite the file with nothing
        with open(self.filename, 'w', encoding='utf-8') as f:
            pass
        print("All mood entries have been erased.")
    else:
        print("Action cancelled.")

# Main Program
def main():
    print("Welcome to the Console Mood Journal!")
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty. Exiting.")
        return
    user = UserProfile(name)
    while True:
        print("\nMenu:")
        print("1. Add Mood Entry")
        print("2. View Mood History")
        print("3. Erase All Mood Entries")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            user.add_entry()
        elif choice == '2':
            user.show_history()
        elif choice == '3':
            user.clear_journal()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
