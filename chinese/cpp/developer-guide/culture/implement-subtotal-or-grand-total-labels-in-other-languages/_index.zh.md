---
title: 用 C++ 实现其他语言的子合计或总计标签
linktitle: 实现其他语言的子合计或总计标签
type: docs
weight: 50
url: /zh/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: 学习如何使用 Aspose.Cells for C++ 在非英语环境中实现子合计和总计标签。
---

## **可能的使用场景**

有时，你可能希望用中文、日文、阿拉伯语、印地语等非英语语言显示子合计和总计标签。Aspose.Cells 允许你使用 [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) 类和 [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/) 属性来实现，请参阅此文章了解如何使用 [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) 类：

- [使用GlobalizationSettings类自定义小计标签和饼图的其他标签](/cells/zh/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **用其他语言实现子合计或总计标签**

以下示例代码加载[示例Excel文件](5115151.xlsx)，用中文实现子合计和总计命名。请参考由此代码生成的[输出Excel文件](5115152.xlsx)。我们首先创建一个 [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) 类的实例，然后在代码中使用它。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings
{
public:
    U16String GetTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }

    U16String GetGrandTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Grand Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }
};
```

现在在代码中像下面这样使用上述创建的类：

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings {
public:
    virtual U16String GetTotalName(ConsolidationFunction functionType) override {
        return u"Custom Total";
    }

    virtual U16String GetGrandTotalName(ConsolidationFunction functionType) override {
        return u"Custom Grand Total";
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sample.xlsx");

    GlobalizationSettingsImp gsi;
    wb.GetSettings().SetGlobalizationSettings(&gsi);

    Worksheet ws = wb.GetWorksheets().Get(0);

    CellArea ca = CellArea::CreateCellArea(u"A1", u"B10");
    ws.GetCells().Subtotal(ca, 0, ConsolidationFunction::Sum, {2, 3, 4});

    ws.GetCells().SetColumnWidth(0, 40);

    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
