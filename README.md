

run build_dataset.py to build a dataset of csv 21 points from a dataset of images 

-------------mediapipe-------------

takes in input image from specified path and outputs 21 points to specified file 


BUILD:
bazel build -c opt --copt -DMESA_EGL_NO_X11_HEADERS --copt -DEGL_NO_X11   mediapipe/examples/desktop/hand_tracking:hand_tracking_gpu

RUN:
specify input image path and output file path
bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_gpu   --calculator_graph_config_file=mediapipe/graphs/hand_tracking/hand_tracking_mobile.pbtxt --input_video_path="/home/bradenbagby/cow.jpg" --output_data_path="/home/bradenbagby/output.txt"