---
title: 入门
linktitle: 入门
type: docs
weight: 4
url: /zh/python-net/getting-started/
description: 了解如何安装Aspose.Cells for Python via .NET并创建Hello World应用程序。
keywords: 如何在Windows Linux和MacOS上安装Aspose.Cells for Python via .NET，Aspose.Cells for Python via .NET的安装指南，使用.NET的Python Hello World程序。 
---

## **系统要求**
Aspose.Cells for Python via .NET是独立于平台的API，可在任何安装了[Python](https://www.python.org/downloads/)的平台（Windows和Linux）上使用。 

## **Python版本**
- Python 3.6或更高版本

## **安装**
### **Windows:**
您可以使用以下命令轻松从[pypi](https://pypi.org/project/aspose-cells-python/)使用Aspose.Cells for Python via .NET。
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
您可以使用以下命令轻松从[pypi](https://pypi.org/project/aspose-cells-python/)使用Aspose.Cells for Python via .NET。
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：在安装前需要运行以下命令
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
您可以使用以下命令轻松从[pypi](https://pypi.org/project/aspose-cells-python/)使用Aspose.Cells for Python via .NET。
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- 注意：如果您的Python是Python3.7（以python3.7为例），在安装aspose-cells-python后，可能会出现以下错误
  '/usr/local/lib/libpython3.7m.dylib'（找不到文件），'/usr/lib/libpython3.7m.dylib'（找不到文件）提示。
  在这种情况下，请将以下命令添加到您的bash_profile（首先找到libpython3.7m.dylib的位置，取/Library/Frameworks/Python.framework/Versions/3.7/lib
  例如在这里）
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- 注意：由于我们依赖SkiaSharp图形库，如果遇到以下错误：
**System.DllNotFoundException: 无法加载共享库“libSkiaSharp”或其任何依赖项。**请安装SkiaSharp。
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.6
{{< /highlight >}}
安装后，请运行以下命令 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.6/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

当然，如果您想简化操作，也可以下载[libSkiaSharp.dylib](libSkiaSharp.dylib)，然后将其**复制**到**/usr/local/lib**目录中。

## **如何使用Aspose.Cells for Python via .NET创建 Hello World 应用程序**

- 创建名为**CreatingHelloWorldFile.py**的文件，并使用以下示例代码:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- 现在将上述代码保存为"CreatingHelloWorldFile.py"，并在命令提示符处运行"python CreatingHelloWorldFile.py"。

## **Python via .NET示例 github**
- 请访问[Aspose.Cells for Python via .NET 示例](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github查看更多示例代码。


