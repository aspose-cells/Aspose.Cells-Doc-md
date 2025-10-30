---
title: Excel XP以降のC++による高度な保護設定
linktitle: Excel XP以降の高度な保護設定
type: docs
weight: 30
url: /ja/cpp/advanced-protection-settings-since-excel-xp/
description: Aspose.Cellsを使用してC++でExcelファイルに高度な保護設定を適用する方法を学びます。
---

{{% alert color="primary" %}}

Excel 2002またはXPのリリース以降、Microsoftは多くの高度な保護設定を追加しました。

{{% /alert %}}

## **紹介**

これらの保護設定により、ユーザーは次の操作を制限または許可できます：

- 行または列の削除。
- 内容、オブジェクト、またはシナリオの編集。
- セル、行、または列の書式設定。
- 行、列、またはハイパーリンクの挿入。
- ロックされたセルまたはロックされていないセルの選択。
- ピボットテーブルなどの使用。

Aspose.CellsはExcel XP以降のバージョンで提供されるすべての高度な保護設定をサポートしています。

### **Excel XPおよびそれ以降のバージョンを使用した高度な保護設定**

Excel XPで利用可能な保護設定を表示するには：

1. **ツール**メニューから、**保護**の後に**シートを保護**を選択します。ダイアログが表示されます。

Excel 2016で利用可能な保護設定を見るには：

1. **ファイル**メニューから、**ワークブックを保護**, その後**現在のシートを保護**を選択します。
1. **レビュー**メニューで**シートを保護**を選択します。

上記の手順に従うと、ダイアログが表示され、シートの機能の許可または制限やシートにパスワードを設定できます。

### **Aspose.Cellsを使用した高度な保護設定**

Aspose.Cellsはすべての高度な保護設定をサポートしています。

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) を提供します。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスには、Excelファイル内の各ワークシートにアクセスできる [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスによって表されます。

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスは、これらの高度な保護設定を適用するために使用される [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) プロパティを提供します。[**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) プロパティは実際には、いくつかの制限を無効または有効にするためのいくつかのブーリアンプロパティをカプセル化した [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) クラスのオブジェクトです。

以下は小さなサンプルアプリケーションです。それはExcelファイルを開いて、Excel XPおよびそれ以降のバージョンでサポートされる高度な保護設定のほとんどを使用します。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)メソッドを使用しないでください。また、[**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/)プロパティを使用してファイルをExcel97-2003またはXlsx形式で保存してください。高度な保護設定はExcel XP以降のみ対応です。

{{% /alert %}}

### **セルロックの問題**

セルの編集を制限したい場合は、保護設定を適用する前にセルをロックする必要があります。そうしないと、シートが保護されていてもセルは編集可能です。Microsoft Excel XPでセルをロックするには次のダイアログを使用します：

|**Excel XPでセルをロックするダイアログ**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells APIを使ってセルをロックすることも可能です。各セルには、Boolean型の[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)書式設定と[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)プロパティがあります。[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)プロパティを**true**または**false**に設定して、セルをロックまたはアンロックします。

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
