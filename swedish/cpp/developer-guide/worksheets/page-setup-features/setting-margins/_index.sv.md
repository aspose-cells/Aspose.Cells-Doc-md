---
title: Inställningar av marginaler med C++
linktitle: Inställning av marginaler
type: docs
weight: 20
url: /sv/cpp/setting-margins/
description: Lär dig hur man ställer in marginalerna för ett Excel ark med C++. Denna guide täcker inställning av sidmarginaler, centrering av innehåll och konfiguration av marginaler för sidhuvuden och sidfötter programmatiskt med Aspose.Cells for C++.
keywords: sätt Excel arbetsbladets marginal till centrerad c++, sätt arbetsbladets sidhuvud och sidfot marginal c++
---

{{% alert color="primary" %}}

Aspose.Cells stödjer helt Microsoft Excels siduppställningsalternativ. Utvecklare kan behöva konfigurera siduppställningsinställningarna för kalkylblad för att kontrollera utskriftsprocessen. Det här avsnittet diskuterar hur man använder Aspose.Cells för att konfigurera sidmarginaler.

{{% /alert %}}

## **Ställa in marginaler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samlingen som ger tillgång till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) erbjuder egenskapen [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) som används för att ställa in sidinställningsalternativ för ett arbetsblad. Attributet [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) är ett objekt av klassen [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) som möjliggör för utvecklare att ställa in olika sidlayoutegenskaper för ett utskrivet arbetsblad. Klassen [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) tillhandahåller olika egenskaper och metoder för att ställa in sidinställningar.

### **Sidmarginaler**

Ställ in sidmarginaler (vänster, höger, topp, botten) med hjälp av [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-klasser. Några av metoderna listas nedan som används för att specificera sidmarginaler:

- [**GetLeftMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getbottommargin/)

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set bottom, left, right, and top page margins
    pageSetup.SetBottomMargin(2);
    pageSetup.SetLeftMargin(1);
    pageSetup.SetRightMargin(1);
    pageSetup.SetTopMargin(3);

    // Save the Workbook
    workbook.Save(outDir + u"SetMargins_out.xls");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Centrera på sidan**

Det är möjligt att centrera något på en sida horisontellt och vertikalt. För detta finns några användbara medlemmar i [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-klassen, [**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/) och [**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Center on page Horizontally and Vertically
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered page setup!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sid- och fotmarginaler**

Ställ in sidhuvud- och sidfotsmarginaler med hjälp av [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-klassens medlemmar som [**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/) och [**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Header / Footer margins
    pageSetup.SetHeaderMargin(2);
    pageSetup.SetFooterMargin(2);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered header and footer margins!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
