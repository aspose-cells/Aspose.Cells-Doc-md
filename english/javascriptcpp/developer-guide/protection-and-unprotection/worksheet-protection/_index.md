---
title: Protect and Unprotect Worksheet with JavaScript via C++
linktitle: Protect and Unprotect Worksheet
type: docs
weight: 40
url: /javascript-cpp/protect-and-unprotect-worksheets/
description: Protect and unprotect worksheet of Excel files with Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
To prevent other users from accidentally or deliberately changing, moving, or deleting data in a worksheet, you can lock the cells on your Excel worksheet and then protect the sheet with a password.  
{{% /alert %}}  

## **Protect and unprotect Worksheet in MS Excel**  

**![protect and unprotect Worksheet](protect-and-unprotect-worksheet.png)**  

1. Click **Review > Protect Worksheet**.  
1. Enter a password in **the Password box**.  
1. Select **allow** options.  
1. Select **OK**, re-enter the password to confirm it, and then select **OK** again.  

## **Protect Worksheet Using Aspose.Cells for JavaScript via C++**  
Only need the following simple lines of code to implement protecting workbook structure of Excel files.  

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

## **Unprotect Worksheet Using Aspose.Cells for JavaScript via C++**  
Unprotecting the worksheet is easy with Aspose.Cells API. If the worksheet is password-protected, a correct password is required.  

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

## **Advance topics**  
- [Advanced Protection Settings since Excel XP](/cells/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [Detect if Worksheet is Password Protected](/cells/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [Protecting Worksheets](/cells/javascript-cpp/protecting-worksheets/)  
- [Unprotect a Worksheet](/cells/javascript-cpp/unprotect-a-worksheet/)  
- [Verify Password Used to Protect the Worksheet](/cells/javascript-cpp/verify-password-used-to-protect-the-worksheet/)