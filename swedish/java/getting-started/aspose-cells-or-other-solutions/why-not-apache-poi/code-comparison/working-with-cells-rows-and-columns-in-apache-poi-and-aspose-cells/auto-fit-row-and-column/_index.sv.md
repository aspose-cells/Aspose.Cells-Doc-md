---
title: Autopassa rad och kolumn
type: docs
weight: 10
url: /sv/java/auto-fit-row-and-column/
---
## **Aspose.Cells - Autopassa rad och kolumn**
Det enklaste sättet att automatiskt anpassa bredd och höjd på en rad är att anropa metoden Worksheet.autoFitRow. AutoFitRow-metoden tar ett radindex (för raden som ska ändras storlek) som en parameter.

**Vänligen notera:**Om du vill automatiskt anpassa rader och kolumner i Excel-kalkylblad med Java, vänligen besök[Autopassa rader och kolumner](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); //Auto-fitting the 2nd row of the worksheet

worksheet.autoFitColumn(0); //Auto-fitting the 1st column of the worksheet

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save("AutoFit_Aspose.xls");


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Autopassning av rad och kolumn**
Apache POI SS - HSSF och XSSF tillhandahåller Sheet.autoSizeColumn för att automatiskt anpassa kolumner

**Java**

{{< highlight "java" >}}

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
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
