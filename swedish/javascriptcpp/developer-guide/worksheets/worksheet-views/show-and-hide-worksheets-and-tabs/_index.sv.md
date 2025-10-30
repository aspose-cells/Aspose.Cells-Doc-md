---
title: Visa och Dölj Arbetsblad och Flikar med JavaScript via C++
linktitle: Visa och Dölja Kalkylblad och Flikar
type: docs
weight: 10
url: /sv/javascript-cpp/show-and-hide-worksheets-and-tabs/
description: Denna artikel ger exempel på kod för att använda JavaScript API eller JavaScript Library för att programmässigt visa och dölja ett Excel ark. Dessutom hur man visar och döljer arbetsboksflikar i Excel.
---

{{% alert color="primary" %}}
Aspose.Cells tillåter användaren att visa och dölja element i en arbetsbok inklusive kalkylblad och flikar.
{{% /alert %}}

## **Visa och dölj ett arbetsblad**

En Excel-fil kan ha ett eller flera arbetsblad. När vi skapar en Excel-fil lägger vi till arbetsblad i Excel-filen där vi arbetar. Varje arbetsblad i en Excel-fil är oberoende från det andra arbetsbladet genom att ha sina egna data och formateringsinställningar osv. Ibland kan utvecklare behöva dölja några arbetsblad och göra andra synliga i Excel-filen för deras eget intresse. Så, **Aspose.Cells** låter utvecklare kontrollera synligheten av arbetsbladen i deras Excel-filer.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klassen innehåller en [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) samling som ger åtkomst till varje arbetsblad i Excel-filen.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att kontrollera arbetsbladets synlighet, använd egenskapen [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) är en boolesk egenskap, vilket betyder att den endast kan lagra ett **true** eller **false** värde.

### **Göra ett arbetsblad synligt**

Gör ett arbetsblad synligt genom att ställa in egenskapen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) för [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--)-klassen till **true**.

### **Dölja ett arbetsblad**

Dölj ett kalkylblad genom att ställa in egenskapen [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) för klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) till **falskt**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Worksheet Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the first worksheet of the Excel file
            worksheet.isVisible = false;

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Visa och dölj flikar**

Om du tittar noga längst ner i en Microsoft Excel-fil, kommer du att se ett antal kontroller. Dessa inkluderar:

- Arkflikar.
- Flikbläddringsknappar.

Arkflikar representerar arbetsbladen i Excel-filen. Klicka på vilken flik som helst för att växla till det arbetsbladet. Ju fler arbetsblad i arbetsboken, desto fler arkflikar finns det. Om Excel-filen har ett bra antal arbetsblad behöver du knappar för att navigera genom dem. Så tillhandahåller Microsoft Excel flikbläddringsknappar för att bläddra igenom arkflikarna.

Genom att använda Aspose.Cells kan utvecklare kontrollera synligheten av arkflikar och flikbläddringsknappar i Excel-filer.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) erbjuder ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för flikar i en Excel-fil kan utvecklare använda egenskapen [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) för klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) är en Boolean-egenskap, vilket betyder att den bara kan lagra ett **true** eller **false** värde.

### **Göra flikar synliga**

Gör flikar synliga med egenskapen [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) för klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) till **true**.

### **Gömma flikar**

Dölj flikar i en Excel-fil genom att ställa in egenskapen [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) för klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) till **falskt**.

Här är ett komplett exempel som öppnar en Excel-fil (book1.xls), döljer dess flikar och sparar den modifierade filen som output.xls. Efter att kodexekveringen har utförts kommer du att se att arbetsbokens flikar är dolda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Tabs Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file
            workbook.settings.showTabs = false;

            // To show the tabs instead, you could set:
            // workbook.settings.showTabs = true;

            // Saving the modified Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Tabs hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Styra fliken Bredd**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Tabs</title>
    </head>
    <body>
        <h1>Hide Tabs Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file (converted setter to property)
            workbook.settings.showTabs = true;

            // Adjusting the sheet tab bar width (converted setter to property)
            workbook.settings.sheetTabBarWidth = 800;

            // Saving the modified Excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
