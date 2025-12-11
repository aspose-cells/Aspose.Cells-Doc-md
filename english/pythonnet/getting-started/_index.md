---
title: Getting Started
linktitle: Getting Started
type: docs
weight: 4
url: /python-net/getting-started/
description: Learn how to install Aspose.Cells for Python via .NET and create a Hello World application.
keywords: How to install Aspose.Cells for Python via .NET in Windows, Linux, and macOS, installation guidelines for Aspose.Cells for Python via .NET, Python via .NET Hello World program.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **System Requirements**
Aspose.Cells for Python via .NET is a platform‑independent API and can be used on any platform (Windows, Linux, and macOS) where [Python](https://www.python.org/downloads/) is installed. 

## **Python Version**
- Python 3.6 or higher

## **Installation**
### **Windows:**
You can easily use Aspose.Cells for Python via .NET from [PyPI](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
You can easily use Aspose.Cells for Python via .NET from [PyPI](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Note: You need to run the following command before installation
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **macOS:**
You can easily use Aspose.Cells for Python via .NET from [PyPI](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Note: If your Python version is 3.7 (take Python 3.7 as an example), after installing **aspose-cells-python**, you may encounter errors such as  
`'/usr/local/lib/libpython3.7m.dylib' (no such file)` or `'/usr/lib/libpython3.7m.dylib' (no such file)`.  
In such a situation, please add the following commands to your **~/.bash_profile** (first locate where `libpython3.7m.dylib` resides, e.g., `/Library/Frameworks/Python.framework/Versions/3.7/lib`):
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Note: Due to our reliance on the SkiaSharp graphics library, if you encounter the following error:  

**System.DllNotFoundException: Unable to load shared library 'libSkiaSharp' or one of its dependencies.**  

please install SkiaSharp.
{{< highlight NET >}}
brew install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.6
{{< /highlight >}}
After installation, run the following command:
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.6/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

Of course, if you want a simpler approach, you can also download [libSkiaSharp.dylib](libSkiaSharp.dylib) and then **copy** it to the **/usr/local/lib** directory.

> ⚠️ **Note:**  
> In some cases, after installing a new version of **aspose-cells-python**, users may encounter an error like the following:  

> **While initializing the host for the ‘WrpNs_Aspose.WrpNs_Cells.WrpCs_Workbook_xxxxxx (Assembly=WrpInterop.Aspose.Cells)’ type, an error occurred – Method ‘call_000_xxxxxx’ not found**  

> This indicates that the previous version was not completely uninstalled, leading to a conflict between the newly installed version and the old one.  
> You can resolve this issue by following the steps below:

- First, create a clean virtual environment to ensure the latest version works properly on your Windows machine:

```bash
# Set up virtual environment
python -m venv .venv
.\.venv\Scripts\activate
# Install aspose-cells-python
pip install aspose-cells-python
```

Then run your program.

- If you prefer to continue using your original environment, please try the following steps:

```bash
pip uninstall aspose-cells-python
```

Make sure the uninstallation is successful. If any errors occur during uninstallation, try running the command multiple times.

Alternatively, locate your **site‑packages** directory, typically something like:

```
\Python3x\Lib\site-packages
```

Then manually delete the following directories (if they exist):

```
aspose
aspose_cells*
```

After that, reinstall the package:

```bash
pip install aspose-cells-python
```

## **How to Create the Hello World Application using Aspose.Cells for Python via .NET**

- Create a file named **CreatingHelloWorldFile.py** and use the following sample code:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Now save the code above to `CreatingHelloWorldFile.py` and run `python CreatingHelloWorldFile.py` at the command prompt.

## **Python via .NET Example GitHub**
- Please visit the [Aspose.Cells for Python via .NET Example repository on GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) to view more sample code.

{{< app/cells/assistant language="python-net" >}}
