---
title: Display and Hide Tabs of Workbook using Aspose.Cells
type: docs
weight: 50
url: /java/display-and-hide-tabs-of-workbook-using-aspose-cells/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Display and Hide Tabs of Workbook**
Aspose.Cells provides a class, Workbook, that represents a Microsoft Excel file. The Workbook class provides a wide range of properties and methods for managing an Excel file. To control the visibility of tabs in an Excel file, developers can use the Workbook class’s setShowTabs method.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object by Excel file path
Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in the default (that is Excel 2003) format
workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in the default (that is Excel 2003) format
workbook.save(dataDir + "AsposeDisplayTabs.xls");

{{< /highlight >}}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)

{{< app/cells/assistant language="java" >}}
