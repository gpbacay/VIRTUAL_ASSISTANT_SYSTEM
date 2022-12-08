import cv2
import face_recognition


known_faces = []
known_names = ['Gianne Bacay']


cap = cv2.VideoCapture(0)
while True:
    _, image = cap.read()
    

    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_faces, face_encoding)

    name = "Unknown"

    # If a match was found in known_faces, just use the first one.
    if True in matches:
        first_match_index = matches.index(True)
        name = known_names[first_match_index]

    # Put text on the image
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.putText(image, name, (left, bottom + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)


    attendance = {}

    for name in known_names:
        attendance[name] = False
    
    for name in known_names:
        if name in attendance:
            attendance[name] = True
            
    print("Attendance:")
    for name, present in attendance.items():
        print(f"{name}: {present}")
        
    cv2.imshow('Recognized', image)
    if cv2.waitKey(30) & 0xFF ==27:
        break
        
cap.release()
cv2.destroyAllWindows()

#Run command: python GPT.py