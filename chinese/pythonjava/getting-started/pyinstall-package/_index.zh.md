---
title: 使用PyInstaller轻松分发Python应用程序
linktitle: 使用Pyinstaller打包
type: docs
weight: 10
url: /zh/python-java/pyinstaller-python/
description: 通过pyinstaller将python代码打包成exe。
---

## **PyInstaller用于什么？**
PyInstaller读取您编写的Python脚本。它会分析您的代码，以发现脚本执行所需的每个其它模块和库。然后，它会收集这些文件的副本，包括活动的Python解释器！

## **为什么使用PyInstaller来打包Python代码？**
PyInstaller用于将Python代码打包成可独立运行的应用程序，适用于各种操作系统。它将Python脚本转换成一个包含所有必要依赖项的单个可执行文件，可以在未安装Python的计算机上运行。这样可以更方便地分发和部署Python应用程序，因为用户不需要在其系统上安装Python和所需的模块就可以运行应用程序。此外，PyInstaller还可以用于创建单文件可执行文件，这些文件包含应用程序所需的所有依赖项。这样可以更轻松地分发应用程序，因为用户只需下载一个文件。

## **如何安装PyInstaller**
PyInstaller作为一个普通的Python包是可用的。发布版本的源代码存档可以从[PyPi](https://pypi.org/project/pyinstaller/)获取，但更容易使用[pip](https://pip.pypa.io/en/stable/)安装最新版本:
{{< highlight java >}}

C:\> pip install pyinstaller

{{< /highlight >}}

要升级现有的PyInstaller安装到最新版本，使用:
{{< highlight java >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
要安装当前的开发版本，使用:
{{< highlight java >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

## **如何使用PyInstaller创建一个EXE**
我们将以一个单一的Python文件作为示例，详细说明打包步骤。以Python 3.11.0为例，在安装[aspose.cells](https://pypi.org/project/aspose-cells/)后。

1. 创建一个名为[example.py](example.py)的Python示例文件。
{{< highlight java >}}

import os
from jpype import *

__cells_jar_dir__ = os.path.dirname(__file__)
addClassPath(os.path.join(__cells_jar_dir__, "aspose-cells-23.1.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcprov-jdk15on-160.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcpkix-jdk15on-1.60.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "JavaClassBridge.jar"))

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType, CellsHelper

print(CellsHelper.getVersion())
workbook = Workbook(FileFormatType.XLSX)
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
workbook.save("output.xlsx")

jpype.shutdownJVM()

{{< /highlight >}}
1. 创建一个名为c:\app的文件夹，并将example.py(附加)复制到c:\app。
1. 打开命令提示符并运行pyinstaller example.py命令。
{{< highlight java >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. 复制jars(aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. 他们在C:\Python311\Lib\site-packages\asposecells\lib文件夹中)到c:\app。
1. 编辑具有spec后缀的文件，在datas部分添加像[example.spec](example.spec)这样。
![todo:image_alt_text](example.png)
1. 在命令提示符窗口中运行pyinstaller example.spec。
{{< highlight java >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. 切换到C:\app\dist\example目录，您会找到example.exe文件。
