---
title: Hitta eller söka data
type: docs
weight: 120
url: /sv/java/find-or-search-data/
---

{{% alert color="primary" %}} 

I Microsoft Excel kan användare söka efter celler som innehåller specifika data. Till exempel öppnas sökdialogen genom att klicka på **Redigera** och sedan **Sök**. Användare skriver in ett värde och klickar på **OK** för att söka efter det. Excel markera matchande fält.

**Använda Sök-dialogrutan för att hitta celler med ett specifikt värde** 

![todo:image_alt_text](find-or-search-data_1.png)

I detta exempel är sökvärdet "Apelsiner".

Aspose.Cells gör det möjligt för utvecklare att söka igenom cellerna i en arbetsbok för att hitta sådana som innehåller ett visst värde.

{{% /alert %}} 
## **Hitta celler som innehåller specifika data**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) innehåller [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), en samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) tillhandahåller [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), en samling som representerar alla celler i kalkylbladet. [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen tillhandahåller flera metoder för att hitta celler i ett kalkylblad som innehåller användarspecifik data. Några av dessa metoder diskuteras nedan mer detaljerat.

Alla sökmetoder returnerar cellreferenser för alla celler som innehåller det angivna sökvärdet.
## **Hitta med en formel**
Utvecklare kan hitta en angiven formel i kalkylbladet genom att anropa [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) metod, ställa in [FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) till [LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) och skicka det som parameter till [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) metod.

Vanligtvis accepterar [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) metoden två eller fler parametrar:

- Objekt att söka efter: representerar ett objekt som behöver hittas i kalkylbladet.
- Den föregående cellen: representerar den föregående cellen med samma formel. Denna parameter kan ställas in på null vid sökning från början.
- Sökalternativ: representerar sökkriterierna. I exemplen nedan används följande kalkylbladsdata för att öva på sökmetoderna:

**Exempel på kalkylbladsdata** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Söka efter strängar**
Det är enkelt och flexibelt att söka efter celler som innehåller en sträng. Det finns olika sätt att söka, till exempel söka efter celler som innehåller strängar som börjar med en specifik tecken eller teckenserie.
### **Söka efter strängar som börjar med specifika tecken**
För att söka efter den första tecknet i en sträng, ring [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) metod, ställ in [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) till [LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START-WITH) och skicka det som en parameter till [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) metoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Söka efter strängar som slutar med specifika tecken**
Aspose.Cells kan också hitta strängar som slutar med specifika tecken. För att söka efter de sista tecknen i en sträng, ring [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) metod, ställ in [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) till [LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END-WITH) och passera det som en parameter till [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) metoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Söka med reguljära uttryck: RegEx-funktionen**
Ett reguljärt uttryck ger ett kortfattat och flexibelt sätt att matcha (ange och känna igen) textsträngar, såsom särskilda tecken, ord eller mönster.

Till exempel matchar reguljärt uttrycksmönstret abc-*~~xyz~~ strängarna "abc-123-xyz", "abc-985-xyz" och "abc-pony-xyz". * är ett jokertecken så mönstret matchar alla strängar som börjar med "abc" och slutar med "-xyz", oavsett vilka tecken som finns i mitten.

Aspose.Cells tillåter dig att söka med reguljära uttryck.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Fortsatta ämnen**
- [Hitta celler med specifikt stil](/cells/sv/java/find-cells-with-specific-style/)
- [Sök data med originalvärden](/cells/sv/java/search-data-using-original-values/)
{{< app/cells/assistant language="java" >}}
