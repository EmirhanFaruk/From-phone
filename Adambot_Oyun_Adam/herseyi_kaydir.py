def herseyi_kaydir(adambot, monitor_buyuklugu, obje_listesi_listesi):
    if not(adambot.x < monitor_buyuklugu[0]*3/4 and adambot.x > monitor_buyuklugu[0]/4):
        #if adambot.x < monitor_buyuklugu[0]/4:
        adambot.x -= adambot.ivme[0]
        for obje_listesi_sayaci in range(len(obje_listesi_listesi)):
            for obje_sayaci in range(len(obje_listesi_listesi[obje_listesi_sayaci])):
            	obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].x -= adambot.ivme[0]
    if not(adambot.y < monitor_buyuklugu[1]*3/4 and adambot.y > monitor_buyuklugu[1]/4):
        adambot.y -= adambot.ivme[1]
        for obje_listesi_sayaci in range(len(obje_listesi_listesi)):
            for obje_sayaci in range(len(obje_listesi_listesi[obje_listesi_sayaci])):
            	obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].y -= adambot.ivme[1]
    return adambot, obje_listesi_listesi

def herseyi_kaydir(adambot, monitor_buyuklugu, obje_listesi_listesi):
    if adambot.x != monitor_buyuklugu[0]/2 or adambot.y - adambot.yerden_yukseklik/2 != monitor_buyuklugu[1]/2:
        x_farki = -(adambot.x - monitor_buyuklugu[0]/2)
        y_farki = -(adambot.y - adambot.yerden_yukseklik/2 - monitor_buyuklugu[1]/2)
        
        adambot.x += x_farki*0.1
        adambot.y += y_farki*0.1
        for obje_listesi_sayaci in range(len(obje_listesi_listesi)):
            for obje_sayaci in range(len(obje_listesi_listesi[obje_listesi_sayaci])):
            	obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].x += x_farki*0.1
            	obje_listesi_listesi[obje_listesi_sayaci][obje_sayaci].y += y_farki*0.1

    return adambot, obje_listesi_listesi