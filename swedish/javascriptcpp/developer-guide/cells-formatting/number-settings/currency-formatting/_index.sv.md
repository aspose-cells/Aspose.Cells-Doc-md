---
title: Hur man formaterar nummer som valuta
type: docs
weight: 10
url: /sv/javascript-cpp/format-number-to-currency/
description: Denna artikel introducerar hur man formaterar nummer till valuta med hjälp av Aspose.Cells for JavaScript via C++ API.
keywords: format nummer som valuta, cellnummerinställningar, formatera nummer till valuta, valutasättningar, valutaformat.
---

## **Möjliga användningsscenario**
Att formatera nummer till valuta i Excel är viktigt av flera skäl, särskilt när man arbetar med finansiella data. Här är varför valutaanpassning är fördelaktigt:

1. Klargör finansiella värden: att formatera ett nummer som valuta gör det tydligt att värdet representerar pengar. Till exempel, istället för att se 1000, vilket kan betyda vad som helst, tydliggör $1 000 att det är ett penningbelopp.
1. Inkluderar valutasymboler: när du hanterar internationella eller flera valutor, att formatera nummer med rätt valutasymbol (t.ex. $, €, £) tydliggör typen av valuta som används, minskar förvirringen i multinationella finansiella rapporter eller transaktioner.
1. Förbättrar professionell presentation: välformaterade valutavärden verkar polerade och professionella, vilket är särskilt viktigt för rapporter, presentationer och affärsdokument. $10 000,00 ser mer trovärdigt och organiserat ut än ett vanligt 10000.
1. Förbättrar läsbarheten: valutastil lägger till kommatecken som tusentalsavgränsare och decimaler, vilket gör stora tal lättare att läsa. Till exempel, 1000000 blir $1 000 000,00, vilket är mer lättläst och lättare att förstå vid en snabb blick.
1. Garanti för konsekvens: genom att tillämpa konsekvent valutastil, säkerställer du att alla penningvärden i en dataset visas i samma format. Denna konsekvens är viktig för finansiell noggrannhet och för professionell kommunikation, särskilt i stora kalkylblad med många siffror.
1. Visar precision: valutastil inkluderar vanligtvis två decimaler, vilket gör det lätt att se exakta penningbelopp. Till exempel, $100.50 är tydligt olika från $100.00, vilket är viktigt i finansiella rapporter där precision spelar roll.
1. Förenklar finansiella beräkningar: vid utförande av finansiella beräkningar (som att summera totalsummor eller beräkna genomsnittskostnader), hjälper valutastil Excel och användare att förstå att datapunkterna är i penningtermer. Det hjälper Excel att tillämpa lämplig formatering i formler och funktioner, vilket säkerställer att resultaten förblir konsekventa.
1. Minskar missförstånd: utan valutastil kan siffror missförstås som generella numeriska värden snarare än belopp av pengar. Till exempel, 500 kan misstolkas som en kvantitet av artiklar eller enheter, medan $500,00 tydligt representerar ett finansiellt belopp.
1. Arbetar med redovisningsfunktioner: valutastil är väl anpassad för funktioner inom bokföring i Excel, såsom balansräkningar eller kassaflödesrapporter. Det gör värden lättare att använda i finansiella rapporter där pengar är den primära fokus.
<br>
Sammanfattningsvis hjälper formatering av nummer som valuta att skilja monetära värden från andra typer av nummer, ökar tydligheten och gör data lättare att tolka, särskilt i finansiella sammanhang.

## **Hur man formaterar nummer till valuta i Excel**
Följ dessa steg för att formatera nummer som valuta i Excel:

### **Använda valutaformatalternativet**
1. Markera cellerna du vill formatera som valuta.
1. Gå till fliken Hem i menyfliksområdet.
1. I gruppen Nummer, klicka på nedåtpilen bredvid rutan för nummerformat (det kan visa "Allmänt" som standard).
<br>
<img src="1.png" width=60% />
1. Välj Valuta från listan.

### **Med hjälp av dialogrutan Formatera celler**
1. Markera cellerna du vill formatera.
1. Högerklicka på de valda cellerna och välj Formatera celler för att öppna dialogrutan Formatera celler.
1. I fliken Nummer, välj Valuta från listan till vänster.
<br>
<img src="2.png" width=60% />
1. Du kan anpassa följande: Decimala platser, Symbol, Negativa tal.
1. Klicka på OK för att tillämpa formateringen.

## **Hur man formaterar nummer till valuta i Aspose.Cells**

För att formatera nummer som valuta i Aspose.Cells for JavaScript via C++ bibliotek för att arbeta med Excel-filer, kan du programmera applikationen för att tillämpa valuta formatering på celler. Så här gör du med Aspose.Cells for JavaScript via C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Currency Formatting Example</h1>
        <p>Optionally select an Excel file to modify. If no file is selected, a new workbook will be created.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value to the cell
            a1.value = 1234.56;

            // Create a style object to apply the currency format
            const a1Style = a1.style;
            // "7" is the currency format in Excel
            a1Style.number = 7;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 3456.78;

            // Create a style object to apply the currency format
            const a2Style = a2.style;
            // Custom format for dollar currency
            a2Style.custom = "$#,##0.00";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CurrencyFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CurrencyFormatted.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
