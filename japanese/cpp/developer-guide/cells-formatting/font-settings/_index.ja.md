---
title: フォント設定のC++による方法
linktitle: フォント設定
type: docs
weight: 30
url: /ja/cpp/cells-font-settings/
description: Aspose.Cellsは、スプレッドシートファイルを操作するC++ライブラリです。セルのフォント設定をサポートし、フォントのスタイルやプロパティをカスタマイズできます。この記事では、Aspose.Cellsライブラリを使用してセルのフォント設定を行う方法を示します。
keywords: Aspose.Cells、Cells、フォント設定、スタイル、プロパティ
---

{{% alert color="primary" %}}

テキストの見た目はフォント設定を変更することで制御できます。フォント設定には、フォント名、スタイル、サイズ、色、その他効果が含まれます。Microsoft Excelと同様に、Aspose.Cellsもセルのフォント設定をサポートしています。

{{% /alert %}}

## **フォント設定の構成**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスにはExcelファイル内の各ワークシートへのアクセスを許可する[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクションを提供します。[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)コレクション内の各アイテムは[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスのオブジェクトを表します。

Aspose.Cellsは、[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの[**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)および[**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)メソッドを提供しており、セルの書式設定スタイルの取得と設定に使用されます。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)クラスはフォント設定を構成するためのプロパティを提供します。

### **フォント名の設定**

開発者は、[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)オブジェクトの[GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/)プロパティを使用して任意のフォントをセル内のテキストに適用できます。

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font name to "Times New Roman"
    style.GetFont().SetName(u"Times New Roman");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **太字にフォントスタイルを設定する**

開発者は、[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)オブジェクトの[**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/)プロパティを**true**に設定することでテキストを太字にすることができます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    style.GetFont().SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **フォントサイズの設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)オブジェクトの[**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/)プロパティでフォントサイズを設定します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font size to 14
    style.GetFont().SetSize(14);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **フォントの色の設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)オブジェクトの[**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/)プロパティを使用してフォントの色を設定します。Color列挙体（C++フレームワークの一部）から任意の色を選択し、[**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/)プロパティに割り当ててください。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font color to blue
    style.GetFont().SetColor(Color::Blue());

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

### **フォントの下線タイプの設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)オブジェクトの[**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/)プロパティを使用してテキストに下線を付けます。Aspose.Cellsでは、[**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/)列挙型でさまざまな予め定義されたフォントの下線タイプを提供しています。

|**フォントの下線の種類**|**説明**|
| :- | :- |
|Accounting|単一のアカウンティング下線
|Double|ダブル下線
|DoubleAccounting|ダブルアカウンティング下線
|None|下線なし
|Single|単一の下線

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font to be underlined
    style.GetFont().SetUnderline(FontUnderlineType::Single);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **取り消し線の効果の設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)オブジェクトの[**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/)プロパティを**true**に設定することで取り消し線を適用します。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Hello Aspose!");

    Style style = cell.GetStyle();
    style.GetFont().SetIsStrikeout(true);
    cell.SetStyle(style);

    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **下付き文字の効果の設定**

[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)オブジェクトの[**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/)プロパティを**true**に設定することで下付き文字を適用します。

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set subscript effect
    style.GetFont().SetIsSubscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **フォントの上付き文字効果の設定**

開発者は、[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)オブジェクトの[**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/)プロパティを**true**に設定することで、フォントに上付き文字効果を適用できます。

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set superscript effect
    style.GetFont().SetIsSuperscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [フォントに上付き文字および下付き文字効果を適用する](/cells/ja/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [スプレッドシートまたはブックで使用されているフォントのリストを取得する](/cells/ja/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
