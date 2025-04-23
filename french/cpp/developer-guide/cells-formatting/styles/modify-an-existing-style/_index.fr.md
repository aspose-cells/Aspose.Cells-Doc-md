---
title: Modifier un style existant avec C++
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de tableurs permettant aux utilisateurs de modifier les styles de cellules existants. Cet article explique comment modifier un style de cellule existant avec la bibliothèque Aspose.Cells pour que les utilisateurs puissent changer l’apparence des cellules selon leurs besoins.
keywords: Modifier les styles existants, personnaliser l apparence de votre application, guides, tutoriels, documentation d aide, documentation de développement, références API, code d exemple, téléchargements, support.
type: docs
weight: 90
url: /fr/cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Pour appliquer les mêmes options de formatage aux cellules, créez un nouvel objet de style de formatage. Un objet de style de formatage est une combinaison de caractéristiques de formatage, telles que la police, la taille de police, l'indentation, le nombre, la bordure, les motifs, etc., nommés et stockés en tant qu'ensemble. Lorsqu'ils sont appliqués, tous les formatages de ce style sont appliqués.

Vous pouvez également utiliser un style existant, le sauvegarder avec le classeur et l'utiliser pour formater des informations avec les mêmes attributs.

Lorsque les cellules ne sont pas explicitement formatées, le style **Normal** (le style par défaut du classeur) est appliqué. Microsoft Excel prédéfinit plusieurs styles en plus du style Normal, y compris Virgule, Monétaire et Pourcentage.

Aspose.Cells permet de modifier n'importe lequel de ces styles ou tout autre style que vous définissez avec les attributs souhaités.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour mettre à jour un style dans Microsoft Excel 97-2003 :

1. Sur le menu **Format**, cliquez sur **Style**.
1. Sélectionnez le style que vous souhaitez modifier dans la liste **Nom du style**.
1. Cliquez sur **Modifier**.
1. Sélectionnez les options de style que vous souhaitez en utilisant les onglets dans la boîte de dialogue Format de cellule.
1. Cliquez sur **OK**.
1. Sous **Le style inclut**, spécifiez les fonctionnalités de style que vous souhaitez.
1. Cliquez sur **OK** pour enregistrer le style et l'appliquer à la plage sélectionnée.

## **Utilisation d'Aspose.Cells**

 Les exemples suivants montrent comment utiliser la méthode [**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/).

### **Créer et modifier un style**

Cet exemple crée un objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/), l’applique à une plage de cellules et modifie l’objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Les modifications sont automatiquement appliquées à la cellule et à la plage à laquelle le style a été appliqué.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red color.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize styleflag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // The change would be reflected (new modification is implemented) to cell (A1) and range (B1:D1).
    style.Update();

    // Save the excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Modification d'un style existant**

Cet exemple utilise un fichier Excel de modèle simple dans lequel un style appelé Pourcentage a déjà été appliqué à une plage. L'exemple :

1. obtient le style,
1. crée un objet de style et
1. modifie le format du style.

Les modifications sont automatiquement appliquées à la plage à laquelle le style a été appliqué.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file. 
     * In the book1.xlsx file, we have applied Ms Excel's 
     * Named style i.e., "Percent" to the range "A1:C8".
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style. so, the style of range "A1:C8" will be changed too.
    style.Update();

    // Save the excel file.	
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
