________________________________________________________________________________

# English Version
### How to write a script

I use Python. I did it at 3.5 or 3.6.\
`python main.py <streamerUsername>`... nothing happens.\
`python main.py <streamerUsername> --v` or --verbose to receive the data that occurs when you scroll down the page.\
`python main.py <streamerUsername> --d` or --download-clips t download 20 clips. --v and --d can be used simultaneously.

If you want to download more than 20, enter a number after --l or --limit.  There may be more than 100.\
When downloading, only 'one week' clips are targeted like clip pages.\
You can choose how old are the clips
* For all period, `--filter-type ALL_TIME`
* For 24 hours `--filter-type LAST_DAY`
* For 30 days `--filter-type LAST_MONTH`

Example : get top 150 clips from past month\
(didn't understand this part)\
`pythong main.py <streamerUsername> --d --l 150 --f LAST_MONTH`

If you want to know what images or data you refer to without downloading, use `--v` instead of `--d`

In my case, for whatver reason, it was canceled during the download , but I think the clip title might contain contain characters that should not be used in filenames. For example, `~, #, %, *, ;` etc.

Uh ... please pull request.

### How to find  CLIENT-ID
1) Enter the twitch clip page.
2) Press F12 to enter the Network tab.
3) Refresh with F5
4) Click on gql.
5) Look for 'client-id' in the 'Headers' section under the 'Request Headers' section.
6) Click > Drag to highlight and copy.

### LifeTime
Come to the YouTube channel and subscribe, and donate. In 2027 I want to build better education. So please ask for donation to keep it alive until then.

[YouTube channel](https://www.youtube.com/channel/UC0i0OcWfKJwCPzmPdxZ7ylQ)\
[Donate Patreon](https://www.patreon.com/youngim)\
Paypal email: chulman444@gmail.com
