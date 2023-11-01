import pprint
import googletrans

trans = googletrans.Translator()

# pprint.pprint(googletrans.LANGUAGES)

result1 = trans.translate("안녕하세요.", dest='en')
result2 = trans.translate("안녕하세요.", dest='ja')
result3 = trans.translate("안녕하세요.", dest='zh-cn')

print(result1.text)
print(result2.text)
print(result3.text)
