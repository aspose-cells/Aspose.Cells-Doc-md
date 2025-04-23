---
title: Configuration des options d impression avec C++
linktitle: Réglage des options d impression
type: docs
weight: 40
url: /fr/cpp/setting-print-options/
description: Cet article montre comment définir de manière programmée les options d impression de la fonction de mise en page de la feuille Excel en utilisant l API et la bibliothèque C++. Vous pouvez définir la zone d impression, les titres d impression et l ordre des pages.
keywords: définir la zone d impression Excel c++, définir les titres d impression Excel c++, définir l ordre des pages Excel c++
---

{{% alert color="primary" %}}

Les paramètres de configuration de page de Microsoft Excel offrent plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul.

{{% /alert %}}

## **Réglage des options d'impression**

Ces options d'impression permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique sur une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

Aspose.Cells supporte toutes les options d'impression proposées par Microsoft Excel, et les développeurs peuvent configurer facilement ces options pour les feuilles en utilisant les propriétés offertes par la classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). La façon dont ces propriétés sont utilisées est expliquée ci-dessous en détail.

### **Définir la zone d'impression**

Par défaut, la zone d'impression intègre toutes les zones de la feuille de calcul contenant des données. Les développeurs peuvent établir une zone d'impression spécifique de la feuille de calcul.

Pour sélectionner une zone d'impression spécifique, utilisez la propriété [**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) de la classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Attribuez à cette propriété une plage de cellules définissant la zone d'impression.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Définir les titres d'impression**

Aspose.Cells vous permet de désigner les en-têtes de lignes et de colonnes à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez les propriétés [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) et [**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) de la classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/).

Les lignes ou colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

```c++
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Définir d'autres options d'impression**

La classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) fournit également plusieurs autres propriétés pour définir les options d'impression générales comme suit :

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/) : propriété booléenne qui définit si les lignes de la grille doivent être imprimées ou non.
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/) : une propriété booléenne qui définit l'impression ou non des en-têtes de lignes et de colonnes.
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/) : une propriété booléenne qui définit l'impression ou non de la feuille de calcul en mode noir et blanc.
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) : définit l'affichage des commentaires d'impression sur la feuille de calcul ou à la fin de la feuille de calcul.
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/) : propriété booléenne qui définit si la feuille doit être imprimée sans graphiques.
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) : définit si les erreurs de cellules sont affichées telles qu'elles sont, en vide, en tiret ou N/A.

Pour définir les propriétés [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) et [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/), Aspose.Cells fournit également deux énumérations, [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) et [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) qui contiennent des valeurs prédéfinies à attribuer respectivement aux propriétés [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) et [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/).

Les valeurs prédéfinies de l'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) sont répertoriées ci-dessous avec leurs descriptions.

|**Types de commentaires d'impression**|**Description**|
| :- | :- |
|PrintInPlace| Spécifie d'imprimer les commentaires tels qu'ils apparaissent sur la feuille de calcul.
|PrintNoComments| Spécifie de ne pas imprimer les commentaires.
|PrintSheetEnd| Spécifie d'imprimer les commentaires à la fin de la feuille de calcul.

Les valeurs prédéfinies de l'énumération [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) sont répertoriées ci-dessous avec leurs descriptions.

|**Types d'erreurs d'impression**|**Description**|
| :- | :- |
|PrintErrorsBlank|Indique de ne pas imprimer les erreurs.|
|PrintErrorsDash|Indique d'imprimer les erreurs sous forme de "--".|
|PrintErrorsDisplayed|Indique d'imprimer les erreurs telles qu'elles sont affichées.|
|PrintErrorsNA|Indique d'imprimer les erreurs sous forme de "#N/A".|

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Définir l'ordre des pages**

La classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) fournit la propriété [**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/) qui est utilisée pour ordonner l'impression de plusieurs pages de votre feuille de calcul. Il existe deux possibilités pour ordonner les pages comme suit.

- **En bas puis à droite :** imprime toutes les pages en bas avant d'imprimer les pages à droite.
- **À droite puis en bas :** imprime les pages de gauche à droite avant d'imprimer les pages en dessous.

Aspose.Cells fournit une énumération, [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) qui contient tous les types d'ordre prédéfinis.

Les valeurs prédéfinies de l'énumération [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) sont répertoriées ci-dessous.

|**Types d'ordre d'impression**|**Description**|
| :- | :- |
|DownThenOver|Représente l'ordre d'impression en bas puis à droite.|
|OverThenDown|Représente l'ordre d'impression à droite puis en bas.|

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
