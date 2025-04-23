---
title: Visa och dölj flikar för arbetsbok i xlsx4j
type: docs
weight: 40
url: /sv/java/display-and-hide-tabs-of-workbook-in-xlsx4j/
---

## **Aspose.Cells - Visa och dölj flikar för arbetsbok**
Aspose.Cells tillhandahåller en klass, Workbook, som representerar en Microsoft Excel-fil. Workbook-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten av flikar i en Excel-fil kan utvecklare använda Workbook-klassens setShowTabs-metod.

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
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidetabs/AsposeDisplayAndHideTabs.java)
{{< app/cells/assistant language="java" >}}
