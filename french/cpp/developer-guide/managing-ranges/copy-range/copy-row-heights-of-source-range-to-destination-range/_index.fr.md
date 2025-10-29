---
title: Copier la hauteur des lignes de la plage source vers la plage de destination avec C++
linktitle: Copier la hauteur des lignes de la plage source vers la plage de destination
type: docs
weight: 590
url: /fr/cpp/copy-row-heights-of-source-range-to-destination-range/
description: Apprenez comment copier la hauteur des lignes d une plage source vers une plage de destination en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, les utilisateurs doivent copier la hauteur des lignes d'une plage source vers une plage de destination. Aspose.Cells fournit l'énumération [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) à cet effet. Lorsque vous définissez la propriété [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) avec l'énumération [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/), les hauteurs de toutes les lignes à l'intérieur de la plage source seront copiées dans la plage de destination.

{{% /alert %}}

Le code d'exemple suivant explique comment utiliser l'énumération [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) pour copier la hauteur des lignes d'une plage source vers une plage de destination. Une fois que vous ouvrez le fichier Excel généré par ce code dans Microsoft Excel, vous verrez que les hauteurs des lignes de la plage de destination sont exactement identiques à celles de la plage source.

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

    // Create workbook object
    Workbook workbook;

    // Source worksheet
    Worksheet srcSheet = workbook.GetWorksheets().Get(0);

    // Add destination worksheet
    Worksheet dstSheet = workbook.GetWorksheets().Add(u"Destination Sheet");

    // Set the row height of the 4th row. This row height will be copied to destination range
    srcSheet.GetCells().SetRowHeight(3, 50);

    // Create source range to be copied
    Range srcRange = srcSheet.GetCells().CreateRange(u"A1:D10");

    // Create destination range in destination worksheet
    Range dstRange = dstSheet.GetCells().CreateRange(u"A1:D10");

    // PasteOptions, we want to copy row heights of source range to destination range
    PasteOptions opts;
    opts.SetPasteType(PasteType::RowHeights);

    // Copy source range to destination range with paste options
    dstRange.Copy(srcRange, opts);

    // Write informative message in cell D4 of destination worksheet
    dstSheet.GetCells().Get(u"D4").PutValue(u"Row heights of source range copied to destination range");

    // Save the workbook in xlsx format
    workbook.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Row heights copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
