---
title: Getting Started
linktitle: Getting Started
type: docs
weight: 4
url: /python-net/getting-started/
description: Learn how to install Aspose.Cells for Python via .NET and create Hello World Application.
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---

## **System Requirements**
Aspose.Cells for Python via .NET is platform-independent API and can be used on any platform (Windows and Linux) where [Python](https://www.python.org/downloads/) is installed. 

## **Python Version**
- Python 3.6 or higher

## **Installation**
### **Windows:**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Note:You need to run the following command before installation
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Note:If your python is Python3.7(take python3.7, for example, here),after installing the aspose-cells-python,there may be the following errors
  '/usr/local/lib/libpython3.7m.dylib' (no such file), '/usr/lib/libpython3.7m.dylib' (no such file) prompt.
  In such a situation,please add the following command to your bash_profile(Find where is libpython3.7m.dylib first,take /Library/Frameworks/Python.framework/Versions/3.7/lib
  for example here)
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Note:Due to our reliance on the SkiaSharp graphics library, if you encounter the following error:
**System.DllNotFoundException: Unable to load shared library 'libSkiaSharp' or one of its dependencies.** please install SkiaSharp.
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.6
{{< /highlight >}}
After installation, please run the following command 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.6/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

Of course, if you want it simpler, you can also download [libSkiaSharp.dylib](libSkiaSharp.dylib) and then **copy** it to the **/usr/local/lib** directory.

## **How to Create the Hello World Application using Aspose.Cells for Python via .NET**

- Create a file named **CreatingHelloWorldFile.py** and use the following sample code:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Now save the code above to "CreatingHelloWorldFile.py" and run "python CreatingHelloWorldFile.py" @command prompt.

## **Python via .NET Example github**
- Please visit the [Aspose.Cells for Python via .NET Example](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github to view more sample codes.


