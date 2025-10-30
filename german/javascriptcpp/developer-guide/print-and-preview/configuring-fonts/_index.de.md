---
title: Konfigurieren von Schriftarten für die Darstellung von Tabellenkalkulationen mit JavaScript via C++
linktitle: Konfigurieren von Schriftarten zur Darstellung von Tabellenkalkulationen
type: docs
weight: 10
url: /de/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Erfahren Sie, wie Sie Schriftarten für die Darstellung von Tabellenkalkulationen mit Aspose.Cells for JavaScript via C++ konfigurieren. Stellen Sie sicher, dass Schriftarten für eine optimale Konvertierungsqualität verfügbar sind.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells APIs bieten die Möglichkeit, Tabellenkalkulationen in Bildformate zu rendern sowie in PDF- und XPS-Formate zu konvertieren. Um die Konvertierungsqualität zu maximieren, müssen die in der Tabelle verwendeten Schriftarten im Standard-Schriftartenverzeichnis des Betriebssystems vorhanden sein. Falls die erforderlichen Schriftarten nicht vorhanden sind, versuchen die APIs, die benötigten Schriftarten durch verfügbare zu ersetzen.

## **Auswahl von Schriftarten**

Im Folgenden wird der Prozess erläutert, den die Aspose.Cells-APIs im Hintergrund durchlaufen.

1. Die API versucht, die Schriftarten im Dateisystem zu finden, die dem exakten Schriftartnamen entsprechen, der in der Tabelle verwendet wird.
1. Wenn die API die Schriftarten mit genau demselben Namen nicht finden kann, versucht sie, die Standardschriftart unter dem [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)-Eigenschaft des Arbeitsblatts zu verwenden.
1. Wenn die API die unter [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) oder [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) Eigenschaft zu verwenden.
1. Wenn die API die unter [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) oder [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--) Eigenschaft zu verwenden.
1. Wenn die API die unter [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--) definierte Schriftart nicht finden kann, versucht sie, die geeignetsten Schriftarten aus allen verfügbaren Schriftarten auszuwählen.
1. Schließlich rendert die API die Tabelle mit Arial, wenn sie keine Schriftarten im Dateisystem finden kann.

## **Benutzerdefinierte Schriftartordner einstellen**

Die APIs von Aspose.Cells durchsuchen das Standard-Schriftartenverzeichnis des Betriebssystems nach den erforderlichen Schriftarten. Falls die Schriftarten im System nicht vorhanden sind, durchsuchen die APIs benutzerdefinierte (vom Nutzer festgelegte) Verzeichnisse. Die Klasse [**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs) bietet verschiedene Methoden, um benutzerdefinierte Schriftartenverzeichnisse festzulegen, wie unten beschrieben.

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): Diese Methode ist nützlich, wenn nur ein Ordner festgelegt werden soll.
1. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): Diese Methode ist nützlich, wenn die Schriftarten in mehreren Ordnern vorhanden sind und der Benutzer alle Ordner separat einrichten möchte, anstatt alle Schriftarten in einem einzigen Ordner zu kombinieren.
1. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): Diese Mechanismus ist nützlich, wenn der Benutzer Schriften aus mehreren Ordnern laden möchte oder eine einzelne Schriftdatei oder Schriftdaten aus einem Byte-Array.

{{% alert color="primary" %}}

