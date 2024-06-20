---
title: Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering
type: docs
weight: 10
url: /sv/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells API:er ger möjligheter att lägga till och manipulera villkorlig formateringsregler för [Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objekt. Dessa regler kan anpassas på olika sätt för att få önskad formatering baserat på villkor eller regler. Denna artikel kommer att visa användningen av Aspose.Cells for Java API för att applicera skuggning på alternerande rader och kolumner med hjälp av villkorlig formatering och Excels inbyggda funktioner.

{{% /alert %}} 
## **Applicera skuggning på alternerande rader och kolumner med hjälp av villkorlig formatering**
Denna artikel använder Excels inbyggda funktioner såsom ROW, COLUMN & MOD. Här är lite detaljer om dessa funktioner för en bättre förståelse av kodsnutten som presenteras nedan.

- **ROW()**-funktionen returnerar radnumret för en cellreferens. Om referensen utelämnas antar den att referensen är celladressen där ROW-funktionen har infogats.
- Funktionen **COLUMN()** returnerar kolumnnumret för en cellreferens. Om referensen utelämnas antar den att referensen är celladressen där COLUMN-funktionen har infogats.
- **MOD()**-funktionen returnerar resten efter att ett nummer har delats av en divisor, där det första parametern till funktionen är det numeriska värdet vars rest du vill hitta och det andra parametern är det tal som används för att dela in i nummerparametern. Om divisorn är 0 kommer den att returnera felen #DIV/0!.

Låt oss börja skriva lite kod för att uppnå målet med hjälp av Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



Följande ögonblicksbild visar det resulterande kalkylarket som är laddat i Excel-applikationen.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

För att applicera nyanser på alternativa kolumner, behöver du bara ändra formeln **=MOD(RAD(),2)=0** till **=MOD(KOLUMN(),2)=0**, det vill säga; istället för att få radindexet, modifiera formeln för att hämta kolumnindexet. 
Den resulterande kalkylbladet kommer i detta fall se ut som den följande bilden.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
