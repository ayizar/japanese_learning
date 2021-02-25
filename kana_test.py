#!/usr/bin/env python3
import sys
import random

# a list of characters in the Japanese hiragana alphabet
hiragana_list = ["あ","お","い","え","う","か","こ","き","け","く","さ","し","す","せ","そ",
"た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も",
"や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ",
"だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ","きゃ","きゅ","きょ","しゃ","しゅ","しょ",
"ちゃ","ちゅ","ちょ","にゃ","にゅ","にょ","ひゃ","ひゅ","ひょ","みゃ","みゅ","みょ","りゃ","りゅ","りょ",
"ぎゃ","ぎゅ","ぎょ","じゃ","じゅ","じょ","ぢゃ","ぢゅ","ぢょ","びゃ","びゅ","びょ","ぴゃ","ぴゅ","ぴょ"]

# a dictionary of the phonetic sounds the hiragana characters correspond to
hiragana = {
    "あ":"a", "い":"i", "う":"u", "え":"e", "お":"o",
    "か":"ka", "き":"ki", "く":"ku", "け":"ke", "こ":"ko",
    "さ":"sa", "し":"shi", "す":"su", "せ":"se", "そ":"so",
    "た":"ta", "ち":"chi", "つ":"tsu", "て":"te", "と":"to",
    "な":"na", "に":"ni", "ぬ":"nu", "ね":"ne", "の":"no",
    "は":"ha", "ひ":"hi", "ふ":"fu", "へ":"he", "ほ":"ho",
    "ま":"ma", "み":"mi", "む":"mu", "め":"me", "も":"mo", 
    "や":"ya", "ゆ":"yu", "よ":"yo",
    "ら":"ra", "り":"ri", "る":"ru", "れ":"re", "ろ":"ro",
    "わ":"wa", "を":"o", "ん":"n",
    "が":"ga", "ぎ":"gi", "ぐ":"gu", "げ":"ge", "ご":"go",
    "ざ":"za", "じ":"ji", "ず":"zu", "ぜ":"ze", "ぞ":"zo",
    "だ":"da", "ぢ":"ji", "づ":"dzu", "で":"de", "ど":"do",
    "ば":"ba", "び":"bi", "ぶ":"bu", "べ":"be", "ぼ":"bo",
    "ぱ":"pa", "ぴ":"pi", "ぷ":"pu", "ぺ":"pe", "ぽ":"po",
    "きゃ":"kya", "きゅ":"kyu", "きょ":"kyo",
    "しゃ":"sha", "しゅ":"shu", "しょ":"sho",
    "ちゃ":"cha", "ちゅ":"chu", "ちょ":"cho",
    "にゃ":"nya", "にゅ":"nyu", "にょ":"nyo",
    "ひゃ":"hya", "ひゅ":"hyu", "ひょ":"hyo",
    "みゃ":"mya", "みゅ":"myu", "みょ":"myo",
    "りゃ":"rya", "りゅ":"ryu", "りょ":"ryo",
    "ぎゃ":"gya", "ぎゅ":"gyu", "ぎょ":"gyo",
    "じゃ":"ja", "じゅ":"ju", "じょ":"jo",
    "ぢゃ":"ja", "ぢゅ":"ju", "ぢょ":"jo",
    "びゃ":"bya", "びゅ":"byu", "びょ":"byo",
    "ぴゃ":"pya", "ぴゅ":"pyu", "ぴょ":"pyo"
}

# a list of characters in the Japanese katakana alphabet
katakana_list = ["ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","サ","シ","ス","セ","ソ",
"タ","チ","ツ","テ","ト","ナ","ニ","ヌ","ネ","ノ","ハ","ヒ","フ","ヘ","ホ","マ","ミ","ム","メ","モ",
"ヤ","ユ","ヨ","ラ","リ","ル","レ","ロ","ワ","ヲ","ン","ガ","ギ","グ","ゲ","ゴ","ザ","ジ","ズ","ゼ","ゾ",
"ダ","ヂ","ヅ","デ","ド","バ","ビ","ブ","ベ","ボ","パ","ピ","プ","ペ","ポ","キャ","キュ","キョ","シャ","シュ","ショ",
"チャ","チュ","チョ","ニャ","ニュ","ニョ","ヒャ","ヒュ","ヒョ","ミャ","ミュ","ミョ","リャ","リュ","リョ",
"ギャ","ギュ","ギョ","ジャ","ジュ","ジョ","ヂャ","ヂュ","ヂョ","ビャ","ビュ","ビョ","ピャ","ピュ","ピョ"]

