---
title: Ställa in dynamiska matrisformler
description: Hur man använder Aspose.Cells-biblioteket för att beräkna dynamiska matrisformler i Microsoft Excel. Genom att ladda en befintlig Excel-fil eller skapa en ny Excel-fil kan vi använda metoden som tillhandahålls av Aspose.Cells för att beräkna den dynamiska matrisformeln och få resultatet. Slutligen sparar vi den modifierade Excel-filen på disken.
keywords: Dynamic Array Formulas, Dynamic Array Formulas in Excel, Set dynamic array formulas, Calculation of dynamic array formulas, operate dynamic array formulas of Excel.
type: docs
weight: 70
url: /sv/net/calculation-of-dynamic-array-formulas/
---
##  **Vad är Excel Array Formel**
I Excel är en matrisformel en speciell typ av formel som låter dig utföra beräkningar på datamatriser snarare än enskilda celler. Matrisformler kan användas för att utföra komplexa beräkningar, manipulera data och lösa specifika problem effektivt. De skrivs in annorlunda än vanliga formler och kräver ofta användning av Ctrl + Shift + Enter.

Här är några viktiga punkter om matrisformler i Excel:
1. Syntax:
<br>
Matrisformler skrivs som vanliga formler men involverar operationer på matriser av värden. De är inneslutna i klammerparenteser { } för att indikera att de är matrisformler. Du skriver dock inte dessa lockiga hängslen själv; Excel lägger till dem automatiskt när du anger formeln korrekt.
1. Ange matrisformler:
<br>
För att ange en matrisformel skriver du formeln i formelfältet.Istället för att trycka på Enter för att avsluta, trycker du på Ctrl + Skift + Enter. Detta talar om för Excel att det är en matrisformel. När den har angetts korrekt visar Excel formeln inom klammerparenteser i formelfältet för att indikera att det är en matrisformel.
1. Användningsfall:
<br>
Matrisformler är användbara för att utföra beräkningar över flera celler eller intervall samtidigt. De kan användas för avancerade matematiska beräkningar, villkorliga operationer, filtrering av data och mer.
1. Fördelar:
<br>
Matrisformler låter dig utföra komplexa beräkningar i en enda formel, vilket kan förbättra effektiviteten och förenkla dina kalkylblad. De kan hantera stora datamängder och utföra beräkningar som annars skulle kräva flera mellansteg.
1. Begränsningar:
<br>
Matrisformler kan vara svårare att förstå och felsöka än vanliga formler. De kan bromsa kalkylbladsprestanda, särskilt om de används i stor utsträckning eller med stora datamängder.
1. Exempel:
<br>
 Summera värdena i ett intervall:**{=SUMMA(A1:A5*B1:B5)}**
