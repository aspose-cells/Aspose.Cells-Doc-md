---
title: Hur man lägger till/infogar TextBox i blad med C++
linktitle: Lägg till textfält i arbetsbladet
type: docs
weight: 10
url: /sv/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Hur man lägger till/infogar TextBox i blad i Aspose.Cells med C++.
keywords: lägg till/infoga textfält textfält arbetsblad Excel Aspose
---

## Lägg till textfält i arbetsbladet i Excel

I Excel-programmet (version 07 och senare) finns två platser där du kan infoga text lådor. En i "infoga-former", den andra är på högra sidan av toppmenyn för "Infoga"-alternativet.

### Metod ett:

![1](1.png)

### Metod två:

![2](2.png)

## Hur man skapar

Du kan skapa textfält med horisontell eller vertikal text.

- Välj motsvarande alternativ (horisontell eller vertikal)
- Vänsterklicka på sidan
- Håll ner vänsterknappen och dra en distans på sidan
- Släpp vänsterknappen

Nu har du ett textfält.

## Lägg till textfält i arbetsbladet i Aspose.Cells

När du behöver massinlägga TextBox i kalkbladet är den manuella insättningsmetoden självklart ett katastrof. Om detta stör dig tror jag att detta dokument hjälper dig. [Aspose.Cells](https://products.aspose.com/cells/) ger dig ett API för att enkelt göra bulkinsättningar i din kod.

Följande provkod skapar en textruta.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Du kommer att få en fil som liknar [resultatfilen](result.xlsx). I filen kommer du se följande:

![](52449.png)
{{< app/cells/assistant language="cpp" >}}
