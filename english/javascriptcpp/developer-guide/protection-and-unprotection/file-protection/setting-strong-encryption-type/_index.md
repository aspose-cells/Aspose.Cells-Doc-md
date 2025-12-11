---
title: Setting Strong Encryption Type with JavaScript via C++
linktitle: Setting Strong Encryption Type
type: docs
weight: 60
url: /javascript-cpp/setting-strong-encryption-type/
description: Learn how to set strong encryption types for Excel files using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) enables you to encrypt and password‑protect spreadsheets. It uses algorithms provided by a Crypto Service Provider. A Crypto Service Provider (or CSP) is a set of cryptographic algorithms with different properties. The default CSP is **Office 97/2000 Compatible**. This is a CSP with some publicly known security issues. Spreadsheets that are secured with the **weak encryption (XOR)** or with the **Office 97/2000 Compatible** encryption type can be cracked easily.

To overcome this problem, use one of the strong encryption types provided by Microsoft Excel. You can change the encryption type to the strongest available CSP. For strong encryption, a minimum key length of 128 bits is required, for example, **Microsoft Strong Cryptographic Provider**.

You can also encrypt and password‑protect Excel files with a strong encryption type using the Aspose.Cells API.

{{% /alert %}}  

## **Applying Encryption with Microsoft Excel**  

To implement file encryption in Microsoft Excel (for example, 2007):

1. From the **Tools** menu, select **Options**.  
2. Select the **Security** tab.  
3. Enter a value for the **Password to open** field.  
4. Click **Advanced**.  
5. Choose the encryption type and confirm the password.  

## **Applying Encryption with Aspose.Cells**  

The code examples below apply strong encryption on a file and set a password.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Encrypt Workbook</title>
    </head>
    <body>
        <h1>Encrypt Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            workbook.encryptionOptions = [AsposeCells.EncryptionType.StrongCryptographicProvider, 128];
            workbook.settings.password = "1234";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```