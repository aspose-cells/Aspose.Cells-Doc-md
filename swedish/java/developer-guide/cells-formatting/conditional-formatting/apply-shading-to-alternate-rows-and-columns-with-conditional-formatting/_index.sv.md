---
title: Använd skuggning på alternativa rader och kolumner med villkorlig formatering
type: docs
weight: 10
url: /sv/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells API:er ger möjlighet att lägga till och manipulera regler för villkorlig formatering för[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objekt. Dessa regler kan skräddarsys på ett antal sätt för att få önskad formatering baserat på villkor eller regler. Den här artikeln kommer att demonstrera användningen av Aspose.Cells for Java API för att tillämpa skuggning på alternerande rader och kolumner med hjälp av villkorliga formateringsregler och Excels inbyggda funktioner.

{{% /alert %}} 
## **Använd skuggning på alternativa rader och kolumner med villkorlig formatering**
Den här artikeln använder sig av Excels inbyggda funktioner som ROW, COLUMN & MOD. Här är små detaljer om dessa funktioner för en bättre förståelse av kodavsnittet som tillhandahålls i förväg.

- **RAD()** funktion returnerar radnumret för en cellreferens. Om referensen utelämnas antar den att referensen är den celladress där ROW-funktionen har skrivits in.
- **KOLUMN()**funktion returnerar kolumnnumret för en cellreferens. Om referensen utelämnas, förutsätter den att referensen är den celladress där funktionen COLUMN har skrivits in.
- **MOD()** funktion returnerar resten efter att ett tal har dividerats med en divisor, där den första parametern till funktionen är det numeriska värdet vars återstod du vill hitta och den andra parametern är talet som används för att dela in i talparametern. Om divisorn är 0, kommer den att returnera #DIV/0! fel.

Låt oss börja skriva lite kod för att uppnå målet med hjälp av Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



Följande ögonblicksbild visar det resulterande kalkylbladet laddat i Excel-applikationen.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

 För att tillämpa skuggningen på alternativa kolumner behöver du bara ändra formeln**=MOD(RAD();2)=0** som**=MOD(KOLUMN(),2)=0** , det är; istället för att hämta radindexet, ändra formeln för att hämta kolumnindexet.
Det resulterande kalkylarket, i det här fallet, kommer att se ut som följande bild.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
