---
title: Nummerinställningar
description: Aspose.Cells är ett Python bibliotek för att arbeta med kalkylblad som stöder många olika inställningar för cellnummer. Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att hantera cellernas nummerinställningar så att användare kan justera nummerformatet i kalkylbladet vid behov.
keywords: Aspose.Cells, Python bibliotek, elektroniskt kalkylblad, cellnummerinställningar, formatering, hantering, Format av Nummer och Datum
type: docs
weight: 10
url: /sv/python-net/cells-number-settings/
---

## **Hur man ställer in visningsformat för nummer och datum**

En mycket stark funktion hos Microsoft Excel är att det tillåter användare att ställa in visningsformat för numeriska värden och datum. Vi vet att numeriska data kan användas för att representera olika värden inklusive decimal, valuta, procent, bråk eller bokföringsvärden, etc. Alla dessa numeriska värden visas i olika format beroende på vilken typ av information det representerar. På samma sätt finns det många format på vilket ett datum eller tid kan visas.
Aspose.Cells för Python via .NET stöder denna funktionalitet och tillåter utvecklare att ställa in önskat visningsformat för ett nummer eller datum.

### **Hur man ställer in visningsformat i Microsoft Excel**

För att ställa in visningsformat i Microsoft Excel:

1. Högerklicka på vilken cell som helst.
1. Välj **Format för celler**. En dialogruta visas som används för att ställa in visningsformat för vilken typ av värde som helst.

På vänstra sidan av dialogrutan finns många kategorier av värden som **Allmänt**, **Tal**, **Valuta**, **Bokföring**, **Datum**, **Tid**, **Procent**, etc. Aspose.Cells för Python via .NET stöder alla dessa visningsformat.

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-samling som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells för Python via .NET tillhandahåller [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) och [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) metoder för [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-klassen. Dessa används för att hämta och ställa in cellens formatering. Klassen [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) ger några användbara egenskaper för att hantera visningsformaten för nummer och datum.

### **Hur man använder inbyggda nummerformat**

Aspose.Cells för Python via .NET erbjuder några inbyggda nummerformat för att konfigurera visningsformaten för nummer och datum. Dessa inbyggda nummerformat kan tillämpas med hjälp av [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number)-egenskapen hos [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objektet. Alla inbyggda nummerformat har unika numeriska värden. Utvecklare kan tilldela vilket önskat numeriskt värde som helst till [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number)-egenskapen hos [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objektet för att tillämpa visningsformatet. Denna metod är snabb. De inbyggda nummerformaten som stöds av Aspose.Cells listas nedan.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **Hur man använder egna nummerformat**

För att definiera din anpassade formatsträng för att ställa in visningsformatet, använd [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objektets [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)-egenskap. Denna metod är inte lika snabb som att använda förinställda format, men den är mer flexibel.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

Om du använder [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)-egenskapen för att ställa in nummerformatet, skrivs eventuellt tidigare format som ställts in med [**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number)-egenskapen över och vice versa.

{{% /alert %}}

## **Fortsatta ämnen**
- [Kontrollera anpassat nummerformat vid inställning av Style.Custom-egenskap](/cells/sv/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [Lista över stödda nummerformat](/cells/sv/python-net/list-of-supported-number-formats/)
- [Rendera anpassat datumformatmönster g och ge mm dd](/cells/sv/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Ange anpassade nummerdecimaler och gruppavgränsare för Arbetsbok](/cells/sv/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specificera DBNum anpassade mönsterformatering](/cells/sv/python-net/specifying-dbnum-custom-pattern-formatting/)

{{< app/cells/assistant language="python-net" >}}
