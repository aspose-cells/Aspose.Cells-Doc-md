---
title: Dölj och visa celler
type: docs
weight: 30
url: /sv/java/hide-and-unhide-cells/
---

## **Aspose.Cells - Dölj och visa rader och kolumner**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en WorksheetCollection som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen. Worksheet-klassen tillhandahåller en Cells-samling som representerar alla celler i kalkylarket. Cells-samlingen tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Dölj/visa celler**
För att dölja en rad eller kolumn tillhandahåller Apache POI SS-metoden Row.setZeroHeight(boolean).

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

För mer information, besök [Dölja och visa rader och kolumner](/java/hiding-and-showing-rows-and-columns).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
