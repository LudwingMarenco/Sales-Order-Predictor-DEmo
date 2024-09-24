# Sales Order Predictor Demo

## Overview

This repository provides a Python implementation of a sales order predictor using DVC pipeline. Implemented pipeline perfom the complete process for data processing and model training. Model is based on a simple multioutput regressor.

<!-- ## Features

<!-- - **Local LLM Deployment**: Run a lightweight LLM model locally.
- **API Integration**: Test the LLM recommendation system in real-time with API integration.
- **UI Interface Mesop Based**: Rapid deployment of a UI interface for direct interaction with the prompt engineering tasks. -->

## How to use it?

### Running locally

1. **Set Up Virtual Environment**: Create a virtual environment to manage dependencies cleanly by running

    ```bash
    ./scripts/sales_create_venv.sh
    ```

2. **Activate virtual envinroment**: Activate your virtual environment. You can do this by running:

    ```bash
     source scripts/sales_activate_venv.sh
    ```

3. **Run the sales predictor pipeline**: Start the pipeline by executing:

    ```bash
    ./main.sh
    ```

4. **Run Mesop UI based interface for prediction**: In a separate terminal, deploy the UI interface to see prediction by executing the following command:

    ```bash
    ./mesop.sh
    ```

    Next, open the provided link in your web browser.

<!-- ### Running in container

1. **Build image**: Build and execute the images within a container by running:

    ```bash
    docker compose up --build
    ``` -->
