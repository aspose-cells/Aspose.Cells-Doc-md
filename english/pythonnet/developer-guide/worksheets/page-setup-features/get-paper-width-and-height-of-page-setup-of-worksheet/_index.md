---
title: Get Paper Width and Height of Page Setup of Worksheet
type: docs
weight: 50
url: /python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: You will discover in this article how to get the Excel Worksheet Page Setup Paper Width and Paper Height using python code programmatically with Aspsoe.Cells for Python via .NET API or Library.
keywords: Python Excel Library, Python excel page setup paper width, excel page setup paper height in Python.
---

## **Possible Usage Scenarios**

Sometimes, you need to know the width and height of paper size as it has been set in page setup of the worksheet. Please use the [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) and [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) properties for this purpose.

## **Get Paper Width and Height of Page Setup of Worksheet**

The following sample code explains the usage of [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) and [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) properties. It first changes the paper size to *A2* and then finds the width and height of the paper, then it changes it to *A3*, *A4*, *Letter* and finds the width and height of paper respectively.

### **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **Console Output**

Here is the console output of the above sample code.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
