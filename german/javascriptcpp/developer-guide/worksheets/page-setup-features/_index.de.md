---
title: Seitenlayout Funktionen mit JavaScript über C++
linktitle: Seiteneinrichtungsfunktionen
type: docs
weight: 60
url: /de/javascript-cpp/page-setup-features/
description: Erkunden Sie Seitenlayout Funktionen mit Aspose.Cells for JavaScript über C++. Lernen Sie, wie man Seitengröße, Ausrichtung und Einstellungen konfiguriert.
keywords: Seitenlayout Funktionen in JavaScript über C++, Seitengröße in JavaScript über C++ konfigurieren, Seitenausrichtung in JavaScript über C++ einstellen
---

## **Einführung**
Mit Aspose.Cells for JavaScript über C++ können Sie verschiedene Seitenlayout-Funktionen eines Excel-Arbeitsbuchs manipulieren. Diese Funktionen umfassen die Einstellung der Seitengröße, Ausrichtung, Ränder und mehr. Eine ordnungsgemäße Konfiguration dieser Funktionen sorgt für eine bessere Druck- und Anzeigeerfahrung.

## ** Seitengröße und Ausrichtung einstellen**
 Sie können die Seitengröße und Ausrichtung eines Arbeitsblatts mit der `PageSetup`-Klasse festlegen. Diese bietet verschiedenste Eigenschaften zur Verwaltung von Seitendimensionen und Layout.

### **Beispielcode**
 Hier ist ein Beispielcode, der zeigt, wie man die Seitengröße und Ausrichtung festlegt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <p>You may optionally upload an existing Excel file to modify. If none is selected, a new workbook will be created.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the page size to A4 (paperSize = 0)
            worksheet.pageSetup.paperSize = 0;

            // Set the page orientation to Landscape (orientation = 1)
            worksheet.pageSetup.orientation = 1;

            // Save the workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetupExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Ränder einstellen**
 Sie können auch die Ränder für die Seite mit derselben `PageSetup`-Klasse festlegen. Die Ränder können für links, rechts, oben und unten angepasst werden.

### **Beispielcode**
 So können Sie die Ränder eines Arbeitsblatts festlegen.
