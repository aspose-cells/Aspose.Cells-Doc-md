---
title: Nummerinställningar med Golang via C++
linktitle: Nummerinställningar
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler som stöder många olika nummerinställningar för celler. Denna artikel visar hur man använder Aspose.Cells biblioteket för att hantera nummersättningar i cellerna så att användare kan justera nummerformatet i kalkylbladet efter behov.
keywords: Aspose.Cells, C++ bibliotek, elektroniskt kalkylblad, cellnummerinställningar, formatering, hantering, nummer och datumformat
type: docs
weight: 10
url: /sv/go-cpp/cells-number-settings/
---

## **Hur man ställer in visningsformat för nummer och datum**

En mycket stark funktion hos Microsoft Excel är att det tillåter användare att ställa in visningsformat för numeriska värden och datum. Vi vet att numeriska data kan användas för att representera olika värden inklusive decimal, valuta, procent, bråk eller bokföringsvärden, etc. Alla dessa numeriska värden visas i olika format beroende på vilken typ av information det representerar. På samma sätt finns det många format på vilket ett datum eller tid kan visas.
Aspose.Cells stöder denna funktion och tillåter utvecklare att ställa in vilket visningsformat som helst för ett nummer eller ett datum.

### **Hur man ställer in visningsformat i Microsoft Excel**

För att ställa in visningsformat i Microsoft Excel:

1. Högerklicka på vilken cell som helst.
1. Välj **Format för celler**. En dialogruta visas som används för att ställa in visningsformat för vilken typ av värde som helst.

På vänster sida av dialogrutan finns det många kategorier av värden som **Allmänt**, **Nummer**, **Valuta**, **Bokföring**, **Datum**, **Tid**, **Procent**, etc. Aspose.Cells stöder alla dessa visningsformat.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) innefattar en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells tillhandahåller metoder [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) och [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) för klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Dessa metoder används för att få och sätta formateringen för en cell. Klassen [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) tillhandahåller några användbara egenskaper för att hantera visningsformat för nummer och datum.

### **Hur man använder inbyggda nummerformat**

Aspose.Cells erbjuder några inbyggda nummerformat för att konfigurera visningsformaten för numren och datum. Dessa inbyggda nummerformat kan tillämpas med hjälp av egenskapen [**Number**](https://reference.aspose.com/cells/go-cpp/style/getnumber/) för objektet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Alla inbyggda nummerformat tilldelas unika numeriska värden. Utvecklare kan tilldela önskat numeriskt värde till egenskapen [**Number**](https://reference.aspose.com/cells/go-cpp/style/getnumber/) för objektet [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) för att tillämpa visningsformatet. Detta tillvägagångssätt är snabbt. De inbyggda nummerformat som stöds av Aspose.Cells listas nedan.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberSettings.go" >}}
### **Hur man använder egna nummerformat**

För att definiera din anpassade formatsträng för att ställa in visningsformatet, använd [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-objektets [**Custom**](https://reference.aspose.com/cells/go-cpp/style/getcustom/)-egenskap. Denna metod är inte lika snabb som att använda förinställda format, men den är mer flexibel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberSettings-1.go" >}}
{{% alert color="primary" %}}

Om du använder [**Custom**](https://reference.aspose.com/cells/go-cpp/style/getcustom/)-egenskapen för att ställa in nummerformatet, skrivs eventuellt tidigare format som ställts in med [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/)-egenskapen över och vice versa.

{{% /alert %}}

## **Fortsatta ämnen**
- [Kontrollera anpassat nummerformat vid inställning av Style.Custom-egenskap](/cells/sv/cpp/check-custom-number-format-when-setting-style-custom-property/)
- [Lista över stödda nummerformat](/cells/sv/cpp/list-of-supported-number-formats/)
- [Rendera anpassat datumformatmönster g och ge mm dd](/cells/sv/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Ange anpassade nummerdecimaler och gruppavgränsare för Arbetsbok](/cells/sv/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specificera DBNum anpassade mönsterformatering](/cells/sv/cpp/specifying-dbnum-custom-pattern-formatting/)
