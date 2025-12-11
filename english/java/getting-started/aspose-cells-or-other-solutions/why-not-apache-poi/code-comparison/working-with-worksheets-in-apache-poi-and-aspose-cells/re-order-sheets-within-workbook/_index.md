---
title: Re-Order Sheets Within Workbook
type: docs
weight: 50
url: /java/re-order-sheets-within-workbook/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Re-Order Sheets Within Workbook**
Aspose.Cells provides a method, `Worksheet.moveTo()`, used to move a worksheet to another location in the same spreadsheet.

**Java**

{{< highlight java >}}
 //Create a new Workbook.
Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();
Worksheet worksheet1 = worksheets.get(0);
Worksheet worksheet2 = worksheets.add("Sheet2");
Worksheet worksheet3 = worksheets.add("Sheet3");

//Move Sheets within Workbook.
worksheet2.moveTo(0);
worksheet1.moveTo(1);
worksheet3.moveTo(2);

//Save the Excel file.
workbook.save(dataDir + "AsposeMoveSheet.xls");
{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Re-Order Sheets Within Workbook**
Apache POI provides the `Workbook.setSheetOrder()` method to set worksheets in the required order.

**Java**

{{< highlight java >}}
Workbook wb = new HSSFWorkbook();
wb.createSheet("new sheet");
wb.createSheet("second sheet");
wb.createSheet("third sheet");
wb.setSheetOrder("second sheet", 0);
wb.setSheetOrder("new sheet", 1);
wb.setSheetOrder("third sheet", 2);
FileOutputStream fileOut = new FileOutputStream(dataDir + "Apache_Reordered.xls");
wb.write(fileOut);
fileOut.close();
{{< /highlight >}}

## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/reordersheets)

{{% alert color="primary" %}} 
For more details, visit [Copying and Moving Worksheets](/cells/java/copying-and-moving-worksheets).
{{% /alert %}}

{{< app/cells/assistant language="java" >}}
