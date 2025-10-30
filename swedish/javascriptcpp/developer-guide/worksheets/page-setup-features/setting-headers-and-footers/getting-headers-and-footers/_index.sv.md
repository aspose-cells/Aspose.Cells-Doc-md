---
title: Hämta sidhuvuden och sidfötter med JavaScript via C++
linktitle: Att få headers eller footers
type: docs
weight: 30
url: /sv/javascript-cpp/get-headers-or-footers/
description: Denna artikel förklarar hur man programmatisk hämtar sidhuvuden och sidfötter från Excel eller OpenOffice filer med JavaScript via C++ API.
---

{{% alert color="primary" %}}

Headers och footers visas endast i vy för sidlayout, utskriftsvisning och på utskrifter. 

Du kan också använda dialogrutan Sidlayout om du vill visa headers eller footers för mer än ett kalkylblad åt gången. 

För andra bladtyper, såsom kalkylblad eller diagram, kan du infoga headers och footers endast genom att använda dialogrutan Sidlayout.

{{% /alert %}}

## **Hämta sidhuvuden och sidfötter i MS Excel**
1. Klicka på kalkylarket där du vill visa eller ändra sidhuvuden eller sidfötter.
2. På fliken Visa, i gruppen arbetsboksvisningar, klicka på Sidlayout.
   Excel visar kalkylarket i Sidlayoutvy.
3. För att visa eller redigera en sidhuvud eller sidfot, klicka i vänster-, mitt- eller höger sidhuvud- eller sidfotstextruta längst upp eller längst ned på kalkylarket (under Sidhuvud eller ovanför Sidfot).


## **Hämta sidhuvuden och sidfötter med Aspose.Cells for JavaScript via C++**
Med [**PageSetup.header(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-) och [**PageSetup.footer(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-) metoder kan JavaScript-utvecklare enkelt hämta sidhuvuden eller sidfötter från filen.

1. Konstruera en arbetsbok för att öppna filen.
2. Hämta kalkylbladet där du vill hämta rubriker eller sidfot.
3. Hämta rubrik eller sidfot med ett specifikt avsnitts-ID.

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

## **Parera sidhuvuden och sidfötter till kommandolista**
Rubrik- eller sidfötters text kan innehålla specialkommandon, exempelvis en platshållare för sidnummer, aktuellt datum eller textformateringsattribut.

Specialkommandon representeras av en enda bokstav med en ledande och-symbol ("&").

Rubrik- och sidföttersträngarna konstrueras med ABNF-grammatik. Det är inte lätt att förstå utan en visare.

Aspose.Cells for JavaScript via C++ tillhandahåller [**PageSetup.commands(string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#commands-string-) metod för att tolka sidhuvuden och sidfötter som en kommandolista.

Följande kod visar hur man tolkar rubrik eller sidfot som kommando lista och bearbetar kommandon:

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
