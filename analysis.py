import xlrd
import xlsxwriter
from konlpy.tag import Twitter
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

## 엑셀 읽기 작업
# 엑셀 지정
read_workbook = xlrd.open_workbook("naver news.xlsx")
# 엑셀 시트 지정
worksheet = read_workbook.sheet_by_index(0)
# 엑셀 줄 수 가져오기
nrow = worksheet.nrows

# Excel 작성 작업
write_workbook = xlsxwriter.Workbook('./naver news 분석결과.xlsx')

# 트위터 형태소 분석기 가져오기
twitter = Twitter()

noun_list = list()
noun_dict = dict()

verb_list = list()
verb_dict = dict()


# 엑셀 줄 수 만큼 for문
for i in range(1, nrow):
  news_contents = worksheet.cell_value(i, 2)

  # twitter_list라는 변수에다가 트위터 형태소 분석기를 사용해 나온 결과물을 저장
  twitter_list = twitter.pos(news_contents)

  # 트위터 형태소 분석기의 결과를 차례대로 출력
  for word in twitter_list:

    # 만약 분석결과가 "명사"일 때
    if word[1] == "Noun":
      noun_list.append(word[0])

    # 만약 분석결과가 "동사"일 때
    elif word[1] == "Verb":
      verb_list.append(word[0])

print("--------명사---------")
for i in noun_list:
  noun_dict.setdefault(i, 0)
  noun_dict[i] += 1

for i in noun_dict:
  print(f"단어 : {i} // 출현횟수 : {noun_dict.get(i)}")

print("--------동사---------")
for i in verb_list:
  verb_dict.setdefault(i, 0)
  verb_dict[i] += 1

for i in verb_dict:
  print(f"단어 : {i} // 출현횟수 : {verb_dict.get(i)}")



# 명사 엑셀시트 추가 및 내용 작성
write_worksheet = write_workbook.add_worksheet("명사")
write_worksheet.write(0, 0, "명사 번호")
write_worksheet.write(0, 1, "명사 내용")
write_worksheet.write(0, 2, "명사 빈도수")

for i_index, i in enumerate(noun_dict):
  write_worksheet.write(i_index + 1, 0, i_index + 1)
  write_worksheet.write(i_index + 1, 1, i)
  write_worksheet.write(i_index + 1, 2, noun_dict.get(i))

# 동사 엑셀시트 추가 및 내용 작성
write_worksheet = write_workbook.add_worksheet("동사")
write_worksheet.write(0, 0, "동사 번호")
write_worksheet.write(0, 1, "동사 내용")
write_worksheet.write(0, 2, "동사 빈도수")

for i_index, i in enumerate(verb_dict):
  write_worksheet.write(i_index + 1, 0, i_index + 1)
  write_worksheet.write(i_index + 1, 1, i)
  write_worksheet.write(i_index + 1, 2, verb_dict.get(i))


write_workbook.close()
