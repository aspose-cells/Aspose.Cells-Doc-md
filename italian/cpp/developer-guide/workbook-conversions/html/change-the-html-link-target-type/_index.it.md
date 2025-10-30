---
title: Cambia il Tipo di Destinazione del Collegamento HTML con C++
linktitle: Modifica il Tipo di Destinazione del Link HTML
type: docs
weight: 320
url: /it/cpp/change-the-html-link-target-type/
description: Impara come cambiare il tipo di destinazione del collegamento HTML usando Aspose.Cells for C++. Controlla l attributo target nei collegamenti HTML programmaticamente.
---

{{% alert color="primary" %}}

Aspose.Cells ti permette di cambiare il tipo di destinazione del link HTML. Il link HTML appare così

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Come puoi vedere, l'attributo di destinazione nel link HTML sopra è **_self**. È possibile controllare questo attributo di destinazione utilizzando la proprietà [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Questa proprietà richiede l'enum [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) che ha i seguenti valori.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Il seguente codice illustra l'uso della proprietà [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Cambia il tipo di destinazione del link a **blank**. Per default, è **parent**.

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
    U16String inputPath = srcDir + u"Sample1.xlsx";

    // Path of output HTML file
    U16String outputPath = outDir + u"Output.out.html";

    // Create workbook
    Workbook workbook(inputPath);

    // Create HTML save options
    HtmlSaveOptions opts;
    opts.SetLinkTargetType(HtmlLinkTargetType::Self);

    // Save the workbook to HTML format
    workbook.Save(outputPath, opts);

    std::cout << "File saved: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
