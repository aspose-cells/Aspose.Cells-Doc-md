---
title: C++でピボットテーブルリボンを無効にします
linktitle: ピボットテーブルリボンの無効化
type: docs
weight: 90
url: /ja/cpp/disable-pivot-table-ribbons/
description: Excelファイル内のピボットテーブルリボンを無効にする方法を学びます（Aspose.Cells for C++）。
---

{{% alert color="primary" %}}

ピボットテーブルベースのレポートは便利ですが、ターゲットユーザーがExcelの詳細な知識を持っていない場合、エラーが発生しやすくなります。このような状況下では、ユーザーがピボットテーブルを変更できないように制限したいでしょう。追加のフィルター、スライサー、フィールドの追加や、レポート内の特定のアイテムの順序変更など、多くのピボットテーブルの機能は一般的にすべてのユーザーに推奨されません。一方、ユーザーはレポートを更新したり、既存のフィルターやスライサーを使用したりできる必要があります。Aspose.Cells は、これらのレポートを作成する際にユーザーによる変更を制限する機能を提供しています。そのために、Excelはピボットテーブルリボンを無効にする機能を提供しており、Aspose.Cells もこれをサポートしています。開発者は、これらのレポートを変更する操作を制限するリボンを無効にできます。

{{% /alert %}}

## **PivotTable.EnableWizardを使用してピボットテーブルリボンを無効にする**

次のコードは、この機能を実演します。シートからピボットテーブルにアクセスし、[**GetEnableWizard()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getenablewizard/) を **false** に設定します。サンプルピボットテーブルファイルはこの [リンク](pivot_table_test.xlsx) からダウンロードできます。

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
    U16String inputFilePath = srcDir + u"pivot_table_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Access the pivot table in the first sheet
    PivotTable pt = wb.GetWorksheets().Get(0).GetPivotTables().Get(0);

    // Disable ribbon for this pivot table
    pt.SetEnableWizard(false);

    // Save output file
    wb.Save(outputFilePath);

    std::cout << "Pivot table ribbon disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
