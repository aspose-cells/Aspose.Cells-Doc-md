---
title: Afficher et masquer les lignes, les colonnes et les barres de défilement avec C++
linktitle: Afficher et masquer les lignes, les colonnes et les barres de défilement
type: docs
weight: 20
url: /fr/cpp/show-and-hide-rows-columns-and-scroll-bars/
description: Cet article démontre comment afficher et masquer de manière programmée les lignes et colonnes d une feuille de calcul Excel en utilisant le langage C++ et l API Aspose.Cells. La visibilité des barres de défilement peut être ajustée, et plusieurs lignes et colonnes peuvent être masquées.
---

{{% alert color="primary" %}}

Aspose.Cells offre des moyens de contrôler la visibilité des lignes, colonnes et barres de défilement d'une feuille de calcul.

{{% /alert %}}

## **Afficher et masquer les lignes et les colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet aux développeurs d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre une collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) qui représente toutes les cellules de la feuille de calcul. La collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) fournit plusieurs méthodes pour gérer les lignes ou colonnes d'une feuille. Quelques-unes de celles-ci sont abordées ci-dessous.

### **Afficher les lignes et les colonnes**

Les développeurs peuvent afficher toute ligne ou colonne cachée en appelant respectivement les méthodes [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) et [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ces deux méthodes prennent deux paramètres :

- **Index de la ligne ou de la colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne assignée à la ligne ou colonne après démasquage.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhiding the 3rd row and setting its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhiding the 2nd column and setting its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Lors de la restitution d'une colonne cachée, si vous avez besoin de la rétablir à sa largeur précédemment attribuée ou à sa largeur d'origine, veuillez démasquer la colonne avec une largeur négative. Par exemple : `worksheet->GetCells()->UnhideColumn(5, -1)`.

{{% /alert %}}

### **Masquer les lignes et les colonnes**

Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) et [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ces deux méthodes prennent en paramètre l'indice de la ligne ou de la colonne pour masquer la ligne ou colonne spécifique.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.

{{% /alert %}}

### **Masquer plusieurs lignes et colonnes**

Les développeurs peuvent masquer plusieurs lignes ou colonnes simultanément en appelant respectivement les méthodes [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) et [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ces deux méthodes prennent en paramètres l'indice de la ligne ou de la colonne de début et le nombre de lignes ou colonnes à masquer.

```c++
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Afficher et masquer les barres de défilement**

Les barres de défilement sont utilisées pour naviguer dans le contenu de n'importe quel fichier. Normalement, il existe deux types de barres de défilement :

- Barres de défilement verticales
- Barres de défilement horizontales

Microsoft Excel propose également des barres de défilement horizontales et verticales permettant aux utilisateurs de naviguer dans le contenu de la feuille de calcul. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des deux types de barres de défilement dans les fichiers Excel.

### **Contrôler la visibilité des barres de défilement**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) offre une large gamme de propriétés et méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des barres de défilement, utilisez les propriétés [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) et [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) et [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) sont des propriétés Boolean, ce qui signifie que ces propriétés ne peuvent stocker que des valeurs **true** ou **false**.

#### **Rendre les barres de défilement visibles**

Rendez les barres de défilement visibles en définissant la propriété [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) ou [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) à **true**.

#### **Masquer les barres de défilement**

Masquez les barres de défilement en définissant la propriété [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) ou [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) à **false**.

**Code d'exemple**

Voici un code complet qui ouvre un fichier Excel, `book1.xls`, masque les deux barres de défilement, puis enregistre le fichier modifié sous le nom `output.xls`.

```c++
#include <iostream>
#include <fstream>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Hide the vertical scroll bar of the Excel file
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the Excel file
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
