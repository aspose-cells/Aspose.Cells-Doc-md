---
title: Aspose.Cells で印刷時にジョブまたはドキュメント名を指定する
type: docs
weight: 160
url: /ja/java/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してワークブックまたはワークシートを印刷する際に、[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)または[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)オブジェクトを使用してジョブまたは文書名を指定することができます。Aspose.Cellsは、ワークブックまたはワークシートを印刷する際に使用できる[**WorkbookRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-java.lang.String-)および[**SheetRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-java.lang.String-)メソッドを提供しています。

{{% /alert %}}

## **Aspose.Cellsを使用して印刷時にジョブまたは文書名を指定する**

サンプルコードは、ソースExcelファイルを読み込み、[**WorkbookRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-java.lang.String-)および[**SheetRender.toPrinter(printerName, jobName)**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-java.lang.String-)メソッドを使用して印刷時にジョブまたは文書名を指定し、プリンターキュー内でのジョブ名の表示を示しています。

![todo:image_alt_text](specify-job-or-document-name-while-printing-with-aspose-cells_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyJoborDocumentName-SpecifyJoborDocumentName.java" >}}

## 関連記事

- [ワークブックの印刷](/cells/ja/java/printing-workbooks/)
{{< app/cells/assistant language="java" >}}
