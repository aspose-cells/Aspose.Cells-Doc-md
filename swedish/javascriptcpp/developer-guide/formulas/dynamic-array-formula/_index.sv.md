---
title: Ställa in dynamiska matrismetaforer med JavaScript via C++
linktitle: Inställning Dynamiska Formelmatriser
description: Hur man använder Aspose.Cells bibliotek för att beräkna dynamiska matrismetaforer i Excel med JavaScript via C++. Ladda, beräkna och spara Excelfiler enkelt.
keywords: Dynamiska matrismetaforer, dynamiska matrismetaforer i Excel, sätta dynamiska matrismetaforer JavaScript via C++, beräkning av dynamiska matrismetaforer JavaScript via C++, operera dynamiska matrismetaforer i Excel.
type: docs
weight: 70
url: /sv/javascript-cpp/calculation-of-dynamic-array-formulas/
---

## **Vad är Excel Array Formula**  
I Excel är en arrayformel en särskild typ av formel som gör det möjligt att utföra beräkningar på datamatriser istället för individuella celler. Arrayformler kan användas för att utföra komplexa beräkningar, manipulera data och effektivt lösa specifika problem. De används på ett annat sätt än vanliga formler och kräver ofta användning av Ctrl + Skift + Retur.

Här är några viktiga punkter om arrayformler i Excel:  
1. Syntax:  
<br>  
Arrayformler skrivs som vanliga formler men innehåller operationer på matriser av värden. De är inneslutna i måsvingar { } för att ange att de är arrayformler. Du skriver dock inte dessa måsvingar själv; Excel lägger till dem automatiskt när du skriver in formeln korrekt.  
2. Mata in arrayformler:  
<br>  
För att mata in en matrisformel skriver du formeln i formelfältet. Istället för att trycka Enter för att avsluta, trycker du Ctrl + Shift + Enter. Detta berättar för Excel att det är en matrisformel. När den är korrekt inmatad visar Excel formeln inom klammerparenteser i formelfältet för att ange att det är en matrisformel.  
3. Användningsområden:  
<br>  
Arrayformler är användbara för att utföra beräkningar över flera celler eller områden samtidigt. De kan användas för avancerade matematiska beräkningar, villkorliga operationer, filtrering av data och mer.  
4. Fördelar:  
<br>  
Arrayformler gör det möjligt att utföra komplexa beräkningar i en enda formel, vilket kan förbättra effektiviteten och förenkla dina kalkylblad. De kan hantera stora datamängder och utföra beräkningar som annars skulle kräva flera mellansteg.  
5. Begränsningar:  
<br>  
Arrayformler kan vara svårare att förstå och felsöka än vanliga formler. De kan sakta ner kalkylbladets prestanda, särskilt om de används omfattande eller med stora datamängder.  
6. Exempel:  
<br>  
Summera värdena i en rad: **{=SUM(A1:A5*B1:B5)}**  
<br>  
Hitta det högsta värdet i en rad: **{=MAX(A1:A5+B1:B5)}**  
<br>  
<image src="1.png" width="70%" />  
<br>  

Kom ihåg att arrayformler bör användas med omdöme, och det är viktigt att förstå hur de fungerar innan de implementeras i dina arbetsblad. De kan vara kraftfulla verktyg för dataanalys och bearbetning i Excel.

## **Vad är Excel Dynamisk Array Formel**  
Dynamiska arrayformler är en ny funktion som introducerades i Excel 365 och Excel 2021. De tillåter dig att arbeta med datamängder mer sömlöst och effektivt jämfört med traditionella arrayformler. Dynamiska arrayformler spiller automatiskt resultat i intilliggande celler, vilket eliminerar behovet av Ctrl + Skift + Enter och möjliggör enklare bearbetning av data.

