---
title: Rendre les compléments Office lors de la conversion d Excel en PDF avec C++
linktitle: Rendre les Compléments Office lors de la conversion d Excel en PDF
type: docs
weight: 100
url: /fr/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: Apprenez à rendre les compléments Office lors de la conversion de fichiers Excel en PDF en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Auparavant, Aspose.Cells ne pouvait pas rendre les compléments Office lorsque un fichier Excel était enregistré au format PDF. Maintenant, Aspose.Cells le rend correctement. Vous n'avez pas besoin d'utiliser une méthode ou propriété spécifique pour rendre les compléments Office dans le PDF de sortie. Il suffit d'enregistrer votre fichier Excel au format PDF, et il rendra les compléments Office.

## **Rendre les compléments Office lors de la conversion Excel en PDF**

Le code d'exemple suivant enregistre le [fichier Excel d'exemple](60489769.xlsx) qui contient les compléments Office. Veuillez voir le [PDF de sortie généré avec la version précédente, c’est-à-dire 17.11](60489770.pdf) et le [PDF de sortie généré avec la version plus récente, c’est-à-dire 17.12 et suivantes](60489771.pdf). Le PDF de la version précédente est vide, mais le PDF de la version plus récente montre le complément Office.

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
