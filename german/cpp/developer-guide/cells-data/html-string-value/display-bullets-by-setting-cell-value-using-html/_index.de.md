---
title: Aufzählungszeichen anzeigen, indem Sie den Zellenwert mit HTML in C++ festlegen
linktitle: Anzeige von Aufzählungszeichen durch Setzen des Zellenwerts mit HTML
type: docs
weight: 130
url: /de/cpp/display-bullets-by-setting-cell-value-using/
description: Fügen Sie Excel Zellen mit HTML und der einfach zu verwendenden API Aspose.Cells for C++ Aufzählungszeichen hinzu.
keywords: Aufzählungszeichen in Excel hinzufügen, Aufzählungszeichen in Excel C++, Aufzählungszeichen in Excel anzeigen, Aufzählungszeichen in Excel C++, Aufzählungszeichen in Excel mit HTML hinzufügen, Aufzählungszeichen in Excel mit HTML C++, Aufzählungszeichen in Excel mit HTML anzeigen, Aufzählungszeichen in Excel mit HTML C++, Aufzählungszeichen in Excel mit HTML verwenden, Aufzählungszeichen in Excel mit HTML hinzufügen
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Anzeigen von Aufzählungszeichen mit HTML-Code. Dieser Artikel erläutert, wie Aufzählungszeichen durch Setzen des Zellenwerts mit HTML angezeigt werden können. Wir werden die [**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)-Eigenschaft verwenden, um den Zellenwert mit unserem HTML zu setzen.

{{% /alert %}}

## C++ Code zum Anzeigen von Aufzählungszeichen durch Setzen des Zellenwerts mit HTML

Der folgende Code verwendet den HTML-Code, um den Zellenwert zu setzen. Sobald Sie diesen Code ausführen, erhalten Sie die Ausgabe, wie im folgenden Bild gezeigt.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Ausgabe, die vom Beispielcode generiert wurde

Der folgende Screenshot zeigt die Ausgabe des obigen Beispielcodes.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
{{< app/cells/assistant language="cpp" >}}
