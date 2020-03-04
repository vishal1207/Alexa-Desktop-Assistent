import speech_recognition as speech

import webbrowser as web
import urllib
import re
def speech_to_text():
    r = speech.Recognizer()
    m = speech.Microphone()
    with m :
        print('SPEAK !')
        audio = r.record(m,duration=4)
        print("ANALYSING !! ")
        result = {"success": True,"error": None,"text": None}
        try:
            result["text"] = r.recognize_google(audio)
        except speech.RequestError:
            result["success"] = False
            result["error"] = "API unavailable"
        except speech.UnknownValueError:
            result["error"] = "Unable to recognize speech"
            print(result["error"])
            exit()
    return result

result=speech_to_text()
query = str(result['text'])
if ('play' in query ):
    query_string=query.replace(" ","+")
    print(query.replace("play","playing"))
    url="https://www.youtube.com/results?search_query="+query_string
    html_cont = urllib.request.urlopen(url)
    search_res = re.findall(r'href=\"\/watch\?v=(.{11})', html_cont.read().decode())
    web.open_new("http://www.youtube.com/watch?v={}".format(search_res[0]))
else:
    print("We can to the search for you:")
    print("Searching for query: ",query)
    query_string=query.replace(" ","+")
    url="https://www.bing.com/search?q="+query_string.replace("search","")
    web.open_new(url)

    

