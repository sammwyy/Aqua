# AQUA: Assured Quality Universal Analysis

An artificial intelligence model prototype to detect vulnerabilities in source code.

Disclaimer: This project is nothing more than an experiment, although it can detect patterns, there are still bypasses that it does not know about because of a small dataset, and in addition, it is not designed to specify which and where the vulnerability is.

Non-functional: The project has a bug in the training phase, where it does not load the dataset correctly because it does not know how to interpret the quotation marks. Although it is a silly error, this note will remain until it is fixed.

## How does it work?

### Learning

1. Compile all raw data samples to AST.
2. Create a vectorization model and a prediction model based on the dataset in AST.
3. Compile and store both models in the "model" directory.
4. The model is evaluated to ensure that there is sufficient data to determine outcomes.

### Prediction

1. Compile the prompt to AST.
2. Vectorize the AST result of the prompt using the precompiled model.
3. Run the prediction model with the vectorized prompt to determine the result.

## Get started

1. Clone and install dependencies.

    ```bash
    git clone https://github.com/sammwyy/aqua
    cd aqua
    pip -r requirements.txt
    ```

2. Run the training workflow.

    ```bash
    # On windows
    run_train_flow.cmd

    # On linux/osx
    ./run_train_flow.sh
    ```

3. (Optional) run unit testing.

    ```bash
    # On windows
    run_tests.cmd

    # On linux/osx
    ./run_tests.sh
    ```

4. Initialize engine and send a prompt file.

    ```bash
    # Use one of the test file.
    python aqua.py samples/bad_insecure_deserialization.py.sample
    ```
