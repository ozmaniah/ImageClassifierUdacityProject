CREATING YOUR OWN IMAGE CLASSIFIER:

Deep Learning :

In this project, we created a neural network in order to classify flowers (from pictures) by their name. In the theory leading up to this project, there were some concepts that were a bit tricky to understand so I am glad this project was there to reinforce these ideas.
It would have been nice to get a bit more understanding on how to construct a neural network, rather than just put the building blocks together with trial and error as I ended up doing.
I came into this course with zero experience in python. However, I can say with confidence that thanks to this program I understand the basics of Python, and neural networks/machine learning. It has motivated me to look deeper into all of these aspects that were covered in the course.

PACKAGES YOU NEED BEFORE YOU START YOUR JOURNEY: 
The Code is written in Python. Additional Packages that are required are: Numpy, Pandas, MatplotLib, Pytorch, PIL and json. In order to intall Pytorch head over to the Pytorch site select your specs and follow the instructions given.


[ You'll Need to access Jupyter notebook through anaconda prompt to do all the required tasks ]


Running codes
To train a new network on a data set with train.py:


Basic usage: python train.py data_directory
Options:
Set directory to save checkpoints: python train.py data_dir --save_dir save_directory
Choose architecture: python train.py data_dir --arch "vgg13"
Set hyperparameters: python train.py data_dir --learning_rate 0.01 --hidden_units 512 --epochs 9
Use GPU for training: python train.py data_dir --gpu
To predict flower name from an image with predict.py:

Basic usage: python predict.py /path/to/image checkpoint
Options:
Return top KKK most likely classes: python predict.py input checkpoint --top_k 3
Use a mapping of categories to real names: python predict.py input checkpoint --category_names cat_to_name.json
Use GPU for inference: python predict.py input checkpoint --gpu