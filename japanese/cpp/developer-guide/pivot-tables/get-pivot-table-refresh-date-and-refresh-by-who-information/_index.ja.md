---
title: C++を使ったピボットテーブルの更新日時と更新者情報の取得
linktitle: ピボットテーブルの更新日時と更新者情報を取得する方法
type: docs
weight: 100
url: /ja/cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Aspose.Cellsを使用してワークブックからリフレッシュ日時と更新者情報を取得する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは今、ワークブックから更新日時と更新者情報を取得する機能をサポートしています。

{{% /alert %}}

 [**PivotTable.GetRefreshDate()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshdate/) はピボットテーブルレポートが最後に更新された日時を返します。同様に、 [**PivotTable.GetRefreshedByWho()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getrefreshedbywho/) プロパティは最後にレポートを更新したユーザーの名前を返します。次の例はこの機能を示しており、サンプルファイルは以下のリンクからダウンロードできます。

[SourcePivotTable.xlsx](77496335.xlsx)

**サンプルコード**

```cpp
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

std::string Date_To_String(const Aspose::Cells::Date& date) {
    char buffer[100];
    snprintf(buffer, sizeof(buffer), "%04d-%02d-%02d %02d:%02d:%02d",
             date.year, date.month, date.day, date.hour, date.minute, date.second);
    return buffer;
}

std::string convert_u16_to_string(const char16_t* str) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(str);
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"sourcePivotTable.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    std::cout << "Pivot table refresh by who = " << convert_u16_to_string(pivotTable.GetRefreshedByWho().GetData()) << std::endl;

    std::cout << "Pivot table refresh date = " << Date_To_String(pivotTable.GetRefreshDate()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
