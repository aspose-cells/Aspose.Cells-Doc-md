---
title: 行と列の自動調整
type: docs
weight: 10
url: /ja/java/auto-fit-row-and-column/
---
## **Aspose.Cells - 行と列の自動調整**
行の幅と高さを自動サイズ変更する最も簡単な方法は、Worksheet.autoFitRow メソッドを呼び出すことです。 autoFitRow メソッドは、(サイズ変更する行の) 行インデックスをパラメーターとして受け取ります。

**ご注意ください：**Java を使用して Excel スプレッドシートの行と列を自動調整する場合は、次の URL にアクセスしてください。[行と列の自動調整](https://docs.aspose.com/cells/java/autofit-rows-and-columns/).

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
## **Apache POI SS - HSSF XSSF - 行と列の自動調整**
Apache POI SS - HSSF および XSSF は、列を自動調整するための Sheet.autoSizeColumn を提供します

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
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/autofitrowandcolumn)
