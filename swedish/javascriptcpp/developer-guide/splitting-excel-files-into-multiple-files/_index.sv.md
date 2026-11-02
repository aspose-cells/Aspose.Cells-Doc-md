---
title: Dela upp Excel-filer i flera filer
linktitle: Dela upp Excel-filer i flera filer
description: Aspose.Cells for JavaScript via C++ är ett JavaScript via C++-bibliotek för att arbeta med kalkylbladsfiler, som stödjer att dela upp en enda Excel-fil i flera filer. Denna artikel visar hur man delar upp Excel-filer genom att kopiera varje kalkylblad till en separat arbetsbok och genom att kopiera specifika cellintervall till andra arbetsböcker.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ library, kalkylblad, dela upp Excel-fil, kopiera kalkylblad, kopiera intervall, flera arbetsböcker, spara som separata filer
type: docs
weight: 195
url: /sv/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ stödjer att dela upp en enda Excel-fil i flera filer. Det finns två huvudsakliga sätt att göra detta: (1) genom att kopiera varje kalkylblad i källarbetsboken till en ny arbetsbok och spara varje som en separat fil, och (2) genom att kopiera ett specifikt cellintervall från ett kalkylblad till en ny arbetsbok. Båda metoderna är användbara när du behöver distribuera delmängder av data, skapa mindre rapporter för olika mottagare eller isolera data för individuell bearbetning.
{{% /alert %}}

## **Introduktion**
Det finns många verkliga scenarier där en utvecklare behöver dela upp en enda Excel‑fil i flera mindre filer. Till exempel kan en arbetsbok innehålla ett kalkylblad per avdelning, och varje avdelningschef behöver bara få sitt eget blad. I andra fall kan du vilja extrahera en viss tabell eller ett datablock från ett kalkylblad och skicka det som en fristående fil via e‑post, utan att avslöja resten av arbetsboken. Stora konsoliderade arbetsböcker kan också behöva delas upp i mindre delar för enklare hantering, snabbare inläsning eller vidare bearbetning av andra system.
Aspose.Cells for JavaScript via C++ erbjuder två flexibla tillvägagångssätt för denna uppgift. Det första tillvägagångssättet itererar igenom varje kalkylblad i källarbetsboken och kopierar dess innehåll till en helt ny `Workbook`‑instans, som sparas som en separat fil. Det andra fokuserar på ett specifikt cellintervall inom ett kalkylblad och kopierar endast det intervallet till en ny arbetsbok. I båda fallen är det allmänna flödet detsamma: ladda källarboken med `Workbook`‑klassen, få åtkomst till data via `Worksheet`‑ och `Cells`‑objekten, överför innehållet till en destinations‑`Workbook` och spara sedan destinationen till disk.

## **Dela upp en Excel‑fil genom att kopiera varje kalkylblad till en ny arbetsbok**

### **Översikt över tillvägagångssättet**
I detta tillvägagångssätt öppnas källarboken en gång, och för varje `Worksheet` i dess `Worksheets`‑samling skapas en ny destinations‑`Workbook`. Innehållet i källkalkylbladet kopieras sedan till det första kalkylbladet i destinationsarboken, och arbetsboken sparas som en fil vars namn hämtas från källkalkylbladets namn. Resultatet blir en utdatafil per kalkylblad, där varje fil innehåller data från ett enskilt källblad.  
Denna metod är rätt val när varje kalkylblad i din källarbok representerar en logiskt oberoende informationsenhet (såsom en avdelning, region, månad eller produktlinje) och du vill leverera eller bearbeta varje enhet separat.

