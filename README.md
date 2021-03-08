# Chess-Board-Split-up
A simple python code to split up the image of a chessboard (in frame from edge to edge) into 64 different images

NOTE :
1.Current form of the code is at it's initial stage
2.The Programme slice_2.py essentially reads an image and splits it up to 8x8 grid and saves each of the 64 squares with a unique name starting from A1 to H8
3.The current programme is not trained to remove noise and only focus on the chessboard hence, only use images which have a complete coverage of the cheesboard in a   perfect frame (Refer sample images for clarification).
4.rgb.py is a programme which produces unique values for each of the 64 images which can be used and compared to track piece movement over the board.
