---
title: Erhalte Kopf und Fußzeilen mit JavaScript via C++
linktitle: Header oder Footer erhalten
type: docs
weight: 30
url: /de/javascript-cpp/get-headers-or-footers/
description: Dieser Artikel erklärt, wie man programmgesteuert Kopf und Fußzeilen aus Excel oder OpenOffice Dateien mit der JavaScript über C++ API abruft.
---

{{% alert color="primary" %}}

Header und Fußzeilen werden nur in der Seitenlayoutansicht, der Druckvorschau und auf gedruckten Seiten angezeigt. 

Sie können auch das Dialogfeld Seitenlayout verwenden, wenn Sie Header oder Footer für mehr als ein Arbeitsblatt gleichzeitig anzeigen möchten. 

Für andere Blatttypen wie Diagrammblätter oder Diagramme können Header und Fußzeilen nur über das Dialogfeld Seitenlayout eingefügt werden.

{{% /alert %}}

## **Header und Fußzeilen in MS Excel erhalten**
1. Klicken Sie auf das Arbeitsblatt, auf dem Sie Header oder Footer anzeigen bzw. ändern möchten.
2. Klicken Sie auf der Ansicht-Registerkarte in der Gruppe Arbeitsblattansichten auf Seitenlayout.
   Excel zeigt das Arbeitsblatt in der Seitenlayoutansicht an.
3. Klicken Sie zum Anzeigen oder Bearbeiten eines Headers oder Footers auf die linke, mittlere oder rechte Kopf- oder Fußzeile am oberen oder unteren Rand der Arbeitsblattseite (unter Kopfzeile oder über Fußzeile).


## **Kopf- und Fußzeilen mit Aspose.Cells for JavaScript via C++ abrufen**
Mit [**PageSetup.header(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-) und [**PageSetup.footer(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-)-Methoden können JavaScript-Entwickler Kopf- oder Fußzeilen aus der Datei einfach abrufen.

1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen.
2. Holen Sie sich das Arbeitsblatt, auf dem Sie Header oder Footer abrufen möchten.
3. Holen Sie sich den Header oder Footer mit einer bestimmten Abschnitts-ID.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Header/Footer Reader Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

        function escapeHtml(str) {
            if (str === null || str === undefined) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerLeft = sheet.pageSetup.header(0);
            // Gets center section of header
            const headerCenter = sheet.pageSetup.header(1);
            // Gets right section of header
            const headerRight = sheet.pageSetup.header(2);
            // Gets center section of footer
            const footerCenter = sheet.pageSetup.footer(1);

            const resultHtml = [
                `<p><strong>Left Header:</strong> ${escapeHtml(headerLeft)}</p>`,
                `<p><strong>Center Header:</strong> ${escapeHtml(headerCenter)}</p>`,
                `<p><strong>Right Header:</strong> ${escapeHtml(headerRight)}</p>`,
                `<p><strong>Center Footer:</strong> ${escapeHtml(footerCenter)}</p>`
            ].join('');

            document.getElementById('result').innerHTML = resultHtml;
        });
    </script>
</html>
```

## **Kopf- und Fußzeilen zu Befehlsliste parsen**
Der Header- oder Footer-Text kann spezielle Befehle enthalten, z.B. einen Platzhalter für die Seitenzahl, das aktuelle Datum oder Textformatierungsattribute.

Spezialbefehle werden durch einen einzelnen Buchstaben mit einem vorangestellten Und-Zeichen ("&") dargestellt.

Die Header- und Footer-Strings werden unter Verwendung der ABNF-Grammatik aufgebaut. Ohne Viewer ist es schwer verständlich.

Aspose.Cells for JavaScript via C++ bietet die [**PageSetup.commands(string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#commands-string-)-Methode zum Parsen von Kopf- und Fußzeilen als Befehlsliste.

Die folgenden Codes zeigen, wie man den Header oder Footer als Befehlsliste parst und Befehle verarbeitet:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Header/Footer Commands Example</title>
    </head>
    <body>
        <h1>Header/Footer Commands Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerSection = sheet.pageSetup.header(0);
            const commands = sheet.pageSetup.commands(headerSection) || [];

            const items = [];
            commands.forEach(c => {
                const type = c.type;
                switch (type) {
                    case AsposeCells.HeaderFooterCommandType.SheetName:
                        // embedded the name of the sheet to header or footer
                        items.push('<li>SheetName command found (embeds sheet name)</li>');
                        break;
                    default:
                        items.push(`<li>Command type: ${type}</li>`);
                        break;
                }
            });

            if (!items.length) {
                items.push('<li>No header/footer commands found.</li>');
            }

            resultDiv.innerHTML = `<ul>${items.join('')}</ul>`;

            // Save the (possibly unchanged) workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HeaderFooter_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Workbook';
        });
    </script>
</html>
```
