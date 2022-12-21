---
title: 生成されるページ数を制限する - Excel から PDF への変換
type: docs
weight: 60
url: /ja/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

ある範囲のページを出力 PDF ファイルに印刷したい場合があります。 Aspose.Cells には、Excel スプレッドシートを PDF に変換するときに生成されるページ数に制限を設定する機能があります。

{{% /alert %}}

## **生成されるページ数の制限**

次の例は、Microsoft Excel ファイルのページ範囲 (3 と 4) を PDF にレンダリングする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) PDF 形式にレンダリングする直前。これにより、式に依存する値が再計算され、正しい値が出力ファイルに表示されます。

{{% /alert %}}
