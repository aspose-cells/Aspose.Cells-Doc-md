---
title: Automatisk anpassning av rad och kolumn
type: docs
weight: 10
url: /sv/java/auto-fit-row-and-column/
description: Lär dig hur man automatiskt anpassar rad och kolumn genom API Aspose.Cells for Java.
keywords: Hur man automatiskt anpassar rad och kolumn i Java, Automatisk datanpassning av rader i arbetsbok med Java, Java autofit kolumndata. 
---

## **Så här använder du Aspose.Cells for Java för automatisk anpassning av rad och kolumn**
Det mest raka tillvägagångssättet för att automatiskt ändra bredd och höjd på en rad är att använda metoden Worksheet.autoFitRow. Metoden autoFitRow tar ett radindex (av den rad som ska ändras storleken på) som parameter.

** Observera:** Om du vill anpassa rader och kolumner i Excel-kalkylblad med Java, besök [Autofit Rader och Kolumner](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Auto Fit Row and Column**
Apache POI SS - HSSF och XSSF tillhandahåller Sheet.autoSizeColumn för att automatiskt anpassa kolumnerna

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet("new sheet");

sheet.autoSizeColumn(0); //adjust width of the first column

sheet.autoSizeColumn(1); //adjust width of the second column

FileOutputStream fileOut;

fileOut = new FileOutputStream("AutoFit_Apache.xls");

workbook.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
