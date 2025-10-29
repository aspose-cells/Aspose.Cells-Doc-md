---
title: Déplacer une plage de cellules dans une feuille de calcul avec C++
linktitle: Déplacer une plage de cellules dans une feuille de calcul
type: docs
weight: 370
url: /fr/cpp/move-range-of-cells-in-a-worksheet/
description: Apprenez comment déplacer une plage de cellules dans une feuille de calcul avec Aspose.Cells en C++.
---

{{% alert color="primary" %}}

Cet article montre comment déplacer une plage de cellules dans une feuille de calcul.

{{% /alert %}}

## **Déplacer une plage de cellules dans une feuille de calcul**
Le code d'exemple utilise un fichier modèle pour démontrer la tâche.

**Le fichier d'entrée**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Veuillez consulter le fichier généré suivant avec la plage A1:B5 déplacée en C1:D5.

**Le fichier de sortie**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the workbook object. Open the Excel file
    U16String inputFilePath = u"book1.xlsx";
    Workbook workbook(inputFilePath);

    // Access the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create a range from A1 to B5
    Range range = cells.CreateRange(u"A1", u"B5");

    // Move the range to the right by 2 columns
    range.MoveTo(0, 2);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
