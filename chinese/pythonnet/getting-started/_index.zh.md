---
title: 开始入门
linktitle: 开始入门
type: docs
weight: 4
url: /zh/python-net/getting-started/
description: 通过.NET了解如何安装Aspose.Cells for Python并创建Hello World Application。
keywords: 如何在Windows Linux和MacOS中通过.NET安装Aspose.Cells for Python， Aspose.Cells for Python通过.NET的安装指南，Python通过.NET Hello World程序。 
---

## **系统要求**
Aspose.Cells for Python通过.NET 是独立于平台的API，可在已安装[Python](https://www.python.org/downloads/)的任何平台（Windows和Linux）上使用。 

## **Python版本**
- Python 3.6或更高版本

## **安装**
### **Windows:**
你可以通过以下命令轻松地使用Aspose.Cells for Python，称为.NET，从[pypi](https://pypi.org/project/aspose-cells-python/)。
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
你可以通过以下命令轻松地使用Aspose.Cells for Python，称为.NET，从[pypi](https://pypi.org/project/aspose-cells-python/)。
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：您需要在安装前运行以下命令
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS：**
你可以通过以下命令轻松地使用Aspose.Cells for Python，称为.NET，从[pypi](https://pypi.org/project/aspose-cells-python/)。
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：如果你的Python版本是Python3.7（以python3.7为例），在安装aspose-cells-python后，可能会出现以下错误
  '/usr/local/lib/libpython3.7m.dylib'（找不到文件），'/usr/lib/libpython3.7m.dylib'（找不到文件）。
  在这种情况下，请将以下命令添加到您的bash_profile（首先找到libpython3.7m.dylib的位置，以/Library/Frameworks/Python.framework/Versions/3.7/lib为例）。
  例如在这里）。
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- 注意：由于我们依赖于SkiaSharp图形库，如果遇到以下错误：
**System.DllNotFoundException: 无法加载共享库'libSkiaSharp'或其任何依赖项。** 请安装SkiaSharp。
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
安装后，请运行以下命令 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

当然，如果你想更简单些，你也可以下载[libSkiaSharp.dylib](libSkiaSharp.dylib)，然后**复制**到**/usr/local/lib**目录。

## **如何使用Aspose.Cells for Python via .NET创建Hello World应用程序**

- 创建一个名为**CreatingHelloWorldFile.py**的文件，并使用以下示例代码：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- 现在将上面的代码保存为"CreatingHelloWorldFile.py"并在"python CreatingHelloWorldFile.py" @命令提示符处运行。

## **Python via .NET示例 github**
- 请访问[Aspose.Cells for Python via .NET Example](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github查看更多示例代码。


