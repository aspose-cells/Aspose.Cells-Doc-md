---
title: C++を使用した塗りつぶし設定
linktitle: 塗りつぶし設定
description: Aspose.Cellsは、スプレッドシートファイルを操作するC++ライブラリです。セルの塗りつぶし設定をサポートし、背景やスタイルをカスタマイズできます。この記事では、Aspose.Cellsライブラリを使用してセルの塗りつぶし設定を行う方法を紹介します。
keywords: Aspose.Cells、Cells、塗りつぶし設定、背景、スタイル
type: docs
weight: 50
url: /ja/cpp/cells-fill-settings/
---

## **色と背景パターン**

Microsoft Excel では、セルの前景（輪郭）と背景（塗りつぶし）の色、および背景パターンを設定できます。

Aspose.Cells もこれらの機能を柔軟にサポートしています。このトピックでは、Aspose.Cells を使用してこれらの機能を使用する方法について学びます。

### **色と背景パターンの設定**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション内の各項目は[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスのオブジェクトを表します。

[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) には [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) および [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) メソッドがあり、セルの書式設定を取得および設定するために使用されます。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) クラスには、セルの前景色と背景色を設定するためのプロパティがあります。 Aspose.Cells には、以下で示される一連の事前定義された背景パターンのタイプが含まれる [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) 列挙型があります。

|**背景パターン**|**説明**|
| :- | :- |
|DiagonalCrosshatch| 対角線のかすかな格子状のパターンを表します|
|DiagonalStripe| 対角線のストライプパターンを表します|
|Gray6| 6.25% グレーのパターンを表します|
|Gray12| 12.5% グレーのパターンを表します|
|Gray25| 25% グレーのパターンを表します|
|Gray50| 50% グレーのパターンを表します|
|Gray75| 75% グレーのパターンを表します|
|HorizontalStripe|水平ストライプパターンを表します|
|None|背景なしを表します|
|ReverseDiagonalStripe|反対角ストライプパターンを表します|
|Solid|ソリッドパターンを表します|
|ThickDiagonalCrosshatch|太い斜めクロスハッチパターンを表します|
|ThinDiagonalCrosshatch|細い斜めクロスハッチパターンを表します|
|ThinDiagonalStripe|細い斜めストライプパターンを表します|
|ThinHorizontalCrosshatch|細い水平クロスハッチパターンを表します|
|ThinHorizontalStripe|細い水平ストライプパターンを表します|
|ThinReverseDiagonalStripe|細い逆斜めストライプパターンを表します|
|ThinVerticalStripe|細い垂直ストライプパターンを表します|
|VerticalStripe|垂直ストライプパターンを表します|

以下の例では、A1セルの前景色が設定されていますが、A2は前景色と背景色の両方を垂直ストライプの背景パターンで構成するように設定されています。

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **重要なこと**

{{% alert color="primary" %}}

- セルの前景色または背景色を設定するには、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) オブジェクトの [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) または [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) プロパティを使用します。どちらのプロパティも、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) オブジェクトの [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) プロパティが構成されている場合のみ効果があります。
- [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) プロパティはセルのシェード色を設定します。
  [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) プロパティは、前景色または背景色に使用される背景パターンの種類を指定します。Aspose.Cells は、一連の事前定義された背景パターンの種類を含む [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) 列挙体を提供します。
- [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) 列挙体から *BackgroundType.None* 値を選択すると、前景色は適用されません。
  同様に、*BackgroundType.None* または *BackgroundType.Solid* 値を選択すると、背景色は適用されません。
- セルのシェード／塗りつぶし色を取得する場合、[**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) が *BackgroundType.None* であれば、[**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) は *Color.Empty* を返します。

{{% /alert %}}

### **グラデーション塗りつぶし効果の適用**

セルに希望のグラデーション塗りつぶし効果を適用するには、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) オブジェクトの [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) メソッドを使用してください。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **色とパレット**

パレットとは、画像を作成するために使用可能な色の数です。プレゼンテーションで標準化されたパレットを使用することで、ユーザーは一貫した外観を作成できます。各 Microsoft Excel (97-2003) ファイルには、セル、フォント、グリッド線、グラフィックオブジェクト、塗りつぶし、およびグラフの線に適用できる 56 色のパレットがあります。

Aspose.Cells を使用すると、パレットの既存の色だけでなく、カスタム色も使用できます。カスタム色を使用する前に、まずパレットに色を追加します。

このトピックでは、パレットにカスタム色を追加する方法について説明します。

### **パレットにカスタム色を追加**

Aspose.Cells は Microsoft Excel の 56 色のパレットをサポートしています。パレットに定義されていないカスタム色を使用するには、その色をパレットに追加します。

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスには、パレットを変更するための [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) メソッドがあり、カスタム色を追加するために次のパラメータを取ります:

- カスタムカラー、追加するカスタムカラー。
カスタムカラーが置き換えるパレット内の色のインデックスです。0〜55の間である必要があります。

以下の例では、カスタムカラー（Orchid）をパレットに追加し、フォントに適用する前に追加します。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

パレットには56色しか保持できません。パレットにカスタムカラーを追加すると、パレットが変更され、前の色でフォーマットされたファイル内の要素が変更されます。したがって、パレットを変更する際は非常に注意してください。さらに、これはXLS（Excel 97-2003）ファイル形式の制限のみであり、XLSXまたはその他の高度なMS Excel（2007/2010または2013）ファイル形式ではこのような制限はありません。

{{% /alert %}}
