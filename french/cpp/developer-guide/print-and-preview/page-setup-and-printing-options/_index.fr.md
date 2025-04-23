---
title: Configuration de la mise en page et options d impression avec C++
linktitle: Configuration de la mise en page et des options d impression
type: docs
weight: 60
url: /fr/cpp/page-setup-and-printing-options/
description: Configurer les paramètres de mise en page et d impression pour contrôler le processus d impression en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, les développeurs doivent configurer la mise en page et les paramètres d'impression pour contrôler le processus d'impression. Les paramètres de mise en page et d'impression offrent diverses options et sont entièrement pris en charge dans Aspose.Cells.

Cet article montre comment créer une application console dans Visual Studio, et appliquer la mise en page et les options d'impression à une feuille de calcul avec quelques lignes de code simples utilisant l'API Aspose.Cells.

{{% /alert %}}

## **Travailler avec la mise en page et les paramètres d'impression**

Pour cet exemple, nous avons créé un classeur dans Microsoft Excel et utilisons Aspose.Cells pour définir la mise en page et les options d'impression.

### **Utilisation d'Aspose.Cells pour définir les options de mise en page**

Créez d'abord une feuille de calcul simple dans Microsoft Excel. Ensuite, appliquez des options de mise en page. L'exécution du code modifie les options de mise en page comme dans la capture d'écran ci-dessous.

| **Fichier de sortie.** |
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Créez une feuille de calcul avec des données dans Microsoft Excel:
   1. Ouvrir un nouveau classeur dans Microsoft Excel.
   1. Ajoutez des données.
1. Définir les options de mise en page :
   Appliquer les options de mise en page au fichier. Ci-dessous se trouve une capture d'écran des options par défaut, avant l'application des nouvelles options.

| **Options de mise en page par défaut.** |
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++.
   1. Installez-le sur votre ordinateur de développement.
      Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.
1. Créer un projet :
   1. Démarrer Visual Studio.
   1. Créez une nouvelle application console.
      Cet exemple montrera une application console en C++.
1. Ajouter des références:
   1. Cet exemple utilise Aspose.Cells, donc ajoutez une référence à ce composant dans le projet. Par exemple :
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Écrivez l'application qui invoque l'API :

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"CustomerReport.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting the orientation to Portrait
    worksheet.GetPageSetup().SetOrientation(PageOrientationType::Portrait);

    // Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Setting the paper size to A4
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Setting the print quality of the worksheet to 1200 dpi
    worksheet.GetPageSetup().SetPrintQuality(1200);

    // Setting the first page number of the worksheet pages
    worksheet.GetPageSetup().SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Paramétrage des options d'impression**

Les paramètres de mise en page fournissent également plusieurs options d'impression (appelées également options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul. Ils permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique d'une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

L'exemple qui suit applique des options d'impression au fichier créé dans l'exemple ci-dessus (PageSetup.xls). La capture d'écran ci-dessous montre les options d'impression par défaut avant l'application de nouvelles options.

|**Document d'entrée**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
L'exécution du code modifie les options d'impression.

|**Fichier de sortie**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"PageSetup.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_Print_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get PageSetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specifying the cells range (from A1 cell to E30 cell) of the print area
    pageSetup.SetPrintArea(u"A1:E30");

    // Defining column numbers A & E as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$E");

    // Defining row numbers 1 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Allowing to print gridlines
    pageSetup.SetPrintGridlines(true);

    // Allowing to print row/column headings
    pageSetup.SetPrintHeadings(true);

    // Allowing to print worksheet in black & white mode
    pageSetup.SetBlackAndWhite(true);

    // Allowing to print comments as displayed on worksheet
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);

    // Allowing to print worksheet with draft quality
    pageSetup.SetPrintDraft(true);

    // Allowing to print cell errors as N/A
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);

    // Setting the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
