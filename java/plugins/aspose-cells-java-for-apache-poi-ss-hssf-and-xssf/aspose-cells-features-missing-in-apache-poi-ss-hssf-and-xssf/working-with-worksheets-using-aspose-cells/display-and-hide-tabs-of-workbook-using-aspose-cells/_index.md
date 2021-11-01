---
title: Display and Hide Tabs of Workbook using Aspose.Cells
type: docs
weight: 50
url: /java/display-and-hide-tabs-of-workbook-using-aspose-cells/
---

## **Aspose.Cells - Display and Hide Tabs of Workbook**
Aspose.Cells provides a class, Workbook, that represents a Microsoft Excel file. The Workbook class provides a wide range of properties and methods for managing an Excel file. To control the visibility of tabs in an Excel file, developers can use the Workbook class' setShowTabs method.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file

workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplayTabs.xls");

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)

{{% alert color="primary" %}} 

For more details, visit [Display or Hide Tabs](http://www.aspose.com/docs/display/cellsjava/Display+or+Hide+Tabs).

{{% /alert %}}
