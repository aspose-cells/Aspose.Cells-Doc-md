---
title: 入门
linktitle: 入门
type: docs
weight: 4
url: /zh/python-net/getting-started/ 
keywords: python, excel, instal
description: 安装程序 Aspose.Cells for Python via .NET 和安装指南。
---
##  **系统要求**
Aspose.Cells for Python via .NET 与平台无关 API 可以在任何平台（Windows 和 Linux）上使用，其中[Python](https://www.python.org/downloads/)已安装。

##  **Python版本**
- Python 3.6 或更高版本

##  **安装**
###  **Windows:**
您可以轻松地使用 Aspose.Cells for Python via .NET 来自[皮皮](https://pypi.org/project/aspose-cells-python/)使用以下命令。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux：**
您可以轻松地使用 Aspose.Cells for Python via .NET 来自[皮皮](https://pypi.org/project/aspose-cells-python/)使用以下命令。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：安装前需要运行以下命令
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **苹果系统：**
您可以轻松地使用 Aspose.Cells for Python via .NET 来自[皮皮](https://pypi.org/project/aspose-cells-python/)使用以下命令。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：如果你的python是Python3.7（这里以python3.7为例），安装aspose-cells-python后，可能会出现如下错误
'/usr/local/lib/libpython3.7m.dylib' (no such file), '/usr/lib/libpython3.7m.dylib' (no such file)提示。
在这种情况下，请将以下命令添加到您的bash_profile（首先找到libpython3.7m.dylib在哪里，取/Library/Frameworks/Python.framework/Versions/3.7/lib
例如这里）
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
##  **创建 Hello World 应用程序**

- 创建一个名为**创建HelloWorldFile.py**并使用以下示例代码：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- 现在将上面的代码保存到“CreatingHelloWorldFile.py”并运行“python CreatingHelloWorldFile.py”@命令提示符。

