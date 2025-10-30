---
title: Åtkomst och uppdatering av delar av riktad text från cellen
linktitle: Riktad formateringstext
type: docs
weight: 40
url: /sv/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Lär dig att komma åt och uppdatera delar av rik text av cellen genom Aspose.Cells for JavaScript via C++ API.
keywords: Kom åt och uppdatera rik text i cell, Få rik text i cell, Redigera rik text i cell, Kom åt rik text i cell, Uppdatera rik text i cell, Ändra rik text i cell
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ tillåter dig att komma åt och uppdatera delar av cellens rik text. För detta ändamål kan du använda [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) och [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) egenskaper. Dessa egenskaper returnerar och accepterar en array av [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) objekt som du kan använda för att komma åt och uppdatera olika egenskaper för typsnitt, som typsnittnamn, typsnittfärg, fetstil med mera.

{{% /alert %}}

## **Åtkomst och uppdatering av delar av riktad text från cellen**

Följande kod demonstrerar användningen av [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) och [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) egenskaper med hjälp av [källfilen för Excel](5112369.xlsx) som du kan ladda ner från länken. Källfilen har rik text i cell A1. Den innehåller tre delar, och varje del har ett annat typsnitt. Kodsnutten använder dessa delar och uppdaterar den första delen med ett nytt typsnitt. Slutligen sparar den arbetsboken som [utdata-excel](5112366.xlsx). När du öppnar den kommer du att se att typsnittet för den första delen av texten har ändrats till **"Arial"**.

### JavaScript-kod för att komma åt och uppdatera delar av rik text i cellen

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Konsoloutput som genereras av provkoden



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
