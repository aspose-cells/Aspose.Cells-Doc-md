---
title: データフィルタリング（C++）
linktitle: データフィルタリング
type: docs
weight: 85
url: /ja/cpp/data-filtering/
description: Aspose.Cells for C++ APIを使用したデータフィルタの追加方法を学びます。
keywords: 色でフィルタを追加, 日付フィルタを追加, 数値フィルタを追加, 動的フィルタを追加, テキストフィルタを追加, Containsでカスタムフィルタを追加, NotContainsでカスタムフィルタを追加, BeginsWithでカスタムフィルタを追加, EndsWithでカスタムフィルタを追加
---

{{% alert color="primary" %}}

Microsoft Excelには、ワークシートデータの自動フィルタリングに役立つ機能がいくつかあります。Aspose.CellsはMicrosoft Excelの自動フィルタ機能を完全にサポートしています。この記事では、Microsoft Excelの機能の使用方法と、Aspose.Cellsを使用したコーディング方法について説明します。

{{% /alert %}}

## **データの自動フィルタリング**

自動フィルタリングは、リスト内で表示したいアイテムのみを素早く選択できる最も簡単な方法です。自動フィルタ機能により、リスト内のアイテムを特定の基準に従ってフィルタリングできます。テキスト、数値、または日付に基づいてフィルタリングできます。

### **Microsoft Excelの自動フィルタ**

Microsoft Excelで自動フィルタ機能を有効にするには：

1. ワークシート内の見出し行をクリックします。
1. **データ** メニューから、**フィルタ** を選択し、その後** 自動フィルタ** を選択します。

ワークシートに自動フィルタを適用すると、フィルタスイッチ（黒い矢印）が列見出しの右側に表示されます。

1. フィルタ矢印をクリックして、フィルタオプションのリストを表示します。

自動フィルタのオプションには次のものがあります:

|**オプション**|**説明**|
| :- | :- |
|All|リストのすべてのアイテムを一度に表示します。|
|Custom|含む/含まないなどのフィルター条件をカスタマイズします|
|Filter by Color|塗りつぶし色に基づくフィルター|
|Date Filters|日付に基づくさまざまな条件で行をフィルター|
|Number Filters|比較、平均、トップ10など、数値に関する異なるタイプのフィルタ。
|Text Filters|始まり、終わり、含むなどのさまざまなフィルター|
|Blanks/Non Blanks|これらのフィルターはテキストフィルター空白を通じて実装できます|

Microsoft Excelのユーザーは、これらのオプションを使用してワークシートデータを手動でフィルタリングします。

### **Aspose.CellsのAutofilter**

Aspose.Cellsは`Workbook`クラスを提供し、これがExcelファイルを表します。`Workbook`クラスには`Worksheets`コレクションが含まれ、各ワークシートにアクセスできます。

ワークシートは`Worksheet`クラスで表されます。`Worksheet`クラスはワークシート管理のためのさまざまなプロパティとメソッドを提供しています。オートフィルターを作成するには、`Worksheet`クラスの`AutoFilter`プロパティを使用します。`AutoFilter`プロパティは`AutoFilter`クラスのオブジェクトであり、ヘッダー行を構成するセル範囲を指定する`Range`プロパティを提供します。オートフィルターはヘッダー行のセル範囲に適用されます。

各ワークシートには1つのフィルター範囲のみ指定可能です。これはMicrosoft Excelによる制限です。カスタムデータフィルタリングには`AutoFilter.Custom`メソッドを使用してください。

以下の例では、前述のMicrosoft Excelで作成したのと同じAutoFilterをAspose.Cellsを使用して作成しています。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range of the heading row
    worksheet.GetAutoFilter().SetRange(u"A1:B1");

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **異なる種類のフィルタ**

Aspose.Cellsでは、カラーフィルタ、日付フィルタ、数値フィルタ、テキストフィルタ、ブランクフィルタ、およびノンブランクフィルタなど、さまざまな種類のフィルタを適用するための複数のオプションが提供されます。

##### **塗りつぶし色**

