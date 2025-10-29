---
title: Ajuster automatiquement la hauteur des lignes et la largeur des colonnes avec C++
linktitle: Ajuster automatiquement les lignes et les colonnes
type: docs
weight: 20
url: /fr/cpp/autofit-rows-and-columns/
description: Cet article montre comment ajuster automatiquement la hauteur des lignes, des colonnes, des lignes de cellules fusionnées et des lignes dans une plage de cellules en utilisant l API Aspose.Cells for C++.
keywords: Ajuster automatiquement les lignes, les colonnes, les lignes de cellules fusionnées et les lignes dans une plage de cellules.
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de redimensionner automatiquement la largeur et la hauteur des cellules en fonction de leur contenu. Cette fonctionnalité est également disponible avec Aspose.Cells, permettant aux développeurs de redimensionner automatiquement les dimensions d'une cellule à l'exécution.

{{% /alert %}}

## **Ajustement automatique**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) permettant d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre un large éventail de méthodes pour gérer une feuille de calcul. Cet article aborde l'utilisation de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) pour autofit les lignes ou les colonnes.

### **Ajuster automatiquement la ligne - Simple**

L'approche la plus simple pour ajuster automatiquement la largeur et la hauteur d'une ligne consiste à appeler la méthode [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La méthode [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) prend un indice de ligne (de la ligne à redimensionner) en paramètre.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Comment ajuster automatiquement une ligne dans une plage de cellules**

Une ligne est composée de plusieurs colonnes. Aspose.Cells permet aux développeurs d'automatiser le réglage de la hauteur d'une ligne en fonction du contenu dans une plage de cellules de cette ligne, en appelant une version surchargée de la méthode [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/). Elle accepte les paramètres suivants :

- **Index de la ligne**, l'index de la ligne à ajuster automatiquement.
- **Index de la première colonne**, l'index de la première colonne de la ligne.
- **Index de la dernière colonne**, l'index de la dernière colonne de la ligne.

La méthode [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) vérifie le contenu de toutes les colonnes de la ligne puis ajuste automatiquement la hauteur de la ligne.

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

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Comment ajuster automatiquement une colonne dans une plage de cellules**

Une colonne est composée de plusieurs lignes. Il est possible d'ajuster automatiquement la largeur d'une colonne en fonction du contenu dans une plage de cellules de cette colonne en appelant une version surchargée de la méthode [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) qui accepte les paramètres suivants :

- **Index de la colonne**, l'index de la colonne à ajuster automatiquement.
- **Index de la première ligne**, l'index de la première ligne de la colonne.
- **Index de la dernière ligne**, l'index de la dernière ligne de la colonne.

La méthode [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) vérifie le contenu de toutes les lignes de la colonne puis ajuste automatiquement la largeur de la colonne.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Comment ajuster automatiquement les lignes pour les cellules fusionnées**

Avec Aspose.Cells, il est possible d'automatiser l'ajustement des lignes même pour les cellules fusionnées en utilisant l'API [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/). La classe [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) fournit la propriété [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) qui peut être utilisée pour autofit les lignes de cellules fusionnées. [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) accepte l'énumération [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/) avec les membres suivants :

- None : Ignorer les cellules fusionnées.
- FirstLine : N'agrandit la hauteur que de la première ligne.
- LastLine : N'agrandit la hauteur que de la dernière ligne.
- EachLine : N'agrandit la hauteur de chaque ligne.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Vous pouvez également essayer d'utiliser les versions surchargées des méthodes [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) et [**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/) acceptant une plage de lignes/colonnes et une instance de [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) pour autofit les lignes/colonnes sélectionnées avec votre [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) souhaité en conséquence.

Les signatures des méthodes susmentionnées sont les suivantes :

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)

{{% /alert %}}

## **Important à savoir**

{{% alert color="primary" %}}

Si une cellule est fusionnée, alors les méthodes AutoFit ne seront pas appliquées, ce qui est le même comportement que dans Microsoft Excel. Vous pouvez contourner cela en utilisant l'API de filtrage automatique. De plus, si le texte dans une cellule est enroulé, la méthode [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) ne sera pas appliquée non plus. Une autre chose à savoir est que les méthodes *AutoFit* sont chronophages. Par conséquent, il faut appeler ces méthodes aussi rarement que possible pour garantir l'efficacité de votre application.

{{% /alert %}}

## **Sujets avancés**
- [Ajustement automatique des lignes pour les cellules fusionnées](/cells/fr/cpp/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="cpp" >}}
