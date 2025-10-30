---
title: C++を使った日時の管理方法
linktitle: 日付と時間の管理方法
type: docs
weight: 600
url: /ja/cpp/how-to-manage-dates-and-times/
description: Aspose.Cells for C++ APIを通じて日時の管理方法を学びます。
keywords: 日付と時間の管理方法、1900年の日付システム、1904年の日付システム、日付と時間の設定、日付と時間の取得、日付と時間の管理、Excelでの日付と時間の格納、セルでの日付と時間の表示。
---

## **Excelでの日付と時間の格納方法**
日時はセル内で数値として保存されます。したがって、日時を含むセルの値は数値型です。日時を示す数値は、日付（整数部）と時間（小数部）の2つの部分から構成されます。`Cell::GetDoubleValue()`メソッドはこの数値を返します。

## **Aspose.Cellsでの日付と時間の表示方法**
数値として表示するには、`Style::SetNumber()`または`Style::SetCustom()`メソッドを使ってセルに必要な日付と時間のフォーマットを適用します。`Cell::GetDateTimeValue()`メソッドは、その数値が意味する日付と時間を示す`DateTime`オブジェクトを返します。
<br>
<image src="1.png" width="70%" />

## **Aspose.Cellsでの2つの日付システムの切り替え方法**
MS-Excelは、日付をシリアル値と呼ばれる数値として格納します。シリアル値は、日付システムの最初の日から経過した日数を示す整数です。Excelは、シリアル値のために以下の日付システムをサポートしています。

1. 1900年の日付システム。最初の日付は1900年1月1日で、そのシリアル値は1です。最後の日付は9999年12月31日で、そのシリアル値は2,958,465です。この日付システムはワークブックのデフォルトで使用されます。
1. 1904日付システム。最初の日付は1904年1月1日で、そのシリアル値は0です。最後の日付は9999年12月31日で、そのシリアル値は2,957,003です。この日付システムをワークブックで使用するには、`Workbook::GetSettings()->SetDate1904(true)`を設定します。

この例は、異なる日付システムで同じ日付に格納されたシリアル値が異なることを示しています。
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    workbook.GetSettings().SetDate1904(false);

    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(45237.0);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.GetDoubleValue() << std::endl;
    }

    workbook.GetSettings().SetDate1904(true);
    std::cout << "use The 1904 date system====================" << std::endl;

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(43775.0);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.GetDoubleValue() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
出力結果：
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Aspose.Cellsでの日時値の設定方法**
この例では、セルA1とA2に`DateTime`値を設定し、A1にはカスタムの書式設定、A2には数値フォーマットを適用し、値のタイプを出力します。

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    time_t now = time(nullptr);
    double oaDate1 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a1.PutValue(oaDate1);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    now = time(nullptr);
    double oaDate2 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a2.SetValue(oaDate2);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

出力結果：
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Aspose.Cellsでの日時値の取得方法**
この例では、セルA1とA2に`DateTime`値を設定し、それぞれにカスタムの書式設定と数値フォーマットを適用します。その後、二つのセルの値のタイプを確認し、`DateTime`値とフォーマット済み文字列を出力します。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(Date{2023, 5, 15});

    if (a1.GetType() == CellValueType::IsNumeric) {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
        Date dateTimeValue = a1.GetDateTimeValue();
        std::cout << "A1 DateTime String Value: " << a1.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(Date{2023, 5, 16});

    if (a2.GetType() == CellValueType::IsNumeric) {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
        Date dateTimeValue = a2.GetDateTimeValue();
        std::cout << "A2 DateTime String Value: " << a2.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

出力結果：
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
{{< app/cells/assistant language="cpp" >}}
