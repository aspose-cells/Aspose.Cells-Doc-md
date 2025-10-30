---
title: Arbeitsblatt mit JavaScript via C++ schützen und ungeschützt lassen
linktitle: Arbeitsblatt schützen und entschützen
type: docs
weight: 40
url: /de/javascript-cpp/protect-and-unprotect-worksheets/
description: Arbeitsblatt in Excel Dateien mit Aspose.Cells for JavaScript via C++ schützen und ungeschützt lassen.
---

{{% alert color="primary" %}}  
Um zu verhindern, dass andere Benutzer versehentlich oder absichtlich Daten in einem Arbeitsblatt ändern, verschieben oder löschen, können Sie die Zellen in Ihrem Excel-Arbeitsblatt sperren und das Blatt dann mit einem Kennwort schützen.  
{{% /alert %}}  

## **Arbeitsblatt in MS Excel schützen und aufheben**  

**![Arbeitsblatt schützen und aufheben](schuetzen-und-aufheben.png)**  

1. Klicken Sie auf **Überprüfen > Arbeitsblatt schützen**.  
1. Geben Sie ein Passwort in das **Passwortfeld** ein.  
1. Wählen Sie die **Zulassen**-Optionen aus.  
1. Wählen Sie **OK**, geben Sie das Passwort erneut ein, um es zu bestätigen, und wählen Sie dann erneut **OK**.  

## **Arbeitsblatt mit Aspose.Cells for JavaScript via C++ schützen**  
Es sind nur die folgenden einfachen Codezeilen erforderlich, um die Arbeitsmappenstruktur von Excel-Dateien zu schützen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            // Create a new file (workbook)
            const workbook = new Workbook();

            // Gets the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Protect contents of the worksheet.
            sheet.protect(ProtectionType.Contents);

            // Protect worksheet with password.
            sheet.protection.password = "test";

            // Save as Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected and file is ready. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Arbeitsblatt mit Aspose.Cells for JavaScript via C++ aufheben**  
Das Entschutz des Arbeitsblatts ist einfach mit Aspose.Cells API. Wenn das Arbeitsblatt kennwortgeschützt ist, wird ein korrektes Passwort benötigt.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Unprotect Worksheet Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Worksheet</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unprotect contents of the worksheet using password
            sheet.unprotect("password");

            // Save the modified workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Erweiterte Themen**  
- [Erweiterte Schutzeinstellungen seit Excel XP](/cells/de/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [Überprüfen Sie, ob das Arbeitsblatt mit einem Kennwort geschützt ist](/cells/de/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [Arbeitsblätter schützen](/cells/de/javascript-cpp/protecting-worksheets/)  
- [Arbeitsblatt entsperren](/cells/de/javascript-cpp/unprotect-a-worksheet/)  
- [Überprüfen Sie das verwendete Kennwort zum Schutz des Arbeitsblatts](/cells/de/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
