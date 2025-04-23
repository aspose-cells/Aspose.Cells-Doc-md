---
title: Aspose.Cellsを使用したワークブックの印刷
type: docs
weight: 20
url: /ja/java/printing-workbooks-using-aspose-cells/
---

## **Aspose.Cells - ワークブックの印刷**
スプレッドシートの作成が完了したら、必要に応じてシートの印刷を行いたいと思うでしょう。印刷を行う際、MS Excelは特定の選択を指定しない限り、ワークシート全体を印刷するものと見なします。

ワークシートの印刷

**Java**

{{< highlight java >}}

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

ワークブックの印刷

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

詳細については、[ワークブックの印刷](/cells/ja/java/printing-workbooks)を参照してください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
