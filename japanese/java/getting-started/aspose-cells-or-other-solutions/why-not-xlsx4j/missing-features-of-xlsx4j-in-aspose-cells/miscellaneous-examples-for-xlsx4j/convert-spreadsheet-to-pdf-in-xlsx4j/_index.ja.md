---
title: スプレッドシートをxlsx4jでPDFに変換
type: docs
weight: 10
url: /ja/java/convert-spreadsheet-to-pdf-in-xlsx4j/
---
## **Aspose.Cells - XLS を PDF に変換**
PDF ドキュメントは、組織、政府部門、および個人の間でドキュメントを交換するための標準形式として広く使用されています。ソフトウェア開発者は、Microsoft Excel ファイルを PDF ドキュメントに簡単に変換する方法を考案するように求められることがよくあります。 Aspose.Cells はこの機能をサポートしています。

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Save the document in PDF format

workbook.save(dataDir + "AsposeConvert.pdf", SaveFormat.PDF);

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/converter/converttoformats/AsposeConverter.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[Excel を PDF ファイルに変換する](/java/converting-excel-to-pdf-files).

{{% /alert %}}
