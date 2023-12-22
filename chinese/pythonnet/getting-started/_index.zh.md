---
title: 入门
linktitle: 入门
type: docs
weight: 4
url: /zh/python-net/getting-started/
description: 了解如何安装 Aspose.Cells for Python via .NET 并创建 Hello World 应用程序。
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---
##  **系统要求**
 Aspose.Cells for Python via .NET 与平台无关 API 可以在任何平台（Windows 和 Linux）上使用[Python](https://www.python.org/downloads/)已安装。

##  **Python版本**
- Python 3.6或更高

##  **安装**
###  **Windows:**
您可以轻松地使用 Aspose.Cells for Python via .NET[皮皮](https://pypi.org/project/aspose-cells-python/)使用以下命令。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux：**
您可以轻松地使用 Aspose.Cells for Python via .NET[皮皮](https://pypi.org/project/aspose-cells-python/)使用以下命令。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：安装前需要运行以下命令
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **苹果系统：**
您可以轻松地使用 Aspose.Cells for Python via .NET[皮皮](https://pypi.org/project/aspose-cells-python/)使用以下命令。
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：如果你的python是Python3.7（这里以python3.7为例），安装aspose-cells-python后，可能会出现以下错误
'/usr/local/lib/libpython3.7m.dylib'（没有这样的文件），'/usr/lib/libpython3.7m.dylib'（没有这样的文件）提示。
在这种情况下，请将以下命令添加到您的bash_profile中（先找到libpython3.7m.dylib在哪里，取/Library/Frameworks/Python.framework/Versions/3.7/lib
例如这里）
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- 注意：由于我们依赖SkiaSharp图形库，如果遇到以下错误：
**System.DllNotFoundException：无法加载共享库“libSkiaSharp”或其依赖项之一。**请安装 SkiaSharp。
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
安装后，请运行以下命令
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

当然，如果你想要更简单，也可以下载[libSkiaSharp.dylib](libSkiaSharp.dylib)进而**复制**它到**/usr/local/lib**目录。

##  **如何使用 Aspose.Cells for Python via .NET 创建 Hello World 应用程序**

- 创建一个名为**创建HelloWorldFile.py**并使用以下示例代码：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- 现在将上面的代码保存到“CreatingHelloWorldFile.py”并在命令提示符下运行“python CreateHelloWorldFile.py”。

