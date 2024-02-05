import bs4, gtts
from gtts import gTTS

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    # 使用BeautifulSoup解析HTML文本
    soup = bs4.BeautifulSoup(text, 'html.parser')

    # 通过类名找到新闻故事块
    story_blocks = soup.find_all(class_='story-text')

    # 提取标题和简要内容
    stories = []
    for block in story_blocks:
        title = block.find('h3', class_='title').get_text(strip=True)
        teaser = block.find('p', class_='teaser').get_text(strip=True) if block.find('p', class_='teaser') else ''
        stories.append((title, teaser))

    return stories

    
def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    # 检查索引是否在有效范围内
    if 0 <= n < len(stories):
        title, teaser = stories[n]

        # 合成文本到语音
        text_to_speech = f"{title}. {teaser}"
        tts = gTTS(text=text_to_speech, lang='en')

        # 保存合成的音频到文件
        tts.save(filename)
        print(f"Audio for story {n + 1} saved to {filename}")
    else:
        print(f"Invalid story index: {n}")