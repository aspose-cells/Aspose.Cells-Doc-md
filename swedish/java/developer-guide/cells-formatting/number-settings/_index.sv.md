---
title: Nummerinställningar
type: docs
weight: 10
url: /sv/java/cells-number-settings/
---
## **Ställa in visningsformat för siffror och datum**

En mycket stark egenskap hos Microsoft Excel är att den tillåter användare att ställa in visningsformat för numeriska värden och datum. Vi vet att numeriska data kan användas för att representera olika värden inklusive decimal-, valuta-, procent-, bråk- eller redovisningsvärden, etc. Alla dessa numeriska värden visas i olika format beroende på vilken typ av information den representerar. På samma sätt finns det många format där ett datum eller en tid kan visas.
Aspose.Cells stöder denna funktion och låter utvecklare ställa in valfritt visningsformat för ett nummer eller datum.

## **Ställa in visningsformat i Microsoft Excel**

Så här ställer du in visningsformat i Microsoft Excel:

1. Högerklicka på valfri cell.
1.  Välj**Format Cells**. En dialogruta kommer att visas som används för att ställa in visningsformat av alla slags värden.

 I den vänstra sidan av dialogrutan finns det många kategorier av värden som**Allmän**, **siffra**, **Valuta**, **Bokföring**, **Datum**, **Tid**, **Procentsats,**etc. Aspose.Cells stöder alla dessa visningsformat.

## **Använda inbyggda nummerformat**

 Aspose.Cells erbjuder några inbyggda talformat för att konfigurera visningsformaten för siffror och datum. Alla inbyggda talformat ges unika numeriska värden. Utvecklare kan tilldela vilket önskat numeriskt värde som helst till[**siffra**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) metod för[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/style) objekt för att tillämpa visningsformatet. Detta tillvägagångssätt är snabbt. De inbyggda talformaten som stöds av Aspose.Cells listas nedan.

|**Värde**|**Typ**|**Formatera sträng**|
|:- |:- |:- |
|0|Allmän|Allmän|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Valuta|$#,##0;$-#,##0|
|6|Valuta|$#,##0;[Röd]$-#,##0|
|7|Valuta|$#,##0.00;$-#,##0.00|
|8|Valuta|$#,##0.00;[Röd]$-#,##0.00|
|9|Procentsats|0%|
|10|Procentsats|0.00%|
|11|Vetenskaplig|0,00E+00|
|12|Fraktion|# ?/?
|
|13|Fraktion|# */*
|
|14|Datum|m/d/åå|
|15|Datum|d-mmm-åå|
|16|Datum|d-mmm|
|17|Datum|mmm-åå|
|18|Tid|h:mm AM/PM|
|19|Tid|h:mm:ss AM/PM|
|20|Tid|h:mm|
|21|Tid|h:mm:ss|
|22|Tid|m/d/åå h:mm|
|37|Valuta|# ,##0;-#,##0
|
|38|Valuta|# ,##0;[Röd]-#,##0
|
|39|Valuta|# ,##0.00;-#,##0.00
|
|40|Valuta|# ,##0.00;[Röd]-#,##0.00
|
|41|Bokföring|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Bokföring|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Bokföring|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Bokföring|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Tid|mm:ss|
|46|Tid|h :mm:ss|
|47|Tid|mm:ss.0|
|48|Vetenskaplig|## 0,0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Använda anpassade nummerformat**

För att definiera din egen anpassade formatsträng för att ställa in visningsformatet, använd[**Beställnings**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Detta tillvägagångssätt är inte lika snabbt som att använda förinställda format men det är mer flexibelt.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Om du använder[**Beställnings**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) för att ställa in talformatet, alla tidigare format som ställts in med hjälp av[**siffra**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Ange anpassade nummerdecimaler och gruppavgränsare för arbetsbok](/cells/sv/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Ange DBNum anpassad mönsterformatering](/cells/sv/java/specifying-dbnum-custom-pattern-formatting/)
