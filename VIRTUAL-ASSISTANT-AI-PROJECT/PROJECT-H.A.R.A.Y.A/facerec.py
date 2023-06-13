def Face_Recognition_System():
    # Import Libraries
    import os
    import cv2
    import numpy as np
    import face_recognition
    import face_recognition as fr
    from datetime import  datetime
    import time
    import mediapipe as mp
    import imutils


    mp_holistic = mp.solutions.holistic
    mp_drawing = mp.solutions.drawing_utils

    #Clear the CSV file
    #Run Command: python facerec.py
    def ClearCSV():
        import csv
        file = open("attendance.csv", "r")
        csvr = csv.reader(file)
        namelist = []
        Header = f'Name, Time'
        Header = Header.split(',')
        namelist.insert(0, Header)
        file = open("attendance.csv", "w", newline = '')
        csvr = csv.writer(file)
        csvr.writerows(namelist)
        file.close()
    ClearCSV()


    # Classify Faces
    #Run Command: python facerec.py
    def Classify_Faces():
        """
        Scans/Locates all of the faces in a given test image within test folder 
        and labels them with their name if they are known faces
        while, on the other hand, unknown faces are labeled as unknown
        :param im: str of file path
        :return: list of face names
        """
        
        
        # Encode Faces
        #Run Command: python facerec.py
        def get_encoded_faces():
            """
            Scans through the faces folder 
            and encodes all the faces with their names

            :return: dict of (name, image encoded)
            """
            encoded = {}
            
            for dirpath, dnames, fnames in os.walk("./faces"):
                for f in fnames:
                    if f.endswith(".jpg") or f.endswith(".png"):
                        face = fr.load_image_file("faces/" + f)
                        encoding = fr.face_encodings(face)[0]
                        encoded[f.split(".")[0]] = encoding
            return encoded
        
        
        def unknown_image_encoded(frame):
            """
            Encode an unknown face given the file name as known face
            """
            face = fr.load_image_file("faces/" + frame)
            encoding = fr.face_encodings(face)[0]
            return encoding


        faces = get_encoded_faces()
        faces_encoded = list(faces.values())
        known_face_names = list(faces.keys())
        
        #Capture video from webcam: 
        cap = cv2.VideoCapture(0)
        
        # Initialize MediaPipe Holistic
        #Run command: python poserec.py
        with mp_holistic.Holistic(static_image_mode = True, 
                            min_detection_confidence = 0.5, 
                            min_tracking_confidence = 0.5
                            ) as holistic:
            
            while True:
                success, frame = cap.read()
                
                if success:
                    #Encode Faces to the Attendance Sheet
                    #Run Command: python facerec.py
                    def MarkAttendance(name):
                        """
                        Encode the name of the scanned faces into the attendance sheet
                        and the time it was encoded
                        """
                        with open("attendance.csv", 'r+') as attendance:
                            MyDatalist =  attendance.readlines()
                            NameList = []
                            for line in MyDatalist :
                                entry = line.split(',')
                                NameList.append(entry[0])
                            if name not in NameList:
                                now = datetime.now()
                                Time = now.strftime('%H:%M')
                                attendance.writelines(f'\n{name}, {Time}')
                    
                    # Resize Frame
                    def resize(frame, size) :
                        width = int(frame.shape[1]*size)
                        height = int(frame.shape[0] * size)
                        dimension = (width, height)
                        return cv2.resize(frame, dimension, interpolation = cv2.INTER_AREA)
                    frame = resize(frame, 0.50)
                    
                    #Flip the captured video
                    frame = cv2.flip(frame, 1)
                    results = holistic.process(frame)
                    
                    #Print Nose Coordinates.
                    frame_height, frame_width, _ = frame.shape
                    if results.pose_landmarks:
                        print(
                        f'Nose Coordinates: ('
                        f'{round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * frame_width)},'
                        f'{round(results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y * frame_height)})')
                    
                    # Find Face Location
                    face_locations = face_recognition.face_locations(frame)
                    unknown_face_encodings = face_recognition.face_encodings(frame, face_locations)

                    # Identify if the face is a match for the known face(s)
                    face_names = []
                    for face_encoding in unknown_face_encodings:
                        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
                        name = "Unknown"

                        # Use the known face with the smallest distance to the new face
                        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                        face_names.append(name)

                        # Create a label with a name above the face and a facemesh around the face
                        for (top, right, bottom, left), name in zip(face_locations, face_names):
                            # Draw Face Landmarks (Tesselation)
                            frame = frame.copy()
                            mp_drawing.draw_landmarks(
                            image = frame, 
                            landmark_list = results.face_landmarks, 
                            connections = mp_holistic.FACEMESH_TESSELATION,
                            landmark_drawing_spec = mp_drawing.DrawingSpec(color = (0,255,0), thickness = 1, circle_radius = 1),
                            connection_drawing_spec = mp_drawing.DrawingSpec(color = (0,255,0), thickness = 1, circle_radius = 1))
                            
                            font = cv2.FONT_HERSHEY_TRIPLEX
                            cv2.putText(frame, name, (left -30, top -30), font + 1, 1, (255, 255, 255), 1)
                            MarkAttendance(name)

                    # Display the Resulting Image
                    cv2.imshow('AI Face Recognition System', frame)
                    key = cv2.waitKey(30) & 0xff
                    max_faces = 1
                    if len(face_names) >= max_faces:
                        cv2.destroyAllWindows()
                        return face_names
                    elif key == 27:
                        cv2.destroyAllWindows()
                        return face_names
                    else:
                        continue
                else:
                    break
    Classify_Faces()
#Run Command: python facerec.py
