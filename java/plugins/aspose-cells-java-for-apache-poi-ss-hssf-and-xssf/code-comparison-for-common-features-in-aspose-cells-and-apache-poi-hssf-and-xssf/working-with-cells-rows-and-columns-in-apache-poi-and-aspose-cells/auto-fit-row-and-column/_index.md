---
title: Auto Fit Row and Column
type: docs
weight: 10
url: /java/auto-fit-row-and-column/
---

## **Aspose.Cells - Auto Fit Row and Column**
The most straight-forward approach to auto-sizing the width and height of a row is to call the Worksheet.autoFitRow method. The autoFitRow method takes a row index (of the row to be resized) as a parameter.

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
Apache POI SS - HSSF and XSSF provides Sheet.autoSizeColumn to auto fit columns

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
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)

{{% alert color="primary" %}} 

For more details, visit [Autofit Rows and Columns](http://docs.aspose.com:8082/docs/display/cellsjava/Autofit+Rows+and+Columns).

{{% /alert %}}
