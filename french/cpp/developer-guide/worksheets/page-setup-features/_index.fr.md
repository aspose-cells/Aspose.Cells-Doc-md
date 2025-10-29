---
title: Fonctionnalités de mise en page avec C++
linktitle: Fonctionnalités de mise en page
type: docs
weight: 60
url: /fr/cpp/page-setup-features/
description: Apprenez à configurer les fonctionnalités de mise en page dans les fichiers Excel en utilisant Aspose.Cells avec C++.
---

## **Fonctionnalités de Configuration de Page**

Aspose.Cells offre un ensemble complet de fonctionnalités pour configurer les options de mise en page des fichiers Excel. Ces fonctionnalités vous permettent de contrôler divers aspects de la disposition de la page, tels que les marges, l'orientation, la taille du papier, et plus encore.

### **Paramétrage des marges de page**

Vous pouvez définir les marges de la page pour une feuille en utilisant la classe `PageSetup`. L'exemple suivant montre comment définir les marges en haut, en bas, à gauche et à droite :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageMargins() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set page margins
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetTopMargin(1.0);
    pageSetup.SetBottomMargin(1.0);
    pageSetup.SetLeftMargin(0.75);
    pageSetup.SetRightMargin(0.75);

    // Save the workbook
    workbook.Save("PageMargins.xlsx");
}
```

### **Définir l'orientation de la page**

Vous pouvez définir l'orientation de la page en portrait ou paysage en utilisant la classe `PageSetup`. L'exemple suivant montre comment définir l'orientation paysage :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageOrientation() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    workbook.Save("PageOrientation.xlsx");
}
```

### **Définir la taille du papier**

Vous pouvez définir la taille du papier pour l'impression en utilisant la classe `PageSetup`. L'exemple suivant montre comment définir la taille du papier à A4 :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPaperSize() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    workbook.Save("PaperSize.xlsx");
}
```

### **Définir la zone d'impression**

Vous pouvez définir une plage spécifique de cellules à imprimer en utilisant la classe `PageSetup`. L'exemple suivant montre comment définir la zone d'impression :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintArea() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea("A1:D10");

    // Save the workbook
    workbook.Save("PrintArea.xlsx");
}
```

### **Définir les sauts de page**

Vous pouvez insérer des sauts de page dans une feuille pour contrôler où les pages se terminent et commencent. L'exemple suivant montre comment insérer un saut de page horizontal :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageBreaks() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a horizontal page break at row 10
    worksheet.GetHorizontalPageBreaks().Add("A10");

    // Save the workbook
    workbook.Save("PageBreaks.xlsx");
}
```

### **Configuration de l'en-tête et du pied de page**

Vous pouvez personnaliser l'en-tête et le pied de page d'une feuille de calcul à l'aide de la classe `PageSetup`. L'exemple suivant montre comment définir un en-tête et un pied de page personnalisés :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetHeaderFooter() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set custom header and footer
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&CHeader Text");
    pageSetup.SetFooter(0, "&CFooter Text");

    // Save the workbook
    workbook.Save("HeaderFooter.xlsx");
}
```

### **Définir les titres d'impression**

Vous pouvez spécifier les lignes ou colonnes à répéter en haut ou à gauche de chaque page imprimée en utilisant la classe `PageSetup`. L'exemple suivant montre comment définir les titres d'impression :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintTitles() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print titles
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows("$1:$1");
    pageSetup.SetPrintTitleColumns("$A:$A");

    // Save the workbook
    workbook.Save("PrintTitles.xlsx");
}
```

### **Définir la qualité d'impression**

Vous pouvez définir la qualité d'impression pour une feuille de calcul à l'aide de la classe `PageSetup`. L'exemple suivant montre comment définir la qualité d'impression :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintQuality() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print quality
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintQuality(600);

    // Save the workbook
    workbook.Save("PrintQuality.xlsx");
}
```

### **Définir l'ordre d'impression**

Vous pouvez définir l'ordre d'impression pour une feuille de calcul à l'aide de la classe `PageSetup`. L'exemple suivant montre comment définir l'ordre d'impression sur "De haut en bas, puis de gauche à droite" :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintOrder() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrder(PrintOrderType::OverThenDown);
    workbook.Save("PrintOrder.xlsx");
}
```

### **Définir les lignes de la grille pour l'impression**

Vous pouvez contrôler si les lignes de la grille sont imprimées à l'aide de la classe `PageSetup`. L'exemple suivant montre comment activer l'impression des lignes de la grille :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of gridlines
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintGridlines(true);

    // Save the workbook
    workbook.Save("PrintGridlines.xlsx");
}
```

