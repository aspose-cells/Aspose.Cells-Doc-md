---
title: Obtenir la largeur et la hauteur du papier de la mise en page de la feuille avec C++
linktitle: Obtenir la largeur et la hauteur du papier de la mise en page
type: docs
weight: 50
url: /fr/cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Apprenez comment obtenir la largeur et la hauteur du papier de la mise en page de la feuille Excel de manière programmatique en utilisant le code C++ avec l API Aspose.Cells for C++.
keywords: largeur du papier de la mise en page Excel en C++, hauteur du papier de la mise en page Excel en C++
---

## **Scénarios d'utilisation possibles**

Parfois, vous avez besoin de connaître la largeur et la hauteur de la taille du papier telle qu'elle a été définie dans la mise en page de la feuille. Veuillez utiliser les méthodes [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) et [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/) à cette fin.

## **Obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul**

Le code d'exemple suivant explique l'utilisation des méthodes [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) et [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/). Il modifie d'abord la taille du papier en *A2* puis trouve la largeur et la hauteur du papier, puis il change en *A3*, *A4*, *Lettre* et trouve respectivement la largeur et la hauteur du papier.

### **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook class
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set paper size to A2 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA2);
    cout << "PaperA2: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A3 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);
    cout << "PaperA3: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A4 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);
    cout << "PaperA4: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to Letter and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperLetter);
    cout << "PaperLetter: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
