---
title: Specificering av DBNum anpassat mönsterformat med C++
linktitle: Ange DBNum anpassad pattern formatering
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler som stöder formatering av datum och nummer med hjälp av anpassade formateringsmönster. Den här artikeln visar hur man använder Aspose.Cells biblioteket för att specificera det anpassade formatmönstret dbnum så att användare får mer kontroll över hur nummer visas.
keywords: Aspose.Cells, C++ bibliotek, elektroniskt kalkylblad, anpassat formatmönster, formatering, dbnum , kontrollera visning
type: docs
weight: 110
url: /sv/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Möjliga användningsscenario**

Aspose.Cells stöder *DBNum* anpassat mönsterformat. Till exempel, om din cellvärde är 123 och du specificerar dess anpassade formatering som [DBNum2][$-804]Allmänt, kommer det att visas som 壹佰贰拾叁. Du kan specificera din anpassade formatering av cellen med [**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)-metoden och [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)-egenskapen.

## **Exempelkod**

Följande exempel visar hur man specificerar anpassad *DBNum*-mönsterformatering. Kontrollera dess [utdata PDF](43352081.pdf) för mer hjälp.

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
