import tkinter as tk
from PIL import Image, ImageTk
import os
import random
from tkinter import messagebox
from cx_Freeze import setup, Executable

# Function to check the current directory
def check_current_directory():
    print("Current Directory:", os.getcwd())

# Function to check if a file exists
def check_file_exists(file_path):
    print(f"File exists at '{file_path}':", os.path.exists(file_path))

# Function to create a deck of cards
def create_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    return [f"{rank}_{suit}" for suit in suits for rank in range(1, 14)]

# Function to draw a card from the deck
def draw_from_deck():
    global deck
    if not deck:
        return "Het kaartendeck is leeg."
    return deck.pop()

# Function to load card images
def load_card_images():
    card_images = {}

    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    placeholder = ImageTk.PhotoImage(Image.new('RGB', (100, 150), color='white'))
    for suit in suits:
        for i in range(1, 14):
            img_path = f"{i}_{suit}.png"
            try:
                img = Image.open(img_path)
                img.thumbnail((100, 150), resample=Image.LANCZOS)
                card_images[f"{i}_{suit}"] = ImageTk.PhotoImage(img)
            except FileNotFoundError:
                card_images[f"{i}_{suit}"] = placeholder
                print(f"Image not found at: {img_path}")

    return card_images

# Function to display card backs
def display_card_backs():
    global deck

    img_path = "cardback.png"
    img = Image.open(img_path)
    img.thumbnail((100, 150), resample=Image.LANCZOS)
    card_back = ImageTk.PhotoImage(img)

    # Clear the existing card_back_frame before adding new cards
    for widget in card_back_frame.winfo_children():
        widget.destroy()

    for i, _ in enumerate(deck):
        card_image = tk.Label(card_back_frame, image=card_back)
        card_image.grid(row=0, column=i)
        card_image.image = card_back

# Function to handle card click event
def card_clicked(index):
    global total_value
    card = draw_from_deck()
    if card == "Het kaartendeck is leeg.":
        result_label.config(text=card)
        return

    img_path = f"{card}.png"
    img = Image.open(img_path)
    img.thumbnail((100, 150), resample=Image.LANCZOS)
    card_image = ImageTk.PhotoImage(img)

    card_buttons[index].config(image=card_image)
    card_buttons[index].image = card_image

    # Calculate card value
    card_rank = int(card.split('_')[0])
    if card_rank in [11, 12, 13]:  
        card_value = 10
    else:
        card_value = min(card_rank, 10)

    total_value += card_value
    current_value_label.config(text=f"Je huidige waarde is: {total_value}")

# Main Tkinter window initialization
root = tk.Tk()
root.title("Solitaire Showdown")

# Initial checks
check_current_directory()

directory_path = "D:\\pwscasinospell"

file_names = [
    "1_clubs.png",
    "1_diamonds.png",
    "1_hearts.png",
    "1_spades.png",
    "2_clubs.png",
    "2_diamonds.png",
    "2_hearts.png",
    "2_spades.png",
    "3_clubs.png",
    "3_diamonds.png",
    "3_hearts.png",
    "3_spades.png",
    "4_clubs.png",
    "4_diamonds.png",
    "4_hearts.png",
    "4_spades.png",
    "5_clubs.png",
    "5_diamonds.png",
    "5_hearts.png",
    "5_spades.png",
    "6_clubs.png",
    "6_diamonds.png",
    "6_hearts.png",
    "6_spades.png",
    "7_clubs.png",
    "7_diamonds.png",
    "7_hearts.png",
    "7_spades.png",
    "8_clubs.png",
    "8_diamonds.png",
    "8_hearts.png",
    "8_spades.png",
    "9_clubs.png",
    "9_diamonds.png",
    "9_hearts.png",
    "9_spades.png",
    "10_clubs.png",
    "10_diamonds.png",
    "10_hearts.png",
    "10_spades.png",
    "11_clubs.png",
    "11_diamonds.png",
    "11_hearts.png",
    "11_spades.png",
    "12_clubs.png",
    "12_diamonds.png",
    "12_hearts.png",
    "12_spades.png",
    "13_clubs.png",
    "13_diamonds.png",
    "13_hearts.png",
    "13_spades.png",
    "cardback.png",
]

for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    check_file_exists(file_path)

def update_bet_label(wallet_amount):
    player_bet_label.config(text=f"Plaats je inzet (maximaal €{wallet_amount}):")

# Labels and widgets for player information
range_label = tk.Label(root, text="Jouw toegewezen range is 20-22. Verdien 4x je inzet!")
range_label.pack(pady=5)

wallet_amount_label = tk.Label(root, text="Portemonnee: €1000")
wallet_amount_label.pack(pady=5)

player_bet_label = tk.Label(root, text="")
player_bet_label.pack(pady=5)

player_bet_entry = tk.Entry(root)
player_bet_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Frame for card buttons
deck_frame = tk.Frame(root)
deck_frame.pack()

# Create deck, shuffle it, and initialize variables
deck = create_deck()
random.shuffle(deck)

current_card = None
bet_button = None
total_value = 0
cards_drawn = []
bet_placed = False
total_value = 0

def create_new_deck():
    global deck
    response = messagebox.askyesno("Leeg Kaartendeck", "Het kaartendeck is leeg. Wil je een nieuw deck maken?")
    if response:
        deck = create_deck()
        random.shuffle(deck)
        display_card_backs()

