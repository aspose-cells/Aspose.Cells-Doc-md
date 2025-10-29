---
title: Fusionner et dissocier des cellules avec C++
linktitle: Fusionner et séparer des cellules
description: Aspose.Cells est une bibliothèque C++ pour le travail avec des fichiers de tableur, qui supporte la fusion et la dissociation de cellules. Cet article présente comment fusionner et dissocier des cellules en utilisant la bibliothèque Aspose.Cells, ainsi que la personnalisation du style des cellules fusionnées.
keywords: Aspose.Cells, bibliothèque C++, tableur, fusionner cellules, dissocier cellules, paramètres de style, styles personnalisés
type: docs
weight: 190
url: /fr/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge cette fonctionnalité et peut également fusionner des cellules dans une feuille de calcul. Vous pouvez également séparer, ou diviser, les cellules fusionnées. La référence de cellule d'une cellule fusionnée est la référence de la cellule en haut à gauche de la plage sélectionnée d'origine.

{{% /alert %}} 

## **Introduction**
Vous ne souhaitez pas toujours le même nombre de cellules dans chaque ligne ou colonne. Par exemple, vous pouvez vouloir mettre un titre dans une cellule qui s'étend sur plusieurs colonnes. Ou, si vous créez une facture, vous souhaitez peut-être moins de colonnes pour le total. Pour fusionner deux cellules ou plus en une seule cellule, utilisez la fusion. Microsoft Excel permet aux utilisateurs de sélectionner des fichiers et de les fusionner pour structurer le tableur à leur convenance.

{{% alert color="primary" %}} 

Remarquez que lorsque des cellules sont fusionnées, seules les données de la cellule en haut à gauche sont conservées. Si des données se trouvent dans les autres cellules de la plage, ces données sont supprimées.
De même, la mise en forme repose sur la cellule de référence de sorte que lorsque vous fusionnez des cellules, les paramètres de mise en forme de la cellule en haut à gauche de la plage sont appliqués sur la cellule fusionnée. Lorsque la cellule est scindée, les nouvelles cellules conservent leurs paramètres de mise en forme d'origine.

{{% /alert %}} 

## **Fusion de cellules dans une feuille de calcul**
### **Fusionner des cellules dans Microsoft Excel**
Les étapes suivantes décrivent comment fusionner des cellules dans la feuille de calcul à l'aide de MS Excel.

1. Copiez les données que vous souhaitez dans la cellule en haut à gauche dans la plage.
1. Sélectionnez les cellules que vous souhaitez fusionner.
1. Pour fusionner des cellules dans une ligne ou une colonne et centrer le contenu de la cellule, cliquez sur l'icône **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

### **Fusion de cellules avec Aspose.Cells**
La classe `Aspose::Cells::Cells` possède des méthodes utiles pour cette tâche. Par exemple, la méthode `Merge()` fusionne les cellules en une seule dans une plage spécifiée.

L'exemple suivant montre comment fusionner des cellules (C6:E7) dans une feuille de calcul.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Dissocier (diviser) les cellules fusionnées**
### **Utilisation de Microsoft Excel**
Les étapes suivantes décrivent comment diviser les cellules fusionnées à l'aide de Microsoft Excel.

1. Sélectionnez la cellule fusionnée.
   Lorsque les cellules ont été combinées, **Fusionner et centrer** est sélectionné dans la barre d'outils **Mise en forme**.
1. Cliquez sur **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

### **Utilisation d'Aspose.Cells**
La classe `Aspose::Cells::Cells` possède une méthode appelée `UnMerge()` qui divise les cellules dans leur état d'origine. La méthode dissocie les cellules en utilisant la référence de la cellule dans la plage fusionnée.

L'exemple suivant montre comment diviser les cellules fusionnées (C6). L'exemple utilise le fichier créé dans l'exemple précédent et divise les cellules fusionnées.

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
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Détecter les cellules fusionnées dans une feuille de calcul](/cells/fr/cpp/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="cpp" >}}
