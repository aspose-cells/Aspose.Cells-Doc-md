---
title: Different Ways to Open Files
type: docs
weight: 10
url: /python-net/different-ways-to-open-files/
description: This article explains how to open an excel file using Aspose.Cells for Python via .NET API.
keywords: Python Open an Excel file without Excel, How do I open an Excel File.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

With Aspose.Cells for Python via .NET it is simple to open files, for example, to retrieve data, or to use a designer template to speed up the development process.

{{% /alert %}}

## **How to Open an Excel File via a Path**

Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells for Python via .NET will automatically detect the file format type.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **How to Open an Excel File via a Stream**

It is also simple to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream* object that contains the file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **How to Open a File with Data only**

To open a file with data only, use the [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) and [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) classes to set the related attribute and options of the classes for the template file to be loaded.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
