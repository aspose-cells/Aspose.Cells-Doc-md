---
title: Extract OLE Objects from Workbook
type: docs
weight: 110
url: /python-net/extract-ole-objects-from-workbook/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to extract OLE objects from a workbook. Aspose.Cells for Python via .NET supports extracting and saving those OLE objects.

This article shows how to create a console application in Visual Studio .NET and extract different OLE objects from a workbook with a few simple lines of code.

{{% /alert %}}

## **Extract OLE Objects from a Workbook**

### **Creating a Template Workbook**

1. Create a workbook in Microsoft Excel.  
1. Add a Microsoft Word document, an Excel workbook, and a PDF document as OLE objects on the first worksheet.

|**Template document with OLE objects (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Next, extract the OLE objects and save them to the hard disk with their respective file types.

### **Extract OLE Objects Using Aspose.Cells for Python Excel Library**

The code below does the actual work of finding and extracting OLE objects. The OLE objects (DOC, XLS, and PDF files) are saved to disk.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
