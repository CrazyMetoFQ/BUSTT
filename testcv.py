from cvzone.HandTrackingModule import HandDetector
import cv2
import WindowHandler_ as WH
import json

with open("config.json") as f:
    d = json.loads(f.read())

wnd = WH.Wnd(d['title']) # title of the window
#wnd.send_keys([0xB3]) # Desired virtual key code

detector = HandDetector(detectionCon=d['confidence'], maxHands=2)

def handle_hands(hands:list)->list[dict]:
    """
    Handles hands
    hands[0]= detector.findHands(img)
    
    returns number of fingers and type of hand
    """
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)
            
            return [{"type":handType1,"fingers":fingers1},{"type":handType2,"fingers":fingers2}]
        
        else:
            return [{"type":handType1,"fingers":fingers1}]
    
    else:
        return [{"type":None,"fingers":None}]

def handle_logic(dat):
    """
    handles logic in relation to fingers
    CONFIGURE THIS
    """
    
    if dat==d['fingers']: # sequence of fingers
        #wnd.send_keys()
        wnd.close_window()
        print(0)
        return True
    else:
        return False



def main():
    cap = cv2.VideoCapture(0) # START RECORDING
    
    while True:
        # Get image frame
        success, img = cap.read()
        # Find the hand and its landmarks
        hands, img = detector.findHands(img)  # with draw
        # hands = detector.findHands(img, draw=False)  # without draw

        out = handle_hands(hands)
        
        # KEY PRESS LOGIC
        if handle_logic(out[0]['fingers']):
            print(1)
            break
            # pass
        else:
            pass 

        # Display
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()