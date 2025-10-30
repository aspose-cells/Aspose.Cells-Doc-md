---
title: Nummerinställningar med C++
linktitle: Nummerinställningar
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler som stöder många olika nummerinställningar för celler. Denna artikel visar hur man använder Aspose.Cells biblioteket för att hantera nummersättningar i cellerna så att användare kan justera nummerformatet i kalkylbladet efter behov.
keywords: Aspose.Cells, C++ bibliotek, elektroniskt kalkylblad, cellnummerinställningar, formatering, hantering, nummer och datumformat
type: docs
weight: 10
url: /sv/cpp/cells-number-settings/
---

## **Hur man ställer in visningsformat för nummer och datum**

En mycket stark funktion hos Microsoft Excel är att det tillåter användare att ställa in visningsformat för numeriska värden och datum. Vi vet att numeriska data kan användas för att representera olika värden inklusive decimal, valuta, procent, bråk eller bokföringsvärden, etc. Alla dessa numeriska värden visas i olika format beroende på vilken typ av information det representerar. På samma sätt finns det många format på vilket ett datum eller tid kan visas.
Aspose.Cells stöder denna funktion och tillåter utvecklare att ställa in vilket visningsformat som helst för ett nummer eller ett datum.

### **Hur man ställer in visningsformat i Microsoft Excel**

För att ställa in visningsformat i Microsoft Excel:

1. Högerklicka på vilken cell som helst.
1. Välj **Format för celler**. En dialogruta visas som används för att ställa in visningsformat för vilken typ av värde som helst.

På vänster sida av dialogrutan finns det många kategorier av värden som **Allmänt**, **Nummer**, **Valuta**, **Bokföring**, **Datum**, **Tid**, **Procent**, etc. Aspose.Cells stöder alla dessa visningsformat.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innefattar en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells tillhandahåller metoder [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) och [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) för klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Dessa metoder används för att få och sätta formateringen för en cell. Klassen [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) tillhandahåller några användbara egenskaper för att hantera visningsformat för nummer och datum.

### **Hur man använder inbyggda nummerformat**

Aspose.Cells erbjuder några inbyggda nummerformat för att konfigurera visningsformaten för numren och datum. Dessa inbyggda nummerformat kan tillämpas med hjälp av egenskapen [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) för objektet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Alla inbyggda nummerformat tilldelas unika numeriska värden. Utvecklare kan tilldela önskat numeriskt värde till egenskapen [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) för objektet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) för att tillämpa visningsformatet. Detta tillvägagångssätt är snabbt. De inbyggda nummerformat som stöds av Aspose.Cells listas nedan.

|**Värde**|**Typ**|**Formatsträng**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::time_t now = std::time(nullptr);
    double excelDate = static_cast<double>(now) / 86400.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetNumber(15);
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetNumber(9);
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetNumber(6);
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hur man använder egna nummerformat**

För att definiera din anpassade formatsträng för att ställa in visningsformatet, använd [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-objektets [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)-egenskap. Denna metod är inte lika snabb som att använda förinställda format, men den är mer flexibel.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    auto now = std::chrono::system_clock::now();
    auto duration = now.time_since_epoch();
    auto hours = std::chrono::duration_cast<std::chrono::hours>(duration).count();
    double excelDate = hours / 24.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetCustom(u"d-mmm-yy");
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetCustom(u"0.0%");
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetCustom(u"£#,##0;[Red]$-#,##0");
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Om du använder [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)-egenskapen för att ställa in nummerformatet, skrivs eventuellt tidigare format som ställts in med [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/)-egenskapen över och vice versa.

{{% /alert %}}

## **Fortsatta ämnen**
- [Kontrollera anpassat nummerformat vid inställning av Style.Custom-egenskap](/cells/sv/cpp/check-custom-number-format-when-setting-style-custom-property/)
- [Lista över stödda nummerformat](/cells/sv/cpp/list-of-supported-number-formats/)
- [Rendera anpassat datumformatmönster g och ge mm dd](/cells/sv/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Ange anpassade nummerdecimaler och gruppavgränsare för Arbetsbok](/cells/sv/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specificera DBNum anpassade mönsterformatering](/cells/sv/cpp/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="cpp" >}}
