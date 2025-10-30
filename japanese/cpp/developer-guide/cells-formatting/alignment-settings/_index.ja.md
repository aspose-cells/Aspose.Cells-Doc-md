---
title: C++による配置設定
linktitle: 配置設定
description: Aspose.Cellsライブラリでは、セルの配置設定を使用してテキストのレイアウトと表示を調整できます。水平配置、垂直配置、テキストの折り返しなどの設定を調整することで、セル内のテキストの流れをより細かく制御できます。このドキュメントでは、Aspose.Cellsを使用したセルの配置設定の詳細な手順とサンプルコードを提供し、すばやく理解するのに役立ちます。
keywords: Aspose.Cells、セルの配置、水平配置、垂直配置、テキストの折り返し
type: docs
weight: 20
url: /ja/cpp/cells-alignment-settings/
---

## **配置設定の構成**

### **Microsoft Excelの配置設定**

セルの書式設定にMicrosoft Excelを使用したことがある人であれば、Microsoft Excelの配置設定に精通しているでしょう。

上記の図から分かるように、異なる種類の配置オプションがあります:

- テキストの配置（水平および垂直）
- インデント
- 方向
- テキスト コントロール。
- テキスト方向。

これらの配置設定は、Aspose.Cellsで完全にサポートされており、以下で詳しく説明します。

### **Aspose.Cellsの配置設定**

Aspose.Cellsは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)を提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスは[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) コレクションを提供します。[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) クラスのオブジェクトを表します。

Aspose.Cellsは、[**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) および[**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) メソッドを提供しています。これらは[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) クラスで使用され、セルの書式設定を取得および設定します。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) クラスには、配置設定を構成するための便利なプロパティが提供されています。

[**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) 列挙型を使用して任意のテキスト配置タイプを選択します。[**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) 列挙型の事前定義されたテキスト配置タイプは次のとおりです:

|**テキスト配置タイプ**|**説明**|
| :- | :- |
|Bottom| 下部のテキスト配置を表します。
|Center| 中央のテキスト配置を表します。
|CenterAcross| 横方向に中央揃えのテキスト配置を表します。
|Distributed| 分散テキスト配置を表します。
|Fill| 塗りつぶしのテキスト配置を表します。
|General| 一般的なテキスト配置を表します。
|Justify| 両端揃えのテキスト配置を表します。
|Left| 左揃えのテキスト配置を表します。
|Right| 右揃えのテキスト配置を表します。
|Top| 上部のテキスト配置を表します。
|JustifiedLow| アラビア語のテキストに対して調整されたカシダ長でテキストを配置します。
|ThaiDistributed| 特にタイ語のテキストを分散配置し、各文字を単語として扱います。

{{% alert color="primary" %}}

また、[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/) プロパティを使用して両端揃え分散設定を適用できます。

{{% /alert %}}

#### **水平配置**

[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) オブジェクトの[**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/) プロパティを使用してテキストを水平に配置します。

```cpp
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

    // Create workbook
    Workbook workbook;

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **垂直配置**

水平配置と同様に、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) オブジェクトの[**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) プロパティを使用してテキストを垂直に配置します。

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

    // Create workbook
    Workbook workbook;

    // Clearing all the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Setting the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment of the text in a cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **インデント**

セル内のテキストのインデントレベルを[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) オブジェクトの[**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) プロパティで設定することができます。

```cpp
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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the indentation level
    style.SetIndentLevel(2);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **方向**

セル内のテキストの方向（回転）を[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) オブジェクトの[**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) プロパティで設定します。

```cpp
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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the rotation angle of the text to 25 degrees
    style.SetRotationAngle(25);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook in Excel 97-2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **テキストコントロール**

次のセクションでは、テキストの折り返し、収縮に合わせるなど、テキストの制御方法について説明します。

##### **テキストの折り返し**

セル内のテキストを折り返すと、テキストが切れたり隣接するセルに流れ出ないようになり、読みやすくなります。テキストの折り返しは、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)の[**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/)プロパティを使用してオンまたはオフに設定できます。

```cpp
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

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 36);

    // Add Text to the First Cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **収縮に合わせる**

フィールド内のテキストを折り返すオプションは、セルのサイズに合わせてテキストサイズを収縮することもできます。これは、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)の[**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/)プロパティを**true**に設定することで行います。

```cpp
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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set shrink to fit
    style.SetShrinkToFit(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **セルの結合**

Aspose.Cellsは、Microsoft Excelのように複数のセルを1つに結合する機能をサポートしています。Aspose.Cellsには、このタスクを行うための2つの方法が提供されています。1つ目は、[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)の[**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/)メソッドを呼び出す方法です。[**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/)メソッドは、次のパラメータを取り、セルを結合します:

- 最初の行: 結合の開始行。
- 最初の列: 結合の開始列。
- 行数: 結合する行数。
- 列数: 結合する列数。

```cpp
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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

もう1つの方法は、まず[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)の[**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)メソッドを呼び出して結合するセルの範囲を作成する方法です。[**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)メソッドは、前述の[**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/)メソッドと同じパラメータを取り、[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)オブジェクトを返します。[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)オブジェクトには、[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)オブジェクトで指定された範囲を結合する[**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/)メソッドも用意されています。

##### **テキストの方向**

セル内のテキストの読み取り順を設定することが可能です。読み取り順は、文字や単語などが表示される視覚的な順序です。たとえば、英語は左から右への言語であり、アラビア語は右から左への言語です。

読み取り順は、[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)の[**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/)プロパティを使用して設定されます。Aspose.Cellsは、[**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/)列挙型で事前定義されたテキストの方向タイプを提供しています。

|**テキスト方向の種類**|**説明**|
| :- | :- |
|Context|最初に入力された文字の言語と一貫した読み取り順|
|LeftToRight|左から右の読み取り順|
|RightToLeft|右から左の読み取り順|

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"I am using the latest version of Aspose.Cells to test this functionality.");

    // Get the style of cell A1
    Style style = cell.GetStyle();

    // Set text direction to left-to-right
    style.SetTextDirection(TextDirectionType::LeftToRight);

    // Apply the modified style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"book1.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **高度なトピック**
- [セルの配置を変更し、既存の書式を保持する](/cells/ja/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [改行とテキストの折り返し](/cells/ja/cpp/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="cpp" >}}
