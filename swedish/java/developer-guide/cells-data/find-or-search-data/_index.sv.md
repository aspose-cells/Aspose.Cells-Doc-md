---
title: Hitta eller sök data
type: docs
weight: 120
url: /sv/java/find-or-search-data/
---
{{% alert color="primary" %}} 

 I Microsoft Excel kan användare söka efter celler som innehåller specifika data. Till exempel att klicka**Redigera** och då**Hitta** öppnar dialogrutan Sök. Användare anger ett värde och klickar**OK** att söka efter det. Excel markerar matchande fält.

**Använda dialogrutan Sök för att hitta celler som innehåller ett specifikt värde** 

![todo:image_alt_text](find-or-search-data_1.png)

det här exemplet är sökvärdet "Apelsiner".

Aspose.Cells tillåter utvecklare att söka igenom cellerna i ett kalkylblad för att hitta de som innehåller ett givet värde.

{{% /alert %}} 
## **Hitta Cells som innehåller specifika data**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) , som representerar en Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) klass innehåller[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) , en samling som ger åtkomst till vart och ett av kalkylbladen i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass.

 De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) , en samling som representerar alla celler i kalkylbladet[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling innehåller flera metoder för att hitta celler i ett kalkylblad som innehåller användarspecificerad data. Några av dessa metoder diskuteras mer i detalj nedan.

Alla sökmetoder returnerar cellreferenserna för alla celler som innehåller det angivna sökvärdet.
## **Hitta som innehåller en formel**
 Utvecklare kan hitta en specificerad formel i kalkylbladet genom att anropa[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens[hitta](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) ) metoden, ställa in[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) till[LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)och skicka det som en parameter till[hitta](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) metod.

 Vanligtvis är[hitta](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) metod accepterar två eller flera parametrar:

- Objekt att söka: representerar ett objekt som behövs för att hitta i kalkylbladet.
- Den föregående Cell: representerar föregående cell med samma formel. Denna parameter kan ställas in på null när du söker från början.
- Sökalternativ: representerar sökkriterierna. I exemplen nedan används följande kalkylbladsdata för att öva på att hitta metoder:

**Exempel på kalkylbladsdata** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Söker efter strängar**
Att söka efter celler som innehåller ett strängvärde är enkelt och flexibelt. Det finns olika sätt att söka, till exempel söka efter celler som innehåller strängar som börjar med ett visst tecken, eller en uppsättning tecken.
### **Söker efter strängar som börjar med specifika tecken**
 För att söka efter det första tecknet i en sträng, anropa[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens[hitta](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) metod, ställ in[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) till[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)och skicka den som en parameter till[hitta](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Söker efter strängar som slutar med specifika tecken**
 Aspose.Cells kan också hitta strängar som slutar med specifika tecken. För att söka efter de sista tecknen i en sträng, anropa[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens[hitta](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) metod, ställ in[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) till[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)och skicka den som en parameter till[hitta](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Söka med reguljära uttryck: RegEx-funktionen**
Ett reguljärt uttryck ger ett kortfattat och flexibelt sätt att matcha (specificera och känna igen) textsträngar, såsom särskilda tecken, ord eller mönster.

Till exempel, det reguljära uttrycksmönstret abc-* ~~xyz~~ matchar strängarna "abc-123-xyz", "abc-985-xyz" och "abc-pony-xyz".* är ett jokertecken så mönstret matchar alla strängar som börjar med "abc" och slutar med "-xyz", oavsett vilka tecken som finns i mitten.

Aspose.Cells låter dig söka med reguljära uttryck.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Förhandsämnen**
- [Hitta celler med specifik stil](/cells/sv/java/find-cells-with-specific-style/)
- [Sök efter data med originalvärden](/cells/sv/java/search-data-using-original-values/)
