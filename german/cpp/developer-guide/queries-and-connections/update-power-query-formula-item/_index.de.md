---
title: Aktualisieren Sie Power Query Formel Item mit C++
linktitle: Aktualisieren des Power Query Formelelements
type: docs
weight: 120
url: /de/cpp/update-power-query-formula-item/
description: Lernen Sie, wie Sie Power Query Formel Elemente mit Aspose.Cells for C++ aktualisieren, um den Speicherort der Quelldatei in Excel Dateien zu ändern.
---

## **Anwendungsszenario**

Es kann Fälle geben, in denen die Quelldateien verschoben wurden und die Excel-Datei die Datei nicht finden kann. In solchen Fällen bietet die Aspose.Cells API die Möglichkeit, das Power Query Formel-Element mit Hilfe der [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) Klasse zu aktualisieren, um den Speicherort der Quelldatei zu ändern.

## **Aktualisierung des Power Query Formel-Elements**

Die Aspose.Cells API bietet die Möglichkeit, Power Query Formel-Elemente zu aktualisieren. Der folgende Codeausschnitt demonstriert die Aktualisierung des Speicherorts der Quelldatei in der Excel-Datei durch Verwendung der [**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/)-Eigenschaft. Die Quelldatei und die Ergebnisdatei sind zu Ihrer Referenz angehängt.

- [Quelldatei 1](106364953.xlsx)
- [Quelldatei 2](106364954.xlsx)
- [Ausgabedatei](106364955.xlsx)

## **Beispielcode**

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
