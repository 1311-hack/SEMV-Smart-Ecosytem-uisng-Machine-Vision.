import cv2
import numpy as np
import time
import datetime
import serial


# Initialize serial connection
arduino_serial = serial.Serial('COM7', 9600)  # Replace 'COM3' with the port name of your Arduino board

# Wait for the serial connection to be established
while not arduino_serial.is_open:
    pass

# Define the pins for the LEDs and grid status input
ledPin1 = 4
ledPin2 = 5

# Load the SSD model
model = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

# Initialize the video capture object
cap = cv2.VideoCapture(0)
x = 3
y = 3
num_grid_cols = y
num_grid_rows = x

# Set the colors for the grid lines and the nearest grid to the person
grid_color = (255, 255, 255)
nearest_grid_color = (255, 255, 255)

# Initialize all grid cells as OFF
grid_status = [[False for j in range(num_grid_cols)] for i in range(num_grid_rows)]
grid_status_main = [[False for j in range(num_grid_cols)] for i in range(num_grid_rows)]

#initializing counters for delay
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0
counter_7 = 0
counter_8 = 0
counter_9 = 0

while True:
    # Capture the current frame
    ret, frame = cap.read()

    # Resize the frame to a smaller size for faster processing
    if not ret:
        break
    frame = cv2.resize(frame, (300, 300))

    # Convert the frame to a blob for input to the SSD model
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)

    # Set the input to the SSD model
    model.setInput(blob)

    # Run the SSD model and get the detections
    detections = model.forward()

    # Loop over the detections
    for i in range(detections.shape[2]):
        # Get the confidence score for the detection
        confidence = detections[0, 0, i, 2]

        # If the confidence score is above the threshold of 0.5
        if confidence > 0.5:
            # Get the class label for the detection
            class_id = int(detections[0, 0, i, 1])

            # If the class label is for a person
            if class_id == 15:
                # Get the bounding box coordinates for the detection
                bbox = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                (startX, startY, endX, endY) = bbox.astype("int")
                temp = {"bbox": bbox, "time": datetime.time(0,0)}

                # Draw the bounding box rectangle and label on the frame
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                label = "Person"
                cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Initialize the time for delay
                #delay_time = time.time()

                # Calculate the nearest grid to the person
                grid_width = int(frame.shape[1] / x)
                grid_height = int(frame.shape[0] / y)
                grid_x = int((startX + endX) / 2 / grid_width)
                grid_y = int((startY + endY) / 2 / grid_height)

                # Draw the grid
                for i in range(x):
                    cv2.line(frame, (i * grid_width, 0), (i * grid_width, frame.shape[1]), grid_color, 1)
                for i in range(y):
                    cv2.line(frame, (0, i * grid_height), (frame.shape[0], i * grid_height), grid_color, 1)

                if not arduino_serial.is_open:
                    arduino_serial.open()

                # Write "ON" on the nearest grid cell
                grid_status[grid_x][grid_y] = True
                nearest_grid_x = grid_x * grid_width
                nearest_grid_y = grid_y * grid_height
                cv2.rectangle(frame, (nearest_grid_x, nearest_grid_y), (nearest_grid_x + grid_width, nearest_grid_y + grid_height), (0, 255, 0), 2)
                cv2.putText(frame, "ON", (nearest_grid_x, nearest_grid_y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2)
            else:
                # Mark all grid cells as OFF
                grid_status = [[False for j in range(num_grid_cols)] for i in range(num_grid_rows)]

    #grid status update using fps
    if grid_status[0][0] == grid_status_main[0][0]:
        counter_1 = 0
    else:
        counter_1 += 1
        if counter_1 >= 400:
            grid_status_main[0][0] = grid_status[0][0]
    if grid_status[0][1] == grid_status_main[0][1]:
        counter_2 = 0
    else:
        counter_2 += 1
        if counter_2 >= 400:
            grid_status_main[0][1] = grid_status[0][1]
    if grid_status[0][2] == grid_status_main[0][2]:
        counter_3 = 0
    else:
        counter_3 += 1
        if counter_3 >= 400:
            grid_status_main[0][2] = grid_status[0][2]
    if grid_status[1][0] == grid_status_main[1][0]:
        counter_4 = 0
    else:
        counter_4 += 1
        if counter_4 >= 400:
            grid_status_main[1][0] = grid_status[1][0]
    if grid_status[1][1] == grid_status_main[1][1]:
        counter_5 = 0
    else:
        counter_5 += 1
        if counter_5 >= 400:
            grid_status_main[1][1] = grid_status[1][1]
    if grid_status[1][2] == grid_status_main[1][2]:
        counter_6 = 0
    else:
        counter_6 += 1
        if counter_6 >= 400:
            grid_status_main[1][2] = grid_status[1][2]
    if grid_status[2][0] == grid_status_main[2][0]:
        counter_7 = 0
    else:
        counter_7 += 1
        if counter_7 >= 400:
            grid_status_main[2][0] = grid_status[2][0]
    if grid_status[2][1] == grid_status_main[2][1]:
        counter_8 = 0
    else:
        counter_8 += 1
        if counter_8 >= 400:
            grid_status_main[2][1] = grid_status[2][1]
    if grid_status[2][2] == grid_status_main[2][2]:
        counter_9 = 0
    else:
        counter_9 += 1
        if counter_9 >= 400:
            grid_status_main[2][2] = grid_status[2][2]
    counter = 0
    #switch status update
    for i in range(num_grid_rows):
        for j in range(num_grid_cols):
            counter += 1
            if grid_status_main[i][j] == True:
                nearest_grid_x1 = i * grid_width
                nearest_grid_y1 = j * grid_height
                cv2.putText(frame, "ON", (nearest_grid_x1, nearest_grid_y1 + 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 0, 0), 2)
                arduino_serial.write(str(counter).encode())
            else:
                arduino_serial.write(str(chr(counter+96)).encode())
    print (grid_status_main)

    # Add the grid overlay to the frame
    height, width = frame.shape[:2]
    xstep = int(width / x)
    ystep = int(height / y)
    for i in range(x):
        cv2.line(frame, (i * xstep, 0), (i * xstep, height), (0, 0, 0), 1)
    for i in range(y):
        cv2.line(frame, (0, i * ystep), (width, i * ystep), (0, 0, 0), 1)


    # Display the output frame
    cv2.imshow('frame', frame)

    # Convert frame to negative
    negative_frame = 255 - frame

    # Display the negative frame
    cv2.imshow('Negative Video', negative_frame)


    # Wait for a key press and check if the key pressed is 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
