---
title: Sätta delad formel med JavaScript via C++
linktitle: Ange Delad Formel
type: docs
weight: 10
url: /sv/javascript-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Om du vill lägga till en funktion i ett kalkylblad som gör beräkningar, förklaras hur du kan åstadkomma detta med Aspose.Cells for JavaScript via C++.

{{% /alert %}}

## Sätta delad formel med Aspose.Cells for JavaScript via C++

Anta att du har ett kalkylblad fyllt med data i det format som liknar det följande exempelkalkylbladet.

|**Inmatningsfil med en kolumn data**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Du vill lägga till en funktion i B2 som kommer att beräkna momsen för den första dataraden. Skatten är **9%**. Formeln som beräknar momsen är: **"=A2*0.09"**. Den här artikeln förklarar hur man tillämpar denna formel med Aspose.Cells.

Aspose.Cells låter dig ange en formel med hjälp av [**Cell.formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) egenskap. Det finns två alternativ för att lägga till formler till de andra cellerna (B3, B4, B5, etc.) i kolumnen.

 Antingen gör du vad du gjorde för den första cellen, effektivt ställer in formeln för varje cell, och uppdaterar cellreferensen därefter (A3*0,09, A4*0,09, A5*0,09 och så vidare). Detta kräver att cellreferenserna för varje rad uppdateras. Det kräver också att Aspose.Cells analyserar varje formel individuellt, vilket kan ta tid för stora kalkylblad och komplexa formler. Det lägger också till extra kodrader även om loopar kan minska detta något.

Ett annat tillvägagångssätt är att använda en **delad formel**. Med en delad formel uppdateras formlerna automatiskt för cellreferenser i varje rad så att momsen beräknas korrekt. [**Cell.sharedFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#sharedFormula-string-number-number-) metoden är mer effektiv än det första tillvägagångssättet.

Följande exempel visar hur du använder den.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Apply Shared Formula</title>
    </head>
    <body>
        <h1>Apply Shared Formula Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection in the first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Apply the shared formula in the range i.e., B2:B14
            const cell = cells.get("B2");
            // Converted setSharedFormula(...) to property assignment per universal rule.
            cell.sharedFormula = { formula: "=A2*0.09", rowCount: 13, columnCount: 1 };

            // Save the excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared formula applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
