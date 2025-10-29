---
title: Paramètres d’alignement avec C++
linktitle: Paramètres d alignement
description: Dans la bibliothèque Aspose.Cells, vous pouvez utiliser les paramètres d alignement des cellules pour ajuster la mise en page et l affichage du texte. En ajustant des paramètres tels que l alignement horizontal, l alignement vertical et le retour à la ligne du texte, vous avez un contrôle accru sur la façon dont le texte circule dans les cellules. Ce document vous fournira des étapes détaillées et un code d exemple pour vous aider à comprendre rapidement comment utiliser Aspose.Cells pour les paramètres d alignement des cellules.
keywords: Aspose.Cells, alignement des cellules, alignement horizontal, alignement vertical, retour à la ligne
type: docs
weight: 20
url: /fr/cpp/cells-alignment-settings/
---

## **Configuration des paramètres d'alignement**

### **Paramètres d'alignement dans Microsoft Excel**

Toute personne ayant utilisé Microsoft Excel pour formater des cellules sera familière avec les paramètres d'alignement dans Microsoft Excel.

Comme vous pouvez le voir sur la figure ci-dessus, il existe différents types d'options d'alignement :

- Alignement du texte (horizontal et vertical)
- Retrait.
- Orientation.
- Contrôle du texte.
- Direction du texte.

Tous ces paramètres d'alignement sont entièrement pris en charge par Aspose.Cells et sont discutés plus en détail ci-dessous.

### **Paramètres d'alignement dans Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Chaque élément de la collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fournit les méthodes [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) et [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) pour la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) qui sont utilisées pour obtenir et définir le formatage d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fournit des propriétés utiles pour configurer les paramètres d'alignement.

Sélectionnez n'importe quel type d'alignement de texte en utilisant l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/). Les types d'alignement de texte prédéfinis dans l'énumération [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) sont:

|**Types d'alignement de texte**|**Description**|
| :- | :- |
|Bottom|Représente un alignement de texte en bas|
|Center|Représente un alignement de texte au centre|
|CenterAcross|Représente un alignement de texte centré sur plusieurs cellules|
|Distributed|Représente un alignement de texte distribué|
|Fill|Représente un alignement de texte en remplissage|
|General|Représente un alignement de texte général|
|Justify|Représente un alignement de texte justifié|
|Left|Représente un alignement de texte à gauche|
|Right|Représente un alignement de texte à droite|
|Top|Représente un alignement de texte en haut|
|JustifiedLow|Aligne le texte avec une longueur de kashida ajustée pour le texte arabe.|
|ThaiDistributed|Distribue le texte thaïlandais en particulier, car chaque caractère est traité comme un mot.|

{{% alert color="primary" %}}

Vous pouvez également appliquer le paramètre de justifier distribué en utilisant la propriété [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/).

{{% /alert %}}

#### **Alignement horizontal**

Utilisez la propriété [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) pour aligner le texte horizontalement.

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

    // Create workbook
    Workbook workbook;

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Alignement vertical**

Tout comme l'alignement horizontal, utilisez la propriété [**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) pour aligner le texte verticalement.

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

    // Create workbook
    Workbook workbook;

    // Clearing all the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Setting the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment of the text in a cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Indentation**

Il est possible de définir le niveau d'indentation du texte dans une cellule avec la propriété [**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

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

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the indentation level
    style.SetIndentLevel(2);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Orientation**

Définissez l'orientation (rotation) du texte dans une cellule avec la propriété [**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

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

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the rotation angle of the text to 25 degrees
    style.SetRotationAngle(25);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook in Excel 97-2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Contrôle du texte**

La section suivante aborde comment contrôler le texte en définissant le retour à la ligne, le rétrécissement pour s'adapter et d'autres options de mise en forme.

##### **Retour à la ligne du texte**

Le retour à la ligne du texte dans une cellule facilite sa lecture : la hauteur de la cellule s'adapte pour contenir tout le texte, au lieu de le couper ou de le faire déborder dans les cellules adjacentes. Définissez le retour à la ligne sur ou hors avec la propriété [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

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

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 36);

    // Add Text to the First Cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Rétrécissement pour s'adapter**

Une option pour le retour à la ligne du texte dans un champ est de rétrécir la taille du texte pour s'adapter aux dimensions d'une cellule. Cela se fait en définissant la propriété [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) sur **true**.

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

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set shrink to fit
    style.SetShrinkToFit(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Fusion de cellules**

Comme Microsoft Excel, Aspose.Cells prend en charge la fusion de plusieurs cellules en une seule. Aspose.Cells propose deux approches à cette tâche. Une façon est d'appeler la méthode [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) de la collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). La méthode [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) prend les paramètres suivants pour fusionner les cellules :

- Première rangée : la première rangée à partir de laquelle commencer la fusion.
- Première colonne : la première colonne à partir de laquelle commencer la fusion.
- Nombre de rangées : le nombre de rangées à fusionner.
- Nombre de colonnes : le nombre de colonnes à fusionner.

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

L'autre façon consiste à appeler d'abord la méthode [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) de la [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection pour créer une plage de cellules à fusionner. La méthode [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) prend le même ensemble de paramètres que la méthode [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) discutée ci-dessus et renvoie un objet [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). L'objet [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) fournit également une méthode [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) qui fusionne la plage spécifiée dans l'objet [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

##### **Direction du texte**

Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

L'ordre de lecture est défini avec la propriété [**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/) de l'objet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Aspose.Cells fournit des types de direction de texte prédéfinis dans l'énumération [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/).

|**Types de direction du texte**|**Description**|
| :- | :- |
|Context|L'ordre de lecture en accord avec la langue du premier caractère saisi|
|LeftToRight|Ordre de lecture de gauche à droite|
|RightToLeft|Ordre de lecture de droite à gauche|

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"I am using the latest version of Aspose.Cells to test this functionality.");

    // Get the style of cell A1
    Style style = cell.GetStyle();

    // Set text direction to left-to-right
    style.SetTextDirection(TextDirectionType::LeftToRight);

    // Apply the modified style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"book1.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sujets avancés**
- [Modifier l'alignement des cellules et conserver la mise en forme existante](/cells/fr/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Sauts de ligne et retour à la ligne](/cells/fr/cpp/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="cpp" >}}
