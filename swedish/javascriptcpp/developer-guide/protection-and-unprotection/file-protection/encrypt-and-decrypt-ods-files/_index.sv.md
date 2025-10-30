---
title: Koda och dekoda ODS filer med JavaScript via C++
linktitle: Kryptera och dekryptera ODS filer
type: docs
weight: 10
url: /sv/javascript-cpp/encrypt-and-decrypt-ods-files/
description: Skydda lösenord och kryptera ODS filer med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}
 OpenOffice.org är en komplett kontorssvit som stöder lösenordsskydd och kryptering av filer. En krypterad ODS-fil kan dock endast öppnas av OpenOffice efter att ha angett lösenordet. Excel kan inte öppna den krypterade ODS-filen och kan visa varningsmeddelanden. Krypteringsalternativen är inte tillämpliga för ODS-filer till skillnad från andra filtyper. 
Aspose.Cells låter dig kryptera och dekryptera ODS-filer. Dekrypterade ODS-filer kan öppnas både i Excel och OpenOffice.
{{% /alert %}}

## **Kryptera med OpenOffice Calc**
1. Välj **Spara som** och klicka på **Spara med lösenord** rutan.
1. Klicka på **Spara**-knappen.
1. Skriv ditt önskade lösenord i både **Ange lösenord för att öppna** och **Bekräfta lösenord**-fälten i dialogrutan Ange lösenord som öppnas. 
1. Klicka på **OK**-knappen för att spara filen.

## **Kryptera ODS-fil med Aspose.Cells for JavaScript via C++**
För att kryptera en ODS-fil, ladda filen och sätt [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--)-värdet till det faktiska lösenordet innan du sparar den. Den krypterade ODS-filen kan öppnas i OpenOffice endast.

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

## **Dekryptera ODS-fil med Aspose.Cells for JavaScript via C++**
För att dekryptera en ODS-fil, ladda filen genom att ange ett lösenord i [**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--). När filen är laddad, sätt [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--)-strängen till null.

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
