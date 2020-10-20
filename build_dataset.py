
import os
import tempfile
from subprocess import Popen

#Get all filenames from root to run in train 
root = "/home/bradenbagby/Downloads/asl_alphabet_train/asl_alphabet_train"
output = "/home/bradenbagby/Downloads/Output/"

files = []
for (dirpath, dirnames, filenames) in os.walk(root):
    for f in filenames:
        files.append(dirpath + "/" + f)

print("" + str(len(files)) + " files found")



#delete all files in output directory
for filename in os.listdir(output):
    file_path = os.path.join(output, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


commands = [] #just keeping array of commands to run then running them in different processes to make use of threads

#create data set
for f in files:
    inputPath = f
    outputPath = output + f[inputPath.rfind("/") + 1:].replace(".jpg",".csv")

    #run media pipe
    runCommand = 'bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_gpu   --calculator_graph_config_file=mediapipe/graphs/hand_tracking/hand_tracking_mobile.pbtxt --input_video_path=' +inputPath+ ' --output_data_path=' + outputPath
    commands.append(runCommand)
    print(runCommand)
    break


#thanks internet
# run in parallel
processes = [Popen(cmd, shell=True) for cmd in commands]
# do other things here..
# wait for completion
for p in processes: p.wait()
print("done")