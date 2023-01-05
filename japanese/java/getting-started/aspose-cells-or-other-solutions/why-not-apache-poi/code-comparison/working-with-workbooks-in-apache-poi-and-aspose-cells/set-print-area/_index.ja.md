---
title: 印刷範囲の設定
type: docs
weight: 40
url: /ja/java/set-print-area/
---
## **Aspose.Cells - 印刷範囲の設定**
デフォルトでは、データを含むワークシートのすべての領域が印刷領域に組み込まれます。開発者は、ワークシートの特定の印刷領域を設定できます。

特定の印刷領域を選択するには、[ページ設定](/java/pagesetup)クラスの setPrintArea メソッド。印刷領域を定義するセル範囲をこのプロパティに割り当てます。

**Java**

{{< highlight "java" >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Workbook file

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.setPrintArea("A1:F20");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 印刷範囲の設定**
Workbook.setPrintArea メソッドを使用して、印刷領域のページ プロパティを設定できます。

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("Sheet1");

//sets the print area for the first sheet

wb.setPrintArea(0, "$A$1:$C$2");

//Alternatively:

wb.setPrintArea(

        0, //sheet index

        0, //start column

        1, //end column

        0, //start row

        0  //end row

);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/setprintarea)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[印刷オプションの設定](/cells/ja/java/page-setup-features/#setting-print-options).

{{% /alert %}}
