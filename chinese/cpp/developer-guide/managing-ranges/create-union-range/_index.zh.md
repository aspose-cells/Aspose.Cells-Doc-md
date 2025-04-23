---
title: 用C++创建联合范围
linktitle: 创建联合范围
type: docs
weight: 360
url: /zh/cpp/create-union-range/
description: 使用Aspose.Cells在Excel文件中创建联合范围
---

## **创建联合范围**
Aspose.Cells提供了通过[CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/)方法创建联合范围的能力。[CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/)方法接受两个参数，一个是创建联合范围的地址，另一个是工作表的索引，返回一个[UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/)对象。

以下代码示例演示了使用[CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/)方法创建联合范围。生成的输出文件已附上供参考。

- [输出文件](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
