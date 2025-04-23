---
title: Tracer une chronologie lors de la rendu Excel en PDF avec C++
linktitle: Dessiner la chronologie lors du rendu d Excel en PDF
type: docs
weight: 60
url: /fr/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Gérer les chronologies des fichiers Excel avec Aspose.Cells avec C++.
keywords: Rendre la chronologie en PDF sans Office 2013, Office 2016, Office 2019 et Office 365
---

## **Dessiner une chronologie lors du rendu d'Excel en PDF**
Si vous avez un fichier Excel avec une chronologie appliquée et que vous souhaitez exporter ce fichier Excel en PDF avec les paramètres de chronologie, Aspose.Cells supporte cela par défaut. Vous exportez simplement le fichier Excel avec une chronologie en PDF, et le PDF généré affichera la chronologie appliquée.

Le code d'exemple suivant charge le [fichier Excel d'exemple](input.xlsx) qui contient une chronologie existante. Il enregistre ensuite le classeur sous la forme de [fichier PDF de sortie](out.pdf). La capture d'écran suivante compare le fichier Excel source et le fichier PDF généré.

<img src="out.png" width="60%">

## **Code d'exemple**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

