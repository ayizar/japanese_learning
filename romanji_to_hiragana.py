#!/usr/bin/env python3
import sys

# a dictionary of hiragana characters and the phonetic sounds they correspond to
hiragana = {
    "a":"あ", "i":"い", "u":"う", "e":"え", "o":"お",
    "ka":"か", "ki":"き", "ku":"く", "ke":"け", "ko":"こ",
    "sa":"さ", "shi":"し", "su":"す", "se":"せ", "so":"そ",
    "ta":"た", "chi":"ち", "tsu":"つ", "te":"て", "to":"と",
    "na":"な", "ni":"に", "nu":"ぬ", "ne":"ね", "no":"の",
    "ha":"は", "hi":"ひ", "fu":"ふ", "he":"へ", "ho":"ほ",
    "ma":"ま", "mi":"み", "mu":"む", "me":"め", "mo":"も", 
    "ya": "や", "yu":"ゆ", "yo":"よ",
    "ra":"ら", "ri":"り", "ru":"る", "re":"れ", "ro":"ろ",
    "wa":"わ", "n":"ん",
    "ga":"が", "gi":"ぎ", "gu":"ぐ", "ge":"げ", "go":"ご",
    "za":"ざ", "ji":"じ", "zu":"ず", "ze":"ぜ", "zo":"ぞ",
    "da":"だ", "ji":"ぢ", "zu":"づ", "de":"で", "do":"ど",
    "ba":"ば", "bi":"び", "bu":"ぶ", "be":"べ", "bo":"ぼ",
    "pa":"ぱ", "pi":"ぴ", "pu":"ぷ", "pe":"ぺ", "po":"ぽ",
    "kya":"きゃ", "kyu":"きゅ", "kyo:":"きょ",
    "sha":"しゃ", "shu":"しゅ", "sho":"しょ",
    "cha":"ちゃ", "chu":"ちゅ", "cho":"ちょ",
    "nya":"にゃ", "nyu":"にゅ", "nyo":"にょ",
    "hya":"ひゃ", "hyu":"ひゅ", "hyo":"ひょ",
    "mya":"みゃ", "myu":"みゅ", "myo":"みょ",
    "rya":"りゃ", "ryu":"りゅ", "ryo":"りょ",
    "gya":"ぎゃ", "gyu":"ぎゅ", "gyo":"ぎょ",
    "ja":"じゃ", "ju":"じゅ", "jo":"じょ",
    "ja":"ぢゃ", "ju":"ぢゅ", "jo":"ぢょ",
    "bya":"びゃ", "byu":"びゅ", "byo":"びょ",
    "pya":"ぴゃ", "pyu":"ぴゅ", "pyo":"ぴょ"
}

# converts the typed romanji string to hiragana, based on the rules of 
# japanese word construction and using the above dictionary
def rom_to_hira (romanji):
    hira_str = ""
    ch = ""
    for letter in romanji:
        if ch == "n" and letter not in {"a","e","i","o","u"}:
            hira_str += hiragana[ch]
            ch = ""
        if len(ch) > 0 and letter == ch[len(ch)-1]:
            hira_str += "っ"
        else:
            ch += letter
        if letter in {"a","e","i","o","u"}:
            hira_str += hiragana[ch]
            ch = ""
    if ch == "n":
        hira_str += hiragana[ch]
    return hira_str

# requests a word or character from the user until 'esc' is typed
input_str = input("Give me a word (romanji)! ")
while input_str != "esc":
    hira = rom_to_hira(input_str)
    print(hira)
    input_str = input("Give me a word (romanji)! ")
