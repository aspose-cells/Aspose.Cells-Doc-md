---
title: 指定したワークシートを PDF に保存
type: docs
weight: 140
url: /ja/python-net/save-specified-worksheets-to-pdf/
description: Aspose.Cells for Python via .NET API を使用して、指定したワークシートを PDF に保存する方法を学習します。
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
デフォルトでは、Aspose.Cells for Python via .NET すべて保存**見える**ワークブック内のワークシートを PDF ファイルに変換します。と**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)**オプションを使用すると、指定したワークシートを PDF ファイルに保存できます。たとえば、アクティブなワークシートを PDF に保存したり、すべてのワークシート (表示されているワークシートと非表示のワークシートの両方) を PDF に保存したり、カスタムの複数のワークシートを PDF に保存したりできます。

##  **アクティブなワークシートを PDF に保存**

アクティブシートのみを PDF にエクスポートしたい場合は、次のように渡すことでこれを実現できます。**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)**に**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)**オプション。

シート `Sheet2` は、ソース ファイルのアクティブなシートです。[シートセットの例.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **すべてのワークシートを PDF に保存**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)**ワークブック内で表示されているシートを示します。**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)**は、ワークブック内の表示シートと非表示/非表示シートの両方を含むすべてのシートを示します。すべてのシートを PDF にエクスポートしたい場合は、次のように渡すだけです。**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)**に**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)**オプション。

ソースファイル[シートセットの例.xlsx](sheetset-example.xlsx)非表示シート `Sheet3` を含む 4 つのシートすべてが含まれています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **指定したワークシートを PDF に保存**
必要な/カスタムの複数のシートを PDF にエクスポートしたい場合は、複数のシート インデックスを**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)**オプション。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)スプレッドシートを PDF 形式にレンダリングする直前。そうすることで、式に依存する値が再計算され、PDF に正しい値が表示されるようになります。

{{% /alert %}}
