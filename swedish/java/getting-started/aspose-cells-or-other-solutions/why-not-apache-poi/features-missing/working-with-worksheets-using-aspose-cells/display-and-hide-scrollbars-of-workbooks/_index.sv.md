---
title: Visa och dölj rullningslister för arbetsböcker
type: docs
weight: 40
url: /sv/java/display-and-hide-scrollbars-of-workbooks/
---
## **Aspose.Cells - Visa och dölj rullningslister för arbetsböcker**
 Aspose.Cells tillhandahåller en klass,**Arbetsbok** som representerar en Excel-fil.**Arbetsbok** class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. Men för att kontrollera synligheten för rullningslisterna i Excel-filen kan utvecklare använda**setVScrollBarVisible** & **setHScrollBarVisible** metoder för**Arbetsbok** klass.

**Java**

{{< highlight "java" >}}

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
## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
