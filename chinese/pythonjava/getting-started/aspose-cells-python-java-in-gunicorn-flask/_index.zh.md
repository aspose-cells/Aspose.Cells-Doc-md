---
title: 如何在Gunicorn+Flask环境中使用 Aspose.Cells for Python via Java
type: docs
weight: 40
url: /zh/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: 此部分比较 Aspose.Cells for Python via Java 组件和其他 Excel Python 操作库。
keywords: Python Excel, Excel Python, Excel Python via Java, Python via Java Excel, 为何选择 Python 的 Aspose.Cells via Java，而不是 xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas。
---

{{% alert color="primary" %}}

 本入门主题展示开发者如何使用 Aspose.Cells for Python via Java 创建一个简单的应用程序（Hello World）。该应用在指定的工作表单元格中创建一个包含“Hello World”的Microsoft Excel文件。

{{% /alert %}}



## ** 完整的环境准备**

 本指南的运行环境为Ubuntu：20.04，您可以根据实际情况调整。为了确保示例能正常运行，我们需要在环境中安装一些必要的工具。以下是帮助您完成该过程的简要步骤。请注意，这只是一个粗略指导，具体细节可能因系统和需求而异。

### Python

如果未安装，请按以下方式安装：
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
检查版本
```
python3 --version
pip3 --version
```

### Java
如果未安装，请按以下方式安装：
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
检查版本
```
java -version
```

### virtualenv 虚拟环境
虚拟环境根据你的实际需求安装。建议在开发和生产环境中使用虚拟环境管理项目依赖。
请按照以下命令进行安装：
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
创建虚拟环境
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
启动虚拟环境
```
source myenv/bin/activate
```

***注意：如果使用虚拟环境，以下操作需要先激活相应的虚拟环境***

### Flask
如果未安装，请按以下命令进行安装：
```
pip install Flask
```

### Gunicorn
如果未安装，请按以下命令进行安装：
```
pip install gunicorn
```

### Jpype
如果未安装，请按以下命令进行安装：
```
pip install jpype1
```

### aspose-cells
如果未安装，请按以下命令进行安装：
```
pip install aspose-cells
```

## **创建Hello World应用程序**

使用 Aspose.Cells API 创建 Hello World 应用程序：

1. 创建 [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) 类的实例。
1. 应用许可证：
   1. 如果您已购买许可证，请在应用程序中使用该许可证以获得对 Aspose.Cells 全部功能的访问。
   1. 如果您正在使用组件的评估版本 （如果您在没有许可证的情况下使用 Aspose.Cells），请跳过此步骤。
1. 创建一个新的 Microsoft Excel 文件，或者打开现有文件，在其中您想要添加/更新一些文本。
1. 访问 Microsoft Excel 文件中的工作表的任何单元格。
1. 在访问的单元格中插入单词**Hello World!**。
1. 生成修改后的Microsoft Excel文件。

下面的示例演示了上述步骤。

### **创建一个工作簿**

以下示例从头开始创建一个新的工作簿，在第一个工作表的单元格A1中写入单词"Hello World!"，然后保存文件。

假设我们有一个测试路径“/app”。在此测试路径下完成以下工作。

#### Flask应用文件：hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### 自定义Gunicorn启动类文件：custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### 启动服务

确保已安装服务所需的所有包，然后启动服务。

如果你使用python3-venv虚拟环境，你需要在测试路径中创建一个虚拟环境，启动它，然后安装所有必需的工具包。

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### 检查结果

1 打开浏览器并访问 http://127.0.0.1:5000/。

2 在输入框中输入你想保存的文件名。

3 点击“生成”按钮以保存文件。

完成此操作后，你会得到一个以你在当前测试路径中输入内容命名的Excel文件。预览效果如下：

![todo:image_alt_text](HelloWorldFileInFlask.png)


## 使用Docker

或者你可以将以上操作放入docker容器中。使用Docker搭建例子所用环境非常简单，只需将上述操作放入Dockerfile文件中。

这里提供一个参考的Dockerfile。它列出了构建环境所需的一些必要工具包。

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

此文件主要用于为Python项目提供依赖环境。你可以修改此文件中的版本以满足你的需要。

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### 主要文件

主要文件结构如下：
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### 启动容器

你可以用以下命令启动容器
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
