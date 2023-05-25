---
title: 各ワークシートを別の PDF ファイルに保存
type: docs
weight: 50
url: /ja/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells は、スプレッドシート ファイル (画像、グラフなどが含まれる) から PDF ドキュメントへの変換をサポートしています。 Aspose.Cells for Java は独立して機能してスプレッドシートを PDF ドキュメントに変換できるため、変換に Aspose.PDF for Java を使用する必要はなくなりました。プロセス全体がメモリ内で実行できるため、変換には一時ファイルを作成/使用する必要もありません。

{{% /alert %}}

各ワークシートをテンプレート Excel ファイルに保存して、異なる PDF ファイルを生成する必要がある場合。これは簡単に達成できます。 1 つのシートのインデックスを次のように設定してみるとよいでしょう。**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**オプションを一度に PDF にレンダリングします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) メソッドを、スプレッドシートを PDF にレンダリングする直前に実行します。これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
