---
title: Uppdatera Power Query formelitem med C++
linktitle: Uppdatera Power Query formelobjekt
type: docs
weight: 120
url: /sv/cpp/update-power-query-formula-item/
description: Lär dig hur du uppdaterar Power Query Formel objekt med Aspose.Cells for C++ för att ändra filplatser för datakällor i Excel filer.
---

## **Användningsscenarie**

Det kan finnas fall där datakälldarna har flyttats, och Excel-filen inte kan hitta filen. I sådana fall ger Aspose.Cells API ett alternativ för att uppdatera Power Query Formel-objektet genom att använda [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) klassen för att ändra platsen för källdfilen.

## **Uppdatera Power Query-formelobjekt**

Aspose.Cells API ger möjlighet att uppdatera Power Query Formel-objekt. Följande kodexempel visar hur man uppdaterar platsen för datakällfilen i Excel-filen genom att använda egenskapen [**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/). Käll- och utgångsfiler är bifogade för din referens.

- [Källfil 1](106364953.xlsx)
- [Källfil 2](106364954.xlsx)
- [Utdatafil](106364955.xlsx)

## **Exempelkod**

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
