---
title: C++ kullanarak HTML içe aktarırken satır sonlarından sonra gereksiz boşlukları silmek
linktitle: HTML içe aktarılırken satır sonrası gereksiz boşlukları silin
type: docs
weight: 20
url: /tr/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aspose.Cells for C++ kullanarak HTML içe aktarırken satır sonlarından sonra gereksiz boşlukları silmeyi öğrenin.
---

{{% alert color="primary" %}}

 Lütfen [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) özelliğini kullanın ve **true** olarak ayarlayın, böylece satır sonu etiketi sonrası gelen tüm gereksiz boşluklar silinir. Varsayılan olarak, bu özellik **false**'dur ve gereksiz boşluklar çıktı Excel dosyalarında korunur.

{{% /alert %}}

HTMLLoadOptions.DeleteRedundantSpaces özelliğini false ve true olarak ayarlamanın etkisi

Bu özelliği **false** ve **true** olarak ayarlamanın etkisini gösteren aşağıdaki ekran görüntüsü.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTML içe aktarılırken satır sonrası gereksiz boşlukları silme

### Programlama Örneği

Aşağıdaki örnek kod, [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) özelliğinin kullanımını gösterir. Yukarıdaki ekran görüntüsünde gösterilen çıktıyı almak için **true** veya **false** olarak ayarlayın.

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
