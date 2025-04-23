---
title: CSS beim Speichern als HTML mit C++ deaktivieren
linktitle: CSS beim Speichern in HTML deaktivieren
type: docs
weight: 320
url: /de/cpp/disable-css-while-saving-to-html/
description: Erfahren Sie, wie Sie CSS beim Speichern von Excel Dateien als HTML mit Aspose.Cells for C++ deaktivieren.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei auf HTML für eine einzelne Seite speichern, werden die CSS-Elemente normalerweise innerhalb der HTML-Datei eingebettet und befinden sich im HEAD-Bereich. Wenn Sie diese Datei als Inhalt/Bilder eines E-Mails anhängen, werden die CSS-Elemente von den meisten E-Mail-Clients entfernt, was zu einer schlechten Darstellung führt. Version 24.12 von Aspose.Cells führt eine Option ein, mit der Sie CSS optional deaktivieren können, sodass Styles direkt innerhalb der HTML-Elemente angewendet werden können. Wenn Sie HTML als Inhalt/Bilder des E-Mails setzen möchten, verwenden Sie bitte die Property [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) und setzen Sie sie auf **true**.

## **CSS beim Speichern in HTML deaktivieren**

Das folgende Beispiel zeigt die Verwendung der [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/)-Eigenschaft.

## **Beispielcode**

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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
