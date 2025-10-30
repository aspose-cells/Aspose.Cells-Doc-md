---
title: Ställ in villkorlig formatering för Excel och ODS filer
linktitle: Villkorliga format
type: docs
weight: 60
url: /sv/javascript-cpp/conditional-formatting/
description: Hur man applicerar villkorliga format på Excel och ODS filer i JavaScript via C++.
keywords: tillämpa villkorliga format JavaScript via C++
---

## **Introduktion**

Villkorsstyrd formatering är en avancerad funktion som tillåter dig att tillämpa format på en cell eller ett cellområde och få formateringen att ändras beroende på cellens värde eller värdet av en formel. Till exempel kan du få en cell att visas i fet stil endast när cellens värde är större än 500. När cellens värde uppfyller villkoret tillämpas det angivna formatet på cellen. Om cellens värde inte uppfyller villkoret används cellens standardformat. I Microsoft Excel, välj **Format**, sedan **Villkorsstyrd formatering** för att öppna dialogrutan för villkorsstyrd formatering.

Aspose.Cells stöder tillämpning av villkorlig formatering på celler vid körning. Den här artikeln förklarar hur. Den förklarar också hur man beräknar färgen som Excel använder för färgskala av villkorlig formatering.

## **Tillämpa villkorlig formatering**

Aspose.Cells stöder villkorlig formatering på flera sätt:

- Använda designerkalkylblad
- Använda kopieringsmetoden
- Skapa villkorlig formatering vid körning

### **Använda designerkalkylblad**

Utvecklare kan skapa ett designerkalkylblad som innehåller villkorlig formatering i Microsoft Excel och sedan öppna det kalkylbladet med Aspose.Cells. Aspose.Cells laddar och sparar designerkalkylbladet och behåller alla inställningar för villkorlig formatering.

### **Använda kopieringsmetoden**

Aspose.Cells tillåter utvecklare att kopiera inställningar för villkorlig formatering från en cell till en annan i kalkylbladet genom att anropa [**Range.copy()**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-)-metoden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon
            const imageData = icon.imageData;

            // Create a blob and provide download link for the image
            const blob = new Blob([imageData], { type: "image/jpeg" });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```


## **Tillämpa villkorlig formatering under körning**

Aspose.Cells låter dig både lägga till och ta bort villkorlig formatering vid körning. Kodsamplerna nedan visar hur man ställer in villkorlig formatering:

1. Skapa en arbetsbok.
1. Lägg till en tom villkorlig formatering.
1. Ange det intervall som formateringen ska tillämpas på.
1. Definiera formateringsvillkoren.
1. Spara filen.

Efter det här exemplet följer ett antal mindre exempel som visar hur man tillämpar teckensnittsinställningar, kantlinjeinställningar och mönster.

Microsoft Excel 2007 lade till mer avancerad villkorsstyrd formatering som även Aspose.Cells stöder. Exemplen här visar hur man använder enkel formatering, medan Microsoft Excel 2007-exemplen visar hur man tillämpar mer avancerad villkorsstyrd formatering.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
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

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.count;
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            let ca = AsposeCells.CellArea.createCellArea(0, 0, 0, 0);
            fcs.addArea(ca);

            ca = AsposeCells.CellArea.createCellArea(1, 1, 1, 1);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "=A2", "100");

            // Adds condition.
            const conditionIndex2 = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");

            // Sets the background color.
            const fc = fcs.get(conditionIndex);
            fc.style.backgroundColor = AsposeCells.Color.Red;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **Ange font**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get the image data from the icon
            const imageData = icon.imageData;

            // Create a Blob and provide a download link for the image
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```



{{% alert color="primary" %}}

Du kan bara ändra teckensnittsstil, textfärg, understrykningsstil och överstrykningsstil.

{{% /alert %}}

### **Ange ram**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FormatConditionType, OperatorType, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, adds conditional formatting and offers the result for download.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(FormatConditionType.CellValue, OperatorType.Between, "50", "100");

            // Sets the borders' line style to dashed and colors
            const fc = fcs.get(conditionIndex);
            fc.style.borders.get(BorderType.LeftBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.RightBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.TopBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Dashed;

            fc.style.borders.get(BorderType.LeftBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.RightBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.TopBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.BottomBorder).color = new Color(255, 255, 0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Du kan endast använda tunn linjestil för kantens kontur. Diagonala linjer är inte tillåtna.

{{% /alert %}}

### **Ange mönster**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Add Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const file = fileInput.files && fileInput.files.length ? fileInput.files[0] : null;

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = AsposeCells.CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");
            const fc = fcs.get(conditionIndex);

            // Apply style using property assignments (getter/setter conversion)
            fc.style.pattern = AsposeCells.BackgroundType.ReverseDiagonalStripe;
            fc.style.foregroundColor = new AsposeCells.Color(255, 255, 0);
            fc.style.backgroundColor = new AsposeCells.Color(0, 255, 255);

            // Save workbook to browser downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added. Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```



## **Fortsatta ämnen**  
- [Lägga till 2-färgskala och 3-färgskala villkorliga formateringar](/cells/sv/javascript-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Tillämpa villkorlig formatering i arbetsblad](/cells/sv/javascript-cpp/apply-conditional-formatting-in-worksheets/)  
- [Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering](/cells/sv/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Generera bilder för databarformat i villkorlig formatering](/cells/sv/javascript-cpp/generate-conditional-formatting-databars-images/)  
- [Hämta ikonsatser, databarer eller färgskalor som används i villkorlig formatering](/cells/sv/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
