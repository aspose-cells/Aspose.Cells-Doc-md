---
title: C++で条件付き書式とともに交互の行と列にシェーディングを適用する
linktitle: 交互の行と列にシェーディングを適用する
description: C++でAspose.Cellsライブラリを使用して、交互の行と列に条件付き書式のシャドウを適用する方法。これらの基準を調整することで、セルの見た目や外観をよりコントロールできます。
keywords: Aspose.Cells、条件付き書式、C++、交互の行、交互の列、シャドウ
type: docs
weight: 30
url: /ja/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells APIは、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)オブジェクトの条件付き書式ルールの追加と操作手段を提供します。これらのルールは、条件やルールに基づいて望ましい書式を得るためにさまざまな方法で調整できます。この記事では、Aspose.Cells for C++ APIを使用して条件付き書式ルールとExcelのビルトイン関数を使用して交互の行と列にシェーディングを適用する方法を示します。

{{% /alert %}}

この記事では、Excelの組み込み関数であるROW、COLUMN、MODなどの詳細について説明します。これらの関数の詳細な内容を提供し、コードスニペットの理解を深めます。

- **ROW()** 関数は、セル参照の行番号を返します。参照パラメータが省略された場合、ROW関数が入力されたセルのセルアドレスを参照するものとします。
- **COLUMN()** 関数は、セル参照の列番号を返します。参照パラメータが省略された場合、COLUMN関数が入力されたセルのセルアドレスを参照するものとします。
- **MOD()** 関数は、数値が除算された後の余りを返します。関数の最初のパラメーターは、余りを求めたい数値で、2番目のパラメーターは、数値パラメーターで除算する数です。除数が0の場合、#DIV/0!エラーが返されます。

この目標を達成するためにAspose.Cells for C++ APIを使用してコードを書き始めましょう。

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

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

次のスナップショットは、Excelアプリケーションで読み込まれた結果のスプレッドシートを示しています。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

交互の列に網掛けを適用するためには、単に式を **=MOD(ROW(),2)=0** から **=MOD(COLUMN(),2)=0** に変更するだけで済みます。つまり、行索引を取得する代わりに、式を変更して列索引を取得します。 
この場合の結果のスプレッドシートは以下のようになります。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
