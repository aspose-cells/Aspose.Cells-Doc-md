---
title: 指定されたワークシートをPDFに保存する
type: docs
weight: 140
url: /ja/python-net/save-specified-worksheets-to-pdf/
description: Aspose.Cells for Python via .NET APIを使用して、指定されたワークシートをPDFに保存する方法を学習する
keywords: PythonでアクティブなワークシートをPDFに保存する方法、すべてのワークシートをPDFに保存する方法、指定されたワークシートをPDFに保存する方法
---

デフォルトでは、Aspose.Cells for Python via .NETではワークブック内のすべての**表示されている**ワークシートをPDFファイルに保存します。指定されたワークシートをPDFファイルに保存するためには、[**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)オプションを使用できます。たとえば、アクティブなワークシートをPDFに保存したり、すべてのワークシート（表示されているワークシートと非表示のワークシートの両方）をPDFに保存したり、カスタムの複数のワークシートをPDFに保存することができます。

## **アクティブワークシートをPDFに保存する**

アクティブなシートのみをPDFにエクスポートする場合は、[**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)を[**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)オプションに渡すことでこれを実現できます。

シート `Sheet2` はソースファイル [sheetset-example.xlsx](sheetset-example.xlsx) のアクティブなシートです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **すべてのワークシートをPDFに保存**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/) はワークブック内で表示されるシートを示し、[**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) はワークブック内のすべてのシート（表示されているシートと非表示/不可視のシートの両方）を示します。すべてのシートをPDFにエクスポートしたい場合は、[**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) オプションに単に [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) を渡すことができます。

ソースファイル [sheetset-example.xlsx](sheetset-example.xlsx) には、非表示シート `Sheet3` を含むすべての4つのシートが含まれています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **指定されたワークシートをPDFに保存**
希望の/カスタム複数のシートをPDFにエクスポートしたい場合は、複数のシートの索引を [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) オプションに渡すことでこれを実現できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
