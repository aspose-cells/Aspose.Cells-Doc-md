---
title: Convertir la table en ODS avec C++
linktitle: Convertir un tableau en ODS
type: docs
weight: 70
url: /fr/cpp/convert-table-to-ods/
description: Convertir un fichier Excel contenant une table en format ODS en utilisant Aspose.Cells avec C++.
---

Aspose.Cells prend en charge la conversion d'un fichier Excel avec une table au format ODS. Il suffit de sauvegarder le fichier au format ODS, et le fichier ODS généré aura une table fonctionnelle.

## Code d'exemple

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an existing file that contains a table/list object in it
    U16String inputFilePath = sourceDir + u"SampleTable.xlsx";
    Workbook workbook(inputFilePath);

    // Save the file in ODS format
    workbook.Save(outputDir + u"ConvertTableToOds_out.ods");

    std::cout << "Conversion to ODS completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Le fichier ODS de sortie généré par le code d'exemple est joint à titre de référence.

[**Output ODS File**](ConvertTableToOds_out.ods)
