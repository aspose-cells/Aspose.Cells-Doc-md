---
title: Comment imprimer Excel en pages ajustées en largeur et en hauteur avec C++
linktitle: Comment imprimer Excel en pages adaptées en largeur et en hauteur
type: docs
weight: 200
url: /fr/cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Cet article vous montre un code expliquant comment définir FitToPagesLarge et FitToPagesHaut en utilisant la bibliothèque Aspose.Cells avec C++.
keywords: C++ Comment définir FitToPagesLarge et FitToPagesHaut, comment ajouter FitToPagesLarge et FitToPagesHaut en C++, comment définir FitToPagesLarge et FitToPagesHaut dans Excel, comment effacer FitToPagesLarge et FitToPagesHaut dans Excel, comment imprimer Excel en pages ajustées en largeur et en hauteur, comment imprimer une feuille en une page, comment imprimer toutes les colonnes d une feuille en une seule page.
---

## **Introduction**

Les réglages FitToPagesWide et FitToPagesTall sont utilisés dans les applications de tableur (comme Microsoft Excel) pour contrôler la mise à l'échelle d'une feuille lors de l'impression. Ces réglages aident à s'assurer que votre sortie imprimée rentre dans un nombre spécifié de pages, horizontalement et verticalement. Voici une explication de chaque réglage :

1. FitToPagesWide : Ce réglage spécifie le nombre de pages en largeur dans lesquelles le contenu imprimé doit tenir. Par exemple, définir FitToPagesWide à 1 signifie que le contenu sera mis à l'échelle pour tenir dans une seule largeur de page, peu importe la largeur de la feuille.
1. FitToPagesTall : Ce réglage spécifie le nombre de pages en hauteur dans lesquelles le contenu imprimé doit tenir. Par exemple, définir FitToPagesTall à 1 signifie que le contenu sera mis à l'échelle pour tenir dans une seule hauteur de page, indépendamment du nombre de lignes.

## **Pourquoi utiliser FitToPagesWide et FitToPagesTall**
Voici quelques raisons de définir FitToPagesWide et FitToPagesTall :
1. Contrôle de la mise en page imprimée : En spécifiant le nombre de pages en largeur et en hauteur, vous pouvez vous assurer que votre document imprimé est facile à lire et bien organisé, sans que des colonnes ou lignes soient mal réparties sur plusieurs pages.
1. Cohérence : Si vous imprimez plusieurs feuilles ou rapports, l'utilisation de ces réglages aide à maintenir un format cohérent, facilitant la comparaison et l'analyse des documents imprimés.
1. Présentation professionnelle : La mise à l'échelle et l'ajustement du contenu dans un nombre spécifié de pages peuvent donner une présentation plus professionnelle et soignée de vos données.

## **Comment imprimer un fichier en pages adaptées en largeur et en hauteur dans Excel**

Pour définir les paramètres FitToPagesWide et FitToPagesTall dans Microsoft Excel, suivez ces étapes :

1. Ouvrez votre classeur Excel et allez à la feuille que vous souhaitez imprimer.
1. Allez à l'onglet Mise en page dans le ruban.
1. Dans le groupe Mise en page, cliquez sur la petite flèche en bas à droite pour ouvrir la boîte de dialogue Mise en page.
1. Dans la boîte de dialogue Mise en page, allez à l'onglet Page.
1. Sous Échelle, sélectionnez l'option "Adapter à" puis indiquez le nombre de pages en largeur et en hauteur que vous souhaitez : Entrez le nombre de pages en largeur dans la première case (Adapter à x pages de large). Entrez le nombre de pages en hauteur dans la seconde case (Adapter à y pages de haut).
<br>
<img src="2.png" width=60% />

1. Cliquez sur OK pour appliquer les paramètres.

## **Comment imprimer Excel en pages adaptées en largeur et en hauteur en utilisant Aspose.Cells**

Pour définir FitToPagesLarge et FitToPagesHaut dans une feuille de calcul spécifiée : Tout d'abord, chargez le [fichier exemple](input.xlsx), puis vous devez modifier les propriétés [**Worksheet.GetFitToPagesTall()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopagestall/) et [**Worksheet.GetFitToPagesWide()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopageswide/) de l'objet [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) pour la feuille souhaitée. Voici un exemple en C++ :

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(U16String(u"input.xlsx"));

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Set the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Save the workbook
    workbook.Save(U16String(u"out_net.pdf"));

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Le résultat en sortie :
<br>
<img src="1.png" width=60% />

## **Comment imprimer une feuille de calcul en une seule page en utilisant Aspose.Cells**

Pour imprimer une feuille de calcul en une seule page : Tout d'abord, chargez le [fichier exemple](sample.xlsx), puis vous devez définir la propriété [**PdfSaveOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getonepagepersheet/) de l'objet [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/). Voici un exemple en C++ :

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions object
    PdfSaveOptions options;

    // Set options for exporting PDF
    options.SetOnePagePerSheet(true);

    // Save the workbook to a PDF file
    workbook.Save(u"OnePagePerSheet.pdf", options);

    std::cout << "Workbook saved as OnePagePerSheet.pdf!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Le résultat en sortie :
<br>
<img src="3.png" width=60% />

## **Comment imprimer toutes les colonnes d'une feuille de calcul en une seule page en utilisant Aspose.Cells**

Pour imprimer toutes les colonnes de la feuille de calcul en une seule page : Tout d'abord, chargez le [fichier exemple](sample.xlsx), puis vous devez définir la propriété [**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getallcolumnsinonepagepersheet/) de l'objet [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/). Voici un exemple en C++ :

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object with the specified file.
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions instance.
    PdfSaveOptions options;

    // Set options for saving the workbook as a PDF.
    options.SetAllColumnsInOnePagePerSheet(true);

    // Save the workbook as a PDF file with the specified options.
    workbook.Save(u"AllColumnsInOnePagePerSheet.pdf", options);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Le résultat en sortie :
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="cpp" >}}
