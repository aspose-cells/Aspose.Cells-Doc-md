---
title: xlsx4j でのスプレッドシートの PDF への変換
type: docs
weight: 10
url: /ja/java/convert-spreadsheet-to-pdf-in-xlsx4j/
---

## **Aspose.Cells - XLS を PDF に変換**
PDFドキュメントは組織間、政府セクター、個人間での文書交換の標準フォーマットとして広く使用されています。ソフトウェア開発者は、Microsoft Excelファイルを簡単にPDF文書に変換する方法を考案するよう求められることがよくあります。Aspose.Cellsはこの機能をサポートしています。

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Save the document in PDF format

workbook.save(dataDir + "AsposeConvert.pdf", SaveFormat.PDF);

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/converter/converttoformats/AsposeConverter.java)

{{% alert color="primary" %}} 

詳細については、[Excel ファイルを PDF に変換](/java/converting-excel-to-pdf-files) をご覧ください。

{{% /alert %}}
