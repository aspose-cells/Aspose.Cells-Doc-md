---
title: 各ワークシートを別の PDF ファイルに保存
type: docs
weight: 130
url: /ja/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

Aspose.Cells は、XLS ファイル (画像、グラフなどが含まれる) から PDF ドキュメントへの変換をサポートしています。 Aspose.Cells for .NET は独立して機能してスプレッドシートを PDF に変換できます。変換に Aspose.PDF for .NET を使用する必要はありません。変換はプロセス全体がメモリ内で実行できるため、ソフトウェアで一時ファイルを作成したり使用したりする必要はありません。

{{% /alert %}} 
##  **各ワークシートを別の PDF ファイルに保存**
各ワークシートをテンプレート Excel ファイルに保存して、異なる PDF ファイルを生成する必要がある場合は、これを簡単に実行できます。 1 つのシートのインデックスを次のように設定してみるとよいでしょう。**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**オプションを一度に PDF にレンダリングします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)スプレッドシートを PDF 形式にレンダリングする直前。そうすることで、式に依存する値が再計算され、PDF に正しい値が表示されるようになります。

{{% /alert %}}
