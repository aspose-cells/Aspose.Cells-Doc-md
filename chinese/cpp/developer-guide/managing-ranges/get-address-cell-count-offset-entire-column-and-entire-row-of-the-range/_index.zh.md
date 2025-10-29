---
title: 使用C++获取范围的地址、单元格数量、偏移量、整列和整行
linktitle: 获取范围的地址、单元格数、偏移、整列和整行
type: docs
weight: 330
url: /zh/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: 学习如何使用Aspose.Cells for C++获取范围的地址、单元格数量、偏移量、整列和整行。
---

## **可能的使用场景**
Aspose.Cells提供了`Range`对象，该对象具有多种实用方法，方便操作Excel范围。本文介绍以下`Range`对象的方法或属性的用法：

- **地址**

  获取范围的地址。

- **单元格计数**

  获取范围内的总单元格数。

- **偏移**

  通过偏移获取范围。

- **整列**

  获取表示整个列（或列）的`Range`对象，该范围包含指定的范围。

- **整行**

  获取表示整个行（或行）的`Range`对象，该范围包含指定的范围。

## **获取范围的地址、单元格数、偏移、整列和整行**
以下示例代码演示了上述方法和属性的使用。请参考以下代码的控制台输出。

## **示例代码**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create range A1:B3
    cout << "Creating Range A1:B3" << endl;
    Range rng = ws.GetCells().CreateRange(u"A1:B3");

    // Print range address and cell count
    cout << "Range Address: " << rng.GetAddress().ToUtf8() << endl;
    cout << "Range row Count: " << rng.GetRowCount() << endl;
    cout << "Range column Count: " << rng.GetColumnCount() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    // Create range A1
    cout << "Creating Range A1" << endl;
    rng = ws.GetCells().CreateRange(u"A1");

    // Print range offset, entire column and entire row
    cout << "Offset: " << rng.GetOffset(2, 2).GetAddress().ToUtf8() << endl;
    cout << "Entire Column: " << rng.GetEntireColumn().GetAddress().ToUtf8() << endl;
    cout << "Entire Row: " << rng.GetEntireRow().GetAddress().ToUtf8() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **控制台输出**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
