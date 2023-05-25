---
title: 指定したワークシートを PDF に保存
type: docs
weight: 51
url: /ja/java/save-specified-worksheets-to-pdf/
---
デフォルトでは、Aspose.Cells すべて保存**見える**ワークブック内のワークシートを PDF ファイルに変換します。と**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**オプションを使用すると、指定したワークシートを PDF ファイルに保存できます。たとえば、アクティブなワークシートを PDF に保存したり、すべてのワークシート (表示されているワークシートと非表示のワークシートの両方) を PDF に保存したり、カスタムの複数のワークシートを PDF に保存したりできます。

##  **アクティブなワークシートを PDF に保存**

アクティブシートのみを PDF にエクスポートしたい場合は、次のように渡すことでこれを実現できます。**[`SheetSet.Active`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)**に**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**オプション。

シート `Sheet2` は、ソース ファイルのアクティブなシートです。[シートセットの例.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

##  **すべてのワークシートを PDF に保存**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)**ワークブック内で表示されているシートを示します。**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)**は、ワークブック内の表示シートと非表示/非表示シートの両方を含むすべてのシートを示します。すべてのシートを PDF にエクスポートしたい場合は、次のように渡すだけです。**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)**に**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**オプション。

ソースファイル[シートセットの例.xlsx](sheetset-example.xlsx)非表示シート `Sheet3` を含む 4 つのシートすべてが含まれています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

##  **指定したワークシートを PDF に保存**
必要な/カスタムの複数のシートを PDF にエクスポートしたい場合は、複数のシート インデックスを**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)**オプション。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、スプレッドシートを PDF 形式にレンダリングする直前に [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) を呼び出すことをお勧めします。そうすることで、式に依存する値が確実に再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
