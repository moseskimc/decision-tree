# decision-tree

In this repo, we implement a decision tree model from scratch.


## Data

Normally, data should be stored in the repo but, in our case, we make an exception since our data is only 8kb. If you wish to see an overview of the data visit the kaggle link [here](https://www.kaggle.com/datasets/yersever/500-person-gender-height-weight-bodymassindex?resource=download)


## Environment

Create an environment using `conda` or `virtualenv`. Make sure `pip` is installed as well as the following:

- pandas
- numpy


## Package

Activate your environment from the repo directory and install the decision tree package from the repo by running:

    pip install .

## Script

First make sure you have installed the repo package by running:

    python -c "import decision_tree"

To run predictions, run the following command:

    PYTHONPATH=./ python scripts/main.py



## Notebook

For more detailed exposition and step-by-step overview of how decision trees are built, the reader is advised to look at the notebook in addition to using the script.
