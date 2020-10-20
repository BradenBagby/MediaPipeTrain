
import os
import tempfile
from subprocess import Popen

THREADS = 4

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
outputs = [] #we can check and make sure it created an output. if it didnt then no hand was detected

#create data set
for f in files:
    inputPath = f
    outputPath = output + f[inputPath.rfind("/") + 1:].replace(".jpg",".csv")

    #run media pipe
    runCommand = 'bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_gpu   --calculator_graph_config_file=mediapipe/graphs/hand_tracking/hand_tracking_mobile.pbtxt --input_video_path=' +inputPath+ ' --output_data_path=' + outputPath
    commands.append(runCommand)
    outputs.append(outputPath)
    


successCount = 0

for i in range(0,len(commands)):
    os.system(commands[i])
    if os.path.isfile(outputs[i]):
        successCount += 1

print("Successes: " + str(successCount) + " - %" + str(float(successCount) / float(len(commands))))
    

   
