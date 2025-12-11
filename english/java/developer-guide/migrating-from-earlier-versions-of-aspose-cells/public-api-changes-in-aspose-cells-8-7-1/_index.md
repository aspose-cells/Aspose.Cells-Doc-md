---
title: Public API Changes in Aspose.Cells 8.7.1
type: docs
weight: 250
url: /java/public-api-changes-in-aspose-cells-8-7-1/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.7.0 to 8.7.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes, etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Added LookInType.ORIGINAL_VALUES Property**
Aspose.Cells APIs already support the [Find or Search Data](/cells/java/find-or-search-data/) feature for spreadsheets in order to find a particular piece of content in cell values and formulas. However, this feature lacked the aspect of formatting applied to the cell that may change the appearance as well as the value of the contents, consequently making the text unsearchable when using the original value. With this release of Aspose.Cells APIs, another constant named **LookInType.ORIGINAL_VALUES** has been exposed to the public API, which allows you to overcome the situation described above. 

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Search Data Using Original Values](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

The following is a simple usage scenario.

**Java**

{{< highlight java >}}

 //Create workbook object
 Workbook workbook = new Workbook();

 //Access first worksheet
 Worksheet worksheet = workbook.getWorksheets().get(0);

 //Add 10 to cells A1 and A2
 worksheet.getCells().get("A1").putValue(10);
 worksheet.getCells().get("A2").putValue(10);

 //Add Sum formula in cell D4 but customize it as ---
 Cell cell = worksheet.getCells().get("D4");
 Style style = cell.getStyle();
 style.setCustom("---");
 cell.setStyle(style);

 //The result of the formula will be 20
 //but 20 will not be visible because
 //the cell is formatted as ---
 cell.setFormula("=Sum(A1:A2)");

 //Calculate the workbook
 workbook.calculateFormula();

 //Create find options
 FindOptions options = new FindOptions();
 options.setLookInType(LookInType.ORIGINAL_VALUES);
 options.setLookAtType(LookAtType.ENTIRE_CONTENT);
 Cell foundCell = null;
 Object obj = 20;

 //Find 20, which is Sum(A1:A2) and formatted as ---
 foundCell = worksheet.getCells().find(obj, foundCell, options);

 //Print the found cell
 System.out.println(foundCell);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
