---
title: Package Python to EXE
linktitle: Package Using Pyinstaller
type: docs
weight: 10
url: /python-java/package-using-pyinstaller/
description: Package python code to exe via pyinstaller.
---

## **Possible Usage Scenarios**
After you have written some python code files using Aspose.Cells for Python via Java, you can package your program into an exe file through pyinstaller. So that you can run your program where there is no python environment.

## **How to Package Python to EXE**
We will take a single python file as an example to explain the packaging steps in detail.

1. Create a python sample file named [example.py](example.py).
1. Create a folder as c:\app, and copy example.py(attached) to c:\app.
1. Open your command prompt and run pyinstaller example.py command.
1. Copy the jars(aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. They exist in C:\Python311\Lib\site-packages\asposecells\lib folder) to c:\app.
1. Edit the file with the spec suffix to add datas section like [example.spec](example.spec).
1. Run pyinstaller example.spec in the command prompt window.
1. Switch the directory to C:\app\dist\example app dist example, and you will find the exe file.