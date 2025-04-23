---
title: Actualizar elemento de fórmula de Power Query con C++
linktitle: Actualizar elemento de fórmula de Power Query
type: docs
weight: 120
url: /es/cpp/update-power-query-formula-item/
description: Aprenda cómo actualizar los elementos de fórmula de Power Query usando Aspose.Cells for C++ para modificar las ubicaciones del archivo de fuente de datos en archivos de Excel.
---

## **Escenario de uso**

Puede haber casos donde los archivos de fuente de datos se mueven, y el archivo de Excel no puede localizar el archivo. En tales casos, la API Aspose.Cells ofrece la opción de actualizar el elemento de fórmula de Power Query utilizando la clase [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) para actualizar la ubicación del archivo origen.

## **Actualizar elemento de fórmula de Power Query**

La API Aspose.Cells proporciona la capacidad de actualizar los elementos de fórmula de Power Query. El siguiente fragmento de código demuestra cómo actualizar la ubicación del archivo de origen de datos en el archivo Excel usando la propiedad [**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/). Los archivos fuente y de salida están adjuntos para su referencia.

- [Archivo de origen 1](106364953.xlsx)
- [Archivo de origen 2](106364954.xlsx)
- [Archivo de salida](106364955.xlsx)

## **Código de muestra**

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
