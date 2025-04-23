---
title: Nummerinställningar
type: docs
weight: 10
url: /sv/java/cells-number-settings/
---

## **Inställning av visningsformat för nummer och datum**

En mycket stark funktion hos Microsoft Excel är att det tillåter användare att ställa in visningsformat för numeriska värden och datum. Vi vet att numeriska data kan användas för att representera olika värden inklusive decimal, valuta, procent, bråk eller bokföringsvärden, etc. Alla dessa numeriska värden visas i olika format beroende på vilken typ av information det representerar. På samma sätt finns det många format på vilket ett datum eller tid kan visas.
Aspose.Cells stöder denna funktion och tillåter utvecklare att ställa in vilket visningsformat som helst för ett nummer eller ett datum.

## **Inställning av visningsformat i Microsoft Excel**

För att ställa in visningsformat i Microsoft Excel:

1. Högerklicka på vilken cell som helst.
1. Välj **Format för celler**. En dialogruta visas som används för att ställa in visningsformat för vilken typ av värde som helst.

På vänster sida av dialogrutan finns det många kategorier av värden som **Allmänt**, **Nummer**, **Valuta**, **Bokföring**, **Datum**, **Tid**, **Procent**, etc. Aspose.Cells stöder alla dessa visningsformat.

## **Använda inbyggda nummerformat**

Aspose.Cells erbjuder några inbyggda nummerformat för att konfigurera visningsformaten för nummer och datum. Alla inbyggda nummerformat har unika numeriska värden. Utvecklare kan tilldela vilket önskat numeriskt värde som helst till [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number)-metoden för objektet [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) för att tillämpa visningsformatet. Detta tillvägagångssätt är snabbt. De inbyggda nummerformat som stöds av Aspose.Cells listas nedan.

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Använda anpassade nummerformat**

För att definiera din egen anpassade formatsträng för att ställa in visningsformatet, använd [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Detta tillvägagångssätt är inte lika snabbt som att använda förinställda formatmen det är mer flexibelt.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

Om du använder [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) för att ställa in nummerformatet, överskrivs eventuellt tidigare format som ställts in med [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) och vice versa.

{{% /alert %}}

## **Fortsatta ämnen**
- [Kontrollera anpassat nummerformat vid inställning av Style.Custom-egenskap](/cells/sv/java/check-custom-number-format-when-setting-style-custom-property/)
- [Ange anpassade nummerdecimaler och gruppavgränsare för Arbetsbok](/cells/sv/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specificera DBNum anpassade mönsterformatering](/cells/sv/java/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="java" >}}
