---
title: C++でExcelおよびODSファイルの条件付き書式を設定
linktitle: 条件付き書式
type: docs
weight: 60
url: /ja/cpp/conditional-formatting/
description: C++でExcelおよびODSファイルに条件付き書式を適用する方法
keywords: 条件付き書式の適用 
---

## **紹介**

条件付き書式は、Microsoft Excel の高度な機能で、セルやセル範囲に書式を適用し、その値や数式に応じて書式を変更することができます。たとえば、セルの値が 500 より大きいときにのみ太字にすることができます。セルの値が条件を満たした場合、指定された書式が適用されます。セルの値が書式条件を満たさない場合は、セルのデフォルトの書式が使用されます。Microsoft Excel では、**書式**、**条件付き書式** を選択して、条件付き書式ダイアログを開きます。

Aspose.Cells はセルに条件付き書式を実行時に適用することをサポートしています。この記事ではその方法を説明します。また、Excel が色スケールの条件付き書式に使用する色の計算方法も説明します。

## **条件付き書式の適用**

Aspose.Cells はいくつかの方法で条件付き書式をサポートしています。

- デザイナー スプレッドシートを使用
- コピー メソッドを使用
- 実行時に条件付き書式を作成

### **デザイナー スプレッドシートを使用**

開発者は、Microsoft Excel で条件付き書式を含むデザイナー スプレッドシートを作成し、そのスプレッドシートを Aspose.Cells で開くことができます。 Aspose.Cells は、デザイナー スプレッドシートを読み込み、保持し、条件付き書式の設定を保持します。

### **コピー メソッドを使用**

Aspose.Cells は、ワークシート内のセルから別のセルへ条件付き書式設定をコピーすることができます。

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int totalRowCount = 0;

    // Iterate through all worksheets in the workbook
    for (int i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        Worksheet sourceSheet = workbook.GetWorksheets().Get(i);

        // Get the maximum display range of the source sheet
        Range sourceRange = sourceSheet.GetCells().GetMaxDisplayRange();

        // Create a destination range in the first worksheet
        Range destRange = worksheet.GetCells().CreateRange(
            sourceRange.GetFirstRow() + totalRowCount, 
            sourceRange.GetFirstColumn(),
            sourceRange.GetRowCount(), 
            sourceRange.GetColumnCount());

        // Copy data from source range to destination range
        destRange.Copy(sourceRange);

        // Update the total row count
        totalRowCount += sourceRange.GetRowCount();
    }

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **ランタイムで条件付き書式を適用**

Aspose.Cells では、条件付き書式をランタイムで追加および削除することができます。以下のコードサンプルでは、条件付き書式の設定方法を示しています。

1. ワークブックをインスタンス化してください。
1. 空の条件付き書式を追加してください。
1. 書式を適用する範囲を設定してください。
1. 書式の条件を定義してください。
1. ファイルを保存します。

この後に、フォント設定や罫線設定、パターン設定などの他の小さな例が続きます。

Microsoft Excel 2007 では、より高度な条件付き書式が追加され、それを Aspose.Cells もサポートしています。ここにある例では単純な書式設定を示していますが、Microsoft Excel 2007 の例ではより高度な条件付き書式の適用方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Instantiating a Workbook object
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range.
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;
    fcs.AddArea(ca);

    ca = CellArea();
    ca.StartRow = 1;
    ca.EndRow = 1;
    ca.StartColumn = 1;
    ca.EndColumn = 1;
    fcs.AddArea(ca);

    // Adds condition.
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"=A2", u"100");

    // Adds condition.
    int conditionIndex2 = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Sets the background color.
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **フォントの設定**

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

    // Set the font weight to bold
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

フォントスタイル、テキストの色、下線スタイル、取り消し線スタイルのみを変更できます。

{{% /alert %}}

### **境界線の設定**

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
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Set the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Add condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Set the background color
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Dashed);

    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetColor(Color{255, 255, 0, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

アウトライン境界線には細い線スタイルのみを使用できます。対角線は許可されていません。

{{% /alert %}}

### **パターンの設定**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetPattern(BackgroundType::ReverseDiagonalStripe);
    fc.GetStyle().SetForegroundColor(Color{255, 255, 0, 255});
    fc.GetStyle().SetBackgroundColor(Color{0, 255, 255, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **高度なトピック**
- [2色系規則と3色系規則の条件付き書式設定を追加する](/cells/ja/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [高度な条件付き書式の適用](/cells/ja/cpp/apply-advanced-conditional-formatting/)
- [ワークシートで条件付き書式設定を適用する](/cells/ja/cpp/apply-conditional-formatting-in-worksheets/)
- [条件付き書式設定を使用して、交互に行と列に影を付ける](/cells/ja/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [条件付き書式データバーイメージの生成](/cells/ja/cpp/generate-conditional-formatting-databars-images/)
- [条件付き書式で使用されるアイコンセット、データバー、またはカラースケールオブジェクトの取得](/cells/ja/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
