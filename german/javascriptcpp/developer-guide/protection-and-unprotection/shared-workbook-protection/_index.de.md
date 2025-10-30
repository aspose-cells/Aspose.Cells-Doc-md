---
title: Passwortschutz oder entfernen der gemeinsam genutzten Arbeitsmappe mit JavaScript via C++
linktitle: Arbeitsmappe mit Kennwort schützen oder entschützen
type: docs
weight: 10
url: /de/javascript-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Mögliche Verwendungsszenarien**

 Sie können die gemeinsam genutzte Arbeitsmappe mit Microsoft Excel schützen oder entsperren, wie im folgenden Screenshot gezeigt. Aspose.Cells for JavaScript via C++ unterstützt diese Funktion ebenfalls mit den Methoden [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#protectSharedWorkbook-string-) und [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Freigegebenes Arbeitsblatt passwortgeschützt oder nicht passwortgeschützt machen**

Der folgende Beispielcode erstellt eine Arbeitsmappe, schützt sie und ermöglicht die Freigabe und speichert sie als [Ausgabedatei Excel](55541777.xlsx). Im Screenshot ist zu sehen, dass beim Versuch, den Schutz aufzuheben, Microsoft Excel Sie auffordert, das Passwort zum Aufheben des Schutzes einzugeben.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Shared Workbook Example</h1>
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
            // Creating an empty Workbook
            const workbook = new Workbook();

            // Protect the Shared Workbook with Password
            workbook.protectSharedWorkbook("1234");

            // Uncomment this line to Unprotect the Shared Workbook
            // workbook.unprotectSharedWorkbook("1234");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputProtectSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
