---
title: Encrypt and Decrypt ODS Files with JavaScript via C++
linktitle: Encrypt and Decrypt ODS Files
type: docs
weight: 10
url: /javascript-cpp/encrypt-and-decrypt-ods-files/
description: Password‑protect and encrypt ODS files using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
OpenOffice.org is a full‑featured office suite that supports password‑protecting and encrypting files. However, an encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise warning messages. Encryption options are not applicable for ODS files unlike other file types.  
Aspose.Cells allows you to encrypt and decrypt ODS files. Decrypted ODS files can be opened both in Excel and OpenOffice.
{{% /alert %}}

## **Encrypt with OpenOffice Calc**
1. Select **Save As** and click the **Save with Password** box.  
2. Click the **Save** button.  
3. Type your desired password into both the **Enter Password to Open** and **Confirm Password** fields in the Set Password window that opens.  
4. Click the **OK** button to save the file.

## **Encrypt ODS file with Aspose.Cells for JavaScript via C++**
To encrypt an ODS file, load the file and set the `WorkbookSettings.password` value to the desired password before saving it. The resulting encrypted ODS file can be opened only in OpenOffice.

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

            // Password‑protect the file
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

## **Decrypt ODS file with Aspose.Cells for JavaScript via C++**
To decrypt an ODS file, load the file by providing the password via `LoadOptions.password`. Once loaded, set the `WorkbookSettings.password` property to `null`.

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

            // Remove the password from settings
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