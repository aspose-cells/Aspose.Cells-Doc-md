---
title: Regroupement et désagrégation de lignes et colonnes avec C++
linktitle: Regroupement et dégroupement des lignes et des colonnes
type: docs
weight: 50
url: /fr/cpp/grouping-and-ungrouping-rows-and-columns/
description: Apprenez comment grouper et dégrouper les lignes et colonnes dans les fichiers Excel à l aide d Aspose.Cells avec C++.
---

## **Introduction**

Dans un fichier Microsoft Excel, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

Cliquez sur les **symboles de plan**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou colonnes fournissant des résumés ou des en-têtes de sections dans une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou une en-tête individuelle comme le montre la figure ci-dessous:

|**Regroupement des lignes et des colonnes.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestion des groupes de lignes et de colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) qui représente toutes les cellules de la feuille de calcul.

La collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) propose plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille de calcul, dont certaines sont discutées plus en détail ci-dessous.

### **Regrouper des lignes et des colonnes**

Il est possible de regrouper des lignes ou des colonnes en appelant les méthodes [**GroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) et [**GroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Les deux méthodes prennent les paramètres suivants :

- Indice de la première ligne/colonne, la première ligne ou colonne du groupe.
- Indice de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est caché, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.

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

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Group first six rows (from 0 to 5) and make them hidden
    worksheet.GetCells().GroupRows(0, 5, true);

    // Group first three columns (from 0 to 2) and make them hidden
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns grouped successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Paramètres de regroupement**

Microsoft Excel vous permet de configurer les paramètres de regroupement pour l'affichage :

- Lignes de récapitulatif en dessous des détails.
- Colonnes de récapitulatif à droite des détails.

Les développeurs peuvent configurer ces paramètres de regroupement en utilisant la propriété [**GetOutline()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoutline/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

### **Lignes de résumé en dessous des détails**

Il est possible de contrôler si les lignes de récapitulatif sont affichées en dessous des détails en définissant la propriété [**GetSummaryRowBelow()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummaryrowbelow/) de la classe [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) à **true** ou **false**.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Setting SummaryRowBelow property to false
    worksheet.GetOutline().SetSummaryRowBelow(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Colonnes récapitulatives à droite du détail**

Les développeurs peuvent également contrôler l'affichage des colonnes de récapitulatif à droite des détails en définissant la propriété [**GetSummaryColumnRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummarycolumnright/) de la classe [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) à **true** ou **false**.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Set summary column to the right
    worksheet.GetOutline().SetSummaryColumnRight(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Désagréger les lignes et les colonnes**

Pour dissocier les lignes ou colonnes regroupées, appelez les méthodes [**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) et [**UngroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Les deux méthodes prennent deux paramètres :

- Indice de la première ligne ou colonne, la première ligne/colonne à dissocier.
- Indice de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.

[**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) a une surcharge qui prend un troisième paramètre booléen. Le définir sur **true** supprime toutes les informations regroupées. Sinon, seules les informations de groupe externe sont supprimées.

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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Ungrouping first six rows (from 0 to 5)
    worksheet.GetCells().UngroupRows(0, 5);

    // Ungrouping first three columns (from 0 to 2)
    worksheet.GetCells().UngroupColumns(0, 2);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```
