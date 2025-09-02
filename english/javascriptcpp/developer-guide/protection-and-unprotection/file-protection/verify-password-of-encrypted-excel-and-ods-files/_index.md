---
title: Verify Password of Encrypted Files with JavaScript via C++
linktitle: Verify Password of Encrypted Files
type: docs
weight: 10
url: /javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Verify the password of encrypted Excel (xlsx, xlsb, xls, xlsm) and Open Office (ODS) files using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
If Excel (xlsx, xlsb, xls, xlsm) and Open Office (ODS) files are locked with a password, Aspose supports simple password verification without parsing specific data of the files.  
{{% /alert %}}  

## **Verify the password of the encrypted file**  

To verify the password of the encrypted file, Aspose.Cells for JavaScript via C++ provides the [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) method. This method accepts two parameters, the file stream and the password that needs to be verified.  
The following code snippet demonstrates the use of the [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) method to verify whether the provided password is valid or not.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Verify Excel Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Verify Password</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;
        
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
            const bytes = new Uint8Array(arrayBuffer);

            const isPasswordValid = FileFormatUtil.verifyPassword(bytes, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```