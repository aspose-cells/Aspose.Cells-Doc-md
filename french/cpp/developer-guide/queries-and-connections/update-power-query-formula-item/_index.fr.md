---
title: Mettre à jour l élément de formule Power Query avec C++
linktitle: Mettre à jour l élément de formule Power Query
type: docs
weight: 120
url: /fr/cpp/update-power-query-formula-item/
description: Découvrez comment mettre à jour les éléments de formule Power Query en utilisant Aspose.Cells for C++ pour modifier les emplacements des fichiers sources de données dans les fichiers Excel.
---

## **Scénario d'utilisation**

Il peut arriver que les fichiers sources de données soient déplacés, et que le fichier Excel ne puisse pas localiser le fichier. Dans ce cas, l'API Aspose.Cells offre la possibilité de mettre à jour l'élément de formule Power Query en utilisant la classe [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) pour mettre à jour l'emplacement du fichier source.

## **Mise à jour de l'élément de formule Power Query**

L'API Aspose.Cells permet de mettre à jour les éléments de formule Power Query. Le fragment de code suivant illustre la mise à jour de l'emplacement du fichier source dans le fichier Excel en utilisant la propriété [**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/). Les fichiers source et de sortie sont joints pour votre référence.

- [Fichier source 1](106364953.xlsx)
- [Fichier source 2](106364954.xlsx)
- [Fichier de sortie](106364955.xlsx)

## **Code d'exemple**

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
