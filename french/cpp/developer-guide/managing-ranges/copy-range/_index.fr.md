--- 
title: Copier des plages Excel avec C++ 
linktitle: Copier des plages 
type: docs 
weight: 105 
url: /fr/cpp/copy-ranges-of-excel/ 
description: Apprenez comment copier des plages dans Excel en utilisant Aspose.Cells avec C++. 
--- 

## **Introduction**

Dans Excel, vous pouvez sélectionner une plage, copier la plage, puis la coller avec des options spécifiques dans la même feuille de calcul, d'autres feuilles de calcul ou d'autres fichiers.

## **Copier des plages en utilisant Aspose.Cells**

 Aspose.Cells propose plusieurs méthodes surcharge [Range.Copy](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) pour copier la plage. Et [Range.CopyStyle](https://reference.aspose.com/cells/cpp/aspose.cells/range/copystyle/) ne copie que le style de la plage ; [Range.CopyData](https://reference.aspose.com/cells/cpp/aspose.cells/range/copydata/) ne copie que la valeur de la plage.

## **Copier la plage**

Création de deux plages : la plage source, la plage cible, puis copie de la plage source vers la plage cible avec la méthode Range.Copy.

Voir le code suivant :

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into
    // A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy source range to target range in the same worksheet 
    targetRange.Copy(sourceRange);

    // Create a new worksheet.
    worksheets.Add();
    worksheet = worksheets.Get(1);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another worksheet 
    targetRange.Copy(sourceRange);

    // Copy to another workbook
    Workbook anotherWorkbook;

    worksheet = workbook.GetWorksheets().Get(0);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another workbook 
    targetRange.Copy(sourceRange);

    std::cout << "Copy operations completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Coller la plage avec des options**

Aspose.Cells prend en charge le collage de la plage avec un type spécifique.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Init paste options.
    PasteOptions options;
    // Set paste type.
    options.SetPasteType(PasteType::ValuesAndFormats);
    options.SetSkipBlanks(true);

    // Copy source range to target range
    targetRange.Copy(sourceRange, options);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Copier uniquement les données de la plage**
Vous pouvez également copier les données avec la méthode Range.CopyData comme dans les codes suivants :

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formatting into
    // A few cells in the range.
    sourceRange.Get(0, 0).SetValue(u"Test");
    sourceRange.Get(1, 0).SetValue(123);

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy the data of source range to target range
    targetRange.CopyData(sourceRange);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Copier les hauteurs de ligne de la plage source vers la plage de destination](/cells/fr/cpp/copy-row-heights-of-source-range-to-destination-range/)
{{< app/cells/assistant language="cpp" >}}