Nyckelpunkter om dynamiska arrayformler i Excel:  
1. Automatisk Spillning:  
<br>  
Dynamiska arrayformler spiller automatiskt resultat i intilliggande celler baserat på storleken på utdata. Detta innebär att du inte behöver välja en mängd celler innan du anger formeln eller använda Ctrl + Skift + Enter för att bekräfta formeln.  
2. Enkelcellsinmatning:  
<br>  
Dynamiska arrayformler matas in i en enda cell, och Excel fyller automatiskt i intilliggande celler med resultaten. Det gör det enklare att hantera och förstå formler, eftersom du bara behöver mata in formeln en gång.  
3. Nya funktioner:  
<br>  
Dynamiska arrayformler introducerar nya funktioner som kan hantera arrayer naturligt, såsom **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY** och **RANDARRAY**. Dessa funktioner kan returnera flera värden eller manipulera arrayer direkt, vilket förenklar komplexa beräkningar.  
4. Flexibel hantering av intervall:  
<br>  
Dynamiska arrayformler justerar storleken på spilld utdata dynamiskt baserat på storleken på indata eller beräkningen som utförs. Denna flexibilitet möjliggör effektivare användning av arbetsboksspace och förenklar skapandet av formler.  
5. Förbättrad prestanda:  
<br>  
Dynamiska arrayformler kan förbättra prestandan jämfört med traditionella arrayformler, särskilt vid arbete med stora datasets eller komplexa beräkningar.  
6. Kompatibilitet:  
<br>  
Dynamiska arrayformler finns i Excel 365 och Excel 2021. De kanske inte stöds i äldre versioner av Excel.  
7. Exempel på dynamiska arrayformler:  
<br>  
**FILTER**: Returnerar en mängd värden som uppfyller specificerade kriterier.  
<br>  
**SORT**: Sorterar värdena i en rad eller array.  
<br>  
**UNIQUE**: Returnerar unika värden från en lista eller rad.  
<br>  
**SEQUENCE**: Genererar en sekvens av nummer eller datum.  
<br>  
**RANDARRAY**: Genererar en array av slumpmässiga nummer.  
<br>  
<image src="2.png" width="70%" />  
<br>  

Dynamiska arrayformler erbjuder kraftfulla möjligheter för dataanalys och manipulation i Excel, vilket gör det enklare att arbeta med datamängder och utföra komplexa beräkningar effektivt.

## **Vad är skillnaden mot Arrayformler och Dynamiska Arrayformler i Excel**  
I Excel används både arrayformler och dynamiska arrayformler för att utföra beräkningar på flera värden samtidigt, men de har vissa skillnader vad gäller funktionalitet och hur de implementeras.

### **Arrayformler Funktioner**  
1. Arrayformler är traditionella formler i Excel som kan utföra beräkningar på datarrayer.  
2. De matas in genom att trycka på Ctrl + Shift + Enter efter att ha skrivit formeln, vilket säger till Excel att det är en matrisformel.  
3. Matrisformler har begränsningar när det gäller deras förmåga att sprida resultat till intilliggande celler. De returnerar vanligtvis ett enda resultat, även om det kan vara en cellmatris.  
4. De har funnits länge och stöds i alla versioner av Excel.

### **Dynamiska array formler Funktioner**  
1. Dynamiska arrayformler är en ny funktion som introducerades i Excel 365 (Office 365-prenumeration) och Excel 2021.  
2. De sprider automatiskt resultaten till intilliggande celler baserat på storleken på insatsdata eller formelns beräkning.  
3. Dynamiska matrisformler kräver inte att man trycker på Ctrl + Shift + Enter; du skriver helt enkelt formeln i en cell, och Excel fyller automatiskt på de intilliggande cellerna med resultaten.  
4. Dessa formler har förmågan att returnera flera resultat (ett cellområde) direkt utan att behöva en matrisformel eller Ctrl + Shift + Enter.  
5. De har nya funktioner som **FILTER**, **SORT**, **UNIQUE**, etc., som kan hantera matriser natively och returnera resultat i ett dynamiskt matrisformat.  
Sammanfattningsvis är dynamiska arrayformler ett mer modernt och bekvämt sätt att arbeta med matriser i Excel, vilket ger automatisk spretning av resultat och förenkla processen att arbeta med matriser jämfört med traditionella arrayformler. De är dock endast tillgängliga i de nyare versionerna av Excel som stödjer dynamiska arrayer.

## **Hur man ställer in och beräknar dynamiska arrayformler i Excel**  
Att ställa in dynamiska arrayformler i Excel innebär att man använder specifika funktioner som är utformade för att fungera med datamatriser och tillåter resultat att automatiskt spridas in i intilliggande celler. 

