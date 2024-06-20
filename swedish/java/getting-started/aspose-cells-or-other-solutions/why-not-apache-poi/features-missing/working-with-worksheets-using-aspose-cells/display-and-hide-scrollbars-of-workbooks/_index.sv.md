---
title: Visa och dölj scrollbarer för arbetsböcker
type: docs
weight: 40
url: /sv/java/display-and-hide-scrollbars-of-workbooks/
---

## **Aspose.Cells - Visa och dölj rullningsfält för arbetsböcker**
Aspose.Cells tillhandahåller en klass, **Workbook**, som representerar en Excelfil. **Workbook**-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excelfil. Men för att kontrollera synligheten av rullningsfälten i Excelfilen kan utvecklare använda metoderna **setVScrollBarVisible** och **setHScrollBarVisible** i **Workbook**-klassen.

**Java**

{{< highlight java >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **Ladda ned körbar kod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
