---
title: Public API Changes in Aspose.Cells 8.8.2
type: docs
weight: 290
url: /java/public-api-changes-in-aspose-cells-8-8-2/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.8.1 to 8.8.2 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Automatically Update References while Deleting Blank Rows & Columns**
Aspose.Cells for Java 8.8.2 has exposed the overloaded versions of the Cells.deleteBlankRows & Cells.deleteBlankColumns methods. The new methods can accept an instance of DeleteOptions class and can be used to overcome the situations that could arise due to the broken references in formulas, chart series data and so on. The DeleteOptions class currently has only one member, a Boolean type property by the name UpdateReference. If the said property is set to true and the instance of DeleteOptions class is passed to the Cells.deleteBlankRows & Cells.deleteBlankColumns methods, the API will internally adjust the formula references (if any) to accommodate the changes. 

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Deleting Blank Rows & Columns with Updated References](/cells/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