# a dictionary of the phonetic sounds the katakana characters correspond to
katakana = {
    "ア":"a", "イ":"i", "ウ":"u", "エ":"e", "オ":"o", 
    "カ":"ka", "キ":"ki", "ク":"ku", "ケ":"ke", "コ":"ko", 
    "サ":"sa", "シ":"shi", "ス":"su", "セ":"se", "ソ":"so",
    "タ":"ta", "チ":"chi", "ツ":"tsu", "テ":"te", "ト":"to",
    "ナ":"na", "ニ":"ni", "ヌ":"nu", "ネ":"ne", "ノ":"no",
    "ハ":"ha", "ヒ":"hi", "フ":"fu", "ヘ":"he", "ホ":"ho",
    "マ":"ma", "ミ":"mi", "ム":"mu", "メ":"me", "モ":"mo",
    "ヤ":"ya", "ユ":"yu", "ヨ":"yo",
    "ラ":"ra", "リ":"ri", "ル":"ru", "レ":"re", "ロ":"ro", 
    "ワ":"wa", "ヲ":"o", "ン":"n", 
    "ガ":"ga", "ギ":"gi", "グ":"gu", "ゲ":"ge", "ゴ":"go",
    "ザ":"za", "ジ":"ji", "ズ":"zu", "ゼ":"ze", "ゾ":"zo", 
    "ダ":"da", "ヂ":"ji", "ヅ":"dzu", "デ":"de", "ド":"do",
    "バ":"ba", "ビ":"bi", "ブ":"bu", "ベ":"be", "ボ":"bo",
    "パ":"pa", "ピ":"pi", "プ":"pu", "ペ":"pe", "ポ":"po",
    "キャ":"kya", "キュ":"kyu", "キョ":"kyo",
    "シャ":"sha", "シュ":"shu", "ショ":"sho",
    "チャ":"cha", "チュ":"chu", "チョ":"cho",
    "ニャ":"nya", "ニュ":"nyu", "ニョ":"nyo",
    "ヒャ":"hya", "ヒュ":"hyu", "ヒョ":"hyo",
    "ミャ":"mya", "ミュ":"myu", "ミョ":"myo",
    "リャ":"rya", "リュ":"ryu", "リョ":"ryo",
    "ギャ":"gya", "ギュ":"gyu", "ギョ":"gyo",
    "ジャ":"ja", "ジュ":"ju", "ジョ":"jo",
    "ヂャ":"ja", "ヂュ":"ju", "ヂョ":"jo",
    "ビャ":"bya", "ビュ":"byu", "ビョ":"byo",
    "ピャ":"pya", "ピュ":"pyu", "ピョ":"pyo"
}

# shuffles the characters before beginning the test
# the user is prompted with a character, and must type the corresponding phonetic English
# if the typed answer is correct, a checkmark is displayed
# otherwise, an x is displayed, along with the correct phonetic pronunciation
# a percentage score is displayed once the user has gone through every character
def kana_test (kana_list, kana):
    count = 0
    random.shuffle(kana_list)
    for ch in kana_list:
        q = input(ch + ": ")
        if q == kana[ch]:
            print("🗸")
            count += 1
        else: print("✘: " + kana[ch])
    
    print(str(100 * count / len(kana)) + "%")

# offers the choice between a test for just hiragana, just katakana, or a simultaneous test for both
# if none of these options are correctly typed, the console shows it is an invalid request
test_choice = input("test for hiragana, katakana, or both? ")
if test_choice == "hiragana":
    kana_test(hiragana_list, hiragana)
elif test_choice == "katakana":
    kana_test(katakana_list, katakana)
elif test_choice == "both":
    kana_list = list(set(hiragana_list) | set(katakana_list))
    kana = {**hiragana, **katakana}
    kana_test(kana_list, kana)
else:
    print("Invalid Selection")
