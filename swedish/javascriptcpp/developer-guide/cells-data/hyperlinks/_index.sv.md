---
title: Infoga hyperlänkar i Excel eller OpenOffice
linktitle: Hantera hyperlänkar
type: docs
weight: 45
url: /sv/javascript-cpp/insert-hyperlinks-to-excel/
description: Hur man infogar hyperlänkar i Excel fil med Aspose.Cells bibliotek utan MS Excel med Javascript via C++.
keywords: Infoga hyperlänkar i Excel Javascript via C++, Lägg till eller infoga hyperlänkar Javascript via C++, Lägg till eller infoga länk till en URL Javascript via C++, Lägg till eller infoga en länk till en cell Javascript via C++, Lägg till en länk till en extern fil Javascript via C++
---

{{% alert color="primary" %}} 

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.
Med Aspose.Cells kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. I det här ämnet diskuteras vilka typer av hyperlänkar som stöds av Aspose.Cells och hur de kan användas i våra Excel-filer.

{{% /alert %}} 

## **Lägga till hyperlänkar**
 Aspose.Cells tillåter utvecklare att lägga till hyperlänkar i Excel-filer antingen med API:et eller diagramblad (blad där hyperlänkar skapas manuellt och Aspose.Cells används för att importera dem till andra blad).

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) som ger tillgång till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) ger olika metoder för att lägga till olika hyperlänkar i Excel-filer.
## **Lägga till länk till en URL**
 Klassen [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) innehåller en [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--) samling. Varje objekt i samlingen [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--) representerar en [Hyperlink](https://reference.aspose.com/cells/javascript-cpp/hyperlink). Lägg till hyperlänkar till URL:er genom att anropa metoden [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) i samlingen [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection). Metoden [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) tar emot följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, URL-adressen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Hyperlink Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create Workbook & Add Hyperlink)</button>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a hyperlink to a URL at "A1" cell
            worksheet.hyperlinks.add("A1", 1, 1, "http://www.aspose.com");

            // Save the Excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}} 

I det ovanstående exemplet läggs en hyperlänk till en URL i en tom cell, **A1**. I sådana fall, om en cell är tom, läggs URL-adressen också till den tomma cellen som dess värde. Om cellen inte är tom och en hyperlänk läggs till, ser cellens värde ut som vanlig text. För att få det att se ut som en hyperlänk, använd lämpliga formateringsinställningar på den cellen.

{{% /alert %}} 
## **Lägga till en länk till en cell i samma fil**
Det är möjligt att lägga till hyperlänkar till celler i samma Excel-fil genom att anropa metoden [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) i samlingen [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection). Metoden [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) fungerar för både interna och externa hyperlänkar. En version av den överlagrade metoden tar emot följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målcellen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Internal Hyperlink Example</h1>
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
            // Create a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            workbook.worksheets.add();

            // Obtaining the reference of the first (default) worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding an internal hyperlink to the "B3" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("B3", 1, 1, "Sheet2!B9");

            // Saving the Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Excel file created successfully. Click the download link to save it.</p>';
        });
    </script>
</html>
```


## **Lägga till en länk till en extern fil**
Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att anropa metoden [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) i samlingen [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection). Metoden [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) tar emot följande parametrar:

- Cellnamn, namnet på den cell som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperrlänksområde.
- Antal kolumner, antalet kolumner i detta hyperrlänksområde.
- URL, adressen till målet, extern Excel-fil.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an optional Excel file to use its filename as the hyperlink target (or leave empty to use "book1.xls"):</p>
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
            const fileInput = document.getElementById('fileInput');
            let targetFileName = 'book1.xls';
            if (fileInput.files.length) {
                targetFileName = fileInput.files[0].name;
            }

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Adding an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("A5", 1, 1, targetFileName);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Fortsatta ämnen**
- [Lägg till bildhyperlänkar](/cells/sv/javascript-cpp/add-image-hyperlinks/)
- [Identifiera hyperlänkstyp](/cells/sv/javascript-cpp/detect-hyperlink-type/)
- [Redigera hyperlänkar på arbetsbladet](/cells/sv/javascript-cpp/editing-hyperlinks-of-worksheet/)
- [Hämta hyperlänkar i omfånget](/cells/sv/javascript-cpp/get-hyperlinks-in-range/)
