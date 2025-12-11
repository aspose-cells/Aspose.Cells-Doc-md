---
title: Auto Fit Row and Column
type: docs
weight: 10
url: /java/auto-fit-row-and-column/
description: Learn how to autofit rows and columns through the Aspose.Cells for Java API.
keywords: How to Autofit Row and Column in Java, Autofit Row Data in workbook using Java, Java Autofit Column Data. 
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **How to Auto Fit Row and Column Using Aspose.Cells for Java**
The most straight‑forward approach to auto‑sizing the width and height of a row is to call the `Worksheet.autoFitRow` method. The `autoFitRow` method takes a row index (of the row to be resized) as a parameter.

**Please note:** If you want to autofit rows and columns in Excel spreadsheets using Java, please visit [Autofit Rows and Columns](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

**Java**

{{< highlight java >}}

Workbook workbook = new Workbook("workbook.xls");

// Accessing the first worksheet in the Excel file
Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.autoFitRow(1); // Auto‑fitting the 2nd row of the worksheet
worksheet.autoFitColumn(0); // Auto‑fitting the 1st column of the worksheet

// Saving the modified Excel file in the default (that is Excel 2003) format
workbook.save("AutoFit_Aspose.xls");

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Auto Fit Row and Column**
Apache POI SS - HSSF and XSSF provide `Sheet.autoSizeColumn` to auto‑fit columns.

**Java**

{{< highlight java >}}

InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet("new sheet");

sheet.autoSizeColumn(0); // Adjusts the width of the first column
sheet.autoSizeColumn(1); // Adjusts the width of the second column

FileOutputStream fileOut;
fileOut = new FileOutputStream("AutoFit_Apache.xls");

workbook.write(fileOut);
fileOut.close();

{{< /highlight >}}

## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)

{{< app/cells/assistant language="java" >}}
