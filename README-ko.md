# MY CLIP MY MONEY

### 스크립트 쓰는 법

파이썬을 사용한다. 나는 3.5인가 3.6에서 했다.

`python main.py 스트리머닉네임`을 하면 ... 아무것도 안된다.

`python main.py 스트리머닉네임 --v` 혹은 --v대신 --verbose를 하면 스크롤을 내릴때 발생되는 데이터를 받는다.

`python main.py 스트리머닉네임 --d` 혹은 --d대신 --download-clips 하면 클림 20개를 다운로드 받는다. --v와 --d 동시 사용가능.

20개 이상 다운 받고 싶으면 --l 혹은 --limit 후 숫자를 입력한다. 100개 이상도 된다.

다운로드할때는 클립 페이지 처럼 '1주일'치 클립들만 타겟되는데, 모든 기간에서 받고 싶다면 `--filter-type ALL_TIME` 옵션을 추가 해준다. 24시간은 `LAST_DAY`, 30일 은 `LAST_MONTH` 이다.

30일 클립중 '이번달 TOP 150 클립!!!' 이라는 제목으로 영상을 올리고 싶어서 클립들을 다운받고 싶으면 (다운로드 날로부터 지난 30일인지 그달 1일 부터 마지막 일까지인지 모른다) 밑의 커맨드를 사용한다.

`pythong main.py 스트리머닉네임 --d --l 150 --f LAST_MONTH`

다운받지 않고 어떤 영상혹은 데이터를 참고하는지 알고 싶으면 `--d` 대신 `--v`를 쓰면 된다.

나 같은 경우 어떤 이유에서인지 다운로드중 취소되었는데 (영상 참고), 재 생각에는 클립 제목에 파일 이름에 쓰이면 안되는 문자가 들어있는듯 하다. 예를 들어 `~, #, %, *, ;` 등등.

어... pull request me please.

### CLIENT-ID 찾는 법

1) 트위치 클립 페이지에 들어간다.
2) F12를 누르고 네트워크 탭으로 들어간다.
3) F5로 새로고침 한번다한다.
4) gql이라 써져있는 것을 클릭한다.
5) Headers, Preview, Response 등등 나와있는 패널이 나오거나 있을텐데, Headers 탭에서 'Request Headers' 섹션 아래에 있는 'client-id'를 찾는다.
6) 클릭 > 드래그 해서 하이라이트 한후 복사한다.

### 연명

유튜브 채널로 와서 구독, 그리고 기부도 좀 해봐라. 2027년에는 내가 더 좋은 교육을 세우고 싶다. 그러니깐 그때까지 연명하기 위해 기부를 부탁한다.

[유튜브 채널](https://www.youtube.com/channel/UC0i0OcWfKJwCPzmPdxZ7ylQ)

[기부 patreon](https://www.patreon.com/youngim)

Paypal 이메일: chulman444@gmail.com
