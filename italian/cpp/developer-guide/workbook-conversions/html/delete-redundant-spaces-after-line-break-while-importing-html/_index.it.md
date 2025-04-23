---
title: Elimina gli spazi ridondanti dopo l interruzione di riga durante l importazione di HTML con C++
linktitle: Eliminare gli spazi ridondanti dopo un interruzione di riga durante l importazione di HTML
type: docs
weight: 20
url: /it/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Impara come eliminare gli spazi ridondanti dopo le interruzioni di riga durante l importazione di HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Per favore usa la proprietà [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) e impostala **true** per eliminare tutti gli spazi ridondanti che seguono il tag di interruzione di riga. Per impostazione predefinita, questa proprietà è **false** e gli spazi ridondanti vengono preservati nei file Excel di output.

{{% /alert %}}

## Effetto dell'impostazione della proprietà HTMLLoadOptions.DeleteRedundantSpaces a false e true

Nella seguente schermata è mostrato l'effetto dell'impostazione di questa proprietà su **false** e **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Eliminare gli spazi ridondanti dopo l'interruzione di riga durante l'importazione di HTML

### Esempio di programmazione

Il seguente codice di esempio mostra l'uso della proprietà [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/). Si prega di impostarla su **true** o **false** per ottenere l'output mostrato nella schermata sopra.

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
