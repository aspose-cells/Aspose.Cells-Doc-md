---
title: Setup Environment and Installation Guidelines
linktitle: Getting Started
type: docs
weight: 4
url: /python-java/setup-environment-and-installation-guidelines/
aliases: [/java/aspose-cells-for-python-via-java-system-requirements/, /pythonjava/system-requirements/]
keywords: "python, excel, install"
description: Setup Aspose.Cells for Python via Java and installation guidelines.
---

## **System Requirements**
Aspose.Cells for Python via Java is platform-independent API and can be used on any platform (Windows, Linux and MacOS) where [Python](https://www.python.org/downloads/) is installed. The machine must have Java 8 or greater versions before setting up the installation.

## **Python Version**
- Python 3.5 or higher
## **Java Version**
- Java 1.8 or higher

## **Windows:**
### **Install Java and set the JAVA_HOME and PATH environment variables**
For example:
{{< highlight java >}}

JAVA_HOME=C:\jdk1.8.0_131

PATH=C:\jdk1.8.0_131\bin;

{{< /highlight >}}
  
### **Install Aspose.Cells for Python via Java from pypi**
You can easily use Aspose.Cells for Python via Java from [pypi](https://pypi.org/project/aspose-cells/) with the following command.
{{< highlight java >}}

 $ pip install aspose-cells

{{< /highlight >}}

### **Test Aspose.Cells for Python via Java**
- Create a file named **example.py** and use the following sample code:

{{< highlight java >}}

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType

workbook = Workbook(FileFormatType.XLSX)
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
workbook.save("output.xlsx")

jpype.shutdownJVM()

{{< /highlight >}}

- Now run "python example.py" @command prompt to run it.

## **Linux:**
### **Install Java**
  
### **Install Aspose.Cells for Python via Java from pypi**
You can easily use Aspose.Cells for Python via Java from [pypi](https://pypi.org/project/aspose-cells/) with the following command.
{{< highlight java >}}

 $ pip install aspose-cells

{{< /highlight >}}

### **Test Aspose.Cells for Python via Java**
- Create a file named **example.py** and use the following sample code:

{{< highlight java >}}

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType

workbook = Workbook(FileFormatType.XLSX)
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
workbook.save("output.xlsx")

jpype.shutdownJVM()

{{< /highlight >}}

- Now run "python example.py" @command prompt to run it.

## **macOS:**
### **Install Java**
  
### **Install Aspose.Cells for Python via Java from pypi**
You can easily use Aspose.Cells for Python via Java from [pypi](https://pypi.org/project/aspose-cells/) with the following command.
{{< highlight java >}}

 $ pip install aspose-cells

{{< /highlight >}}

### **Test Aspose.Cells for Python via Java**
- Create a file named **example.py** and use the following sample code:

{{< highlight java >}}

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType

workbook = Workbook(FileFormatType.XLSX)
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
workbook.save("output.xlsx")

jpype.shutdownJVM()

{{< /highlight >}}

- Now run "python example.py" @command prompt to run it.