### **Steg**
Följande steg beskriver hur du delar upp en Excel‑fil genom att kopiera varje kalkylblad till en ny arbetsbok:
1. Öppna käll‑Excel‑filen genom att skapa ett `Workbook`‑objekt och skicka in filsökvägen till dess konstruktor.  
2. Iterera igenom `Workbook.Worksheets`‑samlingen med en `for`‑ eller `for…of`‑loop så att varje `Worksheet` i källfilen behandlas.  
3. Inuti loopen skapar du en ny destinations‑`Workbook`‑instans (en tom arbetsbok) för det aktuella kalkylbladet.  
5. Kopiera innehållet i källkalkylbladet till destinationskalkylbladet. Detta kan göras genom att iterera cellerna i källkalkylbladets `Cells`‑samling och skriva deras värden till motsvarande celler i destinationskalkylbladet, eller genom att använda `Cells.Copy`‑metoden för att överföra ett helt intervall på en gång.  
6. Konstruera en utfilssökväg som inkluderar källkalkylbladets namn (t.ex. `dataDir + worksheet.Name + ".xls"`), så att varje genererad fil får ett unikt namn.  
7. Anropa destinations‑`Workbook.Save`‑metoden för att skriva filen till disk.  
8. Upprepa steg 3‑7 för nästa kalkylblad tills alla kalkylblad har behandlats.

### **Kodexempel**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

Det förväntade resultatet är en uppsättning nya filer i datakatalogen, en fil per kalkylblad från källarboken. Varje fil får namn efter motsvarande källblad och innehåller data (och eventuellt formatering) från just det bladet.

## **Dela upp en Excel‑fil genom att kopiera ett intervall till en ny arbetsbok**

### **Översikt över tillvägagångssättet**
Ibland motsvarar data som du behöver dela upp inte ett helt kalkylblad utan snarare ett specifikt rektangulärt område i ett kalkylblad, såsom `A1:D10` eller ett namngivet intervall som representerar en viss tabell. I sådana fall är det slöseri att kopiera hela kalkylbladet, och ett mer precist tillvägagångssätt krävs: identifiera källintervallet, kopiera endast det intervallet till en ny arbetsbok och spara den nya filen.  
Detta tillvägagångssätt är idealiskt när du vill extrahera en enskild tabell, rapportblock eller dataområde från ett större kalkylblad samtidigt som allt orelaterat innehåll tas bort. Det är även användbart för att exportera användarvalda områden i ett blad som fristående filer.

### **Steg**
Följande steg beskriver hur du delar upp en Excel‑fil genom att kopiera ett specifikt intervall till en ny arbetsbok:
1. Öppna käll‑Excel‑filen genom att skapa ett `Workbook`‑objekt med filsökvägen.  
2. Hämta mål‑`Worksheet` som innehåller det intervall du vill kopiera, antingen via index (t.ex. det första bladet) eller via namn från `Worksheets`‑samlingen.  
3. Identifiera intervallet som ska kopieras. Detta kan vara ett hårdkodat cellintervall som `A1:C10`, ett namngivet intervall erhållet via `Worksheet.Cells`‑samlingen, eller ett intervall skapat via `Worksheet.Cells.CreateRange`.  
4. Skapa en ny destinations‑`Workbook`‑instans.  
5. Åtkomst till det första `Worksheet` i destinationsarboken (standardbladet).  
6. Kopiera källintervallet till destinationskalkylbladet, vanligtvis med start i cell `A1`. `Cells.Copy`‑metoden på destinations‑`Cells`‑samlingen kan användas för att kopiera ett helt intervall, eller så kan du iterera genom källintervallets celler och skriva deras värden till destinationscellerna med `PutValue`. Valfria `CopyOptions` kan anges för att styra vad som överförs (endast värden, värden och format, formler osv.).  
7. Spara destinationsarboken till en ny filsökväg på disk med `Workbook.Save`‑metoden.

### **Kodexempel**
Det förväntade resultatet är en enda ny fil i datakatalogen som endast innehåller värdena (och eventuellt formateringen) för det angivna intervallet som extraherats från källarboken. Destinationsfilen har ingen relation till någon annan data i källfilen; den innehåller bara det extraherade intervallet, med start i cell `A1` i dess första kalkylblad.

## Relaterade artiklar
- [Lägg till filterfält i en Pivottabell i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/add-page-field-in-pivot-table/)
- [Tillämpa format på Pivottabeller i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)
- [Ändra layout för sidfält i Pivottabell](/cells/sv/javascript-cpp/change-page-field-layout/)
- [Konvertera Sparkline till bild och HTML i Aspose.Cells for JavaScript via C++](/cells/sv/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}