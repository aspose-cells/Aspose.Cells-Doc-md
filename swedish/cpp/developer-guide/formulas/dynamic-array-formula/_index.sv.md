---  
title: Ställa in dynamiska arrayformler med C++  
description: Hur man använder Aspose.Cells biblioteket för att beräkna dynamiska arrayformler i Microsoft Excel med C++.  
keywords: Dynamiska arrayformler, Dynamiska arrayformler i Excel, Ange dynamiska arrayformler, Beräkning av dynamiska arrayformler, Operera dynamiska arrayformler av Excel.  
type: docs  
weight: 70  
url: /sv/cpp/calculation-of-dynamic-array-formulas/  
---  

## **Vad är Excel Array Formula**  
I Excel är en arrayformel en särskild typ av formel som gör det möjligt att utföra beräkningar på datamatriser istället för individuella celler. Arrayformler kan användas för att utföra komplexa beräkningar, manipulera data och effektivt lösa specifika problem. De används på ett annat sätt än vanliga formler och kräver ofta användning av Ctrl + Skift + Retur.  

Här är några viktiga punkter om arrayformler i Excel:  
1. **Syntax:**  
Arrayformler skrivs som vanliga formler men innehåller operationer på matriser av värden. De är inneslutna i måsvingar { } för att ange att de är arrayformler. Du skriver dock inte dessa måsvingar själv; Excel lägger till dem automatiskt när du skriver in formeln korrekt.  
1. **Inmatning av arrayformler:**  
För att mata in en matrisformel skriver du formeln i formelfältet. Istället för att trycka Enter för att avsluta, trycker du Ctrl + Shift + Enter. Detta berättar för Excel att det är en matrisformel. När den är korrekt inmatad visar Excel formeln inom klammerparenteser i formelfältet för att ange att det är en matrisformel.  
1. **Användningsområden:**  
Arrayformler är användbara för att utföra beräkningar över flera celler eller områden samtidigt. De kan användas för avancerade matematiska beräkningar, villkorliga operationer, filtrering av data och mer.  
1. **Fördelar:**  
Arrayformler gör det möjligt att utföra komplexa beräkningar i en enda formel, vilket kan förbättra effektiviteten och förenkla dina kalkylblad. De kan hantera stora datamängder och utföra beräkningar som annars skulle kräva flera mellansteg.  
1. **Begränsningar:**  
Arrayformler kan vara svårare att förstå och felsöka än vanliga formler. De kan sakta ner kalkylbladets prestanda, särskilt om de används omfattande eller med stora datamängder.  
1. **Exempel:**  
Summera värdena i en rad: **{=SUM(A1:A5*B1:B5)}**  
Hitta det högsta värdet i en rad: **{=MAX(A1:A5+B1:B5)}**  
<br><image src="1.png" width="70%" />  
<br>  
Kom ihåg att arrayformler bör användas med omdöme, och det är viktigt att förstå hur de fungerar innan de implementeras i dina arbetsblad. De kan vara kraftfulla verktyg för dataanalys och bearbetning i Excel.  

## **Vad är Excel Dynamisk Array Formel**  
Dynamiska arrayformler är en ny funktion som introducerades i Excel 365 och Excel 2021. De tillåter dig att arbeta med datamängder mer sömlöst och effektivt jämfört med traditionella arrayformler. Dynamiska arrayformler spiller automatiskt resultat i intilliggande celler, vilket eliminerar behovet av Ctrl + Skift + Enter och möjliggör enklare bearbetning av data.  

