---
title : "Extract OLE Objects from Workbook" 
description : "" 
weight : 20432 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/extract+ole+objects+from+workbook/
---

# Aspose.Cells for .NET : Extract OLE Objects from Workbook


Sometimes, you do need to extract OLE objects from a workbook. Aspose.Cells supports extracting and saving those OLe objects.

This article shows how to create a console application in Visual Studio.Net and extract different OLE objects from a workbook with a few simple lines of code.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Extract OLE Objects from a Workbook](#extract-ole-objects-from-a-workbook)
    *   1.1 [Creating a Template Workbook](#creating-a-template-workbook)
    *   1.2 [Download and Install Aspose.Cells](#download-and-install-aspose.cells)
    *   1.3 [Create a Project](#create-a-project)
    *   1.4 [Extract OLE Objects](#extract-ole-objects)
{{< /panel >}}
 

 

## Extract OLE Objects from a Workbook

### Creating a Template Workbook

1.  Created a workbook in Microsoft Excel.
2.  Add a Microsoft Word document, an Excel workbook and a PDF document as OLE objects on first worksheet.
    
{{< table style="table-striped" >}}
|Template document with OLE objects (OleFile.xls)|
|:----|
|        ![](https://docs2.aspose.com/cells/net/attachments/5017693/5112157.png)        Next extract the OLE objects and save them to the hard disk with their respective file types.    |
{{< /table >}}

### Download and Install Aspose.Cells

1.  [Download Aspose.Cells for .NET](http://www.aspose.com/community/files/51/.net-components/aspose.cells-for-.net/default.aspx).
2.  Install it on your development computer.

All Aspose components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.

### Create a Project

Start **Visual Studio.Net** and create a new console application. This example will show a C# console application, but you can use VB.NET too.

1.  Add References
    1.  Add a reference to Aspose.Cells component to your project, for example add a reference to ...\\Program Files\\Aspose\\Aspose.Cells\\Bin\\Net1.0\\Aspose.Cells.dll

### Extract OLE Objects

The code below does the actual work of finding and extracting OLE objects. The OLE objects (DOC, XLS and PDF files) are saved to disk.

