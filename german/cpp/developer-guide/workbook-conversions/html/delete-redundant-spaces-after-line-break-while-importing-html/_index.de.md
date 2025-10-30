---
title: Löschen Sie unnötige Leerzeichen nach Zeilenumbrüchen beim Importieren von HTML mit C++
linktitle: Überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML löschen
type: docs
weight: 20
url: /de/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Erfahren Sie, wie Sie redundante Leerzeichen nach Zeilenumbrüchen beim Importieren von HTML mit Aspose.Cells for C++ entfernen.
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) und setzen Sie sie **true**, um alle redundanten Leerzeichen nach dem Zeilenumbruch-Tag zu löschen. Standardmäßig ist diese Eigenschaft **false**, und redundante Leerzeichen bleiben im Ausgabedokument erhalten.

{{% /alert %}}

## Wirkung der Einstellung der HTMLLoadOptions.DeleteRedundantSpaces-Eigenschaft auf falsch und wahr

Der folgende Screenshot zeigt den Effekt der Einstellung dieser Eigenschaft auf false und true.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Löschen Sie überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML

### Programmierbeispiel

Das folgende Beispiel zeigt die Verwendung der [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/)-Eigenschaft. Bitte setzen Sie sie auf **true** oder **false**, um die Ausgabe wie im obigen Screenshot zu erhalten.

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String html = u8"<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions(LoadFormat::Html);
    loadOptions.SetDeleteRedundantSpaces(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
