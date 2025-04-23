---
title: 行と列の自動調整
type: docs
weight: 10
url: /ja/java/auto-fit-row-and-column/
description: Aspose.Cells for Java API を使用して行と列の自動調整方法を学びます。
keywords: Javaで行と列の自動調整方法、ワークブック内の行データの自動調整方法、Javaで列データの自動調整方法の方法について学ぶ。 
---

## **Aspose.Cells for Javaを使用して行と列の自動調整方法**
行の幅と高さを自動調整するもっとも簡単な方法は、Worksheet.autoFitRow メソッドを呼び出すことです。autoFitRow メソッドは、変更する行のインデックスをパラメータとして取ります。

Javaを使用してExcelスプレッドシート内の行と列を自動調整する場合は、[行と列の自動調整](https://docs.aspose.com/cells/java/autofit-rows-and-columns/)をご覧ください。

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
## **Apache POI SS - HSSF XSSF - 行と列の自動調整**
Apache POI SS - HSSF and XSSF は、Sheet.autoSizeColumn を使用して列を自動調整します

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
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
{{< app/cells/assistant language="java" >}}
