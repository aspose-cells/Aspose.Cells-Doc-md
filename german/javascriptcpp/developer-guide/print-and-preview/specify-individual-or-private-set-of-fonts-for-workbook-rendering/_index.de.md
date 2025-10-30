---
title: Individuelle oder private Schriftarten für das Arbeitsblatt Rendering mit JavaScript via C++ angeben
linktitle: Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben
type: docs
weight: 40
url: /de/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Erfahren Sie, wie Sie einzelne oder private Schriftarten Sätze für das Arbeitsblatt Rendering mit Aspose.Cells for JavaScript via C++ angeben.
---

## **Mögliche Verwendungsszenarien**  

Im Allgemeinen geben Sie das Verzeichnis der Schriftarten oder eine Liste von Schriftarten für alle Arbeitsblätter an, aber manchmal müssen Sie individuelle oder private Schriftarten-Sätze für Ihre Arbeitsblätter angeben. Aspose.Cells for JavaScript via C++ bietet die Klasse [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs), mit der Sie individuelle oder private Schriftarten für Ihr Arbeitsblatt festlegen können.  

## **Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben**  

Der folgende Beispielcode lädt die [Beispieldatei Excel](67338268.xlsx) mit ihren individuellen oder privaten Schriftarten, die mit der Klasse [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs) angegeben sind. Bitte sehen Sie sich die [Beispielschriftart](67338271.zip) an, die im Code verwendet wird, sowie das [Ausgabepdf](67338269.pdf), das damit erstellt wurde. Die folgende Bildschirmaufnahme zeigt, wie das Ausgabepdf aussieht, wenn die Schriftart erfolgreich gefunden wird.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Individual Or Private Fonts Example</title>
    </head>
    <body>
        <h1>Specify Individual Or Private Fonts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, IndividualFontConfigs } = AsposeCells;

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

            // Path of your custom font directory.
            const customFontsDir = "C:\\TempDir\\CustomFonts";

            // Specify individual font configs custom font directory.
            const fontConfigs = new IndividualFontConfigs();

            // If you comment this line or if custom font directory is wrong or 
            // if it does not contain required font then output pdf will not be rendered correctly.
            // Converted setFontFolder -> property assignment (first argument used)
            fontConfigs.fontFolder = customFontsDir;

            // Specify load options with font configs.
            const opts = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
            // Converted setFontConfigs -> property assignment
            opts.fontConfigs = fontConfigs;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file with individual font configs.
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save to PDF format.
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
