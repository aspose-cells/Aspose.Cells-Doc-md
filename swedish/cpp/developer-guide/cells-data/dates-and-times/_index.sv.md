---
title: Hur man hanterar datum och tider med C++
linktitle: Komma åt och hantera datum och tider
type: docs
weight: 600
url: /sv/cpp/how-to-manage-dates-and-times/
description: Lär dig hur du hanterar datum och tider med hjälp av API Aspose.Cells for C++.
keywords: Komma åt och hantera datum och tider, 1900 datumsystemet, 1904 datumsystemet, Ange datum och tider, Hämta datum och tider, Hantera datum och tider, Lagra datum och tider i Excel, Visa datum och tider i celler.
---

## **Hur man lagrar datum och tider i Excel**
 Datum och tider lagras i celler som nummer. Värdena i celler som innehåller datum och tider är således numeriska. Ett nummer som anger ett datum och en tid består av datum (heltal) och tid (bråkdelar). Metoden `Cell::GetDoubleValue()` returnerar detta nummer.

## **Hur man visar datum och tider i Aspose.Cells**
För att visa ett nummer som datum och tid, applicera det önskade datum- och tidsformatet på en cell via metoderna `Style::SetNumber()` eller `Style::SetCustom()`. Metoden `Cell::GetDateTimeValue()` returnerar ett `DateTime`-objekt, som specificerar datum och tid som anges av numret i en cell.
<br>
<image src="1.png" width="70%" />

## **Hur man växlar mellan två datum system i Aspose.Cells**
MS-Excel lagrar datum som nummer som kallas seriella värden. Ett seriellt värde är ett heltal som är antalet passerade dagar från den första dagen i datum systemet. Excel stöder följande datum system för seriella värden:

1. 1900-datum systemet. Det första datumet är den 1 januari 1900 och dess seriella värde är 1. Det sista datumet är den 31 december 9999 och dess seriella värde är 2 958 465. Detta datum system används som standard i arbetsboken.
1. 1904-datumssystemet. Det första datumet är 1 januari 1904, och dess serienummer är 0. Det sista datumet är 31 december 9999, och dess serienummer är 2 957 003. För att använda detta datumssystem i arbetsboken, ställ in egenskapen `Workbook::GetSettings()->SetDate1904(true)`.

Detta exempel visar att de seriella värden som lagras på samma datum i olika datum system är olika.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    workbook.GetSettings().SetDate1904(false);

    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(45237.0);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.GetDoubleValue() << std::endl;
    }

    workbook.GetSettings().SetDate1904(true);
    std::cout << "use The 1904 date system====================" << std::endl;

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(43775.0);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.GetDoubleValue() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
Resultat av utmatning:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Hur man anger datumvärde i Aspose.Cells**
Detta exempel sätter ett `DateTime`-värde i cell A1 och A2, ställer in anpassat format för A1 och numeriskt format för A2, och skriver ut värdetyperna.

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    time_t now = time(nullptr);
    double oaDate1 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a1.PutValue(oaDate1);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    now = time(nullptr);
    double oaDate2 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a2.SetValue(oaDate2);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

Resultat av utmatning:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Hur man får DateTime-värde i Aspose.Cells**
Detta exempel sätter ett `DateTime`-värde i cell A1 och A2, ställer in anpassat format för A1 och numeriskt format för A2, kontrollerar värdetyperna för de två cellerna och skriver ut `DateTime`-värdet samt formaterad sträng.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(Date{2023, 5, 15});

    if (a1.GetType() == CellValueType::IsNumeric) {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
        Date dateTimeValue = a1.GetDateTimeValue();
        std::cout << "A1 DateTime String Value: " << a1.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(Date{2023, 5, 16});

    if (a2.GetType() == CellValueType::IsNumeric) {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
        Date dateTimeValue = a2.GetDateTimeValue();
        std::cout << "A2 DateTime String Value: " << a2.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Resultat av utmatning:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
{{< app/cells/assistant language="cpp" >}}
