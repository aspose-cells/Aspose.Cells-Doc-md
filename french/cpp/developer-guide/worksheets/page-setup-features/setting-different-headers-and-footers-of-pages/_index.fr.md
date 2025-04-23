---
title: Définir des en têtes et pieds de page différents pour différentes pages avec C++
linktitle: Définir des en têtes et pieds de page différents
type: docs
weight: 35
url: /fr/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Cet article fournit un code d exemple qui montre comment définir de manière programmatique divers en têtes et pieds de page des paramètres de mise en page de la feuille Excel en utilisant la bibliothèque et l API C++. Vous pouvez définir les en têtes et pieds de page pour la première page, les pages impaires et les pages paires.
keywords: définir l en tête et le pied de page Excel pour la première page c++, définir l en tête et le pied de page pour les pages impaires c++, définir l en tête et le pied de page pour les pages paires c++
---

{{% alert color="primary" %}}

MS Excel supporte la définition d'en-têtes et pieds de page différents pour la première page, les pages impaires et les pages paires depuis Excel 2007.
Aspose.Cells prend en charge la même fonctionnalité.

{{% /alert %}}

## **Définir des en-têtes et des pieds de page différents dans MS Excel**

**![Définir des en-têtes et des pieds de page différents](difpage.png)**

1. Cliquez sur **Mise en page > Titres d'impression > En-tête/Pied de page**.
1. Cochez **Pages impaires et paires différentes** ou **Première page différente**.
1. Entrez des en-têtes et pieds de page différents.

## **Définir des en-têtes et pieds de page différents avec Aspose.Cells**

Aspose.Cells se comporte de la même manière qu'Excel.
1. Définit les indicateurs [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) et [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) 
1. Entrez des en-têtes et pieds de page différents.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
