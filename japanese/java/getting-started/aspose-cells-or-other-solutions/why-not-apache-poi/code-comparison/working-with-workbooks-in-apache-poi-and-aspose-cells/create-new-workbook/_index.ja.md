---
title: 新しいワークブックを作成
type: docs
weight: 20
url: /ja/java/create-new-workbook/
---
## **Aspose.Cells - 新しいワークブックの作成**
ワークブッククラスは簡単に使用できます

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.save("newWorkBook.xlsx", SaveFormat.XLSX); //Workbooks can be saved in many formats

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 新しいワークブックの作成**
Workbook クラスを使用して新しい Workbook を作成し、FileOutputStream を使用して保存します。

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

FileOutputStream fileOut;

fileOut = new FileOutputStream("newWorkbook.xls");

wb.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/createnewworkbook)
