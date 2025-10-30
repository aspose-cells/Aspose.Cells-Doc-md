---
title: C++を使ったチャート内の図形
linktitle: チャート内の図形
description: Aspose.Cells for C++を使ってMicrosoft Excelでチャートのコントロールを追加しカスタマイズする方法を学びます。ガイドでは、チャート要素の操作、書式設定の調整、全体的な外観と使いやすさの向上を示します。
keywords: Aspose.Cells for C++、チャートコントロール、チャートのカスタマイズ、Microsoft Excel、チャート要素、書式設定。
type: docs
weight: 70
url: /ja/cpp/controls-in-charts/
---

{{% alert color="primary" %}}

時には、ラベル、テキストボックス、画像などの描画オブジェクトをチャートに挿入する必要があります。Aspose.Cellsはランタイムでチャートにコントロールを追加できます。

{{% /alert %}}

## **チャートにラベルコントロールを追加**

ラベルはスプレッドシートの内容に関するユーザーへの情報提供手段を提供します。
Aspose.Cellsを使用して、チャートにラベルを追加したり操作したりすることができます。

 [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) クラスは [**AddLabelInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabelinchart/) というメソッドを持ち、チャートにラベルコントロールを追加するために使用されます。以下は、そのメソッドに使用されるパラメータのリストです：

- **top** - ラベルの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - ラベルの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** - ラベルの高さ、チャートエリアの1/4000単位。
- **width** - ラベルの幅、チャートエリアの1/4000単位。

このメソッドは [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) オブジェクトを返します。[**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) クラスはチャート内のラベルを表し、重要なメンバーをいくつか持ちます:

- [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)（プロパティ） – ラベルのキャプション文字列を指定します。
- [**Fill**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getfill/) (プロパティ) - 塗りつぶしの色属性を指定します。

以下の例では、チャートにラベルを追加する方法が示されています。 この例では、チャートが含まれたデザイナーファイル（**exp_piechart.xls**）を使用します。 このファイルを使用してチャートにラベルを挿入します。 チャートにラベルを追加するための元のコードは以下の通りです。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Aspose::Cells::Charts::Chart chart = sheet.GetCharts().Get(0);

    // Add a new label to the chart
    Label label = chart.GetShapes().AddLabelInChart(100, 100, 350, 900);

    // Set the caption of the label
    label.SetText(u"A Label In Chart");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Label added to chart successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **チャートにテキストボックスコントロールを追加**

レポートの重要な情報をハイライト表示する一つの方法は、テキストボックスを使用することです。例として、会社名を強調したり、売上が最も高い地域を示すためにテキストを入力します。[**AddTextBoxInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addtextboxinchart/)というメソッドは、チャートにテキストボックスコントロールを追加するために使用されます。以下は、そのメソッドに使用されるパラメータリストです。

- **top** - テキストボックスの上部左隅からの垂直オフセット、チャートエリアの1/4000単位。
- **left** - テキストボックスの上部左隅からの水平オフセット、チャートエリアの1/4000単位。
- **height** – テキストボックスの高さ、チャートエリアの1/4000単位で指定します。
- **width** – テキストボックスの幅、チャートエリアの1/4000単位で指定します。

メソッドは[**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/)オブジェクトを返します。[**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/)クラスはチャート内のテキストボックスを表します。

下の例は、チャートにテキストボックスを追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートにテキストボックスを挿入してチャートタイトルを表示します。以下は、チャートにテキストボックスを追加するための元のコードです。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Aspose::Cells::Charts::Chart chart = sheet.GetCharts().Get(0);

    // Add a new textbox to the chart
    TextBox textbox0 = chart.GetShapes().AddTextBoxInChart(100, 1100, 350, 2550);

    // Fill the text
    textbox0.SetText(u"Sales By Region");

    // Set the font color
    textbox0.GetFont().SetColor(Color::Maroon());

    // Set the font to bold
    textbox0.GetFont().SetIsBold(true);

    // Set the font size
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic
    textbox0.GetFont().SetIsItalic(true);

    // Get the fill format of the textbox
    FillFormat fillformat = textbox0.GetFill();

    // Get the line format type of the textbox
    LineFormat lineformat = textbox0.GetLine();

    // Set the line weight
    lineformat.SetWeight(2);

    // Set the dash style to solid
    lineformat.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Textbox added to chart successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **チャートに画像を追加する**

