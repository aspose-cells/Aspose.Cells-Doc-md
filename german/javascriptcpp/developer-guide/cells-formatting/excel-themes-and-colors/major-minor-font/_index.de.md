---
title: Überschriften und Textkörper Thema Schriftart
linktitle: Überschriften und Textkörper Thema Schriftart
description: Aspose.Cells ist eine JavaScript über C++ Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Unterstützt das Festlegen von Überschriften und Fliesstext Theme Schriften in Excel Dokumenten, sodass Benutzer das Erscheinungsbild und den Stil des Dokuments anpassen können. Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek nutzt, um mit Überschrift und Fließtext Theme Schriften in Excel Dokumenten zu arbeiten.
keywords: Aspose.Cells, Excel Dokument, Überschrift, Fließtext, Theme Schriftart, Erscheinungsbild, Stil, JavaScript über C++
type: docs
weight: 120
url: /de/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Die Standardschriftart ändert sich automatisch, wenn die Regionseinstellung geändert wird.

Wenn die Standard-Schriftart geändert wird, ändert sich auch die Zeilenhöhe und Spaltenbreite, und es kann sogar die Seitenlayout durcheinander bringen.

Was hat die Änderung der Standard-Schriftart verursacht?

Wenn die Excel-Themenschriftart festgelegt ist, wechselt Excel automatisch zwischen verschiedenen Schriftarten basierend auf der aktuellen Sprachumgebung.

{{% /alert %}}

## **Überschriften- und Textkörper-Themenschriftart in Excel**

Wählen Sie in Excel die Registerkarte Start, klicken Sie auf die Dropdown-Box für Schriftarten. Sie sehen "Theme Fonts" mit zwei Theme-Schriftarten: Calibri Light (Überschriften) und Calibri (Körper) mit englischer Regions-Einstellung.

**![Themenschriften](Theme-Fonts.png)**

Wenn Theme Font ausgewählt ist, wird der Schriftartname in verschiedenen Regionen unterschiedlich angezeigt. Wenn Sie nicht möchten, dass sich die Schriftart automatisch in verschiedenen Regionen ändert, wählen Sie die beiden Theme Fonts nicht aus.

## **Ändern der Überschrift- und Fließtext-Schriftart programmatisch**
Mit Aspose.Cells for JavaScript über C++ können wir prüfen, ob die Standardschriftart eine Theme-Schriftart ist oder die Theme-Schriftart mit der [**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-)-Methode setzen.

Das folgende Beispiel zeigt, wie man die Theme-Schriftart manipuliert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Dynamisch lokale Design-Schriftart programmatisch abrufen**
Manchmal befinden sich unsere Server und die Rechner der Benutzer nicht in der gleichen Region. Wie können wir dieselbe Schriftart, die Benutzer für die Dateiverarbeitung möchten, erhalten?

Wir müssen die regionalen Systemeinstellungen festlegen, bevor die Datei mit der Methode [**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-) geladen wird.

Der folgende Beispielcode zeigt, wie man lokale Design-Schriftarten erhält.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
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

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```
