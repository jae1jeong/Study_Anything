import ast # 문법을 구조화 시켜준다.



with open('food_dict.txt',mode = 'r') as f:
	food_dict = ast.literal_eval(f.read()) # txt 파일을 문자 그대로 읽어들여 딕셔너리로 변환



def food_get():
	food_input = str(input("$ ")) # input
	while(1): # 무한루프 돌면서 input이 exit이면 나가게 만들고 start면 시작하게 만든다.
		if food_input == 'exit':
			print("Exited")
			break
		elif food_input == 'start':
			all_show()
			a = str(input('음식을 골라 주세요: '))
			if a == 'exit':
				print('Exited')
				break
			else:
				show(a)
				return a
			# input 값 리턴
		else:
			print("잘못 입력하였습니다.") # 이외에 다른 것을 입력한다면 다시 함수 호출
			food_get()



def show(list):
	k= {key:val for key,val in food_dict.items() if key == list or val == list} # Dictionary Comprehension 으로 리턴된 값이 키 값과 일치하는지 여부를 확인하는 변수이다. 없으면 {}
	if k == {}:
		print("찾으시는 음식이 없습니다.")
	else:
		print(f'상극의 음식은 {k}입니다.')
	food_get()


def all_show(): # food_dict의 key 값, value 값을 모두 출력하여 보여준다.
	ls = list()
	for k in food_dict.values(): # 값들을 리스트로 추가
		ls.append(k)
	for i in food_dict.keys(): # 키값들을 리스트로 추가
		ls.append(i)
	print(ls) # 리스트 출력


if __name__ == '__main__':
	food_get()



#숙제 7-4 3의 배수로  self study 7.2