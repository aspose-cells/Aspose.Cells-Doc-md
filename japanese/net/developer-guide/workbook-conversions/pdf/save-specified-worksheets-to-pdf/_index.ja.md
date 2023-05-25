---
title: 指定したワークシートを PDF に保存
type: docs
weight: 140
url: /ja/net/save-specified-worksheets-to-pdf/
---
デフォルトでは、Aspose.Cells すべて保存**見える**ワークブック内のワークシートを PDF ファイルに変換します。と**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**オプションを使用すると、指定したワークシートを PDF ファイルに保存できます。たとえば、アクティブなワークシートを PDF に保存したり、すべてのワークシート (表示されているワークシートと非表示のワークシートの両方) を PDF に保存したり、カスタムの複数のワークシートを PDF に保存したりできます。

##  **アクティブなワークシートを PDF に保存**

アクティブシートのみを PDF にエクスポートしたい場合は、次のように渡すことでこれを実現できます。**[`SheetSet.Active`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)**に**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**オプション。

シート `Sheet2` は、ソース ファイルのアクティブなシートです。[シートセットの例.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

##  **すべてのワークシートを PDF に保存**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/)**ワークブック内で表示されているシートを示します。**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)**は、ワークブック内の表示シートと非表示/非表示シートの両方を含むすべてのシートを示します。すべてのシートを PDF にエクスポートしたい場合は、次のように渡すだけです。**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)**に**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**オプション。

ソースファイル[シートセットの例.xlsx](sheetset-example.xlsx)非表示シート `Sheet3` を含む 4 つのシートすべてが含まれています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

##  **指定したワークシートを PDF に保存**
必要な/カスタムの複数のシートを PDF にエクスポートしたい場合は、複数のシート インデックスを**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)**オプション。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、スプレッドシートを PDF 形式にレンダリングする直前に [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) を呼び出すことをお勧めします。そうすることで、式に依存する値が確実に再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
