---
title: 使用抽象计算引擎与C++返回值范围
linktitle: 使用AbstractCalculationEngine返回一系列值
description: 本文介绍如何使用Aspose.Cells库与C++在Microsoft Excel中返回值范围的抽象计算引擎。通过加载现有Excel文件或创建新Excel文件，我们可以使用Aspose.Cells提供的方法获取值范围并返回结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 返回一系列值的抽象计算引擎
type: docs
weight: 55
url: /zh/cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells提供[**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)类，用于实现Microsoft Excel不支持的用户定义或自定义函数。

本文将解释如何从[**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)返回值范围。

{{% /alert %}}

 以下代码演示了如何使用[**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)类及其方法返回值范围。

 创建一个具有`CalculateCustomFunction`函数的类。该类实现了[**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomFunctionStaticValue : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
		Vector<Object> row1{Object(Date{2015, 6, 12, 10, 6, 30}) ,Object(2)};
        Vector<Object> row2{ Object(3.0) ,Object(U16String(u"Test")) };

        Vector<Vector<Object>> values{ row1 , row2 };

        // Create Object with the 2D Vector and set as calculated value
        Object calculatedValue(values);

        // Set the calculated value in the CalculationData object
        data.SetCalculatedValue(calculatedValue);
    }
};

```

 现在在您的程序中使用上述函数。

```c++
int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    Cell cell = cells.Get(0, 0);
    cell.SetArrayFormula(u"=MYFUNC()", 2, 2);

    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    CalculationOptions calculationOptions;

    // Create and set custom engine with proper memory management
    std::shared_ptr<CustomFunctionStaticValue> customEngine = 
        std::make_shared<CustomFunctionStaticValue>();
    calculationOptions.SetCustomEngine(customEngine.get());

    workbook.CalculateFormula(calculationOptions);

    workbook.GetSettings().GetFormulaSettings().SetCalculationMode(CalcModeType::Manual);
    workbook.Save(outDir + u"output_out.xlsx");
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
