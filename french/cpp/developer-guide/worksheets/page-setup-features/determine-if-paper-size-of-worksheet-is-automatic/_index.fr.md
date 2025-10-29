---
title: Déterminer si la taille du papier de la feuille est automatique avec C++
linktitle: Déterminer si la taille du papier de la feuille de calcul est automatique
type: docs
weight: 90
url: /fr/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Cet article explique comment utiliser l API ou la bibliothèque C++ pour déterminer si la taille du papier d une feuille est automatique de manière programmatique.
keywords: déterminer si la taille du papier de la feuille est automatique en C++
---

## **Scénarios d'utilisation possibles**

La plupart du temps, la taille du papier de la feuille est automatique. Lorsqu'elle l'est, elle est souvent réglée sur *Lettre*. Parfois, l'utilisateur configure la taille du papier selon ses besoins. Dans ce cas, la taille du papier n'est pas automatique. Vous pouvez vérifier si la taille du papier de la feuille est automatique ou non en utilisant la propriété [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/) de la classe **Worksheet**.

## **Déterminer si la taille du papier de la feuille de calcul est automatique**

Le code d'exemple ci-dessous charge les deux fichiers Excel suivants

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

et vérifie si la taille du papier de leur première feuille est automatique ou non. Dans Microsoft Excel, vous pouvez vérifier si la taille du papier est automatique ou non via la fenêtre Mise en page comme montré dans cette capture d'écran.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

Voici la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec les fichiers Excel d'exemple donnés.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
