---
title: Exportera databar, färgschema och ikonuppsättning för villkorsstyrd formatering samtidigt som Excel till HTML konverteras med C++
linktitle: Exportera villkorsstyrd formatering till HTML
type: docs
weight: 30
url: /sv/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: Lär dig hur du exporterar databar, färgschema och ikonuppsättning för villkorsstyrd formatering när du konverterar Excel filer till HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Du kan exportera villkorsstyrd formatering för DataBar, ColorScale och IconSet när du konverterar din Excel-fil till HTML. Denna funktion stöds delvis av Microsoft Excel, men Aspose.Cells for C++ stöder den fullt ut.

{{% /alert %}} 

## **Exportera villkorsstyrd formatering för DataBar, ColorScale och IconSet vid Excel till HTML-omvandling**
Följande skärmbild visar [exempel-Excel-filen](5115558.xlsx) med villkorsstyrd formatering för DataBar, ColorScale och IconSet. Du kan ladda ner [exempel-Excel-filen](5115558.xlsx) via länken.

![todo:image_alt_text](conversion_1.png)

Följande skärmbild visar Aspose.Cells utdata HTML-fil som visar villkorsstyrd formatering för DataBar, ColorScale och IconSet. Som du kan se ser den exakt ut som [exempel-Excel-filen](5115558.xlsx).

![todo:image_alt_text](conversion_2.png)

### **Exempelkod**
Följande exempel kod konverterar exempel-Excel-filen till HTML, vilket är en vanlig [Excel till HTML-omvandling](/cells/sv/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
