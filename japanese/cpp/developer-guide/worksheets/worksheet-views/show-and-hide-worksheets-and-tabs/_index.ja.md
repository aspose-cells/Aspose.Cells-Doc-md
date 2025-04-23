---
title: シートとタブの表示・非表示をC++で行う
linktitle: ワークシートとタブの表示と非表示
type: docs
weight: 10
url: /ja/cpp/show-and-hide-worksheets-and-tabs/
description: Excelシートの表示と非表示を行うサンプルコード、およびExcelブックのタブの表示と非表示の方法を提供します。
---

{{% alert color="primary" %}}

Aspose.Cellsはユーザーに、ワークブック内のワークシートやタブなどの要素を表示または非表示にする機能を提供します。

{{% /alert %}}

## **ワークシートの表示と非表示**

Excelファイルには1つ以上のワークシートが含まれることがあります。Excelファイルを作成するときには、作業するExcelファイルにワークシートを追加します。Excelファイル内の各ワークシートは、独自のデータや書式設定などを持つため、他のワークシートから独立しています。開発者は時々、Excelファイル内で特定のワークシートを非表示にし、他のワークシートを表示したい場合があります。そのため、Aspose.Cellsは開発者がExcelファイル内のワークシートの表示を制御することを可能にします。

Aspose.Cellsは、Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)を提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシートを管理するためのさまざまなプロパティとメソッドを提供します。ワークシートの表示状態を制御するには、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/)プロパティを使用します。[**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/)はBoolean型のプロパティであり、**true**または**false**の値しか保存できません。

### **ワークシートを表示する**

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/)プロパティを**true**に設定して、ワークシートを表示します。

### **ワークシートを非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/)プロパティを**false**に設定して、ワークシートを非表示にします。

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **タブの表示と非表示**

Microsoft Excelの下部をよく見ると、いくつかのコントロールが表示されます。これには次のものが含まれます:

- シートタブ。
- タブのスクロールボタン。

シートタブはExcelファイル内のワークシートを表します。任意のタブをクリックするとそのワークシートに切り替えることができます。ワークブック内にワークシートが多いほど、シートタブも多く表示されます。Excelファイルに多くのワークシートが含まれている場合は、それらをナビゲートするためのボタンが必要になります。そのため、Microsoft Excelはシートタブのスクロールボタンを提供しています。

Aspose.Cellsを使用すると、開発者はExcelファイル内のシートタブとタブのスクロールボタンの表示を制御できます。

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスは、Excelファイルを管理するためのさまざまなプロパティとメソッドを提供します。Excelファイルのタブの表示状態を制御するには、開発者は[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)プロパティを使用できます。[**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)はBoolean型のプロパティであり、**true**または**false**の値しか保存できません。

### **タブを表示する**

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)プロパティを**true**に設定してタブを表示します。

### **タブを非表示にする**

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)プロパティを**false**に設定して、Excelファイルのタブを非表示にします。

以下は、Excelファイル（book1.xls）を開き、そのタブを非表示にして修正したファイルをoutput.xlsとして保存する完全な例です。コードの実行後、ワークブックのタブが非表示になっていることが確認できます。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **タブバーの幅を制御する**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
