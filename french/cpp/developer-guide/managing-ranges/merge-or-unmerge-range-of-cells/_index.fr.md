---
title: Fusionner ou dissocier une plage de cellules avec C++
linktitle: Fusionner ou séparer une plage de cellules
type: docs
weight: 190
url: /fr/cpp/merge-or-unmerge-range-of-cells/
description: Fusionner et dissocier des cellules dans une plage dans Excel avec du code C++.
keywords: fusionner et dissocier des cellules dans une plage en C++, fusionner et dissocier des cellules dans une plage, fusionner et dissocier des cellules dans une plage avec C++, fusionner et dissocier des cellules dans une plage en utilisant C++, fusionner et dissocier des cellules dans Excel avec C++, fusionner et dissocier des cellules dans Excel avec C++, fusionner et dissocier des cellules dans Excel, fusionner des cellules dans Excel, dissocier des cellules dans Excel, fusionner des cellules dans une plage avec C++
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour fusionner ou diviser une plage de cellules. Aspose.Cells fournit les méthodes [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) et [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) à cette fin. Cet article explique comment fusionner une plage de cellules dans une cellule unique.

{{% /alert %}}

## **Exemple**

Le code d'échantillon suivant crée d'abord une plage - A1:D4 - puis fusionne les cellules de la plage en une seule cellule en utilisant la méthode [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/). De même, vous pouvez diviser des cellules en créant une plage et en appelant la méthode [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of output excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
