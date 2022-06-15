---
title: Setup Environment and Installation Guidelines
type: docs
weight: 20
url: /python-net/setup-environment-and-installation-guidelines/
aliases: [/aspose-cells-for-python-via-net-system-requirements/, /pythonnet/system-requirements/]
keywords: "python, excel, install"
description: Setup Aspose.Cells for Python via .NET and installation guidelines.
---

## **System Requirements**
Aspose.Cells for Python via .NET is platform-independent API and can be used on any platform (Windows and Linux) where [Python](https://www.python.org/downloads/) is installed. 

## **Python Version**
- Python 3.7 or higher

## **Windows:**
### **Install Aspose.Cells for Python via .NET from pypi**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Test Aspose.Cells for Python via .NET**
- Create a file named **example.py** and use the following sample code:

{{< highlight NET >}}

import aspose.cells
from asposecells import Workbook, FileFormatType

workbook = Workbook(FileFormatType.XLSX)
workbook.worksheets.get(0).cells.get("A1").put_value("Hello World")
workbook.save("output.xlsx")

{{< /highlight >}}

- Now run "python example.py" @command prompt to run it.

## **Linux:**
### **Install Aspose.Cells for Python via .NET from pypi**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Test Aspose.Cells for Python via .NET**
- Create a file named **example.py** and use the following sample code:

{{< highlight NET >}}

import aspose.cells
from asposecells import Workbook, FileFormatType

workbook = Workbook(FileFormatType.XLSX)
workbook.worksheets.get(0).cells.get("A1").put_value("Hello World")
workbook.save("output.xlsx")

{{< /highlight >}}

- Now run "python example.py" @command prompt to run it.


