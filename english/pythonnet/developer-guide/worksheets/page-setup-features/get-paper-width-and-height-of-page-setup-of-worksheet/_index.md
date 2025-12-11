---
title: Get Paper Width and Height of Page Setup of Worksheet
type: docs
weight: 50
url: /python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: You will discover in this article how to get the Excel worksheet page‑setup paper width and paper height using Python code programmatically with Aspose.Cells for Python via the .NET API or library.
keywords: Python Excel Library, Python Excel page setup paper width, Excel page setup paper height in Python.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, you need to know the width and height of the paper size as set in the page setup of a worksheet. Please use the [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) and [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) properties for this purpose.

## **Get Paper Width and Height of Page Setup of Worksheet**

The following sample code demonstrates the usage of [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) and [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) properties. It first changes the paper size to *A2* and obtains the width and height of the paper; then it changes the size to *A3*, *A4*, and *Letter*, retrieving the dimensions for each size respectively.

### **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **Console Output**

Here is the console output of the above sample code.

{{< highlight python >}}
PaperA2: 16.54x23.39
PaperA3: 11.69x16.54
PaperA4: 8.27x11.69
PaperLetter: 8.5x11
{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
