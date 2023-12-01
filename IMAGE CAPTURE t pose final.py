import time
import os
import cv2
import mediapipe as mp
import math

# Initialize the MediaPipe pose detection model
mp_pose = mp.solutions.pose
pose_drawing = mp.solutions.drawing_utils

# Set up the video capture
cap = cv2.VideoCapture(0)

# Set the output folder path
output_folder = "D:/capstone/tpose"

def calculateAngle(landmark1, landmark2, landmark3):
    # Get the required landmarks coordinates.
    x1, y1, z1 = landmark1.x, landmark1.y, landmark1.z
    x2, y2, z2 = landmark2.x, landmark2.y, landmark2.z
    x3, y3, z3 = landmark3.x, landmark3.y, landmark3.z

    # Calculate the angle between the three points
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    
    # Check if the angle is less than zero.
    if angle < 0:
        # Add 360 to the found angle.
        angle += 360

    # Return the calculated angle.
    return angle

# Define a function to check if the pose is in a T-pose
def is_tpose(results):
    left_elbow_angle = calculateAngle(
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST.value]
    )

    right_elbow_angle = calculateAngle(
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    )

    left_shoulder_angle = calculateAngle(
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP.value]
    )

    right_shoulder_angle = calculateAngle(
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
    )

    left_knee_angle = calculateAngle(
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE.value]
    )

    right_knee_angle = calculateAngle(
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE.value],
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE.value]
    )

    # Check if it is a T-pose based on your constraints
    if (
        left_elbow_angle > 165 and left_elbow_angle < 195 and
        right_elbow_angle > 165 and right_elbow_angle < 195 and
        left_shoulder_angle > 30 and left_shoulder_angle < 60 and
        right_shoulder_angle > 30 and right_shoulder_angle < 60 and
        left_knee_angle > 160 and left_knee_angle < 195 and
        right_knee_angle > 160 and right_knee_angle < 195
    ):
        return True
    else:
        return False

# Detect poses in a loop
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect poses
    results = mp_pose.Pose(min_detection_confidence=0.5).process(rgb_frame)

    # Check if a pose was detected
    if results.pose_landmarks:
        # Make a copy of the frame to save without keypoints
        frame_copy = frame.copy()

        # Check if the pose is in a T-pose
        if is_tpose(results):
            # If the pose is in a T-pose, capture the image without keypoints
            timestamp = time.time()
            filename = f"tpose_{timestamp}.jpg"
            filepath = os.path.join(output_folder, filename)

            cv2.imwrite(filepath, frame_copy)
            break

        # Draw the pose landmarks on the original frame for visualization
        pose_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Display the resulting frame with keypoints
    cv2.imshow('T-pose Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
