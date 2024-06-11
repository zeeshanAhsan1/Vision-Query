# fastapi-ml

This app is made to ask questions about any uploaded image. It works on the Vision-and-Language Transformer (ViLT) which has been fine tuned on VQAv2 available on Hugging Face. [Link to the model](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa)

## Installation

1. Clone the repository :

   ```sh
   git clone https://github.com/zeeshanAhsan1/fastapi-ml.git

   ```

2. In your docker environment, build an image -> This takes care of environment and all dependencies setup for the project.

   ```sh
   docker build -t fastapi-ml-app:1.0 .

   ```

3. Run a container using this image.

   ```sh
   docker run -d --name fastapi-ml-container -p 8004:80 fastapi-ml-app:1.0

   ```

4. Check if the container is up and running.

   ```sh
   docker ps

   ```