Nyckelpunkter om dynamiska arrayformler i Excel:  
1. **Automatiskt Spill:**  
Dynamiska arrayformler spiller automatiskt resultat i intilliggande celler baserat på storleken på utdata. Detta innebär att du inte behöver välja en mängd celler innan du anger formeln eller använda Ctrl + Skift + Enter för att bekräfta formeln.  
1. **Enskild Cells-inmatning:**  
Dynamiska arrayformler matas in i en enda cell, och Excel fyller automatiskt i intilliggande celler med resultaten. Det gör det enklare att hantera och förstå formler, eftersom du bara behöver mata in formeln en gång.  
1. **Nya Funktioner:**  
Dynamiska arrayformler introducerar nya funktioner som kan hantera arrayer naturligt, såsom **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY** och **RANDARRAY**. Dessa funktioner kan returnera flera värden eller manipulera arrayer direkt, vilket förenklar komplexa beräkningar.  
1. **Flexibel hantering av område:**  
Dynamiska arrayformler justerar storleken på spilld utdata dynamiskt baserat på storleken på indata eller beräkningen som utförs. Denna flexibilitet möjliggör effektivare användning av arbetsboksspace och förenklar skapandet av formler.  
1. **Förbättrad prestanda:**  
Dynamiska arrayformler kan förbättra prestandan jämfört med traditionella arrayformler, särskilt vid arbete med stora datasets eller komplexa beräkningar.  
1. **Kompatibilitet:**  
Dynamiska arrayformler finns i Excel 365 och Excel 2021. De kanske inte stöds i äldre versioner av Excel.  
1. **Exempel på dynamiska matrisformler:**  
**FILTER**: Returnerar en mängd värden som uppfyller specificerade kriterier.  
**SORT**: Sorterar värdena i en rad eller array.  
**UNIQUE**: Returnerar unika värden från en lista eller rad.  
**SEQUENCE**: Genererar en sekvens av nummer eller datum.  
**RANDARRAY**: Genererar en array av slumpmässiga nummer.  
<br><image src="2.png" width="70%" />  
<br>  
Dynamiska arrayformler erbjuder kraftfulla möjligheter för dataanalys och manipulation i Excel, vilket gör det enklare att arbeta med datamängder och utföra komplexa beräkningar effektivt.  

## **Vad är skillnaden mot Arrayformler och Dynamiska Arrayformler i Excel**  
I Excel används både arrayformler och dynamiska arrayformler för att utföra beräkningar på flera värden samtidigt, men de har vissa skillnader vad gäller funktionalitet och hur de implementeras.  

### **Arrayformler Funktioner**  
1. Arrayformler är traditionella formler i Excel som kan utföra beräkningar på datarrayer.  
1. De matas in genom att trycka på Ctrl + Skift + Enter efter att ha skrivit formeln, vilket talar om för Excel att det är en arrayformel.  
1. Matrisformler har begränsningar när det gäller deras förmåga att spilling till intilliggande celler. De returnerar vanligtvis ett enda resultat, även om det kan vara en cellmatris.  
1. De har funnits länge och stöds i alla versioner av Excel.  

### **Dynamiska array formler Funktioner**  
1. Dynamiska arrayformler är en ny funktion som introducerades i Excel 365 (Office 365-prenumeration) och Excel 2021.  
1. De sprider automatiskt resultat i intilliggande celler baserat på storleken på indata eller formelns beräkning.  
1. Dynamiska arrayformler kräver inte att du trycker på Ctrl + Skift + Enter; du skriver helt enkelt in formeln i en cell, och Excel fyller automatiskt i intilliggande celler med resultaten.  
1. Dessa formler har förmågan att returnera flera resultat (en rad celler) direkt utan behov av en matrisformel eller Ctrl + Skift + Enter.  
1. De har nya funktioner som **FILTER**, **SORT**, **UNIQUE**, etc., som kan hantera matriser på ett naturligt sätt och returnera resultat i en dynamisk matrisformat.  
Sammanfattningsvis är dynamiska arrayformler ett mer modernt och bekvämt sätt att arbeta med matriser i Excel, vilket ger automatisk spretning av resultat och förenkla processen att arbeta med matriser jämfört med traditionella arrayformler. De är dock endast tillgängliga i de nyare versionerna av Excel som stödjer dynamiska arrayer.  

