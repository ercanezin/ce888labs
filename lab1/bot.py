from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()
connected_nicks=[]

@module.rule('')
def hi(bot, trigger):
    connected_nicks.append(trigger.nick)
    print(connected_nicks)
    print(emo.detect_emotion_in_raw_np(str(trigger)))
    print(trigger, trigger.nick)
   # bot.say('Hi, ' + trigger.nick)




