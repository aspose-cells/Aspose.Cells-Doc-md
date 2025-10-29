---
title: Обновление формулы Power Query с помощью C++
linktitle: Обновление элемента формулы Power Query
type: docs
weight: 120
url: /ru/cpp/update-power-query-formula-item/
description: Узнайте, как обновлять элементы формулы Power Query с помощью Aspose.Cells for C++ для изменения местоположения файла источника данных в файлах Excel.
---

## **Сценарий использования**

Могут возникнуть случаи, когда файлы источника данных были перемещены, и файл Excel не может его найти. В таких случаях API Aspose.Cells предоставляет возможность обновлять элемент формулы Power Query с помощью класса [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) для изменения расположения исходного файла.

## **Обновление элемента формулы Power Query**

API Aspose.Cells позволяет обновлять элементы формулы Power Query. Следующий фрагмент кода демонстрирует изменение местоположения файла источника данных в файле Excel с помощью свойства [**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/). Исходный и выходной файлы приложены для вашего ознакомления.

- [Исходный файл 1](106364953.xlsx)
- [Исходный файл 2](106364954.xlsx)
- [Выходной файл](106364955.xlsx)

## **Образец кода**

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
