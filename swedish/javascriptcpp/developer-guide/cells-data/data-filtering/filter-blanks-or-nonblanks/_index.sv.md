---
title: Hur man filtrerar tomma eller icke tomma.
type: docs
weight: 85
url: /sv/javascript-cpp/how-to-filter-blanks-and-non-blanks/
description: Lär dig hur du filtrerar tomma och icke tomma med hjälp av Aspose.Cells for JavaScript via C++ API.
keywords: Filtrera tomma, filtrera icke tomma, filtrera tomma i kalkylblad, filtrera icke tomma i kalkylblad, filtrera tomma i excel, filtrera icke tomma i excel, filtrera tomma och icke tomma i excel
---

## **Möjliga användningsscenario**
Filtrering av data i Excel är ett värdefullt verktyg som förbättrar dataanalys, utforskning och presentation genom att möjliggöra för användare att fokusera på specifika delmängder av data baserat på deras kriterier, vilket gör hela datahanterings- och tolkningsprocessen mer effektiv och effektiv.

## **Hur man filtrerar tomma eller icke-tomma i Excel**
I Excel kan du enkelt filtrera tomma eller icke-tomma med hjälp av filtreringsalternativen. Så här kan du göra det:

### **Hur man filtrerar tomma i Excel**
1. Välj intervallet: Klicka på bokstaven i kolumnrubriken för att välja hela kolumnen eller välj intervallet där du vill filtrera bort tomma.
1. Öppna filtermenyn: Gå till fliken "Data" i menyfliken.
<br>
<image src="1.png" width="70%" />
1. Filteralternativ: Klicka på knappen "Filter". Detta lägger till filterpilar i det valda intervallet.
1. Filtrera tomma: Klicka på filterpilen i kolumnen där du vill filtrera bort tomma. Avmarkera alla alternativ utom "Tomma" och klicka på OK. Detta visar endast de tomma cellerna i den kolumnen.
<br>
<image src="2.png" width="70%" />
1. Resultatet är som följer:
<br>
<image src="3.png" width="70%" />

### **Hur man filtrerar icke-tomma i Excel**
1. Välj intervallet: Klicka på bokstaven i kolumnrubriken för att välja hela kolumnen eller välj intervallet där du vill filtrera icke-tomma.
1. Öppna filtermenyn: Gå till fliken "Data" i menyfliken.
<br>
<image src="1.png" width="70%" />
1. Filteralternativ: Klicka på knappen "Filter". Detta lägger till filterpilar i det valda intervallet.
1. Filtrera icke-tomma: Klicka på filterpilen i kolumnen där du vill filtrera icke-tomma. Avmarkera alla alternativ utom "Icke-tomma" eller "Anpassat" och ställ in villkoren därefter. Klicka på OK. Detta visar endast cellerna som inte är tomma i den kolumnen.
<br>
<image src="4.png" width="70%" />
1. Resultatet är som följer:
<br>
<image src="5.png" width="70%" />

## ** Hur man filtrerar tomma med Aspose.Cells for JavaScript via C++**
Om en kolumn innehåller text så att några celler är tomma, och filter krävs för att endast välja de rader där tomma celler finns, kan funktionerna [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchBlanks-number-) och [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#addFilter-number-string-) användas som demonstreras nedan. 

Se följande exemplarkod som laddar den [exempel Excel-filen](sample.xlsx) som innehåller lite dummydata. Exempelkoden använder tre metoder för att filtrera tomma. Sedan sparar den arbetsboken som [utdata Excel-filen](FilteredBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Filter for Blank Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.autoFilter.addFilter(1, null);
            worksheet.autoFilter.refresh();

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download FilteredBlanks.xlsx';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied and file ready for download.</p>';
        });
    </script>
</html>
```


## ** Hur man filtrerar icke-tomma med Aspose.Cells for JavaScript via C++**

Se följande exempel som laddar [exempel-Excelfilen](sample.xlsx) som innehåller some dummy data. Efter att ha laddat filen, anropa [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchNonBlanks-number-) funktionen för att filtrera icke-tomma data, och spara slutligen arbetsboken som [utdata Excel-fil](FilteredNonBlanks.xlsx). 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter NonBlanks Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(1);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
