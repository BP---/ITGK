def logg(var):
    for x in range(len(var[0])):    
        print('Msg ', x + 1 ,' ', var[0][x],' ', var[1][x], ' sendte foelgende melding: "', var[2][x],'"', sep='')
def main():
    text = [["23:59","0:00","0:03","0:09","0:09","0:09"],["mr.x","Mdm.Evil","Dr.love","Mr.x","Mr.X","Dr.love"],["Har du mottatt pakken?", "Ja. pakken er mottat", "All you need is love!", "Dr.love, love, calling Dr.love.", "Dr.love, Dr.love wake up now.", "up now!"]]
    logg(text)
main()
    
    
