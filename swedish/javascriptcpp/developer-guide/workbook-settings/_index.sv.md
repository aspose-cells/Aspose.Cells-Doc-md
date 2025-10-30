---
title: Hantera inställningarna för Excel kalkylblad med JavaScript via C++
linktitle: Arbetsboksinställningar 
type: docs
weight: 185
url: /sv/javascript-cpp/workbook-settings/
description: Hantera inställningar för Excel filer med Aspose.Cells for JavaScript via C++.
---

## **Oversikt över arbetsboksinställningar**
Arbete med Excel-filer involverar olika inställningar som kan manipuleras programatiskt med Aspose.Cells for JavaScript via C++. Detta dokument beskriver hur man hanterar dessa inställningar på ett effektivt sätt.

## **Möjliga användningsscenario**
Följande scenarier visar när du kan behöva hantera arbetsboksinställningar:
- Justera visningsalternativ
- Ställa in beräkningsläge
- Konfigurera sidinställningsparametrar

## **Hantera arbetsboksinställningar med Aspose.Cells for JavaScript via C++**
Detta exempel visar hur man hanterar arbetsboksinställningar som beräkningsalternativ och visningsinställningar.

1. Skapa en ny arbetsbok eller ladda en befintlig.
2. Ändra arbetsboksinställningar enligt dina krav.
3. Spara arbetsboken för att behålla ändringarna.

### **Exempel på kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook Settings Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the settings of the workbook
            const settings = workbook.settings;
            settings.calculationMode = 1; // Manual calculation

            // Display options
            settings.showGridLines = false; // Disable gridlines

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookSettingsExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Viktiga arbetsboksinställningar och metoder**
Aspose.Cells for JavaScript via C++ tillhandahåller ett antal egenskaper och metoder för att justera arbetsboksinställningar:
- **Workbook.settings**: Åtkomst till arbetsbokens inställningar.
- **Settings.calculationMode**: Sätter beräkningsläget för arbetsboken.
- **Settings.showGridLines**: Aktiverar eller inaktiverar rutnätlinjer på skärmen.

## **Slutsats**
Att hantera arbetsboksinställningar i Aspose.Cells for JavaScript via C++ är enkelt och ger många alternativ för att anpassa Excel-filer. Genom att använda tillgängliga inställningar kan du skräddarsy arbetsboken för att möta dina specifika krav.
