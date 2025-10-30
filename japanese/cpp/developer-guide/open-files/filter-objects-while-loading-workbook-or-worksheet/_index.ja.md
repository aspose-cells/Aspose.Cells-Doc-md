---
title: C++を使用してワークブックやシートの読み込み時にオブジェクト（チャートや図形、条件付き書式など）をフィルタリングする方法
linktitle: ワークブックまたはワークシートをロードする際にオブジェクトをフィルタリングする
type: docs
weight: 330
url: /ja/cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aspose.Cells for C++を用いて、ワークブックやシートの読み込み時にチャートや図形、条件付き書式などのオブジェクトをフィルタリングする方法を学習します。
---

## **可能な使用シナリオ**
ワークブックからデータをフィルタリングしながら読み込む際は，[LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) プロパティを使用してください。ただし、各シート単位でフィルタリングしたい場合は [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/) メソッドをオーバーライドする必要があります。[LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)列挙から適切な値を指定して、[LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/)を作成または操作してください。

[LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)の可能な値は次の通りです。

- 全て
- ブック設定
- 空白セル
- ブールセル
- データセル
- エラーセル
- 数値セル
- 文字列セル
- 値セル
- Chart
- 条件付き書式
- データの検証
- 定義された名前
- ドキュメントのプロパティ
- 数式
- ハイパーリンク
- 結合エリア
- ピボットテーブル
- 設定
- 図形
- シートデータ
- シート設定
- 構造
- スタイル
- テーブル
- VBA
- XmlMap

## **ワークブックの読み込み中にオブジェクトをフィルタリングする**
以下のサンプルコードは、ワークブックからグラフをフィルタリングする方法を示しています。このコードで使用されている[サンプルエクセルファイル](5115258.xlsx)とその生成された[出力PDF](5115257.pdf)を確認してください。出力PDFでは、すべてのグラフがワークブックからフィルタリングされていることが分かります。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter charts from the workbook
    LoadOptions lOptions;
    lOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Load the workbook with the above filter
    U16String inputFilePath = srcDir + u"sampleFilterCharts.xlsx";
    Workbook workbook(inputFilePath, lOptions);

    // Save worksheet to a single PDF page
    PdfSaveOptions pOptions;
    pOptions.SetOnePagePerSheet(true);

    // Save the workbook in PDF format
    U16String outputFilePath = outDir + u"sampleFilterCharts.pdf";
    workbook.Save(outputFilePath, pOptions);

    std::cout << "Workbook saved successfully with filtered charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ワークシートの読み込み中にオブジェクトをフィルタリングする**
以下のサンプルコードは、[ソースエクセルファイル](5115255.xlsx)を読み込み、カスタムフィルタを使用してそのワークシートから以下のデータをフィルタリングする方法を説明しています。

- NoChartsという名前のワークシートからグラフをフィルタリングします。
- NoShapesという名前のワークシートから形状をフィルタリングします。
- NoConditionalFormattingという名前のワークシートから条件付き書式をフィルタリングします。

1つのカスタムフィルタで[ソースエクセルファイル](5115255.xlsx)を読み込むと、ワークシートを1つずつ画像化します。以下は参照用の出力画像です。最初の画像にはグラフがなく、2番目の画像には形状がなく、3番目の画像には条件付き書式がないことが分かります。

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    void StartSheet(Worksheet& sheet) override
    {
        U16String sheetName = sheet.GetName();

        if (sheetName == u"NoCharts")
        {
            // Load everything and filter charts
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Chart)));
        }

        if (sheetName == u"NoShapes")
        {
            // Load everything and filter shapes
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Drawing)));
        }

        if (sheetName == u"NoConditionalFormatting")
        {
            // Load everything and filter conditional formatting
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::ConditionalFormatting)));
        }
    }
};

// Add main function to serve as entry point
int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Cleanup();
    return 0;

}
```

ワークシート名に従ってCustomLoadFilterクラスを使用する方法

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    CustomLoadFilter() : LoadFilter(LoadDataFilterOptions::All) {}
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter worksheets using CustomLoadFilter class
    LoadOptions loadOpts;
    CustomLoadFilter customLoadFilter;
    loadOpts.SetLoadFilter(&customLoadFilter);

    // Load the workbook with filter defined in CustomLoadFilter class
    Workbook workbook(srcDir + u"sampleCustomFilteringPerWorksheet.xlsx", loadOpts);

    // Take the image of all worksheets one by one
    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        // Access worksheet at index i
        Worksheet worksheet = sheets.Get(i);

        // Create an instance of ImageOrPrintOptions
        // Render entire worksheet to image
        ImageOrPrintOptions imageOpts;
        imageOpts.SetOnePagePerSheet(true);
        imageOpts.SetImageType(Aspose::Cells::Drawing::ImageType::Png);

        // Convert worksheet to image
        SheetRender render(worksheet, imageOpts);
        render.ToImage(0, outDir + u"outputCustomFilteringPerWorksheet_" + worksheet.GetName() + u".png");
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
