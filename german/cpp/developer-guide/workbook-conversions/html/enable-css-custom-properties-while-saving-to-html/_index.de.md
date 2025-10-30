---
title: Beim Speichern als HTML das CSS benutzerdefinierte Eigenschaften aktivieren
linktitle: CSS Benutzerdefinierte Eigenschaften beim Speichern in HTML aktivieren
type: docs
weight: 320
url: /de/cpp/enable-css-custom-properties-while-saving-to-html/
description: Lernen, wie man CSS Kundeneigenschaften beim Speichern von Excel Dateien als HTML mit Aspose.Cells for C++ aktiviert. Leistungsverbesserung durch Reduzierung redundanter Bilddaten.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in HTML speichern, können Sie bei mehreren Vorkommen eines Base64-Bildes mit Kundeneigenschaften die Bilddaten nur einmal speichern, um die Leistung des resultierenden HTML zu verbessern. Bitte verwenden Sie [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) Property und setzen Sie es auf **true** beim Speichern als HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Aktivieren Sie CSS Standard-Eigenschaften beim Speichern in HTML**

Der folgende Beispielcode zeigt die Verwendung der [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/)-Eigenschaft. Das Screenshot zeigt die Auswirkung dieser Eigenschaft, wenn sie nicht auf **true** gesetzt ist. Bitte laden Sie die [Beispieldatei Excel](50528260.xlsx), die in diesem Code verwendet wird, und das [generierte HTML](50528261.zip) als Referenz herunter.

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
    Workbook wb(srcDir + u"sampleEnableCssCustomProperties.xlsx");

    // Create HtmlSaveOptions object
    HtmlSaveOptions opts;

    // Set ExportImagesAsBase64 to true
    opts.SetExportImagesAsBase64(true);

    // Enable EnableCssCustomProperties
    opts.SetEnableCssCustomProperties(true);

    // Save the workbook in HTML format
    wb.Save(outDir + u"outputEnableCssCustomProperties.html", opts);

    std::cout << "Workbook saved successfully with CSS custom properties enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
