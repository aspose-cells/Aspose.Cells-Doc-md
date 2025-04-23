---
title: Salva file ODS in specifiche ODF 1.1, 1.2 e 1.3 con C++
linktitle: Salva come ODF 1.1, 1.2 e 1.3
description: Converti Excel in specifiche ODF 1.1, 1.2 e 1.3 con Aspose.Cells usando C++.
type: docs
weight: 230
url: /it/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supporta il salvataggio di un file ODS (**OpenDocument Spreadsheet**) nei requisiti ODF (**OpenDocument Format**) 1.1, 1.2 e 1.3. Aspose.Cells ha la proprietà [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/) che specifica la versione ODF per il salvataggio dei file ODS. Il valore predefinito di questa proprietà è [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), quindi il file ODS salvato senza questa impostazione utilizza le specifiche 1.2.

{{% /alert %}}

Il codice di esempio di seguito crea un oggetto workspace, aggiunge alcuni valori alla cella A1 del primo foglio di lavoro e quindi salva il file ODS secondo le specifiche ODF 1.1, 1.2 e 1.3. Per impostazione predefinita, il file ODS viene salvato secondo le specifiche ODF 1.2.

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
