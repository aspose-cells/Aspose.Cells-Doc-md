---
title: Arbeitsblattstruktur mit JavaScript via C++ schützen und ungeschützt lassen
linktitle: Arbeitsmappenstruktur schützen und entschützen
type: docs
weight: 40
url: /de/javascript-cpp/protect-and-unprotect-workbook-structure/
description: Schützen und aufheben des Schutzes der Arbeitsblattstruktur von Excel Dateien mit JavaScript über C++.
---


{{% alert color="primary" %}}  
Um zu verhindern, dass andere Benutzer versteckte Arbeitsblätter einsehen, Arbeitsblätter hinzufügen, verschieben, löschen oder ausblenden und Arbeitsblätter umbenennen, können Sie die Struktur Ihres Excel-Arbeitsblatts mit einem Kennwort schützen.  
{{% /alert %}}  


## **Schützen und entschützen der Arbeitsmappenstruktur in MS Excel**  

**![Arbeitsmappenstruktur schützen und entschützen](schuetzen-und-entschuetzen-arbeitsmappenstruktur.png)**  

1. Klicken Sie auf **Überprüfen > Arbeitsmappe schützen**.  
1. Geben Sie ein Passwort in das **Passwortfeld** ein.  
1. Wählen Sie **OK**, geben Sie das Passwort erneut ein, um es zu bestätigen, und wählen Sie dann erneut **OK**.  


## **Arbeitsblattstruktur mithilfe von Aspose.Cells for JavaScript via C++ schützen**  
Es sind nur die folgenden einfachen Codezeilen erforderlich, um die Arbeitsmappenstruktur von Excel-Dateien zu schützen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Protect workbook structure with a password
            workbook.protect(ProtectionType.Structure, "password");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1_protected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Arbeitsblattstruktur mit Aspose.Cells for JavaScript via C++ aufheben**  
Die Entschützung der Arbeitsmappenstruktur ist mit der Aspose.Cells API einfach.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Unprotect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Workbook</button>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            workbook.unprotect("password");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/(\.xlsx|\.xls|\.csv)$/i, '');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook structure unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Hinweis: Ein korrektes Passwort ist erforderlich.  
{{% /alert %}}
