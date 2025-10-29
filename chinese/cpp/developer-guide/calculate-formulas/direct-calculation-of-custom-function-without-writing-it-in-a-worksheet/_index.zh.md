---
title: 用C++直接计算自定义函数，无需在工作表中编写
linktitle: 直接计算自定义函数
description: 本文介绍如何使用Aspose.Cells库在Microsoft Excel中直接计算自定义函数，而无需在工作表中编写函数。 通过加载现有的Excel文件或创建一个新的Excel文件，我们可以使用Aspose.Cells提供的方法来计算自定义函数并获得结果。 最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 自定义函数, 直接计算, 无需书写, 工作表
type: docs
weight: 90
url: /zh/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **无需在工作表中编写，直接计算自定义函数**

本主题介绍如何在不先写入工作表的情况下直接计算自定义函数。请使用[**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/)方法实现此目的。

请参见以下示例代码，说明了此方法的使用。我们使用了一个名为MyCompany::CustomFunction()的自定义函数，自己计算其值为“Aspose.Cells。”，然后此值将由计算引擎自动与单元格A1的值“欢迎来到”拼接，最终返回“欢迎来到Aspose.Cells。”。如代码所示，我们没有在工作表中写入任何自定义函数，而是通过我们自己的自定义逻辑直接计算。

### **编程示例**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class ICustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        // Check the formula name and calculate it yourself
        if (data.GetFunctionName() == u"MyCompany.CustomFunction")
        {
            // This is our calculated value
            data.SetCalculatedValue(Aspose::Cells::Object(u"Aspose.Cells."));
        }
    }
};

class ImplementDirectCalculationOfCustomFunction
{
public:
    static void Run()
    {
        Aspose::Cells::Startup();

        // Create a workbook
        Workbook wb;

        // Access first worksheet
        Worksheet ws = wb.GetWorksheets().Get(0);

        // Add some text in cell A1
        ws.GetCells().Get(u"A1").PutValue(u"Welcome to ");

        // Create a calculation options with custom engine
        CalculationOptions opts;
        opts.SetCustomEngine(new ICustomEngine());

        // This line shows how you can call your own custom function without
        // a need to write it in any worksheet cell
        // After the execution of this line, it will return
        // Welcome to Aspose.Cells.
        Aspose::Cells::Object ret = ws.CalculateFormula(u"=A1 & MyCompany.CustomFunction()", opts);

        // Print the calculated value on Console
        std::cout << "Calculated Value: " << ret.ToString().ToUtf8() << std::endl;

        Aspose::Cells::Cleanup();
    }
};

int main()
{
    ImplementDirectCalculationOfCustomFunction::Run();
    return 0;
}
```

### **控制台输出**

以下是上面示例代码的控制台输出。

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **相关文章**

{{% alert color="primary" %}}

[实现自定义计算引擎以扩展Aspose.Cells的默认引擎](/cells/zh/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
