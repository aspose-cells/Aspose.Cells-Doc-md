---
title: ワークブックの印刷とプレビュー
linktitle: 印刷とプレビュー
type: docs
weight: 70
url: /ja/python-net/workbook-and-worksheet-print-preview/
description: Aspose.Cells for Python via .NET は、Microsoft ExcelのインストールなしでExcelファイルの印刷やプレビューをサポートします。
---

{{% alert color="primary" %}}

ワークシートを作成した後、しばしばそのハードコピーを印刷したくなります。この記事では、Aspose.Cells for Python via .NETを使ったスプレッドシートの印刷方法について説明します。

{{% /alert %}}

## **印刷の概要**

Microsoft Excelは、選択範囲を指定しなければワークシート全体を印刷することを想定しています。Aspose.Cells for Python via .NET を使って印刷するには、最初にプログラムに `aspose.cells.rendering` 名前空間をインポートします。そこにはいくつかの便利なクラスがあります、例えば `[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)` と `[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)`。

### **SheetRenderを使用して印刷**

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) クラスはワークシートを表し、[**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/) メソッドはワークシートを印刷することができます。次のサンプルコードは、ワークシートを印刷する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **WorkbookRenderを使用して印刷**

ワークブック全体を印刷するには、シートをイテレートして印刷するか、[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)を使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET は、`[**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str)` と `[**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings)` のオーバーロードも提供しており、エクセルスプシートの印刷ジョブ名を設定することができます。デフォルトでは、すべての印刷ジョブの名前は「Document」となります。

{{% /alert %}}

## **印刷プレビュー**

数百万ページのExcelファイルをPDFまたは画像に変換する必要がある場合があります。このようなファイルを処理すると、多くの時間とリソースが消費されます。そのような場合に、ワークブックおよびワークシートの印刷プレビュー機能が役立つ可能性があります。ファイルを変換する前に、ユーザーは総ページ数を確認し、ファイルを変換するかどうかを決定できます。この記事では、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) クラスを使用して、生成されたプレビューの総ページ数を調べる方法に焦点を当てています。

Aspose.Cells for Python via .NET は、印刷プレビュー機能も提供します。これには `[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)` と `[**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)` のクラスが含まれます。全ワークブックの印刷プレビューを作成するには、 `[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)` クラスのインスタンスを作成し、 `[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)` と `[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)` のオブジェクトを渡してコンストラクタを呼び出します。`[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)` クラスは、生成されたプレビューのページ数を返す `[**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/)` メソッドを提供します。 `[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)` クラスと類似した `[**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)` クラスは、特定のワークシートの印刷プレビューを生成するために使用されます。ワークシートの印刷プレビューを作るには、 `[**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)` クラスのインスタンスを作成し、 `[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)` と `[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)` のオブジェクトを渡します。 `[**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)` クラスもまた、生成されたプレビューのページ数を返す `[**SheetPrintingPreview.evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview/evaluated_page_count/)` メソッドを提供します。

次のコードスニペットは、[サンプルExcelファイル](94896177.xlsx)を使用して、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)クラスの両方の使用方法を示しています。

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

上記のコードを実行した結果生成された出力は次のとおりです。

### **コンソール出力**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

