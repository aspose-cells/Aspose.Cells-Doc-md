---
title: Disabilitare l Esportazione di Script di Frame e Proprietà del Documento con C++
type: docs
weight: 310
url: /it/cpp/disable-exporting-frame-scripts-and-document-properties/
description: Disabilita l esportazione di script di frame e proprietà del documento usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells esporta script di frame e proprietà del documento durante la conversione di un workbook in HTML. La versione 8.6.0 di Aspose.Cells for C++ introduce un'opzione che ti permette di disattivare opzionalmente l'esportazione di script di frame e proprietà del documento. Usa la proprietà HtmlSaveOptions.ExportFrameScriptsAndProperties per disattivare l'esportazione.

{{% /alert %}}

## **Disabilita l'esportazione degli script frame e delle proprietà del documento**

Il seguente codice di esempio ti permette di disabilitare l'esportazione degli script frame e delle proprietà del documento. Una volta convertito un workbook in HTML, il file di output non conterrà alcuno script frame o proprietà del documento.

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

    // Open the required workbook to convert
    U16String inputFilePath = srcDir + u"Sample1.xlsx";
    Workbook workbook(inputFilePath);

    // Disable exporting frame scripts and document properties
    HtmlSaveOptions options;
    options.SetExportFrameScriptsAndProperties(false);

    // Save workbook as HTML
    workbook.Save(outDir + u"output.out.html", options);

    std::cout << "Workbook saved successfully as HTML!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
