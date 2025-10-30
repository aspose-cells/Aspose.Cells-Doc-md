---
title: Hur man ställer in utskriftsområde med JavaScript via C++
linktitle: Hur man ställer in utskriftsområde
type: docs
weight: 200
url: /sv/javascript-cpp/how-to-set-print-area/
description: Denna artikel visar kod som förklarar hur man ställer in utskriftsområde med hjälp av Aspose.Cells biblioteket för JavaScript via C++.
keywords: Begränsa utskriftsområde, Ställ in utskriftsområde, Rensa utskriftsområde, Ställ in och rensa utskriftsområde med JavaScript via C++, JavaScript via C++ Hur man ställer in utskriftsområde, Ställ in och rensa utskriftsområde med JavaScript via C++, Hur man rensar utskriftsområdet i JavaScript via C++, Hur man lägger till utskriftsområde med JavaScript via C++, Hur man tar bort utskriftsområde med JavaScript via C++, Hur man ställer in utskriftsområde i Excel, Hur man rensar utskriftsområde i Excel.
---

## **Möjliga användningsscenario**

Att ställa in ett utskriftsområde i ett dokument, så som ett Excel-ark, hjälper till att kontrollera vilka innehåll som inkluderas vid utskrift. Här är några skäl att ställa in ett utskriftsområde:

1. Fokusera på specifika data: Du kan skriva ut endast de mest relevanta delarna, vilket undviker onödigt innehåll.
1. Förbättrad layout: Det hjälper till att organisera och passa innehållet snyggt på de utskrivna sidorna, vilket förhindrar avdelningar eller oönskade sidbrytningar.
1. Spara resurser: Genom att begränsa utskriftsområdet kan du minska mängden papper och bläck som används.
1. Professionell presentation: Det säkerställer att endast den polerade och slutgiltiga versionen av data skrivs ut, vilket är särskilt viktigt för rapporter eller presentationer.
1. Konsekvens: När du skriver ut samma dokument flera gånger, säkerställer ett inställt utskriftsområde konsekvent resultat.

<br>
Att ställa in ett utskriftsområde är särskilt användbart i större dokument där endast en del behöver delas eller granskas i tryckt form.

## **Hur man sätter in utskriftsområde i Excel**

För att ställa in ett utskriftsområde i Excel, följ dessa steg:

1. Välj cellerna: Klicka och dra för att välja det cellområde du vill ange som utskriftsområde.
1. Öppna fliken Sida Layout: Gå till "Sida Layout"-fliken i ribbonen längst upp i Excel-fönstret.
1. Ange Utskriftsområde: I gruppen "Sidan Setup" klickar du på "Utskriftsområde". Väljs från rullgardinsmenyn, välj "Ställ in Utskriftsområde".
<br>
<img src="3.png" width=60% />

1. Lägg till i Utskriftsområdet: Vill du lägga till fler celler till det befintliga utskriftsområdet, markera de ytterligare cellerna, gå till "Utskriftsområde" i "Sida Layout"-fliken, och välj "Lägg till i Utskriftsområde".

<br>
Denna åtgärd definierar de valda cellerna som utskriftsområdet. När du skriver ut kalkbladet, kommer endast detta område att skrivas ut.

## **Hur man rensar utskriftsområde i Excel**

Följ dessa steg för att rensa utskriftsområdet i Excel:

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.
1. Rensa Utskriftsområde: I gruppen "Sidan Setup" klickar du på "Utskriftsområde". Välj "Rensa Utskriftsområde" från rullgardinsmenyn.
<br>
<img src="4.png" width=60% />

<br>
Denna åtgärd tar bort eventuellt tidigare angivet utskriftsområde, vilket gör att hela kalkbladet kan skrivas ut.

## **Vad händer efter att ha rensat utskriftsområdet**

Att rensa utskriftsområdet i ett kalkulsprogram som Excel med Aspose.Cells gör att hela kalkbladet inkluderas när du skriver ut dokumentet. Om ett utskriftsområde är angett, skrivs endast det specifika cellområdet ut. Genom att rensa utskriftsområdet säkerställer du att inget specifikt område är definierat, och den standardskrivningen som inkluderar hela bladet kommer att träda i kraft.

1. Standard utskriftsbeteende: Hela kalkbladet kommer att betraktas för utskrift. Det innebär att alla celler med data eller formatering kommer att skrivas ut.
1. Inga begränsningar för Utskriftsområde: Tidigare definierade gränser för utskriftsområdet tas bort. Om det fanns specifika rader och kolumner för utskrift, begränsas de inte längre av dessa.
1. Fullständig innehållsutskrift: Allt innehåll, inklusive rubriker, sidfötter och annan data inom kalkbladet, kommer att ingå i utskriftsjobbet.

## **Hur man ställer in utskriftsområde med Aspose.Cells for JavaScript via C++**

För att ställa in utskriftsområdet i ett specificerat blad: Ladda först [exempelfilen](input.xlsx), och du måste sedan ändra [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--)-egenskapen hos [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)-objektet för det önskade bladet. Att ange denna egenskap till en rad- eller kolumnsträng kommer att ställa in utskriftsområdet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Area</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet (first worksheet)
            const worksheet = workbook.worksheets.get(0);

            // Set the print area - specify the range you want to print
            worksheet.pageSetup.printArea = "A1:D10";

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Utmatningsresultat:
<br>
<img src="1.png" width=60% />

## **Hur man rensar utskriftsområdet med Aspose.Cells for JavaScript via C++**

För att rensa utskriftsområdet i ett specifikt kalkblad: Först, ladda [exempelfilen](input.xlsx), och sedan behöver du ändra egenskapen [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) för objektet [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) för det önskade kalkbladet. Att sätta denna egenskap till en tom sträng kommer att rensa utskriftsområdet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Clear Print Area</title>
    </head>
    <body>
        <h1>Clear Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the print area
            worksheet.pageSetup.printArea = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultEl.innerHTML = '<p style="color: green;">Print area cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

Utmatningsresultat:
<br>
<img src="2.png" width=60% />
