from video import video_procces
import os


SAVE_DIRECTORY = 'run_data/'

def main():
    setup()
    main_menu()

def setup():
    try:
        os.makedirs(SAVE_DIRECTORY)
    except FileExistsError:
        pass
    except Exception as err:
        print(err)

def main_menu():
    options = {'0 - Play video': pre_processed,
               '1 - Process new video': proccess_new,
               '2 - Clean up run data': clean_up,
               '3 - Exit': None
              }
    
    for op in options:
        print(op)
    option = prompt_input('> ', int, lambda x: x > -1 and x < len(options))

    for k, v in options.items():
        if k.startswith(str(option)):
            if v is None:
                return
            v()
            print()
            main_menu()

def pre_processed():
    print('Available ASCII Files:')
    files_dict = dict(enumerate(filter(lambda f: f.startswith('ascii') and f.endswith('.txt'), os.listdir(SAVE_DIRECTORY))))

    for i, file in files_dict.items():
        print(i, '-', file)
    
    index = prompt_input('> ', int, lambda x: x > -1 and x < len(files_dict))
    file = SAVE_DIRECTORY + files_dict[index]

    video_procces.play_ascii(file)

def proccess_new():
    fps = prompt_input('Frames per second: ', int, lambda x: x > 0 and x <= 60)
    vfile = prompt_input('Video file: ', str, lambda f: f.endswith('.mp4') and os.path.exists(f), 'Invalid video file!')

    save_file = SAVE_DIRECTORY + f"ascii_frames_{vfile.split('.')[0]}.txt"
    if os.path.exists(save_file):
        os.remove(save_file)

    with open(save_file, 'a') as afile:
        afile.write(f'fps.{fps}')

    video_procces.video_to_ascii(vfile, save_file, fps, 1000)

def clean_up():
    deleted = 0
    for file in os.listdir(SAVE_DIRECTORY):
        if file.endswith('.jpg'):
            os.remove(SAVE_DIRECTORY + file)
            deleted += 1
    print(f'Cleaned up {deleted} files!')

def prompt_input(prompt: str, return_type: type, criteria = lambda i: i, reprompt: str = None,) -> int:
    while True:
        try:
            user_input = input(prompt)
            converted_input = return_type(user_input)
            if criteria(converted_input):
                return converted_input
        except ValueError:
            pass
        if reprompt is not None:
            print(reprompt)

if __name__ == "__main__":
    main()