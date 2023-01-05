---
title: xlsx4j でワークブックを印刷する
type: docs
weight: 30
url: /ja/java/printing-workbooks-in-xlsx4j/
---
## **Aspose.Cells - ワークブックの印刷**
スプレッドシートの作成が完了したら、必要に応じてシートのハード コピーを印刷することをお勧めします。印刷するとき、MS Excel は、選択を指定しない限り、ワークシート領域全体を印刷すると想定します。

**ワークシートの印刷**

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook

Workbook book = new Workbook(dataDir + "AsposeDataInput.xls");

//Create an object for ImageOptions

ImageOrPrintOptions  imgOptions = new ImageOrPrintOptions ();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}

**ワークブックの印刷**

**Java**

{{< highlight "java" >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ワークブックの印刷](/cells/ja/java/printing-workbooks).

{{% /alert %}}
