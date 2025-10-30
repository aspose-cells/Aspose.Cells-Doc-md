---
title: ワークシートに条件付き書式を適用（C++）
linktitle: 条件付き書式の適用
description: C++でAspose.Cellsライブラリを使用して、ワークシートに条件付き書式を適用する方法。これらの基準を調整することで、セルの外観と表示をより細かく制御できます。
keywords: Aspose.Cells、条件付き書式、C++、ワークシート、書式設定
type: docs
weight: 130
url: /ja/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

この記事では、ワークシートのセル範囲に条件付き書式設定を追加する方法について詳しく説明しています。

条件付き書式設定は、Microsoft Excelの高度な機能であり、セルの値や数式の値に応じて書式を適用し、その書式を変更することを可能にします。たとえば、セルの背景が赤くなるとマイナスの値が強調表示されたり、テキストの色が緑色になるとプラスの値が強調表示されます。セルの値が条件を満たしている場合、書式が適用されます。セルの値が条件を満たしていない場合、セルのデフォルトの書式が使用されます。

Microsoft Office Automationで条件付き書式設定を適用することは可能ですが、その欠点があります。たとえば、セキュリティ、安定性、拡張性、速度などの理由や問題が存在します。他のソリューションを探す主な理由は、Microsoft自体がソフトウェアソリューション向けにOffice Automationを強く推奨していないことです。

この記事では、Aspose.Cells APIを使用して、わずか数行のコードでセルに条件付き書式設定を追加するコンソールアプリケーションを作成する方法を示しています。

{{% /alert %}}

## **セルの値に基づいた条件付き書式を適用するためのAspose.Cellsの使用**

1. **Aspose.Cellsをダウンロードしてインストールします。**
   1. Aspose.Cells for C++をダウンロードします。
1. 開発コンピュータにインストールします。
   すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。
1. **プロジェクトを作成します**。
   C++の開発環境を開始し、新しいコンソールアプリケーションを作成します。
1. **参照を追加します。**
   プロジェクトにAspose.Cellsへの参照を追加します。たとえば、….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dllへの参照を追加します。
1. セルの値に基づいて条件付き書式を適用します**。
   次のコードは、タスクを達成するために使用されるものです。セルに条件付き書式を適用します。

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

上記のコードを実行すると、最初のワークシートのセル「A1」に条件付き書式が適用されます。A1に適用される条件付き書式はセルの値に依存します。A1の値が50から100の範囲内なら、条件付き書式により背景色が赤になります。

## **Aspose.Cellsを使用してセルの値に基づいた条件付き書式を適用する**

 1. 【数式に応じた条件付き書式の適用（コードスニペット）】
   以下はそのタスクを達成するためのコードです。B3に条件付き書式を適用します。

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

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

上記のコードを実行すると、最初のワークシートのセル「B3」に条件付き書式が適用されます。適用される条件付き書式は、「B3」の値をB1とB2の合計として計算する式に依存します。
{{< app/cells/assistant language="cpp" >}}
