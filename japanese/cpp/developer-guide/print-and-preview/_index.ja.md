---
title: C++でのワークブックの印刷とプレビュー
linktitle: 印刷とプレビュー
type: docs
weight: 70
url: /ja/cpp/workbook-and-worksheet-print-preview/
description: Aspose.CellsはMicrosoft Excelのインストール不要で、C++を使用してExcelファイルの印刷とプレビューをサポートしています。
---

{{% alert color="primary" %}}

ワークシートを作成した後、通常はそれを印刷したいと思うことがあります。この記事ではAspose.Cellsを使用してスプレッドシートを印刷する方法について説明しています。

{{% /alert %}}

## **印刷の概要**

Microsoft Excelは、選択を指定しない限り、ワークシート全体を印刷すると仮定しています。Aspose.Cellsを使用して印刷するには、まずAspose.Cells.Rendering名前空間をプログラムにインポートします。これにはいくつかの有用なクラスがあり、たとえば、[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)と[**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)があります。


## **印刷プレビュー**

数百万ページのExcelファイルをPDFまたは画像に変換する必要がある場合があります。このようなファイルを処理すると、多くの時間とリソースが消費されます。そのような場合に、ワークブックおよびワークシートの印刷プレビュー機能が役立つ可能性があります。ファイルを変換する前に、ユーザーは総ページ数を確認し、ファイルを変換するかどうかを決定できます。この記事では、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) クラスを使用して、生成されたプレビューの総ページ数を調べる方法に焦点を当てています。

Aspose.Cellsは印刷プレビュー機能を提供しています。APIは[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)および[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)クラスを提供しています。ワークブック全体の印刷プレビューを作成するには、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)オブジェクトをコンストラクタに渡して[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)クラスのインスタンスを作成します。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)クラスは、生成されたプレビューのページ数を返す[**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/)メソッドを提供します。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)クラスに類似して、[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)クラスは特定のワークシートの印刷プレビューを生成するために使用されます。ワークシートの印刷プレビューを作成するには、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)オブジェクトをコンストラクタに渡して[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)クラスのインスタンスを作成します。[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)クラスもまた、生成されたプレビューのページ数を返す[**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/)メソッドを提供します。

次のコードスニペットは、[サンプルExcelファイル](94896177.xlsx)を使用して、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)クラスの両方の使用方法を示しています。

### **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

上記のコードを実行した結果生成された出力は次のとおりです。

### **コンソール出力**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **高度なトピック**
- [スプレッドシートのレンダリング用フォントの設定](/cells/ja/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [ワークシートをイメージに変換 - データ周りの空白を削除](/cells/ja/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [ワークシートを画像に変換し、ページごとに画像をワークシートに変換する](/cells/ja/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [ImageOrPrintオプションを使用してワークシートを画像に変換](/cells/ja/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [ワークシートのセルの範囲をイメージにエクスポート](/cells/ja/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [希望の幅と高さでワークシートまたはチャートを画像にエクスポート](/cells/ja/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ImageOrPrintOptionsを使用してワークシートから画像を抽出](/cells/ja/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [ワークシートのサムネイルを生成](/cells/ja/cpp/generate-thumbnail-of-the-worksheet/)
- [印刷するものがない場合、空白ページを出力](/cells/ja/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [ページ設定および印刷オプション](/cells/ja/cpp/page-setup-and-printing-options/)
- [ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用したページのシーケンスをレンダリングする](/cells/ja/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [ワークシートをグラフィックコンテキストにレンダリング](/cells/ja/cpp/render-worksheet-to-graphic-context/)
- [ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する](/cells/ja/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
