# conversion_logic.py

# Full mapping of Paleo-Hebrew characters to Egyptian hieroglyphs
PALEO_HEBREW_TO_EGYPTIAN = {
    # Aleph - Ox
    '𐤀': '𓀀',  # Aleph (Ox) -> Egyptian Ox
    # Bet - House
    '𐤁': '𓃀',  # Bet (House) -> Egyptian House
    # Gimel - Camel
    '𐤂': '𓎼',  # Gimel (Camel) -> Egyptian Camel
    # Dalet - Door
    '𐤃': '𓂀',  # Dalet (Door) -> Egyptian Door
    # He - Window
    '𐤄': '𓉔',  # He (Window) -> Egyptian Window
    # Vav - Hook
    '𐤅': '𓋴',  # Vav (Hook) -> Egyptian Hook
    # Zayin - Sword
    '𐤆': '𓆇',  # Zayin (Sword) -> Egyptian Sword
    # Chet - Fence
    '𐤇': '𓆸',  # Chet (Fence) -> Egyptian Fence
    # Tet - Basket
    '𐤈': '𓋞',  # Tet (Basket) -> Egyptian Basket
    # Yod - Hand
    '𐤉': '𓂝',  # Yod (Hand) -> Egyptian Hand
    # Kaf - Palm
    '𐤊': '𓃌',  # Kaf (Palm) -> Egyptian Palm
    # Lamed - Ox Goad
    '𐤋': '𓃾',  # Lamed (Ox Goad) -> Egyptian Ox Goad
    # Mem - Water
    '𐤌': '𓈖',  # Mem (Water) -> Egyptian Water
    # Nun - Fish
    '𐤍': '𓆇',  # Nun (Fish) -> Egyptian Fish
    # Samekh - Support
    '𐤎': '𓋤',  # Samekh (Support) -> Egyptian Support
    # Ayin - Eye
    '𐤏': '𓂀',  # Ayin (Eye) -> Egyptian Eye
    # Pe - Mouth
    '𐤐': '𓂋',  # Pe (Mouth) -> Egyptian Mouth
    # Tsade - Fishhook
    '𐤑': '𓆣',  # Tsade (Fishhook) -> Egyptian Fishhook
    # Qof - Monkey
    '𐤒': '𓆷',  # Qof (Monkey) -> Egyptian Monkey
    # Resh - Head
    '𐤓': '𓅱',  # Resh (Head) -> Egyptian Head
    # Shin - Teeth
    '𐤔': '𓄿',  # Shin (Teeth) -> Egyptian Teeth
    # Tav - Mark
    '𐤕': '𓂝',  # Tav (Mark) -> Egyptian Mark

    # Final Forms (optional usage in the word)
    '𐤖': '𓀀',  # Final Aleph (Ox) -> Egyptian Ox
    '𐤗': '𓃀',  # Final Bet (House) -> Egyptian House
    '𐤘': '𓎼',  # Final Gimel (Camel) -> Egyptian Camel
    '𐤙': '𓂀',  # Final Dalet (Door) -> Egyptian Door
    '𐤚': '𓉔',  # Final He (Window) -> Egyptian Window
    '𐤛': '𓋴',  # Final Vav (Hook) -> Egyptian Hook
    '𐤜': '𓆇',  # Final Zayin (Sword) -> Egyptian Sword
    '𐤝': '𓆸',  # Final Chet (Fence) -> Egyptian Fence
    '𐤞': '𓋞',  # Final Tet (Basket) -> Egyptian Basket
    '𐤟': '𓂝',  # Final Yod (Hand) -> Egyptian Hand
    '𐤠': '𓃌',  # Final Kaf (Palm) -> Egyptian Palm
    '𐤡': '𓃾',  # Final Lamed (Ox Goad) -> Egyptian Ox Goad
    '𐤢': '𓈖',  # Final Mem (Water) -> Egyptian Water
    '𐤣': '𓆇',  # Final Nun (Fish) -> Egyptian Fish
    '𐤤': '𓋤',  # Final Samekh (Support) -> Egyptian Support
    '𐤥': '𓂀',  # Final Ayin (Eye) -> Egyptian Eye
    '𐤦': '𓂋',  # Final Pe (Mouth) -> Egyptian Mouth
    '𐤧': '𓆣',  # Final Tsade (Fishhook) -> Egyptian Fishhook
    '𐤨': '𓆷',  # Final Qof (Monkey) -> Egyptian Monkey
    '𐤩': '𓅱',  # Final Resh (Head) -> Egyptian Head
    '𐤪': '𓄿',  # Final Shin (Teeth) -> Egyptian Teeth
    '𐤫': '𓂝',  # Final Tav (Mark) -> Egyptian Mark
}

def convert_to_egyptian(paleo_text):
    egyptian_text = ""
    for char in paleo_text:
        if char in PALEO_HEBREW_TO_EGYPTIAN:
            egyptian_text += PALEO_HEBREW_TO_EGYPTIAN[char]
        else:
            egyptian_text += char  # If no mapping found, just append the character as is
    return egyptian_text