## **Hur man ställer in och beräknar dynamiska arrayformler i Excel**  
Att ställa in dynamiska arrayformler i Excel innebär att man använder specifika funktioner som är utformade för att fungera med datamatriser och tillåter resultat att automatiskt spridas in i intilliggande celler.  

Här är en steg-för-steg-guide för att ställa in dynamiska arrayformler:  
1. **Välj cell:**  
Välj cellen där du vill att resultatet av den dynamiska arrayformeln ska visas. Dynamiska arrayformler sprider resultaten till intilliggande celler, så se till att det finns tillräckligt med utrymme för det spridna resultatet.  
1. **Ange formeln:**  
Skriv in den dynamiska arrayformeln i formelfältet för den valda cellen. Använd en av de dynamiska arrayfunktionerna som finns i Excel 365 och Excel 2021, som **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY**, eller **RANDARRAY**.  
Till exempel kan du använda FILTER-funktionen för att filtrera en lista med data baserat på specifika kriterier: **=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br><image src="3.png" width="70%" />  
<br>  
1. **Tryck på Enter:**  
Efter att ha skrivit formeln, tryck helt enkelt på Enter på ditt tangentbord. Till skillnad från traditionella arrayformler behöver du inte trycka på Ctrl + Skift + Enter.  
1. **Observera spillområdet:**  
Excel sprider automatiskt resultaten av formeln till intilliggande celler. Det spridda intervallet justeras dynamiskt baserat på storleken på utdata eller beräkningen som utförs av formeln. Excel markerar det spridda intervallet med en ram och en diagonalpilikon för att indikera att det innehåller spridda data.  
1. **Interagera med spillområdet:**  
Du kan interagera med det spridda intervallet precis som vilket annat cellintervall som helst i Excel. Använd det spridda intervallet i andra formler, utför beräkningar på det, formatera det, eller referera till det i diagram eller tabeller.  
1. **Uppdatera formeln:**  
Om du behöver ändra den dynamiska arrayformeln, redigera helt enkelt formeln i den ursprungliga cellen där den angavs.  
Efter redigering, tryck på Enter igen för att bekräfta ändringarna. Excel kommer automatiskt att uppdatera det spridda intervallet vid behov.  
1. **Rensa spillområdet:**  
Om du vill rensa de spridda datan kan du ta bort formeln från den ursprungliga cellen. Excel kommer också att rensa det spridda intervallet. Alternativt kan du ta bort det spridda intervallet direkt genom att markera det och trycka på Delete-tangenten.  
<br>  
Genom att följa dessa steg kan du ställa in dynamiska arrayformler i Excel för att effektivt analysera och manipulera datamatriser, vilket möjliggör enklare dataanalys och rapportuppgifter.  

## **Hur man ställer in och Uppdatera dynamiska arrayformler med Aspose.Cells**  
Se följande exempel på kod som laddar den [exempel Excel-fil](dynamicArrayFormula.xlsx) som innehåller dummydata. Efter att ha laddat filen, anropa funktionen [Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) för att ställa in en dynamisk matrisformel och [Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) för att uppdatera dynamiska matrisformler innan du utför formelberäkning, och spara slutligen arbetsboken som [utdata Excel-fil](out.xlsx).  

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(u"dynamicArrayFormula.xlsx");

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Getting the F16 
    Cell f16 = ws.GetCells().Get(u"F16");

    // Set dynamic array formula
    FormulaParseOptions formulaParseOptions;
    f16.SetDynamicArrayFormula(u"=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", formulaParseOptions, false);

    // Refresh the dynamic array formulas
    workbook.RefreshDynamicArrayFormulas(true);

    workbook.CalculateFormula();
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```  

Utgångsbild:  
<br><image src="4.png" width="70%" />  
{{< app/cells/assistant language="cpp" >}}
