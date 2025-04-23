---
title: Mettre en œuvre une taille de papier personnalisée pour la feuille lors du rendu avec C++
linktitle: Implémenter une taille de papier personnalisée de la feuille de calcul pour le rendu
type: docs
weight: 70
url: /fr/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Cet article explique comment utiliser l API C++ pour définir une taille de papier personnalisée pour vos feuilles souhaitées lors de la conversion d un fichier Excel en PDF de manière programmatique.
keywords: définir une taille de papier personnalisée lors du rendu d un Excel en PDF en C++
---

## **Scénarios d'utilisation possibles**

Il n'existe pas d'option directe pour créer des tailles de papier personnalisées dans MS Excel ; cependant, vous pouvez définir une taille de papier personnalisée pour vos feuilles lors du rendu d'un fichier Excel en PDF. Ce document explique comment définir une taille de papier personnalisée à l'aide des API Aspose.Cells.

## **Implémenter une taille de papier personnalisée de la feuille de calcul pour le rendu**

Aspose.Cells permet de mettre en œuvre la taille de papier souhaitée pour la feuille de calcul. Vous pouvez utiliser la méthode [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/) de la classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) pour spécifier une taille de page personnalisée. Le code d'exemple suivant illustre comment spécifier une taille de papier personnalisée pour la première feuille de calcul du classeur. Veuillez également consulter le [PDF de sortie](45056028.pdf) généré avec le code ci-dessous pour référence.

## **Capture d'écran**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
