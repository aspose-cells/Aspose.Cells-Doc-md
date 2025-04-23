---
title: Copier les paramètres de mise en page d une feuille source vers une feuille de destination avec C++
linktitle: Copier les paramètres de mise en page
type: docs
weight: 80
url: /fr/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Cet article explique comment utiliser l API ou la bibliothèque C++ pour copier les paramètres de mise en page d une feuille source vers une feuille de destination de manière programmatique.
keywords: copier les paramètres de mise en page en C++, copier les paramètres de mise en page vers la feuille cible en C++
---

## **Scénarios d'utilisation possibles**

Lorsque vous ajoutez une nouvelle feuille à un classeur, elle contient les paramètres par défaut de *configuration de la page*. Il peut arriver que vous ayez besoin de transférer les paramètres ([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)) d'une feuille à une autre. Ce document explique comment copier les paramètres de configuration de la page d'une feuille à une autre à l'aide des API Aspose.Cells.

## **Copier les paramètres de configuration de la page de la feuille source dans la feuille de destination**

Le code d'exemple suivant illustre comment copier les *paramètres de configuration de la page* d'une feuille à une autre en utilisant la méthode [**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/). Veuillez consulter le code d'exemple suivant et sa sortie console pour référence.

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie console**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
