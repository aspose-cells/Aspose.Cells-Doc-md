---
title: Définir les formats conditionnels des fichiers Excel et ODS avec C++
linktitle: Formats conditionnels
type: docs
weight: 60
url: /fr/cpp/conditional-formatting/
description: Comment appliquer des formats conditionnels aux fichiers Excel et ODS en C++.
keywords: appliquer des formats conditionnels 
---

## **Introduction**

La mise en forme conditionnelle est une fonctionnalité avancée de Microsoft Excel qui vous permet d'appliquer des formats à une cellule ou à une plage de cellules et de faire en sorte que la mise en forme change en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, une cellule peut apparaître en gras uniquement lorsque sa valeur est supérieure à 500. Lorsque la valeur de la cellule satisfait la condition, le format spécifié est appliqué à la cellule. Si la valeur de la cellule ne satisfait pas la condition de format, la mise en forme par défaut de la cellule est utilisée. Dans Microsoft Excel, sélectionnez **Format**, puis **Mise en forme conditionnelle** pour ouvrir la boîte de dialogue Mise en forme conditionnelle.

Aspose.Cells prend en charge l'application de la mise en forme conditionnelle aux cellules à l'exécution. Cet article explique comment procéder. Il explique également comment calculer la couleur utilisée par Excel pour la mise en forme conditionnelle de l'échelle de couleurs.

## **Application de la mise en forme conditionnelle**

Aspose.Cells prend en charge la mise en forme conditionnelle de plusieurs manières :

- Utilisation de la feuille de calcul du concepteur
- Utilisation de la méthode de copie.
- Création de la mise en forme conditionnelle à l'exécution.

### **Utilisation de la feuille de calcul du concepteur**

Les développeurs peuvent créer une feuille de calcul du concepteur contenant une mise en forme conditionnelle dans Microsoft Excel, puis ouvrir cette feuille de calcul avec Aspose.Cells. Aspose.Cells charge et enregistre la feuille de calcul du concepteur en conservant tous les paramètres de mise en forme conditionnelle.

### **Utilisation de la méthode de copie**

Aspose.Cells permet aux développeurs de copier les paramètres de mise en forme conditionnelle d'une cellule à une autre dans la feuille de calcul en appelant la méthode [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/).

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int totalRowCount = 0;

    // Iterate through all worksheets in the workbook
    for (int i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        Worksheet sourceSheet = workbook.GetWorksheets().Get(i);

        // Get the maximum display range of the source sheet
        Range sourceRange = sourceSheet.GetCells().GetMaxDisplayRange();

        // Create a destination range in the first worksheet
        Range destRange = worksheet.GetCells().CreateRange(
            sourceRange.GetFirstRow() + totalRowCount, 
            sourceRange.GetFirstColumn(),
            sourceRange.GetRowCount(), 
            sourceRange.GetColumnCount());

        // Copy data from source range to destination range
        destRange.Copy(sourceRange);

        // Update the total row count
        totalRowCount += sourceRange.GetRowCount();
    }

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Application de la mise en forme conditionnelle à l'exécution**

Aspose.Cells vous permet d'ajouter et de supprimer la mise en forme conditionnelle à l'exécution. Les exemples de code ci-dessous montrent comment définir la mise en forme conditionnelle :

1. Instancier un classeur.
1. Ajouter une mise en forme conditionnelle vide.
1. Définir la plage à laquelle la mise en forme doit s'appliquer.
1. Définir les conditions de formatage.
1. Enregistrez le fichier.

Après cet exemple, voici un certain nombre d'autres exemples plus petits qui montrent comment appliquer les paramètres de la police, les paramètres des bordures et les motifs.

Microsoft Excel 2007 a ajouté une mise en forme conditionnelle plus avancée que Aspose.Cells prend également en charge. Les exemples ici illustrent comment utiliser la mise en forme simple, les exemples de Microsoft Excel 2007 montrent comment appliquer une mise en forme conditionnelle plus avancée.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Instantiating a Workbook object
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range.
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;
    fcs.AddArea(ca);

    ca = CellArea();
    ca.StartRow = 1;
    ca.EndRow = 1;
    ca.StartColumn = 1;
    ca.EndColumn = 1;
    fcs.AddArea(ca);

    // Adds condition.
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"=A2", u"100");

    // Adds condition.
    int conditionIndex2 = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Sets the background color.
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Définir la police**

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Vous ne pouvez changer que le style de police, la couleur du texte, le style de soulignement et le style de barré.

{{% /alert %}}

### **Définir la bordure**

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
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Set the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Add condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Set the background color
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Dashed);

    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetColor(Color{255, 255, 0, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Vous ne pouvez utiliser que des styles de ligne fine pour la bordure de contour. Les lignes diagonales ne sont pas autorisées.

{{% /alert %}}

### **Définir le motif**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetPattern(BackgroundType::ReverseDiagonalStripe);
    fc.GetStyle().SetForegroundColor(Color{255, 255, 0, 255});
    fc.GetStyle().SetBackgroundColor(Color{0, 255, 255, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sujets avancés**
- [Ajout de mises en forme conditionnelles à 2 couleurs et à 3 couleurs](/cells/fr/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Appliquer une mise en forme conditionnelle avancée](/cells/fr/cpp/apply-advanced-conditional-formatting/)
- [Appliquer une mise en forme conditionnelle dans les feuilles de calcul](/cells/fr/cpp/apply-conditional-formatting-in-worksheets/)
- [Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle](/cells/fr/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Générer des images de barres de données pour la mise en forme conditionnelle](/cells/fr/cpp/generate-conditional-formatting-databars-images/)
- [Obtenir des ensembles d'icônes, des barres de données ou des objets de couleurs utilisés dans la mise en forme conditionnelle](/cells/fr/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
{{< app/cells/assistant language="cpp" >}}
