---
title : "Copy Worksheets" 
description : "" 
weight : 16794 
toc : false
type: docs
url: /net/plugins/vsto/codeinvsto/copy+worksheets/
---

# Aspose.Cells for .NET : Copy Worksheets


#### Migration Tip:

1\. Create Workbook object and get Worksheet.  
2\. Insert text in worksheet.  
3\. Create new Worksheet and Copy it to previous before made worksheet.

#### VSTO

Error rendering macro 'code' : Invalid value specified for parameter lang

#### Aspose.Cells

{{< code lang="cs" >}}
 private static string fileName ="CopyWorksheets.xlsx";
 Workbook newWorkbook = new Workbook();
 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");
 Cells cells = worksheet.Cells;
 cells[0, 0].PutValue("Some Text");
 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");
 worksheet2.Copy(worksheet);
 newWorkbook.Save(fileName);
{{< /code >}}

#### Download

*   [CodePlex](https://asposevsto.codeplex.com/downloads/get/1459764)
*   [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)

