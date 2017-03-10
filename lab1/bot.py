from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()
#for emotions anger disgust fear joy sadness surprise
initials = [0] * 6
averages = [0] * 6
counter = 0

@module.rule('')
def hi(bot, trigger):
    global initials, averages, counter
    #connected_nicks.append(trigger.nick)
    #print(connected_nicks)
    #print(emo.detect_emotion_in_raw_np(str(trigger)))
    #print(trigger, trigger.nick)
    bot.say('Hi, ' + trigger.nick)

    emotions_list = emo.detect_emotion_in_raw_np(trigger)
    counter = counter + 1 # her seferinde counter donusumlu artiyor.
    for i in range(len(emotions_list)):
        initials[i] += emotions_list[i]
        averages[i] = initials[i] / counter

    print("Anger:{} , Disgust:{} , Fear:{} , Joy:{} , Sadness: {} , Suprise:{} ".format(str(averages[0]),str(averages[1]),str(averages[2]),str(averages[3]),str(averages[4]),str(averages[5])))
