---
title: Cambiar el tipo de destino del enlace HTML con C++
linktitle: Cambiar el tipo de destino del enlace HTML
type: docs
weight: 320
url: /es/cpp/change-the-html-link-target-type/
description: Aprenda cómo cambiar el tipo de destino del enlace HTML usando Aspose.Cells for C++. Controle el atributo target en los enlaces HTML de forma programática.
---

{{% alert color="primary" %}}

Aspose.Cells te permite cambiar el tipo de destino del enlace HTML. El enlace HTML luce así

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Como puedes ver, el atributo destino en el enlace HTML anterior es **_self**. Puedes controlar este atributo de destino usando la propiedad [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Esta propiedad toma la enumeración [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) que tiene los siguientes valores.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

El siguiente código ilustra el uso de la propiedad [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Cambia el tipo de destino del enlace a **blank**. Por defecto, es **parent**.

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
