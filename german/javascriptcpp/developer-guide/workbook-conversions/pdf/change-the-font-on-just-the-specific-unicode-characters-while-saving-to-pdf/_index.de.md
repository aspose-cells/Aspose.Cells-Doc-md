---
title: Ändern Sie die Schriftart nur für bestimmte Unicode Zeichen beim Speichern in PDF mit JavaScript via C++
linktitle: Ändern Sie die Schriftart nur für bestimmte Unicode Zeichen beim Speichern in PDF
type: docs
weight: 260
url: /de/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Lernen Sie, wie man die Schriftart bestimmter Unicode Zeichen beim Speichern in PDF mit Aspose.Cells for JavaScript via C++ ändert. 
---

{{% alert color="primary" %}} 

Einige Unicode-Zeichen können von der benutzerdefinierten Schriftart nicht angezeigt werden. Ein solches Unicode-Zeichen ist **Trennstrich** (U+2011) und seine Unicode-Nummer ist 8209. Dieses Zeichen kann nicht mit **Times New Roman** angezeigt werden, aber es kann mit anderen Schriften wie **Arial Unicode MS** angezeigt werden.

 Wenn ein solches Zeichen innerhalb eines Wortes oder Satzes auftritt, das in einer bestimmten Schriftart wie Times New Roman vorliegt, ändert Aspose.Cells die Schriftart des gesamten Wortes oder Satzes in eine Schriftart, die dieses Zeichen anzeigen kann, z.B. Arial Unicode oder MS.

 Dies ist jedoch unerwünscht und einige Nutzer möchten nur die Schriftart dieses spezifischen Zeichens ändern, statt der gesamten Wort- oder Satzschriftart.

 Um dieses Problem zu lösen, stellt Aspose.Cells die Eigenschaft `PdfSaveOptions.isFontSubstitutionCharGranularity` bereit, die auf true gesetzt werden sollte, damit nur die Schriftart der nicht darstellbaren Zeichen in eine darstellbare Schriftart geändert wird, während der Rest des Wortes oder Satzes in der Originalschriftart bleibt.

{{% /alert %}} 

## **Beispiel**
Der folgende Screenshot vergleicht die beiden Ausgabepdf-Dateien, die vom unten stehenden Beispielcode erstellt wurden.

Es gibt ein PDF ohne Einstellung der Eigenschaft `PdfSaveOptions.isFontSubstitutionCharGranularity` und ein anderes, nachdem diese auf true gesetzt wurde.

Wie Sie im ersten PDF sehen können, hat sich die Schriftart des gesamten Satzes von Times New Roman zu Arial Unicode MS geändert, wegen des Nicht-Brechenden Gedankenstrichs. Im zweiten PDF hat sich nur die Schriftart des Nicht-Brechenden Gedankenstrichs geändert.

|**Erste PDF-Datei**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Zweite PDF-Datei**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Beispielcode**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result PDF 1</a>
        <a id="downloadLink2" style="display: none;">Download Result PDF 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p>Running example...</p>';

            // Create workbook object
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            let style = cell1.style;
            style.font.name = "Times New Roman";
            cell1.style = style;
            cell2.style = style;

            // Put the values inside the cell
            cell1.value = "Hello without Non-Breaking Hyphen";
            cell2.value = "Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen";

            // Autofit the columns
            worksheet.autoFitColumns();

            // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'SampleOutput_out.pdf';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download SampleOutput_out.pdf';

            // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
            const opts = new PdfSaveOptions();
            opts.isFontSubstitutionCharGranularity = true;
            const outputData2 = workbook.save(SaveFormat.Pdf, opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SampleOutput2_out.pdf';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download SampleOutput2_out.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated PDFs.</p>';
        });
    </script>
</html>
```
