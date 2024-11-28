---
title: How to use Aspose.Cells for Python via Java in Gunicorn+Flask environment
type: docs
weight: 40
url: /python-java/aspose-cells-python-java-in-gunicorn-flask/
description: This section compares Aspose.Cells for Python via Java components and some other Excel Python operation libraries.
keywords: Python Excel, Excel Python, Excel Python via Java, Python via Java Excel, Why Aspose.Cells for Python via Java, Why not xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas.
---

{{% alert color="primary" %}}

This beginner's topic shows how developers can create a simple application (Hello World) using Aspose.Cells for Python via Java. The application creates a Microsoft Excel file with the words Hello World in a specified cell of a worksheet.

{{% /alert %}}



## **Complete environment preparation**

The example running environment of this guide is Ubuntu: 20.04, you can adjust it according to your actual situation. In order to ensure that the examples can run properly, we need to install some necessary tools in the environment. The following is a brief step-by-step guide to help you complete the process. Please note that this is only a rough guide, and the specific details may vary depending on your system and needs.

### Python

If not installed, install it as follows:
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
Check version
```
python3 --version
pip3 --version
```

### Java
If not installed, install it as follows:
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
Check version
```
java -version
```

### virtualenv virtual environment
The virtual environment is installed based on your actual needs. It is recommended to use virtual environments to manage project dependencies in both development and production environments.
Please follow the following command to install:
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
Create a virtual environment
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
Start the virtual environment
```
source myenv/bin/activate
```

***Notice: If a virtual environment is used, the following operations require the activation of the corresponding virtual environment first***

### Flask
If not installed, please follow the following command to install:
```
pip install Flask
```

### Gunicorn
If not installed, please follow the following command to install:
```
pip install gunicorn
```

### Jpype
If not installed, please follow the following command to install:
```
pip install jpype1
```

### aspose-cells
If not installed, please follow the following command to install:
```
pip install aspose-cells
```

## **Creating the Hello World Application**

To create the Hello World application using Aspose.Cells API:

1. Create an instance of the [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) class.
1. Apply the license:
   1. If you have purchased a license, then use the license in your application to get access to Aspose.Cells' full functionality
   1. If you are using the evaluation version of the component (if you're using Aspose.Cells without a license), skip this step.
1. Create a new Microsoft Excel file, or open an existing file in which you want to add/update some text.
1. Access any cell of a worksheet in the Microsoft Excel file.
1. Insert the words **Hello World!** into a cell accessed.
1. Generate the modified Microsoft Excel file.

The examples below demonstrate the above steps.

### **Creating a Workbook**

The following example creates a new workbook from scratch, writes the words "Hello World!" into cell A1 on the first worksheet, and saves the file.

Suppose we have a test path "/app". We will complete the following work under this test path.

#### Flask application files: hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### Custom Gunicorn startup class file: custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### Start the service

Verify that all packages required by the service are installed, then start the service.

If you use the python3-venv virtual environment, you need to create a virtual environment in the test path, start it, and then install all the required tool packages.

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### Check results

1 Open the browser and visit http://127.0.0.1:5000/.

2 Enter the file name you want to save in the input box.

3 Click the 'Generate' button to save the file.

After doing this, you will get an Excel file named after the content you entered in the current test path. The preview effect is as follows:

![todo:image_alt_text](HelloWorldFileInFlask.png)


## Using Docker

Or you can put the above operations into a docker container. It is very simple to use Docker to build the environment used by the example. Just put the above operations into the Dockerfile file.

Here is a Dockerfile file for reference. It lists some necessary toolkits required to build the environment.

### Dockerfile

``` 
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    openjdk-11-jdk \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "custom_gunicorn.py"]
```

### requirements.txt

This file is mainly used to provide a dependency environment for Python projects. You can modify the version in this file to suit your needs.

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### Main files

The main file structure is as follows:
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### Start the container

You can start the container using the following command
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
