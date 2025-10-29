---
title: Cacher l affichage des valeurs zéro dans la feuille avec C++
linktitle: Masquer l affichage des valeurs zéro dans la feuille de calcul
type: docs
weight: 50
url: /fr/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Cet article vous montrera du code d exemple expliquant comment masquer de manière programmatique les valeurs zéro dans une feuille Excel en utilisant la bibliothèque ou API C++.
keywords: cacher les valeurs zéro de la feuille Excel en C++
---

{{% alert color="primary" %}} 

Parfois, vous devez masquer les valeurs zéro dans une feuille de calcul. Cela peut être une préférence personnelle ou une norme de formatage.

{{% /alert %}} 

Pour masquer les valeurs zéro dans une feuille de calcul dans Microsoft Excel (par exemple Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**, puis sélectionnez l'onglet **Affichage**.
1. Désélectionnez l'option **Zéro**.
1. Cliquez sur **OK**.

Veuillez consulter le code d'exemple suivant qui démontre comment masquer les zéros à l'aide d'Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
