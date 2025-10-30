---
title: Aggiorna l elemento della formula Power Query con C++
linktitle: Aggiornare l Elemento della Formula di Power Query
type: docs
weight: 120
url: /it/cpp/update-power-query-formula-item/
description: Impara come aggiornare gli elementi della Formula Power Query utilizzando Aspose.Cells for C++ per modificare le posizioni del file della sorgente dati in file Excel.
---

## **Scenario di Utilizzo**

Potrebbero esserci casi in cui i file della sorgente dati vengono spostati e il file Excel non riesce a individuare il file. In tali casi, l'API Aspose.Cells offre l'opzione di aggiornare l'elemento della Formula Power Query utilizzando la classe [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) per aggiornare la posizione del file di origine.

## **Aggiornare elemento della Formula Power Query**

L'API Aspose.Cells fornisce la possibilità di aggiornare gli elementi della Formula Power Query. Il seguente esempio di codice dimostra come aggiornare la posizione del file di origine dati nel file Excel utilizzando la proprietà [**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/). I file di origine e di output sono allegati per il vostro riferimento.

- [File di origine 1](106364953.xlsx)
- [File di origine 2](106364954.xlsx)
- [File di output](106364955.xlsx)

## **Codice di Esempio**

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