### **Définir les en-têtes d'impression**

Vous pouvez contrôler si les en-têtes de lignes et de colonnes sont imprimés à l'aide de la classe `PageSetup`. L'exemple suivant montre comment activer l'impression des en-têtes :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintHeadings() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of headings
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintHeadings(true);

    // Save the workbook
    workbook.Save("PrintHeadings.xlsx");
}
```

### **Définir l'impression en noir et blanc**

Vous pouvez contrôler si la feuille de calcul est imprimée en noir et blanc à l'aide de la classe `PageSetup`. L'exemple suivant montre comment activer l'impression en noir et blanc :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintBlackAndWhite() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable black and white printing
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetBlackAndWhite(true);

    // Save the workbook
    workbook.Save("PrintBlackAndWhite.xlsx");
}
```

### ** Configuration de l'impression en mode brouillon**

Vous pouvez contrôler si la feuille de calcul est imprimée en mode brouillon à l'aide de la classe `PageSetup`. L'exemple suivant montre comment activer l'impression en mode brouillon :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintDraft() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintDraft(true);
    workbook.Save("PrintDraft.xlsx");
}
```

### **Définir les commentaires d'impression**

Vous pouvez contrôler si les commentaires sont imprimés à l'aide de la classe `PageSetup`. L'exemple suivant montre comment activer l'impression des commentaires :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintComments() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);
    workbook.Save("PrintComments.xlsx");
}
```

### **Définir les erreurs d'impression**

Vous pouvez contrôler la manière dont les erreurs sont imprimées à l'aide de la classe `PageSetup`. L'exemple suivant montre comment définir l'option d'impression des erreurs :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintErrors() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsBlank);
    workbook.Save("PrintErrors.xlsx");
}
```

### **Ajuster la zone d'impression pour qu'elle tienne sur plusieurs pages**

Vous pouvez contrôler si la zone d'impression est mise à l'échelle pour s'adapter à un nombre spécifique de pages à l'aide de la classe `PageSetup`. L'exemple suivant montre comment définir la zone d'impression pour qu'elle tienne sur une page de largeur et une page de hauteur :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintAreaFitToPages() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area to fit to one page wide and one page tall
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the workbook
    workbook.Save("PrintAreaFitToPages.xlsx");
}
```

### **Définir l'échelle d'impression**

Vous pouvez définir l'échelle d'impression pour une feuille de calcul à l'aide de la classe `PageSetup`. L'exemple suivant montre comment définir l'échelle d'impression à 50% :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintScale() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print scale to 50%
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetZoom(50);

    // Save the workbook
    workbook.Save("PrintScale.xlsx");
}
```

### **Centrez horizontalement et verticalement l'impression**

Vous pouvez contrôler si la feuille de calcul est centrée horizontalement et verticalement sur la page imprimée à l'aide de la classe `PageSetup`. L'exemple suivant montre comment centrer horizontalement et verticalement la feuille :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintCenterHorizontallyAndVertically() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Center the worksheet horizontally and vertically
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the workbook
    workbook.Save("PrintCenterHorizontallyAndVertically.xlsx");
}
```

### **Définir le numéro de la première page à imprimer**

Vous pouvez définir le numéro de la première page pour l'impression à l'aide de la classe `PageSetup`. L'exemple suivant montre comment définir le numéro de la première page :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintFirstPageNumber() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the first page number
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save("PrintFirstPageNumber.xlsx");
}
```

### **Définir le numéro de la page à imprimer**

Vous pouvez contrôler si le numéro de page est imprimé à l'aide de la classe `PageSetup`. L'exemple suivant montre comment activer l'impression du numéro de page :

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPrintPageNumber() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&P");
    workbook.Save("PrintPageNumber.xlsx");
}
```

### **Paramètre de l'impression de l'ordre des pages**

Vous pouvez définir l'ordre dans lequel les pages sont imprimées en utilisant la classe `PageSetup`. L'exemple suivant montre comment définir l'ordre des pages sur "Descendre, puis Sur":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPageOrder() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the page order to "Down, then Over"
    PageSetup
{{< app/cells/assistant language="cpp" >}}
