---
title: Insertion et suppression de lignes et de colonnes dans un fichier Excel avec C++
linktitle: Insertion et suppression de lignes et de colonnes
type: docs
weight: 70
url: /fr/cpp/inserting-and-deleting-rows-and-columns/
description: Cet article montre comment insérer et supprimer des lignes et des colonnes en utilisant l API Aspose.Cells for C++.
keywords: Aspose.Cells C++ gère les lignes et colonnes, insère des lignes et colonnes, supprime des lignes et colonnes
---

## **Introduction**

Que vous créiez une nouvelle feuille de calcul à partir de zéro ou travailliez sur une feuille de calcul existante, vous pouvez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, vous pouvez également avoir besoin de supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul.
Pour répondre à ces exigences, Aspose.Cells fournit un ensemble très simple de classes et de méthodes, expliquées ci-dessous.

### **Gérer les lignes et les colonnes**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) qui représente toutes les cellules de la feuille.

La collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) offre plusieurs méthodes pour gérer les lignes et colonnes dans une feuille. Certaines sont expliquées ci-dessous.

{{% alert color="primary" %}}

Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille est décalé vers le bas ou vers la droite, et si des lignes ou colonnes sont supprimées, le contenu est décalé vers le haut ou vers la gauche.

{{% /alert %}}

## **Insérer des lignes et des colonnes**

### **Comment Insérer une Ligne**

Insérez une ligne dans la feuille à n'importe quelle position en appelant la méthode [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) de la collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). La méthode [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) prend l'indice de la ligne où la nouvelle ligne sera insérée.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Comment Insérer Plusieurs Lignes**

Pour insérer plusieurs lignes dans une feuille, appelez la méthode [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) de la collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). La méthode [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, le nombre total de lignes à insérer.

```c++
#include <iostream>
#include <fstream>
#include <memory>
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

    // Insert 10 rows into the worksheet starting from 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Comment insérer une ligne avec mise en forme**

Pour insérer une ligne avec des options de mise en forme, utilisez la surcharge [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) qui prend [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) en paramètre. Configurez la propriété [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) de la classe [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) avec l'énumération [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/). L'énumération [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) possède trois membres listés ci-dessous.

- SameAsAbove : Met en forme la ligne comme la ligne ci-dessus.
- SameAsBelow : Met en forme la ligne comme la ligne ci-dessous.
- Clear: Efface la mise en forme.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"InsertingARowWithFormatting_out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting Formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Comment insérer une colonne**

Les développeurs peuvent également insérer une colonne dans la feuille à n'importe quelle position en appelant la méthode [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) de la collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). La méthode [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) prend l'indice de la colonne où la nouvelle colonne sera insérée.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a column into the worksheet at 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Supprimer des lignes et des colonnes**

### **Comment supprimer plusieurs lignes**

Pour supprimer plusieurs lignes d'une feuille, appelez la méthode [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) de la collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). La méthode [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, le nombre total de lignes à supprimer.

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

    // Delete 10 rows from the worksheet starting from 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Comment supprimer une colonne**

Pour supprimer une colonne de la feuille à n'importe quelle position, appelez la méthode [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) de la collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). La méthode [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) prend l'indice de la colonne à supprimer.

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

    // Delete a column from the worksheet at 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
