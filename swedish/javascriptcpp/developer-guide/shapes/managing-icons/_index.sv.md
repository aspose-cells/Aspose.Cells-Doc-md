---
title: Lägg till ikoner i kalkbladet med JavaScript via C++
linktitle: Hantera ikoner
type: docs
weight: 100
url: /sv/javascript-cpp/insert-svg-to-excel/
---

## Lägg till ikoner i kalkbladet i Aspose.Cells for JavaScript via C++

Om du behöver använda [Aspose.Cells](https://products.aspose.com/cells/) för att lägga till 'ikoner' i en Excelfil, kan detta dokument ge dig hjälp.

Gränssnittet för Excel som motsvarar infogning av ikoner är följande:

![](1.png)

- Välj positionen för ikonen som ska infogas i arbetsboken
- Vänsterklicka på *Infoga*->*Ikoner*
- I fönstret som öppnas väljer du ikonen i rutan med röd ram i figuren ovan
- Vänsterklicka *Infoga*, den kommer att infogas i Excel-filen.

Effekten är följande:

![](2.png)

Här har vi förberett *exempelkod* för att hjälpa dig att infoga ikoner med [Aspose.Cells](https://products.aspose.com/cells/). Det finns också en nödvändig [exempelfil](sample.xlsx) och en ikon [resursfil](icon.zip). Vi använde Excel-gränssnittet för att infoga en ikon med samma visningseffekt som [resursfilen](icon.zip) i [exempelfilen](sample.xlsx).

### JavaScript

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Icon to Worksheet Example</h1>
        <p>Select an Excel file and an SVG icon file, then click "Run Example".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="iconInput" accept=".svg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            const iconInput = document.getElementById('iconInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!iconInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an SVG icon file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const iconFile = iconInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const iconArrayBuffer = await iconFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the icon to the worksheet
            const iconBytes = new Uint8Array(iconArrayBuffer);
            sheet.shapes.addIcons(3, 0, 7, 0, 100, 100, iconBytes, null);

            // Set a prompt message
            const c = sheet.cells.get(8, 7);
            c.value = "Insert via Aspose.Cells";
            const s = c.style;
            s.font.color = Color.Blue;
            c.style = s;

            // Save and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Icon added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

När du utför ovanstående kod i ditt projekt kommer du att få följande resultat:

![](3.png)