def reveal_card():
    global current_card, bet_button
    if bet_placed:
        if deck:
            current_card = draw_from_deck()
            card_image = card_images.get(current_card)
            if card_image:
                card_button.config(image=card_image)
                card_button.image = card_image
                bet_button.config(state=tk.DISABLED)
                calculate_card_value(current_card)
            else:
                result_label.config(text="Afbeelding niet gevonden voor de kaart.")
        else:
            create_new_deck()
    else:
        result_label.config(text="Plaats eerst een inzet.")

def calculate_card_value(card):
    global total_value

    card_rank = int(card.split('_')[0])
    if card_rank in [11, 12, 13]:
        card_value = 10
    else:
        card_value = min(card_rank, 10)

    total_value += card_value
    current_value_label.config(text=f"Je huidige waarde is: {total_value}")

    if total_value >= 20 and total_value <= 22:
        handle_win()
    elif total_value > 22:
        handle_loss()
    else:
        # Ensure 'wallet_amount' is defined and has a valid value here
        wallet_text = wallet_amount_label.cget("text")
        wallet_amount = int(wallet_text.split(" ")[1][1:])
        update_bet_label(wallet_amount)  # Update bet label with the current wallet amount

def handle_win():
    global bet_placed, total_value

    bet_placed = False
    bet_amount = int(player_bet_entry.get())
    winnings = 4 * bet_amount

    wallet_text = wallet_amount_label.cget("text")
    wallet_amount = int(wallet_text.split(" ")[1][1:])
    wallet_amount -= bet_amount  # Deduct the bet amount
    wallet_amount += winnings  # Add 4 times the bet amount as winnings

    wallet_amount_label.config(text=f"Portemonnee: €{wallet_amount}")
    result_label.config(text=f"Gefeliciteerd! Je hebt €{winnings} gewonnen!")

    total_value = 0  # Reset the total value after a win

    play_again = messagebox.askyesno("Opnieuw spelen?", "Wil je opnieuw spelen?")
    if play_again:
        reset_game()
    else:
        root.destroy()

def handle_loss():
    global bet_placed, total_value

    bet_placed = False
    
    bet_amount = int(player_bet_entry.get())

    wallet_text = wallet_amount_label.cget("text")
    wallet_amount = int(wallet_text.split(" ")[1][1:])

    remaining_bet_amount = int(0.75 * bet_amount)
    wallet_amount -= remaining_bet_amount  # Deduct 75% of the bet amount after a loss

    wallet_amount_label.config(text=f"Portemonnee: €{wallet_amount}")
    result_label.config(text=f"Jammer! je hebt €{remaining_bet_amount} verloren!")
    total_value = 0  # Reset the total value after a loss

    play_again = messagebox.askyesno("Opnieuw spelen?", "Je hebt verloren. Wil je opnieuw spelen?")
    if play_again:
        reset_game()
    else:
        root.destroy()

def reset_game():
    global total_value, deck
    total_value = 0
    current_value_label.config(text="Je huidige waarde is: 0")
    result_label.config(text="")
    card_button.config(image=card_back_image)
    card_button.image = card_back_image

    if bet_placed:
        bet_amount = int(player_bet_entry.get())
        wallet_text = wallet_amount_label.cget("text")
        wallet_amount = int(wallet_text.split(" ")[1][1:])
        loss_amount = int(0.25 * bet_amount)
        wallet_amount -= bet_amount
        wallet_amount += loss_amount
        wallet_amount_label.config(text=f"Portemonnee: €{wallet_amount}")

    player_bet_entry.delete(0, tk.END)
    bet_button.config(state=tk.NORMAL)

def update_bet_label(wallet_amount):
    player_bet_label.config(text=f"Plaats je inzet (maximaal €{wallet_amount}):")

def place_bet():
    global bet_placed

    try:
        bet_amount = int(player_bet_entry.get())
        wallet_text = wallet_amount_label.cget("text")
        wallet_amount = int(wallet_text.split(" ")[1][1:])  # Extract wallet amount

        if bet_amount > 0 and bet_amount <= wallet_amount:
            bet_placed = True
            result_label.config(text=f"Je hebt €{bet_amount} ingezet.")
        else:
            result_label.config(text="Plaats een geldige inzet (tussen 1 en je portemonneebedrag).")
            bet_placed = False  # Reset bet_placed if the bet is not valid
    except ValueError:
        result_label.config(text="Voer een geldig bedrag in.")
        bet_placed = False  # Reset bet_placed if the input is not a number

    update_bet_label(wallet_amount)  # Update the bet label after placing the bet

# Update the bet label initially with the maximum wallet amount
wallet_text = wallet_amount_label.cget("text")
wallet_amount = int(wallet_text.split(" ")[1][1:])
update_bet_label(wallet_amount)

# Create a button to place bets
bet_button = tk.Button(root, text="Plaats inzet", command=place_bet)
bet_button.pack()

# Create a button to reveal cards
card_button = tk.Button(root, command=reveal_card)
card_button.pack(pady=25)

# Load the card images
card_images = load_card_images()

# Create a button to show the card back image
card_back_image = Image.open("cardback.png")
card_back_image = card_back_image.resize((100, 150))
card_back_image = ImageTk.PhotoImage(card_back_image)

card_back_button = tk.Button(root, image=card_back_image, command=reveal_card)
card_back_button.image = card_back_image  # Keep a reference to the image
card_back_button.pack()

current_value_label = tk.Label(root, text="Je huidige waarde is: 0")
current_value_label.pack()

# Start the Tkinter main loop
root.mainloop()


















