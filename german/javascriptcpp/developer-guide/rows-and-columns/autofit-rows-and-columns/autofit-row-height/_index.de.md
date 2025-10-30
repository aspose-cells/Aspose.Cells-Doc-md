---
title: Autoanpassung der Zeilenhöhe beim Laden der Datei mit JavaScript über C++
linktitle: Automatische Anpassung der Zeilenhöhe beim Laden der Datei
type: docs
weight: 120
url: /de/javascript-cpp/autofit-row-height/
description: Erfahren Sie, wie Sie Zeilen, deren Höhe nicht angepasst ist, beim Laden der Datei mit Aspose.Cells for JavaScript über C++ anpassen.
keywords: Automatische Zeilenhöhenanpassung beim Laden der Datei JavaScript über C++, Zeilenhöhe beim Öffnen der Excel Datei automatisch anpassen JavaScript über C++ 
---

## **Mögliche Verwendungsszenarien**
Die Höhe der Zeile passt automatisch zur Schriftart des Inhalts, aber wenn die gespeicherte Zeilenhöhe nicht mit der Höhe des Inhalts in der Datei übereinstimmt, passt MS Excel beim Laden der Datei die Zeilenhöhe automatisch an, während Aspose.Cells for JavaScript über C++ dies nicht automatisch zur Leistungssteigerung tut. Wenn Sie das Aspose.Cells-Programm verwenden möchten, um beim Laden von Dateien automatisch Zeilenhöhen anzupassen, können Sie dies durch den Parameter [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) in Ihrem Code erreichen.

Bitte beachten Sie die folgende Bilddaten. Wir können beobachten, dass die zwischengespeicherte Zeilenhöhe in Zeile 11 15 beträgt, aber Excel hat die Zeilenhöhe beim Laden der Datei automatisch angepasst.
<br>
<img src="1.png" width=70% />

## **Zeilenhöhe mit Aspose.Cells for JavaScript über C++ anpassen**
Wenn Sie die Datei direkt laden und im PDF-Format speichern, werden die Daten im PDF nicht vollständig angezeigt, da die zwischengespeicherte Zeilenhöhe nur 15 beträgt.
<br>
<img src="2.png" width=70% />
<br>
Wenn Sie beim Laden der Datei den Parameter [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) auf true setzen, passt Aspose.Cells die Zeilenhöhe automatisch an. Die angepasste Zeilenhöhe kann die Textanzeigeanforderungen effektiv erfüllen.
<br>
<img src="3.png" width=70% />

## **JavaScript-Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LoadOptions & AutoFitter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;">Download out.pdf</a>
        </div>
        <div>
            <a id="downloadLink2" style="display: none;">Download out2.pdf</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, AutoFitterOptions } = AsposeCells;

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
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const data = new Uint8Array(arrayBuffer);

            // Load workbook and save as out.pdf
            const workbook = new Workbook(data);
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink1.href = URL.createObjectURL(blob);
            downloadLink1.download = 'out.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download out.pdf';

            // Prepare LoadOptions with AutoFitterOptions and onlyAuto = true
            const loadOptions = new LoadOptions();
            loadOptions.autoFitterOptions = new AutoFitterOptions();
            loadOptions.autoFitterOptions.onlyAuto = true;

            // Load workbook with loadOptions and save as out2.pdf
            const book = new Workbook(data, loadOptions);
            const outputData2 = book.save(SaveFormat.Pdf);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out2.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download out2.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download links to get the generated PDF files.</p>';
        });
    </script>
</html>
```
