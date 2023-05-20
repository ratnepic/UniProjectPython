import mediapipe as mp
import cv2


class HandTracker:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.cap = cv2.VideoCapture(0)

    def get_hand_landmarks(self):
        success, img = self.cap.read()
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = self.hands.process(img_rgb)
        return results.multi_hand_landmarks

    def get_hand_coords(self):
        hand_lms = self.get_hand_landmarks()
        if hand_lms is None:
            return None

        hand_points = [[lm for lm in hand.landmark] for hand in hand_lms]
        results = [(hand[9].x, hand[9].y, self.get_hand_status(hand)) for hand in hand_points]

        return results

    def get_hand_status(self, points):
        return (points[9].y < points[0].y and
                points[8].y > points[5].y and
                points[12].y > points[9].y and
                points[16].y > points[13].y and
                points[20].y > points[17].y)