Aspose.Cellsは`AddFillColorFilter`関数を提供し、セルの塗りつぶし色に基づくデータフィルタを可能にします。以下の例では、異なる塗りつぶし色を持つシートの最初の列を使用して色フィルター機能をテストしています。サンプルファイルは以下のリンクからダウンロード可能です。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

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
    Workbook workbook(srcDir + u"ColouredCells.xlsx");

    // Instantiating a CellsColor object for foreground color
    CellsColor clrForeground = workbook.CreateCellsColor();
    clrForeground.SetColor(Color::Red());

    // Instantiating a CellsColor object for background color
    CellsColor clrBackground = workbook.CreateCellsColor();
    clrBackground.SetColor(Color::White());

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddFillColorFilter function to apply the filter
    worksheet.GetAutoFilter().AddFillColorFilter(0, BackgroundType::Solid, clrForeground, clrBackground);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredColouredCells.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **日付**

さまざまなタイプの日時フィルターを実装できます。例として、2018年1月のすべての日付を含む行をフィルタリングする方法を示します。以下に示すコード例では`AddDateFilter`関数を使用しています。サンプルファイルも提供されています。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddDateFilter function to apply the filter
    worksheet.GetAutoFilter().AddDateFilter(0, DateTimeGroupingType::Month, 2018, 1, 0, 0, 0, 0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Date filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **動的日付**

日時に基づく動的フィルターも必要となる場合があります。たとえば、年に関係なくすべてのセルの日付が1月のものだけを選択。こうした場合は`DynamicFilter`関数を使用します。サンプルも提供しています。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDynamicDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call DynamicFilter function to apply the filter
    worksheet.GetAutoFilter().Dynamic_Filter(0, DynamicFilterType::January);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Dynamic filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **番号**

カスタムフィルターは、範囲内の数値を選択するなどAspose.Cellsを使って適用できます。例として`Custom()`関数を用いて数値をフィルタリングする方法を示します。サンプルも提供しています。

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Number.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"FilteredNumber.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Custom function to apply the filter
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::GreaterOrEqual, 5, true, FilterOperatorType::LessOrEqual, 10);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **テキスト**

列にテキストが含まれ、特定の文字列を含むセルを選択したい場合、`Filter()`関数を使用できます。例では、テンプレートファイルに国名リストがあり、特定の国名を含む行を選択する例を示します。フィルタリング例も併せて示しています。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Text.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredText.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Filter function to apply the filter
    worksheet.GetAutoFilter().Filter(0, u"Angola");

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **空欄**

列に空白のセルが含まれ、それらの行だけを選択したい場合、`MatchBlanks()`関数を使用します。例を示します。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

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
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredBlank.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **非空白セル**

テキストを含むセルをフィルタリングしたい場合は、`MatchNonBlanks`フィルタを使用します。例を示します。

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

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

    // Create workbook object and open the Excel file
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchNonBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredNonBlank.xlsx");

    std::cout << "Non-blank filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Contains カスタムフィルタ**

Excelは、特定の文字列を含む行をフィルタリングするなど、カスタムフィルターを提供しています。この機能はAspose.Cellsで利用可能で、以下ではサンプルファイルの名前をフィルタリングすることで、デモンストレーションしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::Contains, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **NotContains カスタムフィルタ**

Excel は特定の文字列を含まない行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下で示されているサンプルファイル内の名前をフィルタリングしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::NotContains, u"Be");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File filtered and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **BeginsWith カスタムフィルタ**

Excel は特定の文字列で始まる行をフィルタするなど、カスタムフィルタを提供しています。この機能は Aspose.Cells で利用可能であり、以下で示されているサンプルファイル内の名前をフィルタリングしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows starting with string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **EndsWith カスタムフィルタ**

Excelは、特定の文字列で終わる行をフィルタリングするなど、カスタムフィルターを提供しています。この機能はAspose.Cellsで利用可能で、以下ではサンプルファイルの名前をフィルタリングすることで、デモンストレーションしています。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows end with string "ia"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"ia");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [複雑な基準を満たすレコードを表示するMicrosoft Excelの高度なフィルタの適用](/cells/ja/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [オートフィルタの更新後の非表示行インデックスの取得](/cells/ja/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
