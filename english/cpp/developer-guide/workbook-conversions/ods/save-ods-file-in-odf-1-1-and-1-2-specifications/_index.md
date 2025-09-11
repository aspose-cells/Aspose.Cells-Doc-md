---
title: Save ODS File in ODF 1.1, 1.2 and 1.3 Specifications with C++
linktitle: Save as ODF 1.1, 1.2 and 1.3
description: Convert Excel to ODF 1.1, 1.2 and 1.3 Specifications with Aspose.Cells using C++.
type: docs
weight: 230
url: /cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supports saving an ODS file (**OpenDocument Spreadsheet**) in the ODF (**OpenDocument Format**) 1.1, 1.2 and 1.3 specifications. Aspose.Cells has [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/) property that specifies the ODF version for saving ODS files. The default value of this property is [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), so the ODS file saved without this setting uses the 1.2 specifications.

{{% /alert %}}

The sample code below creates a workbook object, adds some value to cell A1 on the first worksheet and then saves the ODS file in ODF 1.1, 1.2 and 1.3 specifications. By default, the ODS file is saved in ODF 1.2 specification.

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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some value in cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Welcome to Aspose!");

    // Save ODS in ODF 1.2 version which is default
    OdsSaveOptions options;
    workbook.Save(outDir + u"ODF1.2_out.ods", options);

    // Save ODS in ODF 1.1 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf11);
    workbook.Save(outDir + u"ODF1.1_out.ods", options);

    // Save ODS in ODF 1.3 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf13);
    workbook.Save(outDir + u"ODF1.3_out.ods", options);

    std::cout << "ODS files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}