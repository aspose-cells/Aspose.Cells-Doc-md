---
title: Använd skuggning på alternativa rader och kolumner med villkorlig formatering
type: docs
weight: 30
url: /sv/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells API:er ger möjlighet att lägga till och manipulera regler för villkorlig formatering för[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)objekt. Dessa regler kan skräddarsys på ett antal sätt för att få önskad formatering baserat på villkor eller regler. Den här artikeln kommer att demonstrera användningen av Aspose.Cells for .NET API:er för att tillämpa skuggning på alternerande rader och kolumner med hjälp av regler för villkorlig formatering och Excels inbyggda funktioner.

{{% /alert %}}

Den här artikeln använder sig av Excels inbyggda funktioner som ROW, COLUMN & MOD. Här är några detaljer om dessa funktioner för en bättre förståelse av kodavsnittet som tillhandahålls i förväg.

- **RAD()** funktion returnerar radnumret för en cellreferens. Om referensparametern utelämnas antar den att referensen är den celladress där ROW-funktionen har skrivits in.
- **KOLUMN()** funktion returnerar kolumnnumret för en cellreferens. Om referensparametern utelämnas, förutsätter den att referensen är den celladress där funktionen COLUMN har skrivits in.
- **MOD()** funktion returnerar resten efter att ett tal har dividerats med en divisor, där den första parametern till funktionen är det numeriska värdet vars återstod du vill hitta och den andra parametern är talet som används för att dela in i talparametern. Om divisorn är 0, kommer den att returnera #DIV/0! fel.

Låt oss börja skriva lite kod för att uppnå detta mål med hjälp av Aspose.Cells for .NET API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

Följande ögonblicksbild visar det resulterande kalkylbladet laddat i Excel-applikationen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
|:- |

 För att tillämpa skuggningen på alternativa kolumner behöver du bara ändra formeln**=MOD(RAD();2)=0** som**=MOD(KOLUMN(),2)=0** , det är; istället för att hämta radindexet, ändra formeln för att hämta kolumnindexet.
Det resulterande kalkylarket, i det här fallet, kommer att se ut som följer.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
|:- |
