#Practice WordCloud(Trump)
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
f = open("C:\\Users\\GNsoft\\Desktop\\TrumpSpeech.txt")  #텍스트 파일 열기 (트럼프 취임 연설문)
lines = f.readlines()[0] #파일에 있는 모든 문자열 리스트를 반환, readline은 한줄씩 읽고 반환
f.close() #파일 닫기
lines[0:100] #0번부터 100자까지 읽기
tokenizer = RegexpTokenizer('[\w]+') #특수문자등 처리기
stop_words = stopwords.words('english') #영어로 처리
words = lines.lower() #모든 단어를 소문자로 변경
tokens = tokenizer.tokenize(words) #소문자로 변경된 string을 불용어 및 한 글자들 제거 후 단어 단위로 토큰화
stopped_tokens = [ i for i in list((tokens)) if not i in stop_words] 
stopped_tokens2 = [i for i in stopped_tokens if len(i)>1] #최종 단어 리스트
pd.Series(stopped_tokens2).value_counts().head(10) #빈도 수 상위 10개 (head(10)) 단어 반환
from wordcloud import WordCloud #word cloud를 사용하기 위한 추가, 처음이라면 Jupiter command 창에 'pip install wordcloid' 입력
from collections import Counter
font_path = 'C:\\Users\\GNsoft\\Desktop\\Nanum.ttf' #사용할 폰트 경로
wordcloud = WordCloud(
font_path = font_path, #폰트 설정
width = 800, #이미지의 너비
height = 800, #이미지의 높이
background_color = "white" #배경 화면
)
count = Counter(stopped_tokens2) #토큰화 된 단어 수를 카운트
wordcloud = wordcloud.generate_from_frequencies(count) #count 변수로 wordcloud 객체 생성 자세히 모름
def __array__(self): #함수 생성
    """Convert to numpy array.
    Returns
    ------
    image : nd-array size(width, height, 3)
        Word cloud image as numpy matrix.
    """
    return self.to_array()
def to_array(self): #함수 생성
    """Converty to numpy array.
    Returns
    --------
    image : nd-array size (width, height, 3)
        Word cloud image as numpy matrix
    """
    return np.array(self.to_image())
array = wordcloud.to_array()
%matplotlib inline #Jupiter Notebook을 실행한 브라우저에서 바로 그림을 볼 수 있게 해줌
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 10)) #한 화면에 여러 그래프를 그림
plt.imshow(array, interpolation="bilinear") #이미지를 시각화
plt.show() #화면 출력?
fig.savefig('wordcloid.png')