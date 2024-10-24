# Video To Console
This project lets you play videos directly in your terminal as ASCII art! It converts video frames into ASCII characters to play back videos in real time, providing a unique way to experience your favorite videos right in the console.

## Features
- Play any video in ASCII art format
- Customizable resolution and frame rate
- Supports a the .mp4 video format

## Usage
### Intial setup
1. Clone the repository
   - Your choice of using a git integration in vscode, or a direct zip download.
2. Install the required dependencies
   - Run ```pip install -r requirements.txt```


### Running the program
To start the application, run the following command: ```python main.py```

Upon launching, you'll be presented with a menu with the following options:

#### Play Video:
- Option **0**, will present you with a list of available ASCII files in the `run_data/` directory. Select the file you wish to play by entering its index.

#### Process new video:
- Option **1** will prompt you to enter the desired frames per second (FPS) for the ASCII video (must be between 1 and 60). Provide the path to the video file you want to process. The file must be in `.mp4` format and exist at the specified path.The application will generate an ASCII file in the `run_data/` directory based on your video. Be patient, depending on the length and frame rate of the video it could take upwords of a minute to process.
#### Clean up run data: 
- Choose option **2** to remove temporary `.jpg` files created during video processing. The application will inform you how many files were deleted.

#### Exit: Quit the application.
- Choose option 3 to quit the application.
