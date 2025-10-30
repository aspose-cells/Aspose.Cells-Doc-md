---
title: Prevenire l esportazione dei contenuti nascosti del foglio di lavoro durante il salvataggio in HTML con C++
linktitle: Prevenire l esportazione dei contenuti nascosti del foglio di lavoro
type: docs
weight: 210
url: /it/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Impara come prevenire l esportazione dei contenuti nascosti del foglio di lavoro durante il salvataggio di cartelle di lavoro Excel in HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

È possibile salvare i fogli di lavoro di Excel in HTML. Tuttavia, se il foglio di lavoro contiene fogli di lavoro nascosti, Aspose.Cells esporta per impostazione predefinita il contenuto del foglio di lavoro nascosto nella directory di output HTML (_files) che contiene file come fogli di lavoro, immagini, tabstrip.htm, stylesheet.css, ecc. A volte, esportare il contenuto dei fogli di lavoro nascosti in questo modo non è appropriato. Ad esempio, se il foglio di lavoro nascosto contiene immagini che non dovrebbero essere esportate nella directory _files.

{{% /alert %}}

Aspose.Cells fornisce la proprietà [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexporthiddenworksheet/). Per impostazione predefinita, è impostata su **true** e i fogli di lavoro nascosti vengono esportati in HTML. Se lo si imposta su **false**, Aspose.Cells non esporterà il contenuto del foglio di lavoro nascosto.

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
    U16String inputFilePath = srcDir + u"WorkbookWithHiddenContent.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"HtmlWithoutHiddenContent_out.html";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Create HTML save options
    HtmlSaveOptions options;

    // Do not export hidden worksheet contents
    options.SetExportHiddenWorksheet(false);

    // Save the workbook
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully without hidden content!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
