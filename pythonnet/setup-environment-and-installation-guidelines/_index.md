---
title: Setup Environment and Installation Guidelines
linktitle: Getting Started
type: docs
weight: 4
url: /python-net/setup-environment-and-installation-guidelines/
aliases: [/aspose-cells-for-python-via-net-system-requirements/, /pythonnet/system-requirements/]
keywords: "python, excel, install"
description: Setup Aspose.Cells for Python via .NET and installation guidelines.
---

## **System Requirements**
Aspose.Cells for Python via .NET is platform-independent API and can be used on any platform (Windows and Linux) where [Python](https://www.python.org/downloads/) is installed. 

## **Python Version**
- Python 3.7 or higher

## **Installing**
### **Windows:**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

Run Aspose.Cells for Python via .NET in Windows
- Create or pull a file named [HelloWorld.py](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Example) ,you can also use the following sample code:

{{< highlight NET >}}

import aspose.cells
from aspose.cells import Workbook, FileFormatType

workbook = Workbook(FileFormatType.XLSX)
workbook.worksheets.get(0).cells.get("A1").put_value("Hello World")
workbook.save("output.xlsx")

{{< /highlight >}}

- Now save the code above to "HelloWorld.py" and run "python HelloWorld.py" @command prompt to test it.

### **Linux:**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

Run Aspose.Cells for Python via .NET in Linux
- Create or pull a file named [HelloWorld.py](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Example) ,you can also use the following sample code:

{{< highlight NET >}}

import aspose.cells
from aspose.cells import Workbook, FileFormatType

workbook = Workbook(FileFormatType.XLSX)
workbook.worksheets.get(0).cells.get("A1").put_value("Hello World")
workbook.save("output.xlsx")

{{< /highlight >}}

- Now save the code above to "HelloWorld.py" and run "python HelloWorld.py" @command prompt.


