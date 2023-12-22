---
title: 自动调整行和列
type: docs
weight: 10
url: /zh/java/auto-fit-row-and-column/
description: 通过 Aspose.Cells for Java API 了解如何自动调整行和列。
keywords: How to Autofit Row and Column in Java, Autofit Row Data in workbook using Java, Java Autofit Column Data. 
---
##  **如何使用 Aspose.Cells for Java 自动调整行和列**
自动调整行的宽度和高度的最直接方法是调用 Worksheet.autoFitRow 方法。 autoFitRow 方法采用行索引（要调整大小的行的索引）作为参数。

**请注意：**如果您想使用 Java 自动调整 Excel 电子表格中的行和列，请访问[自动调整行和列](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

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
##  **Apache POI SS - HSSF XSSF - 自动调整行和列**
Apache POI SS - HSSF 和 XSSF 提供 Sheet.autoSizeColumn 来自动调整列

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
##  **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
##  **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
