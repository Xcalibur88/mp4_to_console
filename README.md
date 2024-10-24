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
- Option **0** will present you with a list of available ASCII files in the `run_data/` directory. Select the file you wish to play by entering its index.

#### Process New Video:
- Option **1** will allow you to create a new ASCII file for playback
- It will first prompt for the path to the video file. The file must be in `.mp4` format and exist at the specified path.
- Next you will need to specify a width and height. This could require some trial and error to find the best option for your specifc screen size and video. Start with a low resulotion and work you way up to find your screens max
- You will need to enter the desired frames per second (FPS) for the ASCII video (must be between 1 and 60).
> [!TIP]
> You'll see the best results with a frame rate between 10 and 25
- Specify a frame limit next. Only proccesing a few hundered frames, instead of a whole video, can be a great for testing. If you want to process the whole video, simply enter a negative number.
- The application will then generate an ASCII file in the `run_data/` directory based on your settings. Be patient, depending on the length and frame rate of the video it could take upwords of a minute to process.


#### Clean Up run_data: 
- Choose option **2** to remove temporary `.jpg` files created during video processing. The application will inform you how many files were deleted.

#### Exit:
- Choose option 3 to quit the application.

## Testing
The projects contains a number of tests to verify the functionality of image processing and file writing functions. Using these tests you can assure that changes made to the code did not negatively impact the program.

### Running Tests
Please use vscode's integrated test identification and handling for running tests. Manually interactions using pytest to run the files will fail.
> [!NOTE]
> The tests rely on a number of test images and files. Given significant updates to the code, they will need updated to reflect said changes.