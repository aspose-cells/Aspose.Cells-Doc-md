---
title: Aggiungere icone al foglio di lavoro con JavaScript tramite C++
linktitle: Gestione delle icone
type: docs
weight: 100
url: /it/javascript-cpp/insert-svg-to-excel/
---

## Aggiungi icone al foglio di lavoro in Aspose.Cells for JavaScript tramite C++

Se hai bisogno di utilizzare [Aspose.Cells](https://products.aspose.com/cells/) per aggiungere 'icone' in un file Excel, allora questo documento può offrirti un aiuto.

L'interfaccia Excel corrispondente all'operazione di inserimento icona è la seguente:

![](1.png)

- Seleziona la posizione dell'icona da inserire nel foglio di lavoro
- Clicca sinistro su *Inserisci*->*Icone*
- Nella finestra che si apre, seleziona l'icona nel rettangolo rosso nella figura sopra
- Clic sinistro *Inserisci*, verrà inserito nel file Excel.

L'effetto è il seguente:

![](2.png)

Qui abbiamo preparato *codice di esempio* per aiutarti a inserire icone usando [Aspose.Cells](https://products.aspose.com/cells/). C'è anche un *file di esempio* necessario [sample.xlsx] e un [file di risorse] di icona [icon.zip]. Abbiamo usato l'interfaccia di Excel per inserire un'icona con lo stesso effetto di visualizzazione del [file di risorse](icon.zip) nel [file di esempio](sample.xlsx).

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

Quando esegui il codice sopra nel tuo progetto, otterrai i seguenti risultati:

![](3.png)
