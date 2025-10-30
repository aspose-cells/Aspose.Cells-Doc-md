---
title: Hantering av sidbrytningar med JavaScript via C++
linktitle: Hantera sidbrytningar
type: docs
weight: 30
url: /sv/javascript-cpp/managing-page-breaks/
description: Denna artikel innehåller exempel på kod och förklarar hur man lägger till, rensar eller tar bort specifika sidbrytningar i Excel ark programmässigt med Aspose.Cells for JavaScript via C++.
keywords: sidbrytningar JavaScript via C++, excel sidbrytningar JavaScript via C++, rensa sidbrytning JavaScript via C++, ta bort specifik sidbrytning JavaScript via C++
---

{{% alert color="primary" %}}

Enligt definitionen är en sidbrytning en plats i en textflöde där en sida slutar och den nästa börjar. Microsoft Excel låter användare lägga till sidbrytningar i valfri markerad cell i ett kalkylblad.

Placeringen av cellen där sidbrytningen läggs till, sidan avslutas och resten av datan efter sidbrytningen skrivs ut på nästa sida under utskrift. Med andra ord delar sidbrytningar ditt kalkylblad i flera sidor enligt dina specifikationer. Du kan också lägga till sidbrytningar i dina kalkylblad vid runtime med hjälp av Aspose.Cells. Aspose.Cells tillåter utvecklare att lägga till två typer av sidbrytningar:

- Horisontell sidbrytning
- Vertikal sidbrytning

I resten av diskussionen kommer vi att beskriva hur du kan lägga till horisontella eller vertikala sidbrytningar i dina kalkylblad med hjälp av Aspose.Cells.

{{% /alert %}}

## **Sidbrytningar**

Aspose.Cells for JavaScript via C++ ger en [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klass som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som ger åtkomst till varje ark i Excel-filen.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder som används för att hantera ett kalkylblad.

Använd [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassens [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) och [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) egenskaper för att lägga till sidbrytningar.

Egenskaperna [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) och [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) är samlingar som kan innehålla flera sidbrytningar. Varje samling innehåller flera metoder för att hantera horisontella och vertikala sidbrytningar.

### **Lägga till sidbrytningar**

För att lägga till en sidbrytning i ett arbetsblad, infoga vertikala och horisontella sidbrytningar vid den angivna cellen genom att anropa [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#add-number-number-number-)- och [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#add-number-number-number-)-metoderna. Varje **add**-metod tar namnet på cellen där brytningen ska läggas till.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Page Breaks Example</h1>
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a page break at cell Y30
            worksheet.horizontalPageBreaks.add("Y30");
            worksheet.verticalPageBreaks.add("Y30");

            // Save the Excel file (Excel 97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingPageBreaks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

I sidbrytning förhandsgranskning eller utskriftsförhandsgranskning kan du se hur dessa sidbrytningar fungerar.

{{% /alert %}}

### **Ta bort en specifik sidbrytning**

För att ta bort en specifik sidbrytning, anropa [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#removeAt-number-)- och [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#removeAt-number-)-metoderna. Varje **removeAt**-metod tar indexet för sidbrytningen som ska tas bort.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Remove Specific Page Break Example</title>
    </head>
    <body>
        <h1>Remove Specific Page Break Example</h1>
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

            // Removing a specific page break
            worksheet.horizontalPageBreaks.removeAt(0);
            worksheet.verticalPageBreaks.removeAt(0);

            // Saving the Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveSpecificPageBreak_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Viktig information att veta**

När du ställer in **fitToPages**-egenskaper (det vill säga [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) och [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)) i sidinställningarna påverkas sidbrytningarnas inställningar, så att om du skriver ut arbetsbladet beaktas inte sidbrytningarna även om de fortfarande är inställda.
