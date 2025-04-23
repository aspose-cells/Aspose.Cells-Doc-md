---
title: Paramètres de protection avancés depuis Excel XP avec C++
linktitle: Paramètres de protection avancée depuis Excel XP
type: docs
weight: 30
url: /fr/cpp/advanced-protection-settings-since-excel-xp/
description: Apprenez comment appliquer des paramètres de protection avancés dans des fichiers Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Depuis la publication d'Excel 2002 ou XP, Microsoft a ajouté de nombreux paramètres de protection avancés.

{{% /alert %}}

## **Introduction**

Ces paramètres de protection restreignent ou permettent aux utilisateurs de:

- Supprimer des lignes ou des colonnes.
- Modifier le contenu, les objets ou les scénarios.
- Formater les cellules, lignes ou colonnes.
- Insérer des lignes, colonnes ou hyperliens.
- Sélectionner des cellules verrouillées ou déverrouillées.
- Utiliser des tableaux croisés dynamiques et bien plus encore.

Aspose.Cells prend en charge tous les paramètres de protection avancés offerts par Excel XP ou les versions ultérieures.

### **Paramètres de protection avancés utilisant Excel XP et les versions ultérieures**

Pour afficher les paramètres de protection disponibles dans Excel XP :

1. Dans le menu **Outils**, sélectionnez **Protection** puis **Protéger la feuille**. Une boîte de dialogue s'affiche.

Pour voir les paramètres de protection disponibles dans Excel 2016 :

1. Dans le menu **Fichier**, sélectionnez **Protéger le classeur** puis **Protéger la feuille en cours**.
1. Sélectionnez **Protéger la feuille** dans le menu **Révision**.

Les étapes mentionnées ci-dessus afficheront une boîte de dialogue où vous pourrez autoriser ou restreindre les fonctionnalités de la feuille de calcul ou appliquer un mot de passe à la feuille.

### **Paramètres de protection avancés utilisant Aspose.Cells**

Aspose.Cells prend en charge tous les paramètres de protection avancés.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit la propriété [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) utilisée pour appliquer ces paramètres de protection avancés. La propriété [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) est en fait un objet de la classe [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) qui encapsule plusieurs propriétés booléennes pour désactiver ou activer les restrictions.

Voici un petit exemple d'application. Il ouvre un fichier Excel et utilise la plupart des paramètres de protection avancés pris en charge par Excel XP et les versions ultérieures.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

Veuillez ne pas appeler la méthode [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) lors de l'utilisation de la propriété [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/). Enregistrez également le fichier au format Excel97To2003 ou Xlsx car les paramètres de protection avancée ne sont pris en charge que par Excel XP et versions ultérieures.

{{% /alert %}}

### **Problème de verrouillage de cellules**

Si vous souhaitez restreindre la modification des cellules par les utilisateurs, celles-ci doivent être verrouillées avant l'application des paramètres de protection. Sinon, les cellules peuvent être modifiées même si la feuille est protégée. Dans Microsoft Excel XP, les cellules peuvent être verrouillées via la boîte de dialogue suivante :

|**Boîte de dialogue pour verrouiller les cellules dans Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Il est également possible de verrouiller des cellules en utilisant l'API Aspose.Cells. Chaque cellule peut recevoir un format [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contenant une propriété booléenne [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Définissez la propriété [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) sur **true** ou **false** pour verrouiller ou déverrouiller la cellule.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
