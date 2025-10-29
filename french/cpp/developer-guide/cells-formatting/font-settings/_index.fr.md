---
title: Paramètres de police avec C++
linktitle: Paramètres de la police
type: docs
weight: 30
url: /fr/cpp/cells-font-settings/
description: Aspose.Cells est une bibliothèque C++ pour le travail avec des fichiers de tableur. Elle supporte la configuration des paramètres de police des cellules, permettant aux utilisateurs de personnaliser le style et les propriétés de la police des cellules. Cet article montre comment utiliser la bibliothèque Aspose.Cells pour définir les paramètres de police des cellules.
keywords: Aspose.Cells, Cellules, Paramètres de police, Styles, Propriétés
---

{{% alert color="primary" %}}

L'apparence d'un texte peut être contrôlée en modifiant les paramètres de police. Ces paramètres incluent le nom, le style, la taille, la couleur et d'autres effets de la police. Comme Microsoft Excel, Aspose.Cells supporte la configuration des paramètres de police des cellules.

{{% /alert %}}

## **Configuration des paramètres de police**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Chaque élément de la collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fournit les méthodes [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) et [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) utilisées pour obtenir et définir le style de mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fournit des propriétés pour configurer les paramètres de police.

### **Définition du nom de la police**

Les développeurs peuvent appliquer n'importe quelle police au texte d'une cellule en utilisant la propriété [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

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

    // Set the font name to "Times New Roman"
    style.GetFont().SetName(u"Times New Roman");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Définition du style de police en gras**

Les développeurs peuvent mettre en gras le texte en définissant la propriété [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) sur **true**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

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
    style.GetFont().SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Définition de la taille de police**

Définissez la taille de la police avec la propriété [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

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

    // Set the font size to 14
    style.GetFont().SetSize(14);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Définition de la couleur de police**

Utilisez la propriété [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) pour définir la couleur de la police. Sélectionnez n'importe quelle couleur dans l'énumération Color (faisant partie du framework C++) et assignez-la à la propriété [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

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

    // Set the font color to blue
    style.GetFont().SetColor(Color::Blue());

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

### **Définition du type de soulignement de la police**

Utilisez la propriété [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) pour souligner le texte. Aspose.Cells propose divers types de soulignement de police prédéfinis dans l'énumération [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/).

|**Types de soulignement de police**|**Description**|
| :- | :- |
|Accounting|Un soulignement de comptabilité unique|
|Double|Double soulignement|
|DoubleAccounting|Double soulignement de comptabilité|
|None|Pas de soulignement|
|Single|Un seul soulignement|

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

    // Set the font to be underlined
    style.GetFont().SetUnderline(FontUnderlineType::Single);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Définition de l'effet Barré**

Appliquer l'effet barré en définissant la propriété [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) à **true**.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Hello Aspose!");

    Style style = cell.GetStyle();
    style.GetFont().SetIsStrikeout(true);
    cell.SetStyle(style);

    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Définir l'effet de bas indice**

Appliquer le bas indice en définissant la propriété [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) à **true**.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set subscript effect
    style.GetFont().SetIsSubscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Définition de l'effet exposant sur la police**

Les développeurs peuvent appliquer l'effet exposant sur la police en définissant la propriété [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) à **true**.

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

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set superscript effect
    style.GetFont().SetIsSuperscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Appliquer les effets exposant et bas indice sur les polices](/cells/fr/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur](/cells/fr/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="cpp" >}}
