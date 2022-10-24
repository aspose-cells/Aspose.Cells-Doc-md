---
title: Getting Started
linktitle: Getting Started
type: docs
weight: 4
url: /python-net/getting-started/ 
aliases: [/aspose-cells-for-python-via-net-system-requirements/, /pythonnet/system-requirements/, /python-net/setup-environment-and-installation-guidelines/]
keywords: "python, excel, install"
description: Setup Aspose.Cells for Python via .NET and installation guidelines.
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

### **MacOS:**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Note:If your python is Python3.7,after installung the aspose-cells-python,There may be the following errors
  '/usr/local/lib/libpython3.7m.dylib' (no such file), '/usr/lib/libpython3.7m.dylib' (no such file) prompt.
  Please add the following command to your bash_profile(Find where is libpython3.7m.dylib first,take /Library/Frameworks/Python.framework/Versions/3.7/lib
  for example here)
  {{< highlight NET >}}
    export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
	export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
  {{< /highlight >}}
## **Creating the Hello World Application**

- Create a file named **CreatingHelloWorldFile.py** and use the following sample code:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Now save the code above to "CreatingHelloWorldFile.py" and run "python CreatingHelloWorldFile.py" @command prompt.
