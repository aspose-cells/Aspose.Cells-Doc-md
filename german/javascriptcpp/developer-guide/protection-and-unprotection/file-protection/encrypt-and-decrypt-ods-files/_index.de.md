---
title: ODS Dateien mit JavaScript via C++ verschlüsseln und entschlüsseln
linktitle: ODS Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/javascript-cpp/encrypt-and-decrypt-ods-files/
description: ODS Dateien mit Aspose.Cells for JavaScript via C++ passwortgeschützt und verschlüsselt verarbeiten. 
---

{{% alert color="primary" %}}
OpenOffice.org ist eine voll ausgestattete Office-Suite, die das Passwortschutz und die Verschlüsselung von Dateien unterstützt. Eine verschlüsselte ODS-Datei kann jedoch nur geöffnet werden, nachdem das Passwort eingegeben wurde. Excel kann die verschlüsselte ODS-Datei nicht öffnen und warnt möglicherweise. Die Verschlüsselungsoptionen sind für ODS-Dateien im Gegensatz zu anderen Dateitypen nicht anwendbar. 
Aspose.Cells ermöglicht die Verschlüsselung und Entschlüsselung von ODS-Dateien. Entschlüsselte ODS-Dateien können sowohl in Excel als auch in OpenOffice geöffnet werden.
{{% /alert %}}

## **Mit OpenOffice Calc verschlüsseln**
1. Wählen Sie **Speichern unter** und aktivieren Sie das Kästchen **Mit Passwort speichern**.
1. Klicken Sie auf die **Speichern**-Schaltfläche.
1. Geben Sie Ihr gewünschtes Passwort in die Felder **Kennwort eingeben zum Öffnen** und **Kennwort bestätigen** im Fenster **Passwort festlegen** ein, das geöffnet wird. 
1. Klicken Sie auf die Schaltfläche **OK**, um die Datei zu speichern.

## **ODS-Datei mit Aspose.Cells for JavaScript via C++ verschlüsseln**
Um eine ODS-Datei zu verschlüsseln, laden Sie die Datei und setzen Sie den [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) Wert vor dem Speichern auf das tatsächliche Passwort. Die verschlüsselte ODS-Ausgabedatei kann nur in OpenOffice geöffnet werden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect ODS File</title>
    </head>
    <body>
        <h1>Protect ODS File Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Protect and Download ODS</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded ODS file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Password protect the file (converted from getSettings().setPassword -> settings.password)
            workbook.settings.password = "1234";

            // Saving the ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEncryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File protected successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```

## **Entschlüsseln Sie ODS-Datei mit Aspose.Cells for JavaScript via C++**
Um eine ODS-Datei zu entschlüsseln, laden Sie die Datei, indem Sie ein Passwort in [**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--) angeben. Sobald die Datei geladen ist, setzen Sie den [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) String auf null.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Decrypt ODS Example</title>
    </head>
    <body>
        <h1>Decrypt ODS Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open an encrypted ODS file with load options
            const loadOptions = new LoadOptions(LoadFormat.Ods);

            // Set original password
            loadOptions.password = "1234";

            // Load the encrypted ODS file with the appropriate load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Set the password to null (remove password from settings)
            workbook.settings.password = null;

            // Save the decrypted ODS file and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDecryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Decrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Decryption completed successfully! Click the download link to get the decrypted file.</p>';
        });
    </script>
</html>
```
