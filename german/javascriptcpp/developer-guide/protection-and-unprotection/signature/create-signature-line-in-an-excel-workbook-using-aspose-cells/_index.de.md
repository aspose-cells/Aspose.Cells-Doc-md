---
title: Signaturzeile in einer Excel Arbeitsmappe mit Aspose.Cells for JavaScript via C++ erstellen
linktitle: Erstellen Sie eine Signaturlinie in einer Excel Arbeitsmappe mit Aspose.Cells
type: docs
weight: 150
url: /de/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Dieser Artikel beschreibt, wie man mit JavaScript und Aspose.Cells for JavaScript eine Signaturzeile in einer Excel Arbeitsmappe erstellt.
keywords: Signaturzeile in einer Excel Arbeitsmappe mit JavaScript via C++, Wie man eine Signaturzeile in einer Excel Arbeitsmappe erstellt, Wie man eine Signatur hinzufügt, Wie man eine Signaturzeile zu einer Excel Datei hinzufügt.
---

## **Einführung**  

Microsoft Excel bietet die Möglichkeit, **Signaturlinie** in Excel-Arbeitsmappen hinzuzufügen. Sie können eine Signaturlinie hinzufügen, indem Sie auf die Registerkarte **Einfügen** klicken und dann **Signaturlinie** aus der Gruppe **Text** auswählen.  

## **Wie man eine Signaturlinie für Excel erstellt**  

 Aspose.Cells for JavaScript via C++ bietet diese Funktion ebenfalls und hat die Eigenschaft [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) für diesen Zweck freigegeben. Dieser Artikel erklärt, wie man diese Eigenschaft verwendet, um mit Aspose.Cells eine Signaturzeile hinzuzufügen.  

Der folgende Beispielcode fügt eine Signaturzeile mit der Eigenschaft [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) hinzu und speichert die Arbeitsmappe.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
