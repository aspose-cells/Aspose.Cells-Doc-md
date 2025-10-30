---
title: Ta bort överflödiga mellanslag efter radbrytning när du importerar HTML med C++
linktitle: Ta bort överflödiga mellanslag efter radbrytning vid import av HTML
type: docs
weight: 20
url: /sv/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Lär dig hur man tar bort överflödiga mellanslag efter radbrytningar vid import av HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Använd [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/)-egenskapen och ställ in den på **true** för att ta bort alla överflödiga mellanslag som kommer efter radbrytnings-taggen. Som standard är den här egenskapen **false** och överskottslinjer bevaras i de utmatade Excel-filerna.

{{% /alert %}}

## Effekten av att ställa in HTMLLoadOptions.DeleteRedundantSpaces egenskapen till false och true

Följande skärmbild visar effekten av att ställa denna egenskap till **false** och **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Ta bort överflödiga mellanslag efter radbrytning vid import av HTML

### Programexempel

Följande kodexempel visar användningen av egenskapen [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/). Vänligen ange den som **true** eller **false** för att få utdata som visas i ovanstående skärmdump.

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
