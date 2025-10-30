---
title: Hur man ställer in utskriftstitlar med JavaScript via C++
linktitle: Hur man ställer in Utskriftsrubriker
type: docs
weight: 200
url: /sv/javascript-cpp/how-to-set-print-titles/
description: Denna artikel visar hur man ställer in utskriftstitlar med Aspose.Cells biblioteket för JavaScript via C++.
keywords: Skriv ut rader och kolumner upprepade gånger, JavaScript Hur man ställer in utskriftstitlar, Ställ in och rensa utskriftstitlar med JavaScript, Hur man rensar utskriftstitlar i JavaScript, Hur man lägger till utskriftstitlar med JavaScript, Hur man tar bort utskriftstitlar med JavaScript, Hur man ställer in utskriftstitlar i Excel, Hur man rensar utskriftstitlar i Excel.  
---

## **Möjliga användningsscenario**  

Att ställa in utskriftstitlar i Excel säkerställer att specifika rader eller kolumner upprepas på varje utskriven sida, vilket är särskilt användbart för stora kalkylblad som sträcker sig över flera sidor. Här är några anledningar till varför du kan ställa in utskriftstitlar:  

1. Förbättrad läsbarhet: Utskriftstitlar hjälper läsarna att förstå data genom att hålla rubriker synliga på alla sidor, vilket gör det lättare att tolka informationen på varje sida utan att behöva hänvisa tillbaka till första sidan.  

1. Professionell presentation: Att konsekvent visa rubriker eller etiketter på varje sida skapar ett mer polerat och professionellt utseende på utskrivna dokument.  

1. Förbättrad navigering: För dokument med omfattande data gör upprepning av rubriker på varje sida snabbare navigering och referens, vilket minskar behovet av att vända fram och tillbaka mellan sidor.  

1. Minskade fel: När rubriker är närvarande på varje sida minimeras missförstånd eller datainmatningsfel, eftersom användare lätt kan se sammanhanget för data.  

1. Konsekvens: Att säkerställa att viktig information, som kolumnrubriker eller radetiketter, alltid är synlig upprätthåller konsekvens och tydlighet genom hela dokumentet.  

## **Hur man ställer in utskriftstitlar i Excel**  

Följ dessa steg för att ställa in utskriftstitlar i Excel:  

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.  
1. Få tillgång till Utskriftstitlar: I gruppen "Siduppställning" klickar du på "Utskriftstitlar".  
1. Ställ in rader att upprepa: I dialogrutan "Siduppställning" går du till fliken "Blad". I avsnittet "Utskriftstitlar" anger du de rader som ska upprepas överst genom att klicka på rutan bredvid "Rader att upprepa längst upp" och välja rad(er) du vill upprepa.  
1. Ställ in kolumner att upprepa (om behövs): På liknande sätt kan du ange de kolumner som ska upprepas längst till vänster genom att klicka på rutan bredvid "Kolumner att upprepa till vänster" och välja den eller de kolumner du vill upprepa.  
<br>  
<img src="3.png" width=60% />  

1. Bekräfta och skriv ut: Klicka på "OK" för att tillämpa inställningarna. När du skriver ut kalkylbladet kommer de angivna raderna eller kolumnerna att visas på varje utskriven sida.  

## **Hur man rensar utskriftstitlar i Excel**  

För att rensa utskriftstitlar i Excel måste du ta bort de rader eller kolumner som är inställda att upprepas på varje utskriven sida. Så här gör du:  

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.  
1. Få tillgång till Utskriftstitlar: I gruppen "Siduppställning" klickar du på "Utskriftstitlar".  
1. Rensa utskriftstitlar: I dialogrutan "Siduppställning" går du till fliken "Blad". Radera texten i rutorna för "Rader att upprepa längst upp" och "Kolumner att upprepa till vänster" genom att ta bort innehållet i dem.  
<br>  
<img src="4.png" width=60% />  

1. Bekräfta och stäng: Klicka på "OK" för att tillämpa ändringarna.  

## **Hur man ställer in utskriftstitlar med Aspose.Cells for JavaScript via C++**  

För att ställa in utskriftstitlar i ett angivet kalkylblad: Ladda först [provfilen](input.xlsx), och du behöver sedan ändra egenskaperna [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) och [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) av [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)-objektet för det önskade kalkylbladet. Att ställa in dessa egenskaper till ett områdesträng kommer att ställa in utskriftstitlarna.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Titles</title>
    </head>
    <body>
        <h1>Set Print Titles Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set rows to repeat at the top (e.g., rows 1 and 2)
            worksheet.pageSetup.printTitleRows = "$1:$2";

            // Set columns to repeat at the left (e.g., columns A and B)
            worksheet.pageSetup.printTitleColumns = "$A:$B";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Utmatningsresultat:  
<br>  
<img src="1.png" width=60% />  

## **Hur man rensar utskriftstitlar med Aspose.Cells for JavaScript via C++**  

För att rensa utskriftstitlar i ett specificerat kalkylblad: Ladda först [provfilen](input.xlsx), och du behöver sedan ändra egenskaperna [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) och [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) av [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)-objektet för det önskade kalkylbladet. Att ställa in dessa egenskaper till en tom sträng rensar utskriftstitlarna.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Clear Print Titles Example</title>
    </head>
    <body>
        <h1>Clear Print Titles Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the rows and columns set to repeat
            worksheet.pageSetup.printTitleRows = "";
            worksheet.pageSetup.printTitleColumns = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Utmatningsresultat:  
<br>  
<img src="2.png" width=60% />
