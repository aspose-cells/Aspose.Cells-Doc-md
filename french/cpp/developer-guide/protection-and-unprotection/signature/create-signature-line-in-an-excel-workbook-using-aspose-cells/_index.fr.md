---
title: Créer une ligne de signature dans un classeur Excel avec C++ en utilisant Aspose.Cells
linktitle: Créer une ligne de signature dans un classeur Excel
type: docs
weight: 150
url: /fr/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Cet article décrit comment créer une ligne de signature dans un classeur Excel en utilisant des codes C++ avec Aspose.Cells for C++.
keywords: Créer une ligne de signature dans un classeur Excel, comment créer une ligne de signature dans un classeur Excel, comment ajouter une ligne de signature, comment ajouter une ligne de signature à un fichier Excel.
---

## **Introduction**

Microsoft Excel permet d'ajouter une **ligne de signature** dans les classeurs Excel. Vous pouvez ajouter une ligne de signature en cliquant sur l'onglet **Insertion** puis en sélectionnant **Ligne de signature** dans le groupe **Texte**.

## **Comment créer une ligne de signature pour Excel**

Aspose.Cells propose également cette fonctionnalité et a exposé la propriété [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) à cette fin. Cet article expliquera comment utiliser cette propriété pour ajouter une ligne de signature en utilisant Aspose.Cells.

Le code d'exemple suivant ajoute une ligne de signature en utilisant la propriété [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) et enregistre le classeur.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Create signature line object
    SignatureLine s;
    s.SetSigner(u"John Doe");
    s.SetTitle(u"Development Lead");
    s.SetEmail(u"john.doe@aspose.com");

    // Adds a Signature Line to the worksheet.
    workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);

    // Save the workbook
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully with signature line!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
