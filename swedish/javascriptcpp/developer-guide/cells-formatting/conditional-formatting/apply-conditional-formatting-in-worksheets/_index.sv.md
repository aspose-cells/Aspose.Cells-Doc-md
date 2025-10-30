---
title: Tillämpa villkorlig formatering i arbetsblad
linktitle: Tillämpa villkorlig formatering i arbetsblad
description: Hur du använder Aspose.Cells biblioteket i JavaScript via C++ för att tillämpa villkorsstyrd formatering i arbetsblad för bättre kontroll över cellens utseende.
keywords: Aspose.Cells, Villkorsstyrd formatering, JavaScript via C++, Arbetsblad, Formatering
type: docs
weight: 130
url: /sv/javascript-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Den här artikeln syftar till att ge en detaljerad förståelse för hur man lägger till villkorlig formatering till en rad celler i ett arbetsblad.

Villkorlig formatering är en avancerad funktion i Microsoft Excel som gör det möjligt att tillämpa format på en rad celler och ha den formateringen ändras beroende på cellens värde eller värdet på en formel. Till exempel kan bakgrunden för en cell vara röd för att markera ett negativt värde eller textfärgen kan vara grön för ett positivt värde. När cellens värde uppfyller formatvillkoret tillämpas formatet. Om cellens värde inte uppfyller formatvillkoret används cellens standardformatering.

Det är möjligt att tillämpa villkorlig formatering med Microsoft Office Automation men det har sina nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet och hastighet. Det främsta skälet till att hitta en annan lösning är att Microsoft själva starkt avråder från Office Automation för programvarulösningar.

Denna artikel visar hur man skapar en webbapplikation, lägger till villkorsstyrd formatering på celler med några enklaste kodrader med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Använda Aspose.Cells för att tillämpa villkorlig formatering baserat på cellvärde**

1. **Ladda ner och installera Aspose.Cells**.
   1. Ladda ner Aspose.Cells for JavaScript via C++.
1. Installera det på din utvecklingsdator.
   Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.
1. **Skapa ett projekt**.
   Starta ditt JavaScript-projekt genom att initiera det. Detta exempel demonstrerar användning i en webbläsarbaserad applikation.
1. **Lägg till referenser**.
   Lägg till en referens till Aspose.Cells i ditt projekt, till exempel genom att inkludera biblioteket på följande sätt:
   ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Conditional Formatting Example</title>
    </head>
    <body>
        <h1>Apply Conditional Formatting Based on Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormatConditionType, OperatorType, CellArea, Color } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add conditional formatting collection
            const cfCollection = worksheet.conditionalFormattings;
            const idx = cfCollection.add();
            const formatConditionCollection = cfCollection.get(idx);

            // Define the cell area to apply conditional formatting (A1)
            const area = CellArea.createCellArea(0, 0, 0, 0); // fromRow, fromCol, toRow, toCol
            formatConditionCollection.addArea(area);

            // Add a condition: Cell Value > 100
            const conditionIndex = formatConditionCollection.addCondition(
                FormatConditionType.CellValue,
                OperatorType.Greater,
                "100",
                null
            );

            const formatCondition = formatConditionCollection.get(conditionIndex);

            // Modify the style for the condition: bold and red font
            const style = formatCondition.style;
            if (!style.font) {
                style.font = {};
            }
            style.font.bold = true;
            style.font.color = Color.fromArgb(255, 255, 0, 0); // ARGB red

            // Assign modified style back (property assignment pattern)
            formatCondition.style = style;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'conditional_formatting_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied to cell A1 (value &gt; 100). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

När den ovan nämnda koden körs, tillämpas villkorlig formatering på cell "A1" i det första arket i utdatafilen (output.xls). Den villkorsstyrda formateringen som tillämpas på A1 beror på cellens värde. Om cellens värde i A1 är mellan 50 och 100 är bakgrundsfärgen röd på grund av den tillämpade villkorliga formateringen.

## **Använd Aspose.Cells för att tillämpa villkorlig formatering baserat på formel**

1. Tillämpa villkorlig formatering beroende på formel (kodsöndag)
   Nedan är koden för att utföra uppgiften. Den tillämpar villkorlig formatering på B3.
