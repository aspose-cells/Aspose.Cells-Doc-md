---
title: Räkna sidinställningsskalningsfaktor med C++
linktitle: Beräkna siduppsättningsskalningsfaktorn
type: docs
weight: 300
url: /sv/cpp/calculate-page-setup-scaling-factor/
description: Denna artikel ger exempel på kod som förklarar hur man använder C++ API eller bibliotek för att beräkna sidinställningsskalningsfaktor med anpassning till n sidor brett av m högt i Excel, programmatiskt.
keywords: Anpassa till n sidor brett av m högt excel c++, beräkna sidinställningsskalningsfaktor c++
---

{{% alert color="primary" %}}

När du ställer in sidlayoutskalning med alternativet **Passar till n sidor breda och m höga** beräknar Microsoft Excel sidlayoutskalningsfaktorn. Du kan beräkna samma sak med hjälp av [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/)-egenskapen. Denna egenskap returnerar ett dubbelt värde som kan konverteras till procentvärde. Till exempel, om den returnerar 0,5 innebär det att skalningsfaktorn är 50%.

{{% /alert %}}

Följande exempelkod illustrerar hur man beräknar sidlayoutskalningsfaktorn med hjälp av [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/)-egenskapen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
