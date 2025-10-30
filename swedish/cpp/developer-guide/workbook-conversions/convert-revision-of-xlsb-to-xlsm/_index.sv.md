---
title: Konvertera revision av XLSB till XLSM med C++
linktitle: Konvertera revision av XLSB till XLSM
type: docs
weight: 290
url: /sv/cpp/convert-revision-of-xlsb-to-xlsm/
description: Lär dig att konvertera revisioner av XLSB filer till XLSM format med Aspose.Cells och C++.
---

{{% alert color="primary" %}} 

Aspose.Cells stöder nu fullständig konvertering av revisioner av XLSB-filer till XLSM-filer. Revisionerna finns i mappen \xl\revisions. Du kan visa dem genom att byta filändelsen på din XLSB till ZIP.\xl\revisions-mappen innehåller filer som slutar med .bin-ändelser.

När du konverterar din XLSB-fil till XLSM med Aspose.Cells, konverteras dessa .bin-filer framgångsrikt till .xml-filer som visas i dessa två skärmbilder.

{{% /alert %}} 

Följande kodexempel visar hur du konverterar XLSB-filen till XLSM-format med Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsb";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Save Workbook to XLSM format
    workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully in XLSM format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