Beide [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) und [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) Methoden akzeptieren einen booleschen Typ als zweiten Parameter. Das Übergeben von **true** als zweitem Parameter leitet die Aspose.Cells-APIs an, die Unterordner nach den Schriftarten-Dateien zu durchsuchen.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Font Configuration Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Font Configuration Example</h1>
        <p>Select an Excel file (optional) and font resources to configure Aspose.Cells font sources in the browser.</p>

        <label>Excel File (optional):</label>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>

        <label>Font File (.ttf/.otf) (optional):</label>
        <input type="file" id="fontFileInput" accept=".ttf,.otf" />
        <br/><br/>

        <label>Font Folder (optional, select a folder):</label>
        <input type="file" id="fontFolderInput" webkitdirectory directory multiple />
        <br/><br/>

        <button id="runExample">Configure Fonts</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fontFileInput = document.getElementById('fontFileInput');
            const fontFolderInput = document.getElementById('fontFolderInput');
            const resultDiv = document.getElementById('result');

            // Basic validation: ensure at least one font resource is provided (file or folder)
            if (!fontFileInput.files.length && !fontFolderInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least one font file or a font folder.</p>';
                return;
            }

            // Defining string variables to store paths/names to font folders & font file
            // (In browser environment we use simple names or uploaded file names)
            const fontFolder1 = "Arial";
            const fontFolder2 = "Calibri";
            const fontFile = "arial.ttf";

            // Setting first font folder (converted from setFontFolder)
            AsposeCells.FontConfigs.fontFolder = fontFolder1;
            // Preserve the subfolder-search flag from original API call as a separate property
            AsposeCells.FontConfigs.fontFolderSearchSubFolders = true;

            // Setting both font folders (converted from setFontFolders)
            AsposeCells.FontConfigs.fontFolders = [fontFolder1, fontFolder2];
            // Preserve the subfolder-search flag as a separate property
            AsposeCells.FontConfigs.fontFoldersSearchSubFolders = false;

            // Defining FolderFontSource
            const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

            // Defining FileFontSource
            const sourceFile = new AsposeCells.FileFontSource(fontFile);

            // Defining MemoryFontSource
            let memoryFontBytes = new Uint8Array([]);
            if (fontFileInput.files.length) {
                const ff = fontFileInput.files[0];
                const arrayBuffer = await ff.arrayBuffer();
                memoryFontBytes = new Uint8Array(arrayBuffer);
            } else if (fontFolderInput.files.length) {
                // If a folder was provided, try to find a .ttf/.otf inside it and use the first found
                const files = Array.from(fontFolderInput.files);
                const fontCandidate = files.find(f => f.name.toLowerCase().endsWith('.ttf') || f.name.toLowerCase().endsWith('.otf'));
                if (fontCandidate) {
                    const arrayBuffer = await fontCandidate.arrayBuffer();
                    memoryFontBytes = new Uint8Array(arrayBuffer);
                }
            }
            const sourceMemory = new AsposeCells.MemoryFontSource(memoryFontBytes);

            // Setting font sources (converted from setFontSources)
            AsposeCells.FontConfigs.fontSources = [sourceFolder, sourceFile, sourceMemory];

            // Provide feedback to the user
            resultDiv.innerHTML = '<p style="color: green;">Font configuration applied successfully.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Bitte verwenden Sie eine der oben genannten Methoden zu Beginn der Anwendung, also bevor andere Objekte der Aspose.Cells-APIs aufgerufen werden.

{{% /alert %}} {{% alert color="primary" %}}

Wenn alle oben genannten Methoden zum Festlegen der Schriftquellen verwendet werden, gelten nur die letzten Einstellungen.

{{% /alert %}}

## **Schriftarten-Ersatzmechanismus**

Die APIs von Aspose.Cells bieten auch die Möglichkeit, Ersatzschriften für Renderungszwecke anzugeben. Dieses Mechanismus ist hilfreich, wenn eine benötigte Schriftart auf dem System nicht verfügbar ist. Nutzer können eine Liste von Schriftartenamen als Alternativen zu der ursprünglich geforderten Schriftart angeben. Dafür hat die API die Methode [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-) freigegeben, die 2 Parameter akzeptiert. Der erste Parameter ist vom Typ **string**, der Name der zu ersetzenden Schriftart. Der zweite Parameter ist ein Array vom Typ **string**. Nutzer können eine Liste von Schriftartnamen als Ersatz für die ursprüngliche Schriftart (im ersten Parameter angegeben) bereitstellen.

Hier ist ein einfaches Anwendungsbeispiel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Substituting the Arial font with Times New Roman & Calibri
            // Converted from: AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
            AsposeCells.FontConfigs.fontSubstitutes = { "Arial": ["Times New Roman", "Calibri"] };

            // Saving the (possibly modified) workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the processed file.</p>';
        });
    </script>
</html>
```

## **Informationssammlung**

Zusätzlich zu den oben genannten Methoden bieten die APIs von Aspose.Cells auch Mittel, um Informationen über festgelegte Quellen und Alternativen zu sammeln.

1. Die [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) Methode gibt ein Array vom Typ [**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase) zurück, das die Liste der angegebenen Schriftartenquellen enthält. Falls keine Quellen festgelegt wurden, gibt die [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) Methode ein leeres Array zurück.
1. Die [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) Methode akzeptiert einen Parameter vom Typ **string**, um den Namen der Schriftart anzugeben, für die eine Ersetzung festgelegt wurde. Falls für den angegebenen Schriftartnamen keine Ersetzung festgelegt ist, gibt die [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) Methode null zurück.

## **Erweiterte Themen**
- [Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen](/cells/de/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Die Eigenschaft DefaultFont von PdfSaveOptions und ImageOrPrintOptions festlegen, um Priorität zu haben](/cells/de/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Unterstützte Schriftformate](/cells/de/javascript-cpp/supported-font-formats/)
- [Arbeitsblatt zu Bild - Setzen des Pixelformats für das gerenderte Bild](/cells/de/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
