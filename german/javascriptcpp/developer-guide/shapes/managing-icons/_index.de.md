---
title: Fügen Sie Icons mit JavaScript via C++ in das Arbeitsblatt ein
linktitle: Symbole verwalten
type: docs
weight: 100
url: /de/javascript-cpp/insert-svg-to-excel/
---

## Icons in das Arbeitsblatt in Aspose.Cells for JavaScript via C++ hinzufügen

Wenn Sie [Aspose.Cells](https://products.aspose.com/cells/) verwenden müssen, um 'Symbole' in eine Excel-Datei hinzuzufügen, kann Ihnen dieses Dokument einige Hilfe bieten.

Die Excel-Benutzeroberfläche für die Einfüge-Symbol-Operation sieht wie folgt aus:

![](1.png)

- Wählen Sie die Position des Symbols, das in das Arbeitsblatt eingefügt werden soll
- Klicken Sie links auf *Einfügen*->*Symbole*
- In dem sich öffnenden Fenster wählen Sie das Symbol im roten Rechteck in der obigen Abbildung aus
- Linksklick *Einfügen*, es wird in die Excel-Datei eingefügt.

Der Effekt ist wie folgt:

![](2.png)

Hier haben wir *Beispiellcode* vorbereitet, um Ihnen beim Einfügen von Symbolen mit [Aspose.Cells](https://products.aspose.com/cells/) zu helfen. Es gibt auch eine notwendige [Beispiel-Datei](sample.xlsx) und eine Symbol [Ressourcendatei](icon.zip). Wir haben die Excel-Oberfläche benutzt, um ein Symbol mit dem gleichen Anzeigeeffekt wie die [Ressourcendatei](icon.zip) in der [Beispiel-Datei](sample.xlsx) einzufügen.

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

Wenn Sie den obigen Code in Ihrem Projekt ausführen, erhalten Sie die folgenden Ergebnisse:

![](3.png)