Aspose.Cellsを使用すると、チャートに画像を挿入することができます。たとえば、チャートやその内容を強調したり、意味を追加するために画像を追加したり、ブランドのイメージファイルを挿入することができます。

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)クラスは[**AddPictureInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpictureinchart/)というメソッドを提供し、これを使ってチャートに画像オブジェクトを追加します。以下は、そのメソッドに使用されるパラメータリストです。

- **top** – 画像の上部左隅からの垂直オフセット、チャートエリアの1/4000単位で指定します。
- **left** – 画像の上部左隅からの水平オフセット、チャートエリアの1/4000単位で指定します。
- **stream** – 画像データを含むストリームオブジェクト。
- **widthScale** – 画像幅のスケール、パーセンテージ値。
- **heightScale** – 画像の高さのスケール、パーセンテージ値。

メソッドは[**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)オブジェクトを返します。[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)クラスはチャート内の画像オブジェクトを表します。

下の例は、チャートに画像を追加する方法を示しています。この例では、以前のデザイナーファイル（**exp_piechart.xls**）を使用し、その中にチャートが含まれています。このファイルを使用してチャートに画像を挿入します。以下は、チャートに画像を追加するための元のコードです。

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

std::vector<uint8_t> ReadFileData(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<uint8_t> buffer(size);
    if (!file.read(reinterpret_cast<char*>(buffer.data()), size)) {
        throw std::runtime_error("Error reading file");
    }
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"chart.xls");
    std::vector<uint8_t> imageData = ReadFileData(srcDir + u"logo.jpg");

    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Chart chart = sheet.GetCharts().Get(0);
    Vector<uint8_t> data(imageData.data(), static_cast<int32_t>(imageData.size()));
    Picture pic0 = chart.GetShapes().AddPictureInChart(50, 50, data, 40, 40);
    LineFormat lineFormat = pic0.GetLine();

    lineFormat.SetDashStyle(MsoLineDashStyle::Solid);
    lineFormat.SetWeight(4);

    workbook.Save(outDir + u"chart.out.xls");
    std::cout << "Chart modified successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **チャートにチェックボックスを追加する**

Aspose.Cellsを使用すると、[**MsoDrawingType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msodrawingtype/)列挙型を使用して、チャートシートにチェックボックスを挿入することができます。以下の例では、チャートシートにチェックボックスを追加する方法を示しています。

次の画像は、出力ファイルに含まれるチャートシートにチェックボックスが表示されています。

![todo:image_alt_text](controls-in-charts_1.jpg)

次のコードスニペットによって生成された[出力ファイル](101089316.xlsx)が添付されています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a chart sheet to the workbook
    int32_t index = workbook.GetWorksheets().Add(SheetType::Chart);

    // Get the newly added chart sheet
    Worksheet sheet = workbook.GetWorksheets().Get(index);

    // Add a floating chart to the sheet
    sheet.GetCharts().AddFloatingChart(ChartType::Column, 0, 0, 1024, 960);

    // Add data series to the chart
    sheet.GetCharts().Get(0).GetNSeries().Add(U16String(u"{1,2,3}"), false);

    // Add a checkbox to the chart
    sheet.GetCharts().Get(0).GetShapes().AddShapeInChart(MsoDrawingType::CheckBox, PlacementType::Move, 400, 400, 1000, 600);

    // Set text for the checkbox
    sheet.GetCharts().Get(0).GetShapes().Get(0).SetText(U16String(u"CheckBox 1"));

    // Save the workbook
    workbook.Save(outDir + u"InsertCheckboxInChartSheet_out.xlsx");

    std::cout << "Checkbox added to chart sheet successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [ワードアートウォーターマークをグラフに追加する](/cells/ja/cpp/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="cpp" >}}
