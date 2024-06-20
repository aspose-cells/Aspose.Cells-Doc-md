---
title: ワークシートのすべての列を単一の PDF ページに収める
type: docs
weight: 70
url: /ja/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

ワークシートのすべての列を単一のページにフィットさせたい場合があります。[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) プロパティは、非常に使いやすく、出力 PDF ページの高さや幅などの複雑な計算は内部で処理され、ワークシートのデータに基づいています。

{{% /alert %}}

## **ワークシートの列を単一の PDF ページに収める**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) は、ワークシートのすべての列が単一の PDF ページにレンダリングされることを確実にします。ただし、ワークシートのデータに応じて複数のページにまたがることがあります。

{{% alert color="primary" %}}

あるワークシートに多くの列がある場合、レンダリングされた PDF ファイルは非常に小さなサイズでコンテンツが表示されることがあります。Acrobat Reader などの表示アプリケーションで拡大表示するとまだ読み取れます。

{{% /alert %}}

以下のサンプルコードは、[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) プロパティを使用して 100 列の大きなワークシートをレンダリングする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF 形式に変換する直前に [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) メソッドを呼び出すことが最適です。これにより、数式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
