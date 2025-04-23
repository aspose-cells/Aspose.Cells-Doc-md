---
title: Masquer et afficher des lignes et colonnes avec C++
linktitle: Masquer et afficher des lignes et des colonnes
type: docs
weight: 60
url: /fr/cpp/hiding-and-showing-rows-and-columns/
description: Apprenez comment masquer et afficher les lignes et colonnes dans les fichiers Excel de manière programmatique avec Aspose.Cells et C++.
---

{{% alert color="primary" %}}

Parfois, il est logique de masquer certaines lignes ou colonnes dans une feuille de calcul et de les afficher ultérieurement. Microsoft Excel offre cette fonctionnalité, tout comme Aspose.Cells.

{{% /alert %}}

## **Contrôler la visibilité des lignes et des colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) qui représente toutes les cellules de la feuille de calcul. La collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous.

### **Masquer les lignes et les colonnes**

Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) et [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Les deux méthodes prennent l'index de la ligne ou de la colonne comme paramètre pour masquer la ligne ou colonne spécifique.

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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.

{{% /alert %}}

### **Afficher des lignes et des colonnes**

Les développeurs peuvent afficher toute ligne ou colonne masquée en appelant respectivement les méthodes [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) et [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Les deux méthodes prennent deux paramètres :

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

Pour rendre visible une colonne masquée, si vous devez la restaurer à la largeur précédemment attribuée ou à sa largeur d'origine, veuillez démasquer la colonne avec une largeur négative. Par exemple : `worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **Masquer plusieurs lignes et colonnes**

Les développeurs peuvent masquer plusieurs lignes ou colonnes en une seule fois en appelant respectivement les méthodes [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) et [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Les deux méthodes prennent l'index de la ligne ou de la colonne de départ et le nombre de lignes ou de colonnes à masquer comme paramètres.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Il est également possible d'utiliser les méthodes [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) et [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) de la classe [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) pour rendre plusieurs lignes et colonnes visibles.

{{% /alert %}}
