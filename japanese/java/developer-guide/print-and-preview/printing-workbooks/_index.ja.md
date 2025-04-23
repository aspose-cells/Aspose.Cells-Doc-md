---
title: ワークブックの印刷
type: docs
weight: 20
url: /ja/java/printing-workbooks/
description: Javaを使用してワークシートおよびワークブックを印刷する方法。この記事では、Aspose.Cells for Java APIを使用してワークシートおよびワークブックを印刷するためのJavaコードを提供します。
keywords: ワークブックの印刷、ワークシートの印刷、ワークブックシートの印刷、ワークブックの印刷、ワークブックの印刷Java、ワークシートの印刷Java、エクセルワークブックの印刷Java、エクセルワークシートの印刷Java、ワークブックの印刷、ワークシートの印刷
---

{{% alert color="primary" %}}

このドキュメントは、開発者にスプレッドシートの印刷方法についての理解を提供するために設計されています。

{{% /alert %}}

## 使用シナリオ

スプレッドシートの作成が完了したら、必要に応じてシートの印刷を行いたいと思うでしょう。印刷時、MS Excelは選択を指定しない限り、ワークシート全体を印刷したいと仮定します。以下のスクリーンショットはExcelでワークブックを印刷するためのダイアログボックスを示しています。

![todo:image_alt_text](printing-workbooks_1.png)

**図:** 印刷ダイアログボックス

## Aspose.Cellsを使用したワークブックの印刷

Aspose.Cells for Javaは[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)クラスの[**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-)メソッドを提供します。[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-)メソッドを使用することで、プリンター名および印刷ジョブ名を指定できます。

## サンプルコード

### 選択したワークシートの印刷

[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-)メソッドを使用して選択したワークシートを印刷する使用例を次に示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### ワークブック全体の印刷

[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-)メソッドを使用してワークブック全体を印刷する使用例を次に示します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## 関連記事

- [Aspose.Cellsを使用して印刷時にジョブまたは文書名を指定する](/cells/ja/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="java" >}}
