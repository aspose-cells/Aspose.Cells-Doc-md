---
title: Benutzerdefinierte Papiergröße des Arbeitsblatts für Rendering mit JavaScript über C++ implementieren
linktitle: Benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung implementieren
type: docs
weight: 70
url: /de/javascript-cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Dieser Artikel erklärt, wie man die JavaScript API über C++ verwendet, um eine benutzerdefinierte Papiergröße für die gewünschten Arbeitsblätter beim automatischen Konvertieren einer Excel Datei in PDF Format festzulegen.
keywords: Benutzerdefinierte Papiergröße beim Rendern von Excel nach PDF mit JavaScript über C++ festlegen
---

## **Mögliche Verwendungsszenarien**  

Es gibt keine direkte Option, um benutzerdefinierte Papiergrößen in MS Excel zu erstellen, jedoch können Sie beim Programmgesteuerten Exportieren einer Excel-Datei in PDF-Format eine benutzerdefinierte Papiergröße für Ihre gewünschten Arbeitsblätter festlegen. Dieses Dokument erklärt, wie man eine benutzerdefinierte Papiergröße eines Arbeitsblatts mit Aspose.Cells APIs festlegt.  

## **Benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung implementieren**  

Aspose.Cells ermöglicht es Ihnen, die gewünschte Papiergröße des Arbeitsblatts festzulegen. Sie können die [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#customPaperSize-number-number-)-Methode der [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)-Klasse verwenden, um eine benutzerdefinierte Seitengröße anzugeben. Der folgende Beispielcode zeigt, wie Sie eine benutzerdefinierte Papiergröße für das erste Arbeitsblatt im Arbeitsbuch festlegen. Bitte beachten Sie auch das [Ausgabe-PDF](45056028.pdf), das mit dem folgenden Code zur Referenz erstellt wurde.  

## **Screenshot**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom PDF Paper Size Example</h1>
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
                // If no file provided, create a new workbook as in the original JavaScript example
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Set custom paper size in unit of inches
                ws.pageSetup.customPaperSize(6, 4);

                // Access cell B4
                const b4 = ws.cells.get("B4");

                // Add the message in cell B4
                b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

                // Save the workbook in pdf format
                const outputData = wb.save(SaveFormat.Pdf);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputCustomPaperSize.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Set custom paper size in unit of inches
            ws.pageSetup.customPaperSize(6, 4);

            // Access cell B4
            const b4 = ws.cells.get("B4");

            // Add the message in cell B4
            b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

            // Save the workbook in pdf format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCustomPaperSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
