---
title: 指定されたワークシートをPDFに保存する
type: docs
weight: 140
url: /ja/net/save-specified-worksheets-to-pdf/
---

デフォルトでは、Aspose.Cellsはブック内の**表示されている**すべてのワークシートをpdfファイルに保存します。[**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) オプションを使用すると、特定のワークシートをpdfファイルに保存できます。例えば、アクティブなワークシートをpdfに保存する、すべてのワークシート（表示されているワークシートと非表示のワークシートの両方）をpdfに保存する、複数のカスタムワークシートをpdfに保存することができます。

## **アクティブワークシートをPDFに保存する**

アクティブなシートのみをPDFにエクスポートする場合は、[**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)を[**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)オプションに渡すことでこれを実現できます。

シート `Sheet2` はソースファイル [sheetset-example.xlsx](sheetset-example.xlsx) のアクティブなシートです。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **すべてのワークシートをPDFに保存**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/) はワークブック内で表示されるシートを示し、[**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) はワークブック内のすべてのシート（表示されているシートと非表示/不可視のシートの両方）を示します。すべてのシートをPDFにエクスポートしたい場合は、[**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) オプションに単に [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) を渡すことができます。

ソースファイル [sheetset-example.xlsx](sheetset-example.xlsx) には、非表示シート `Sheet3` を含むすべての4つのシートが含まれています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **指定されたワークシートをPDFに保存**
希望の/カスタム複数のシートをPDFにエクスポートしたい場合は、複数のシートの索引を [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) オプションに渡すことでこれを実現できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## **ワークシートを並べ替えてPDFに変換**

ソースファイルを変更せずにシートの順序（逆順など）を並び替えてPDFにしたい場合、[**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)オプションに並び替えたシートのインデックスを渡すことで実現できます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
