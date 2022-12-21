---
title: ワークブックの印刷
type: docs
weight: 20
url: /ja/java/printing-workbooks/
description: この記事では、Aspose.Cells for Java API を使用してワークシートとブックを印刷する Java コードを提供します。
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

このドキュメントは、開発者がスプレッドシートを印刷する方法を (簡潔に) 理解できるようにすることを目的としています。

{{% /alert %}}

## 利用シーン

スプレッドシートの作成が完了したら、必要に応じてシートのハード コピーを印刷することをお勧めします。印刷するとき、MS Excel は、選択を指定しない限り、ワークシート領域全体を印刷すると想定します。次のスクリーンショットは、Excel でワークブックを印刷するためのダイアログ ボックスを示しています。

![todo:画像_代替_文章](printing-workbooks_1.png)

**形：**印刷ダイアログボックス

## Aspose.Cells を使用したワークブックの印刷

Aspose.Cells for Java は、[**プリンターへ**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) の方法[**シートレンダリング**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)クラス。を使用することにより、[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) メソッドでは、印刷ジョブ名だけでなくプリンター名も指定できます。

## サンプルコード

### 選択したワークシートを印刷

次のコード スニペットは、[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)メソッドを使用して、選択したワークシートを印刷します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### ワークブック全体を印刷

また、[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) ) ワークブック全体を印刷するメソッド。次のコード スニペットは、[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) ワークブック全体を印刷するメソッド。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## 関連記事

- [Aspose.Cells で印刷中にジョブまたはドキュメント名を指定する](/cells/ja/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
