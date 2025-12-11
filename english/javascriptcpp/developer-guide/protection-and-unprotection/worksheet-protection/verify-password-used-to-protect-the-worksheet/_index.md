---  
title: Verify Password Used to Protect the Worksheet with JavaScript via C++  
linktitle: Verify Password Used to Protect the Worksheet  
type: docs  
weight: 370  
url: /javascript-cpp/verify-password-used-to-protect-the-worksheet/  
description: Learn how to verify the password used to protect a worksheet using Aspose.Cells for JavaScript via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells APIs have enhanced the **Protection** class by introducing useful properties and methods. One such method is **Protection.verifyPassword(string)**, which allows specifying a password as an instance of a *string* and verifies whether the same password has been used to protect the **worksheet**.  

{{% /alert %}}  

The **Protection.verifyPassword(string)** method returns **true** if the specified password matches the password used to protect the given worksheet and **false** if it does not match. The following piece of code uses the **Protection.verifyPassword(string)** method in conjunction with the **Protection.isProtectedWithPassword()** property to detect password protection and verify the password.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Worksheet Password Protection</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;
        
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook with file bytes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Check if the worksheet is password protected
            if (sheet.protection.isProtectedWithPassword()) {
                // Verify the password used to protect the worksheet
                if (sheet.protection.verifyPassword("1234")) {
                    resultDiv.innerHTML = '<p style="color: green;">Specified password matches</p>';
                } else {
                    resultDiv.innerHTML = '<p style="color: red;">Specified password does not match</p>';
                }
            } else {
                resultDiv.innerHTML = '<p style="color: blue;">Worksheet is not password protected</p>';
            }
        });
    </script>
</html>
```