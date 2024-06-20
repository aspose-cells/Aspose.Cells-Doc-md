---
title: 指定されたワークシートをPDFに保存する
type: docs
weight: 51
url: /ja/java/save-specified-worksheets-to-pdf/
---

デフォルトでは、Aspose.Cellsはブック内の**表示されている**すべてのワークシートをpdfファイルに保存します。[**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) オプションを使用すると、特定のワークシートをpdfファイルに保存できます。例えば、アクティブなワークシートをpdfに保存する、すべてのワークシート（表示されているワークシートと非表示のワークシートの両方）をpdfに保存する、複数のカスタムワークシートをpdfに保存することができます。

## **アクティブワークシートをPDFに保存する**

アクティブなシートのみをPDFにエクスポートする場合は、[**SheetSet.Active**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)を[**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)オプションに渡すことでこれを実現できます。

シート `Sheet2` はソースファイル [sheetset-example.xlsx](sheetset-example.xlsx) のアクティブなシートです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

## **すべてのワークシートをPDFに保存**

[**SheetSet.Visible**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--) はワークブック内で表示されるシートを示し、[**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) はワークブック内のすべてのシート（表示されているシートと非表示/不可視のシートの両方）を示します。すべてのシートをPDFにエクスポートしたい場合は、[**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) オプションに単に [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) を渡すことができます。

ソースファイル [sheetset-example.xlsx](sheetset-example.xlsx) には、非表示シート `Sheet3` を含むすべての4つのシートが含まれています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

## **指定されたワークシートをPDFに保存**
希望の/カスタム複数のシートをPDFにエクスポートしたい場合は、複数のシートの索引を [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) オプションに渡すことでこれを実現できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
