---
title: 用C++更新Power Query公式项
linktitle: 更新Power Query公式项
type: docs
weight: 120
url: /zh/cpp/update-power-query-formula-item/
description: 学习如何使用Aspose.Cells for C++更新Power Query公式项，以修改Excel文件中的数据源文件位置。
---

## **使用场景**

在某些情况下，数据源文件可能已移动，Excel文件无法找到该文件。在此情况下，Aspose.Cells API提供通过使用[*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/)类来更新源文件位置的选项。

## **更新Power Query公式项**

Aspose.Cells API提供了更新Power Query公式项的能力。以下代码演示如何使用[**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/)属性在Excel文件中更新数据源文件的位置。源文件和输出文件已附上供参考。

- [源文件1](106364953.xlsx)
- [源文件 2](106364954.xlsx)
- [输出文件](106364955.xlsx)

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SamplePowerQueryFormula.xlsx");
    DataMashup mashupData = workbook.GetDataMashup();

    PowerQueryFormulaCollection powerQueryFormulas = mashupData.GetPowerQueryFormulas();
    for (int i = 0; i < powerQueryFormulas.GetCount(); ++i)
    {
        PowerQueryFormula formula = powerQueryFormulas.Get(i);
        PowerQueryFormulaItemCollection powerQueryFormulaItems = formula.GetPowerQueryFormulaItems();
        for (int j = 0; j < powerQueryFormulaItems.GetCount(); ++j)
        {
            PowerQueryFormulaItem item = powerQueryFormulaItems.Get(j);
            if (item.GetName() == u"Source")
            {
                U16String newValue = u"Excel.Workbook(File.Contents(\"" + srcDir + u"SamplePowerQueryFormulaSource.xlsx" + u"\"), null, true)";
                item.SetValue(newValue);
            }
        }
    }

    workbook.Save(outDir + u"SamplePowerQueryFormula_out.xlsx");
    std::cout << "PowerQueryFormula updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
