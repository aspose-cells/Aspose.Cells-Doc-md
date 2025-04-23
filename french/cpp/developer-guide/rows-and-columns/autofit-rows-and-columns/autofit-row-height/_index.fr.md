---
title: Ajustement automatique de la hauteur des lignes lors du chargement du fichier avec C++
linktitle: Ajuster automatiquement la hauteur de la ligne lorsque le fichier est chargé
type: docs
weight: 120
url: /fr/cpp/autofit-row-height/
description: Apprenez comment ajuster la hauteur des lignes qui ne sont pas personnalisées en utilisant Aspose.Cells avec C++.
keywords: Ajuster automatiquement la hauteur de la ligne lors du chargement du fichier, ajuster automatiquement la hauteur de la ligne lors de l ouverture du fichier Excel.
---

## **Scénarios d'utilisation possibles**
La hauteur de la ligne correspond automatiquement à la police du contenu, mais lorsque la hauteur de la ligne mise en cache ne correspond pas à celle du contenu du fichier, MS Excel ajuste automatiquement la hauteur de la ligne lors du chargement du fichier, tandis qu'Aspose.Cells ne l'ajuste pas automatiquement pour améliorer la performance. Si vous souhaitez utiliser le programme Aspose.Cells pour faire correspondre automatiquement la hauteur des lignes lors du chargement des fichiers, vous pouvez atteindre cet objectif via le paramètre [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/).

Veuillez vous référer aux données d'image suivantes. Nous pouvons observer que la hauteur de la ligne mise en cache dans la ligne 11 est de 15, mais Excel a ajusté automatiquement la hauteur de la ligne lors du chargement du fichier.
<br>
<img src="1.png" width=70% />

## **Ajuster la hauteur de la ligne en utilisant Aspose.Cells**
Si vous chargez directement le fichier et le sauvegardez en PDF, les données ne seront pas entièrement affichées dans le PDF car sa hauteur de ligne mise en cache est seulement de 15.
<br>
<img src="2.png" width=70% />
<br>
Si vous définissez le paramètre [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) à vrai lors du chargement du fichier, alors Aspose.Cells ajustera automatiquement la hauteur des lignes. La hauteur ajustée peut efficacement répondre aux exigences d'affichage du texte.
<br>
<img src="3.png" width=70% />

## **Exemple de code C++**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
