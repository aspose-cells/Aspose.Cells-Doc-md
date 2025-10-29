---
title: 用C++用Aspose.Cells计算IFNA函数
linktitle: 计算IFNA函数
description: 如何使用Aspose.Cells库的C++实现对IFNA函数的计算。通过加载现有Excel文件或创建新Excel文件，我们可以使用Aspose.Cells提供的方法计算IFNA函数并获得结果。最后将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells、Excel、IFNA函数、计算、C++
type: docs
weight: 40
url: /zh/cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells支持计算IFNA Excel函数。IFNA函数在公式返回#N/A错误值时返回您指定的值；否则返回公式的结果。

{{% /alert %}} 

## **使用Aspose.Cells计算IFNA函数**
下面的示例代码示例了使用Aspose.Cells计算IFNA函数。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for VLOOKUP
    worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
    worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
    worksheet.GetCells().Get(u"A3").PutValue(u"Banana");

    // Access cell A5 and A6
    Cell cellA5 = worksheet.GetCells().Get(u"A5");
    Cell cellA6 = worksheet.GetCells().Get(u"A6");

    // Assign IFNA formula to A5 and A6
    cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
    cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");

    // Calculate the formula of workbook
    workbook.CalculateFormula();

    // Print the values of A5 and A6
    std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
    std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **控制台输出**
这是上面示例代码的控制台输出。

{{< highlight java >}}

Not found

Orange

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
