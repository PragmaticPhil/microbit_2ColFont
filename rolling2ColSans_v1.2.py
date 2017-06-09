from microbit import *
# WHALEYSANS_INTEGERS designed by David Whale (@WhaleyGeek) and replicated here verbatim
# PHILSANS_TEXT alpha font 100% inspired by WHALEYSANS_INTEGERS, and implementation method borrowed from @WhaleyGeek
# so, all credit for inspiration to: https://github.com/whaleygeek/mb_clock/blob/master/clock.py

# The purpose of this app is to scroll chars from the WhaleySans integer font and the PHILSANS_TEXT alpha font.
# At the time of writing Python does not scroll images wider than 5 pixels using display.show
# an implementation of that scrollLargeImage(imageDataStr, delay) has been built, and could be extracted

WHALEYSANS_INTEGERS = (
("99","99","99","99","99"),
("09","09","09","09","09"),
("99","09","99","90","99"),
("99","09","99","09","99"),
("90","90","99","09","09"),
("99","90","99","09","99"),
("99","90","99","99","99"),
("99","09","09","09","09"),
("99","99","00","99","99"),
("99","99","99","09","99")
)

PHILSANS_TEXT = (
("00", "00", "99", "99", "09"),     # a
("90", "90", "90", "99", "99"),     # b
("00", "00", "99", "90", "99"),     # c
("09", "09", "99", "99", "99"),     # d
("99", "90", "99", "90", "99"),     # e
("99", "90", "99", "90", "90"),     # f
("99", "99", "09", "09", "99"),     # g
("90", "90", "99", "99", "99"),     # h
("90", "00", "90", "90", "90"),     # i
("09", "00", "09", "49", "99"),     # j
("92", "97", "90", "97", "92"),     # k
("90", "90", "90", "90", "96"),     # l
("90", "09", "90", "09", "90"),     # m
("00", "00", "99", "99", "99"),     # n
("00", "99", "99", "99", "00"),     # o
("99", "99", "94", "90", "90"),     # p
("00", "99", "99", "49", "09"),     # q
("00", "00", "99", "90", "90"),     # r
("99", "90", "99", "09", "99"),     # s
("00", "90", "99", "90", "99"),     # t
("00", "00", "99", "99", "99"),     # u
("00", "00", "99", "99", "44"),     # v
("09", "90", "09", "90", "09"),     # w
("99", "44", "99", "44", "99"),     # x
("00", "99", "99", "09", "99"),     # y
("00", "99", "09", "90", "99"),     # z
)

def show2ColSansNumber(n):                # displaying integers is less costly (doesn't use getCharRef), so make a special case for it
    show2ColSansString(str(n), True)

def show2ColSansString(showStr, isInt):             # pass in the string to show and a flag indicating if it is int or str     
    rawImageStrData = ["", "", "", "", ""]          # a nice clean and new string for each ROW in image to show on 5x5 LED matrix
    for i in range(len(showStr)):                   # extract each char in turn from string we are showing
        currentChar = getFontSet(showStr[i], isInt)    # currentChar set as pointer to a 5 record array, e.g. ("00", "99", "99", "09", "99")
        for j in range(5):                          # we now review the raw data for char and extract and add it to our long render str
            rawImageStrData[j] += (currentChar[j] + "0")    # the +"0" bit adds a blank column between chars.
    convertImageDataToImage(rawImageStrData)        # here we have a long (more than 5 cols) image data set - we send it off to render into frames.

def getFontSet(showChar, isInt):                          # a pointer to either WHALEYSANS_INTEGERS or PHILSANS_TEXT
    if(isInt):                                           # isInt is TRUE if WHOLE input to function was integer (so does not refer to just this char)
        return WHALEYSANS_INTEGERS[int(showChar)]      # FONT[i] is correct ROW in Font - contains info to rendercurrentInt
    return getCharFontData(showChar)                  # char could be integer or alpha - this will resolve
    

def getCharFontData(charStr):       # used to identify the char and return the raw (static) data needed to render it:
    if(charIsInt(charStr)):         # first we'll establish if char is an int
        return WHALEYSANS_INTEGERS[int(charStr)]    # if we haven't returned chat is not an int - must be an alpha (a-z) - need to find it in PHILSANS_TEXT:
    return(PHILSANS_TEXT[getCharRef(charStr)])

# couple of utility methods:----------------------------------------------------------------------------------------------

def getCharRef(rawChar):        # takes the ascii code of the char to render and converts to ref to PHILSANS array
    charInt = ord(rawChar)      # a = 97, A = 65
    if(charInt > 96):
        return (charInt - 97)   
    return (charInt - 65)


def charIsInt(rawChar):
    try:
        arbInt = int(rawChar)
        return True
    except:
        return False


# methods that deal with rendering the long image into individual frames:--------------------------------------------------

def convertImageDataToImage(rawImageStrData):       # here we take the 5 separate row data string and concat them, with : separating each
    bufStr = ""
    for i in range(5):
        bufStr += rawImageStrData[i] + ":"          # no drawback to leaving a trailing ;, so not spending resource avoiding it.
    scrollLargeImage(bufStr, 300)

def scrollLargeImage(imageDataStr, delay):          # imageDataStr = "09900999:09909900: " etc - NB - ASSUME predictable structure with *NO trailing colon*
    frameCount = int((len(imageDataStr) - 4)  / 5)  # (len(imageDataStr) - 4) = total number of chars in data string. We stripped out the colons
                                                    # 5 separate discrete strings /5 gives total in 1.  Then -4 means all frames have 5 cols.
    for i in range(frameCount-5):
        bufStr = ""
        for j in range(5):
            bufStr += imageDataStr[j*frameCount + i + j: j*frameCount + i + j + 5] + ":"  
        display.show(Image(bufStr))
        sleep(delay)

#----------------------------------------------------------------------------------------------------------------------------


while True:
    if(button_a.is_pressed()):
        show2ColSansNumber(2106754389)

    if(button_b.is_pressed()):
        show2ColSansString("abcdefghijklmnopqrstuvwxyz", False)