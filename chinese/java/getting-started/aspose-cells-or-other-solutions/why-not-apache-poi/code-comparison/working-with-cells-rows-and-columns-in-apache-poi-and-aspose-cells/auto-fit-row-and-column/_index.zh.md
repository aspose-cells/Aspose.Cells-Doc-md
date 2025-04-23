---
title: 自动调整行和列
type: docs
weight: 10
url: /zh/java/auto-fit-row-and-column/
description: 通过Aspose.Cells for Java API了解如何自动调整行和列。
keywords: 如何在Java中自动调整行和列，使用Java在工作簿中自动调整行数据，Java自动调整列数据。 
---

## **如何使用Aspose.Cells for Java自动调整行和列**
自动调整行的宽度和高度的最直接方法是调用Worksheet.autoFitRow方法。autoFitRow方法接受要调整大小的行索引作为参数。

请注意：如果您希望使用Java自动调整Excel电子表格中的行和列，请访问 [自动调整行和列](https://docs.aspose.com/cells/java/autofit-rows-and-columns/)。

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
## **Apache POI SS - HSSF XSSF - 自适应行和列**
Apache POI SS - HSSF 和 XSSF 提供 Sheet.autoSizeColumn 以自动调整列宽

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
{{< app/cells/assistant language="java" >}}
