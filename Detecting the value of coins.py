import numpy as np
import cv2 as cv


video_cap = cv.VideoCapture("coins.mp4")

# Coins
coin1 = 0
coin5 = 0
coin10 = 0
coin50 = 0

while True:
    # Get a frame from the video
    _, frame = video_cap.read()
    # Blur the frame
    frame_blur = cv.GaussianBlur(frame, (5,5), 0)
    # Convert the frame to gray scale
    gray = cv.cvtColor(frame_blur, cv.COLOR_BGR2GRAY)
    # Run the circle detection
    circle = cv.HoughCircles(gray, cv.HOUGH_GRADIENT,0.9,20,param1=180,param2=4.0,minRadius=10,maxRadius=80)

    if circle is not None:
        # Round the values
        circle = np.uint16(np.around(circle))
        # Drow the circles
        for i in circle[0,:]:
            # Draw the outer circle
            cv.circle(frame,(i[0],i[1]),i[2],(0,255,20),2)
            # Draw the center of the circle
            cv.circle(frame,(i[0],i[1]),2,(0,0,255),2)
            # Check the radius of circle
            # cv.putText(frame, str(i[2]), (i[0],i[1]), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0), 1)
            # print(i[2])


            # Detection fo values of coins
            # if i[2] > 21 and i[2] < 26:
            #     cv.putText(frame, str("1 Ban"), (i[0],i[1]), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0), 1)
            #     coin1 += 1
            if i[2] > 25 and i[2] < 29:
                cv.putText(frame, str("5 Bani"), (i[0],i[1]), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0), 1)
                coin5 += 1
            elif i[2] > 30 and i[2] < 34:
                cv.putText(frame, str("10 Bani"), (i[0],i[1]), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0), 1)
                coin10 += 1
            elif i[2] > 34:
                cv.putText(frame, str("50 Bani"), (i[0],i[1]), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0), 1)
                coin50 += 1
    # Calculate the total value
    total = coin1 * 1 + coin5 * 5 + coin10 * 10 + coin50 * 50
    if total >= 100:
        total /= 100.0
    print(total)
    # Show the total on screen
    cv.putText(frame, "Estimated sum: " + str(total) + " RON",(10,40), cv.FONT_HERSHEY_COMPLEX, 1, (40,0,200), 2)
    # Reset the values for every frame
    coin1 = 0
    coin5 = 0
    coin10 = 0
    coin50 = 0



    # Show annotated frame
    cv.imshow("Coin detection video", frame)
    # Quit loop
    if cv.waitKey(1) == ord("q") or cv.getWindowProperty("Coin detection video",cv.WND_PROP_VISIBLE) == 0:
        break
# End while

# Close video feed
video_cap.release()
# Close all windows
cv.destroyAllWindows()
