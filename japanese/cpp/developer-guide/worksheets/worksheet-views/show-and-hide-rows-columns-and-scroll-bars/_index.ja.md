---
title: 行、列、スクロールバーの表示・非表示をC++で行う
linktitle: 行、列、スクロールバーの表示・非表示
type: docs
weight: 20
url: /ja/cpp/show-and-hide-rows-columns-and-scroll-bars/
description: この記事は、C++言語とAspose.Cells APIを使用してExcelワークシートの行と列をプログラム的に表示・非表示にする方法を示しています。スクロールバーの表示状態を調整でき、複数の行と列を非表示にすることも可能です。
---

{{% alert color="primary" %}}

Aspose.Cellsは、ワークシートの行、列、スクロールバーの表示状態を制御する方法を提供します。

{{% /alert %}}

## **行や列の表示と非表示**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスは、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、そのワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションは、ワークシートの行や列を管理するための複数のメソッドを提供します。その一部を以下に示します。

### **行と列を表示**

開発者は、[**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/)と[**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/)のメソッドを呼び出すことで、非表示になっている行や列を表示させることができます。どちらのメソッドも、2つのパラメータを取ります：

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。

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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhiding the 3rd row and setting its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhiding the 2nd column and setting its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

非表示の列の幅を元に戻す必要がある場合や、元の幅に復元したい場合は、負の幅を指定して列の非表示を解除してください。例：`worksheet->GetCells()->UnhideColumn(5, -1)`。

{{% /alert %}}

### **行と列を非表示**

開発者は、[**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/)と[**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/)のメソッドを呼び出すことで、行や列を非表示にできます。どちらのメソッドも、特定の行や列のインデックスをパラメータとして受け取り、その行または列を非表示にします。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。

{{% /alert %}}

### **複数の行と列を非表示**

開発者は、[**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/)と[**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/)のメソッドを呼び出し、複数の行や列を一度に非表示にできます。これらの両方のメソッドは、開始行または列のインデックスと隠す行または列の数をパラメータとして受け取ります。

```c++
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **スクロールバーの表示と非表示**

スクロールバーは、どのファイルの内容をナビゲートするために使用されます。通常、2種類のスクロールバーがあります。

- 垂直スクロールバー
- 水平スクロールバー

Microsoft Excelは、ユーザーがワークシートの内容をスクロールできるように、水平および垂直のスクロールバーを提供しています。Aspose.Cellsを使用すると、Excelファイルの両方のタイプのスクロールバーの表示/非表示を制御することができます。

### **スクロールバーの表示を制御する**

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスは、Excelファイルの管理に役立つさまざまなプロパティとメソッドを提供します。スクロールバーの表示状態を制御するには、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)と[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)プロパティを使用します。[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)と[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)はBooleanプロパティであり、これらのプロパティは**true**または**false**の値のみを格納します。

#### **スクロールバーを表示する**

スクロールバーを表示するには、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)または[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)プロパティを**true**に設定します。

#### **スクロールバーを非表示にする**

スクロールバーを非表示にするには、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)または[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)プロパティを**false**に設定します。

**サンプルコード**

以下は、Excelファイル`book1.xls`を開き、スクロールバーを非表示にして、変更後のファイルを`output.xls`として保存する完全なコード例です。

```c++
#include <iostream>
#include <fstream>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Hide the vertical scroll bar of the Excel file
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the Excel file
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
