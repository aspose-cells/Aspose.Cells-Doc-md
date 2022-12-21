---
title: ワークシートのすべての列を 1 つの PDF ページに収める
type: docs
weight: 70
url: /ja/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

ワークシートのすべての列が 1 ページに収まる PDF ファイルを生成したい場合があります。の[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)プロパティは、この機能を非常に使いやすい方法で提供します。出力 PDF ページの高さや幅などの複雑な計算は内部で処理され、ワークシートのデータに基づいています。

{{% /alert %}}

## **単一の PDF ページにワークシートの列を合わせる**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)ワークシートのすべての列が 1 つの PDF ページにレンダリングされることを保証しますが、ワークシートのデータによっては行が複数のページに拡張される場合があります。

{{% alert color="primary" %}}

特定のワークシートに多くの列がある場合、レンダリングされた PDF ファイルは非常に小さいサイズで内容を表示する場合があります。 Acrobat Reader などの表示アプリケーションで拡大しても、読み取り可能です。

{{% /alert %}}

以下のサンプル コードは、[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)プロパティを使用して、100 列の大きなワークシートをレンダリングします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) スプレッドシートを PDF 形式にレンダリングする直前のメソッド。そうすることで、数式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}
