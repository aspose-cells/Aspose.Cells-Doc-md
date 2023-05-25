---
title: 使用 PyInstaller 轻松分发应用程序 Python
linktitle: 使用 Pyinstaller 打包
type: docs
weight: 10
url: /zh/python-java/pyinstaller-python/
description: 通过pyinstaller将python代码打包成exe。
---
##  **PyInstaller 有什么用？**
PyInstaller 读取您编写的 Python 脚本。它分析您的代码以发现您的脚本执行所需的所有其他模块和库。然后它收集所有这些文件的副本——包括活动的 Python 解释器！

##  **为什么要用Pyinstaller打包Python？**
PyInstaller 用于将 Python 代码打包成适用于各种操作系统的独立可执行应用程序。它采用 Python 脚本并生成一个包含所有必要依赖项的单个可执行文件，并且可以在未安装 Python 的计算机上运行。这允许轻松分发和部署 Python 应用程序，因为用户无需在其系统上安装 Python 和任何必需的模块即可运行该应用程序。此外，PyInstaller 还可用于创建单文件可执行文件，这些文件是包含应用程序所有必需依赖项的单个可执行文件。这可以使分发应用程序变得更加容易，因为用户只需要下载一个文件。

##  **如何安装 PyInstaller**
 PyInstaller 作为常规 Python 包提供。已发布版本的源存档可从[皮皮](https://pypi.org/project/pyinstaller/) 但使用安装最新版本更容易[点](https://pip.pypa.io/en/stable/):
{{< highlight "java" >}}

C:\> pip install pyinstaller

{{< /highlight >}}

要将现有的 PyInstaller 安装升级到最新版本，请使用：
{{< highlight "java" >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
要安装当前的开发版本，请使用：
{{< highlight "java" >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

##  **如何使用 PyInstaller 创建 EXE**
下面以单个python文件为例详细讲解打包步骤，安装后以Python 3.11.0为例[aspose.cells](https://pypi.org/project/aspose-cells/).

1. 创建一个名为[例子.py](example.py).
{{< highlight "java" >}}

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
1. 创建一个文件夹为c:\app，并将example.py(附件)复制到c:\app。
1. 打开命令提示符并运行 pyinstaller example.py 命令。
{{< highlight "java" >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. 复制 jars（aspose-cells-xxx.jar、bcprov-jdk15on-160.jar、bcpkix-jdk15on-1.60.jar、JavaClassBridge.jar。它们位于 C:\Python311\Lib\site-packages\asposecells\lib 文件夹中) 到 c:\app。
1. 编辑带有 spec 后缀的文件以添加数据部分，例如[示例.spec](example.spec).
![待办事项：image_alt_text](example.png)
1. 在命令提示符窗口中运行 pyinstaller example.spec。
{{< highlight "java" >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. 将目录切换到C:\app\dist\example，即可找到example.exe文件。