Här är en steg-för-steg-guide för att ställa in dynamiska arrayformler:  
1. Välj cellen:  
<br>  
Välj cellen där du vill att resultatet av den dynamiska arrayformeln ska visas. Dynamiska arrayformler sprider resultaten till intilliggande celler, så se till att det finns tillräckligt med utrymme för det spridna resultatet.  
2. Ange formeln:  
<br>  
Skriv in den dynamiska arrayformeln i formelfältet för den valda cellen. Använd en av de dynamiska arrayfunktionerna som finns i Excel 365 och Excel 2021, som **FILTER**, **SORT**, **UNIQUE**, **SEQUENCE**, **SORTBY**, eller **RANDARRAY**.  
<br>  
Till exempel kan du använda FILTER-funktionen för att filtrera en lista med data baserat på specifika kriterier: **=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br>  
<image src="3.png" width="70%" />  
<br>  
3. Tryck på Enter:  
<br>  
Efter att ha skrivit formeln, tryck helt enkelt på Enter på ditt tangentbord. Till skillnad från traditionella arrayformler behöver du inte trycka på Ctrl + Skift + Enter.  
4. Observera det spillande området:  
<br>  
Excel sprider automatiskt resultaten av formeln till intilliggande celler. Det spridda intervallet justeras dynamiskt baserat på storleken på utdata eller beräkningen som utförs av formeln. Excel markerar det spridda intervallet med en ram och en diagonalpilikon för att indikera att det innehåller spridda data.  
5. Interagera med det spillande området:  
<br>  
Du kan interagera med det spridda intervallet precis som vilket annat cellintervall som helst i Excel. Använd det spridda intervallet i andra formler, utför beräkningar på det, formatera det, eller referera till det i diagram eller tabeller.  
6. Uppdatera formeln:  
<br>  
Om du behöver ändra den dynamiska matrisformeln, redigera helt enkelt formeln i den ursprungliga cellen där den matade in. Efter redigering, tryck på Enter igen för att bekräfta ändringarna. Excel uppdaterar automatiskt det spillande området om det är nödvändigt.  
7. Rensa det spillande området:  
<br>  
Om du vill rensa de spridda datan kan du ta bort formeln från den ursprungliga cellen. Excel kommer också att rensa det spridda intervallet. Alternativt kan du ta bort det spridda intervallet direkt genom att markera det och trycka på Delete-tangenten.  
<br>  

Genom att följa dessa steg kan du ställa in dynamiska arrayformler i Excel för att effektivt analysera och manipulera datamatriser, vilket möjliggör enklare dataanalys och rapportuppgifter.

## **Hur man ställer in och Uppdatera dynamiska arrayformler med Aspose.Cells**  
Se följande exempel kod som laddar den [exempel-Excel-fil](dynamicArrayFormula.xlsx) som innehåller some dummy data. Efter att ha laddat filen, anropa [Cell.dynamicArrayFormula(string, FormulaParseOptions, boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dynamicArrayFormula-string-formulaparseoptions-boolean-) för att ställa in dynamisk matrismetafor och [Workbook.refreshDynamicArrayFormulas(boolean)](https://reference.aspose.com/cells/javascript-cpp/workbook/#refreshDynamicArrayFormulas-boolean-) för att uppdatera dynamiska matrismetaforer innan du kör formelberäkning, och spara slutligen arbetsboken som [utdata Excel-fil](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Dynamic Array Formula Example</title>
    </head>
    <body>
        <h1>Dynamic Array Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormulaParseOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = wb.worksheets.get(0);

            // Getting the F16 cell
            const f16 = ws.cells.get("F16");

            // Set dynamic array formula (converted from setDynamicArrayFormula to property assignment)
            // Assigning an array containing the formula string, parse options object, and the boolean flag
            f16.dynamicArrayFormula = ["=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", new FormulaParseOptions(), false];

            // Refresh the dynamic array formulas
            wb.refreshDynamicArrayFormulas(true);

            // Calculate formulas
            wb.calculateFormula();

            // Saving the modified Excel file and preparing download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Utgångsbild:  
<br>  
<image src="4.png" width="70%" />  
<br>
