---
title: Nummerinställningar
type: docs
weight: 10
url: /sv/java/cells-number-settings/
---
##  **Ställa in visningsformat för Numbers och datum**

En mycket stark egenskap hos Microsoft Excel är att den tillåter användare att ställa in visningsformat för numeriska värden och datum. Vi vet att numeriska data kan användas för att representera olika värden inklusive decimal-, valuta-, procent-, bråk- eller redovisningsvärden, etc. Alla dessa numeriska värden visas i olika format beroende på vilken typ av information den representerar. På samma sätt finns det många format där ett datum eller en tid kan visas.
Aspose.Cells stöder denna funktion och låter utvecklare ställa in valfritt visningsformat för ett nummer eller datum.

##  **Ställa in visningsformat i Microsoft Excel**

Så här ställer du in visningsformat i Microsoft Excel:

1. Högerklicka på valfri cell.
1. Välj *Format Cells**. En dialogruta kommer att visas som används för att ställa in visningsformat av alla slags värden.

 I den vänstra sidan av dialogrutan finns det många kategorier av värden som**Allmänt**, **Antal**, **Valuta**, **Redovisning**, **Datum**, **Tid**, **Procentandel,**etc. Aspose.Cells stöder alla dessa visningsformat.

##  **Använda inbyggda nummerformat**

 Aspose.Cells erbjuder några inbyggda talformat för att konfigurera visningsformaten för siffror och datum. Alla inbyggda talformat ges unika numeriska värden. Utvecklare kan tilldela vilket önskat numeriskt värde som helst till[**siffra**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) metod för[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/style) objekt för att tillämpa visningsformatet. Detta tillvägagångssätt är snabbt. De inbyggda talformaten som stöds av Aspose.Cells listas nedan.

|**Värde**|**Typ**|**Formatera sträng**|
| :- | :- | :- |
|0|General|Allmän|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Röd]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Röd]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0,00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|m/d/åååå|
|15|Date|d-mmm-åå|
|16|Date|d-mmm|
|17|Date|mmm-åå|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/åå h:mm|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[Röd]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[Röd]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|## 0,0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

##  **Använda anpassade nummerformat**

 För att definiera din egen anpassade formatsträng för att ställa in visningsformatet, använd[**Beställnings**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Detta tillvägagångssätt är inte lika snabbt som att använda förinställda format men det är mer flexibelt.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Om du använder[**Beställnings**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) för att ställa in talformatet, alla tidigare format som ställts in med hjälp av[**siffra**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Ange anpassade nummerdecimaler och gruppavgränsare för arbetsbok](/cells/sv/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Ange DBNum anpassad mönsterformatering](/cells/sv/java/specifying-dbnum-custom-pattern-formatting/)