<br>
 Hitta det maximala värdet i ett intervall:**{=MAX(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

Kom ihåg att matrisformler bör användas med omtanke, och det är viktigt att förstå hur de fungerar innan du implementerar dem i dina kalkylblad. De kan vara kraftfulla verktyg för dataanalys och manipulation i Excel.

##  **Vad är Excel Dynamic Array Formula**
Dynamiska matrisformler är en ny funktion som introduceras i Excel 365 och Excel 2021. De låter dig arbeta med matriser av data mer sömlöst och effektivt jämfört med traditionella matrisformler. Dynamiska matrisformler spiller automatiskt in resultat i närliggande celler, vilket eliminerar behovet av Ctrl + Shift + Enter och möjliggör enklare manipulering av data.

Huvudpunkter om dynamiska matrisformler i Excel:
1. Automatiskt spill:
<br>
Dynamiska matrisformler spelar automatiskt in resultat i angränsande celler baserat på storleken på utdata. Det betyder att du inte behöver markera ett cellområde innan du anger formeln eller använd Ctrl + Skift + Retur för att bekräfta formeln.
1. Singel-Cell Post:
<br>
Dynamiska matrisformler skrivs in i en enskild cell och Excel fyller automatiskt i angränsande celler med resultaten. Detta gör det lättare att hantera och förstå formler, eftersom du bara behöver mata in formeln en gång.
1. Nya funktioner:
<br>
Dynamiska arrayformler introducerar nya funktioner som kan hantera arrayer inbyggt, som *FILTER**, *SORT**, *UNIQUE**, *SEQUENCE**, *SORTBY** och *RANDARRAY**. Dessa funktioner kan returnera flera värden eller manipulera matriser direkt, vilket förenklar komplexa beräkningar.
1. Flexibel räckviddshantering:
<br>
Dynamiska matrisformler justerar storleken på det utspillda området dynamiskt baserat på storleken på indata eller beräkningen som utförs. Denna flexibilitet möjliggör effektivare användning av kalkylbladsutrymme och förenklar skapandet av formel.
1. Förbättrad prestanda:
<br>
Dynamiska matrisformler kan förbättra prestandan jämfört med traditionella matrisformler, särskilt när du arbetar med stora datamängder eller komplexa beräkningar.
1. Kompatibilitet:
<br>
Dynamiska matrisformler är tillgängliga i Excel 365 och Excel 2021. De kanske inte stöds i äldre versioner av Excel.
1. Exempel på dynamiska matrisformler:
<br>
*FILTER**: Returnerar en matris med värden som uppfyller angivna kriterier.
<br>
*SORTERA**: Sorterar värdena i ett område eller en matris.
<br>
*UNIQUE**: Returnerar unika värden från en lista eller ett område.
<br>
*SEKVENS**: Genererar en sekvens av tal eller datum.
<br>
*RANDARRAY**: Genererar en matris med slumptal.
<br>
<image src="2.png" width="70%" />
<br>

Dynamiska matrisformler erbjuder kraftfulla möjligheter för datamanipulation och analys i Excel, vilket gör det lättare att arbeta med datamatriser och utföra komplexa beräkningar effektivt.

##  **Vad är skillnaden mellan matrisformler och dynamiska matrisformler i Excel**
I Excel används både matrisformler och dynamiska matrisformler för att utföra beräkningar på flera värden samtidigt, men de har vissa skillnader när det gäller funktionalitet och hur de implementeras.

###  **Funktioner för matrisformler**
1. Matrisformler är traditionella formler i Excel som kan utföra beräkningar på matriser av data.
1. De skrivs in genom att trycka på Ctrl + Skift + Enter efter att ha skrivit formeln, vilket talar om för Excel att det är en matrisformel.
1. Matrisformler har begränsningar när det gäller deras förmåga att spilla resultat till intilliggande celler. De returnerar vanligtvis ett 1. enstaka resultat, även om det resultatet kan vara en cellmatris.
1. De har funnits länge och stöds i alla versioner av Excel.

###  **Funktioner för dynamiska arrayformler**
1. Dynamiska matrisformler är en ny funktion som introduceras i Excel 365 (Office 365-prenumeration) och Excel 2021.
1. De överför automatiskt resultat till intilliggande celler baserat på storleken på indata eller formelns beräkning.
1. Dynamiska matrisformler kräver inte att du trycker på Ctrl + Shift + Enter; du skriver helt enkelt in formeln i en cell, och Excel fyller automatiskt de intilliggande cellerna med resultaten.
1. Dessa formler har förmågan att returnera flera resultat (ett intervall av celler) direkt utan behov av en matrisformel eller Ctrl + Skift + Enter.
1. De har nya funktioner som *FILTER**, *SORT**, *UNIQUE**, etc., som kan hantera arrayer inbyggt och returnera resultat i ett dynamiskt arrayformat.
Sammanfattningsvis är dynamiska matrisformler ett modernare och bekvämare sätt att arbeta med matriser i Excel, vilket ger automatiskt spill av resultat och förenklar processen att arbeta med matriser jämfört med traditionella matrisformler. De är dock bara tillgängliga i de nyare versionerna av Excel som stöder dynamiska arrayer.

##  **Hur man ställer in och beräknar dynamiska matrisformler i Excel**
 Att ställa in dynamiska arrayformler i Excel innebär att man använder specifika funktioner som är designade för att fungera med arrayer av data och låter resultaten automatiskt spilla in i angränsande celler.

Här är en steg-för-steg-guide för att ställa in dynamiska matrisformler:
1. Välj Cell:
<br>
Välj den cell där du vill att resultaten av dynamiska arrayformler ska visas. Dynamiska arrayformler överför resultaten till intilliggande celler, så se till att det finns tillräckligt med utrymme för den utspillda utmatningen.
1. Ange formeln:
<br>
 Skriv den dynamiska matrisformeln i formelfältet i den markerade cellen. Använd en av de dynamiska array-funktionerna som är tillgängliga i Excel 365 och Excel 2021, till exempel *FILTER**, *SORT**, *UNIQUE**, *SEQUENCE**, *SORTBY** eller *RANDARRAY**.
<br>
Till exempel kan du använda FILTER-funktionen för att filtrera en lista med data baserat på specifika kriterier: *=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.
<br>
<image src="3.png" width="70%" />
<br>
1. Tryck enter:
<br>
När du har skrivit formeln trycker du bara på Enter på tangentbordet. Till skillnad från traditionella matrisformler behöver du inte trycka på Ctrl + Skift + Enter.
1. Observera det utspillda området:
<br>
Excel överför automatiskt resultaten av formeln till närliggande celler. Det utspillda området justeras dynamiskt baserat på storleken på utdata eller beräkningen som utförs av formeln. Excel markerar det utspillda området med en ram och en diagonal pilikon för att indikera att den innehåller utspilld data.
1. Interagera med det spillda området:
<br>
Du kan interagera med det utspillda området precis som alla andra cellområden i Excel. Använd det utspillda området i andra formler, utför beräkningar på det, formatera det eller referera till det i diagram eller tabeller.
1. Uppdatera formeln:
<br>
Om du behöver ändra den dynamiska matrisformeln, redigera helt enkelt formeln i den ursprungliga cellen där den skrevs in.
Efter redigering, tryck på Enter igen för att bekräfta ändringarna. Excel kommer automatiskt att uppdatera det utspillda intervallet vid behov.
1. Rensa det utspillda området:
<br>
Om du vill rensa utspilld data kan du ta bort formeln från den ursprungliga cellen. Excel kommer också att rensa det utspillda området. Alternativt kan du ta bort det utspillda området direkt genom att markera det och trycka på Delete-tangenten.
<br>

Genom att följa dessa steg kan du ställa in dynamiska matrisformler i Excel för att effektivt analysera och manipulera datamatriser, vilket möjliggör enklare dataanalys och rapporteringsuppgifter.

##  **Så här ställer du in och uppdaterar dynamiska matrisformler med Aspose.Cells**
 Se följande exempelkod som laddar[exempel på Excel-fil](dynamicArrayFormula.xlsx) som innehåller lite dummydata. Efter att ha laddat filen, ring[Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) funktion för att ställa in dynamisk matrisformel och[Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) funktion för att uppdatera dynamiska matrisformler innan formelberäkning anropas och slutligen spara arbetsboken som[utdata Excel-fil](out.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

Utgångsbilden:
<br>
<image src="4.png" width="70%" />