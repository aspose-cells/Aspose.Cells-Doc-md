---
title: Avancerade skyddsinställningar sedan Excel XP med JavaScript via C++
linktitle: Avancerade skyddsinställningar sedan Excel XP
type: docs
weight: 30
url: /sv/javascript-cpp/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Sedan utgåvan av Excel 2002 eller XP har Microsoft lagt till många avancerade skyddsinställningar.

{{% /alert %}}


## **Introduktion**

Dessa skyddsinställningar begränsar eller tillåter användare att:

- Ta bort rader eller kolumner.
- Redigera innehåll, objekt eller scenarier.
- Formatera celler, rader eller kolumner.
- Infoga rader, kolumner eller hyperlänkar.
- Välj låsta eller olåsta celler.
- Använd pivottabeller och mycket annat.

Aspose.Cells for JavaScript via C++ stöder alla de avancerade skyddsinställningarna som erbjuds av Excel XP eller senare versioner.

### **Avancerade skyddsinställningar med Excel XP och senare versioner**

För att visa de tillgängliga skyddsinställningarna i Excel XP:

1. Från **Verktyg**-menyn, välj **Skydda** följt av **Skydda kalkylblad**. En dialogruta kommer att visas.

För att visa de tillgängliga skyddsinställningarna i Excel 2016:

1. Från **Arkiv**-menyn, välj **Skydda arbetsbok** följt av **Skydda aktuellt kalkylblad**.
1. Välj **Skydda kalkylblad** i **Granska**-menyn.

Följ stegen ovan visar en dialogruta där du kan tillåta eller begränsa arbetsbladets funktioner eller tillämpa ett lösenord på arbetsbladet.

### **Avancerade skyddsinställningar med Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript via C++ stöder alla avancerade skyddsinställningar.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)-kollektion som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen.

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen ger egenskapen [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) som används för att tillämpa dessa avancerade skyddsinställningar. Egenskapen [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) är faktiskt ett objekt av [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection)-klassen som kapslar in flera booleska egenskaper för att inaktivera eller aktivera restriktioner.

Nedan finns en liten exempelapplikation. Den öppnar en Excel-fil och använder de flesta av de avancerade skyddsinställningarna som stöds av Excel XP och senare versioner.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Worksheet Protection Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const protection = worksheet.protection;

            // Restricting users to delete columns of the worksheet
            protection.allowDeletingColumn = false;

            // Restricting users to delete row of the worksheet
            protection.allowDeletingRow = false;

            // Restricting users to edit contents of the worksheet
            protection.allowEditingContent = false;

            // Restricting users to edit objects of the worksheet
            protection.allowEditingObject = false;

            // Restricting users to edit scenarios of the worksheet
            protection.allowEditingScenario = false;

            // Restricting users to filter
            protection.allowFiltering = false;

            // Allowing users to format cells of the worksheet
            protection.allowFormattingCell = true;

            // Allowing users to format rows of the worksheet
            protection.allowFormattingRow = true;

            // Allowing users to insert columns in the worksheet
            protection.allowFormattingColumn = true;

            // Allowing users to insert hyperlinks in the worksheet
            protection.allowInsertingHyperlink = true;

            // Allowing users to insert rows in the worksheet
            protection.allowInsertingRow = true;

            // Allowing users to select locked cells of the worksheet
            protection.allowSelectingLockedCell = true;

            // Allowing users to select unlocked cells of the worksheet
            protection.allowSelectingUnlockedCell = true;

            // Allowing users to sort
            protection.allowSorting = true;

            // Allowing users to use pivot tables in the worksheet
            protection.allowUsingPivotTable = true;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protection settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Vänligen ring inte metoden [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) för klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) när du använder egenskapen [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--). Spara också filen i Excel97Till2003 eller Xlsx-format eftersom de avancerade säkerhetsinställningarna endast stöds av Excel XP och senare versioner.

{{% /alert %}}

### **Cellåsningsproblem**

Om du vill begränsa användare från att redigera celler måste cellerna låsas innan några skyddsinställningar tillämpas. Annars kan cellerna redigeras även om arket är skyddat. I Microsoft Excel XP kan celler låsas genom följande dialog:

|**Dialogruta för att låsa celler i Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Det är också möjligt att låsa celler med Aspose.Cells API. Varje cell kan få [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) formatering som innehåller en Boolean-egenskap, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Sätt [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) egenskapen till **true** eller **false** för att låsa eller låsa upp cellen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Lock cell A1 by setting the style property
            const cell = worksheet.cells.get("A1");
            cell.style.isLocked = true;

            // Protect the sheet now.
            worksheet.protect(ProtectionType.All);

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
