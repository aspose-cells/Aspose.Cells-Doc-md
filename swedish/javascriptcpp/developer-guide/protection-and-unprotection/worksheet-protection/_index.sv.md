---
title: Skydda och avskärma arbetsblad med JavaScript via C++
linktitle: Skydda och avskydda kalkylblad
type: docs
weight: 40
url: /sv/javascript-cpp/protect-and-unprotect-worksheets/
description: Skydda och avskärma arbetsblad i Excel filer med Aspose.Cells for JavaScript via C++
---

{{% alert color="primary" %}}  
För att förhindra att andra användare avsiktligt eller oavsiktligt ändrar, flyttar eller tar bort data i ett kalkylblad kan du låsa cellerna i ditt Excel-kalkylblad och sedan skydda kalkylbladet med ett lösenord.  
{{% /alert %}}  

## **Skydda och avskydda arbetsblad i MS Excel**  

**![skydda och avskydda Arbetsblad](skydda-och-avskydda-arbetsblad.png)**  

1. Klicka på **Översikt > Skydda arbetsblad**.  
1. Ange ett lösenord i **Lösenordsrutan**.  
1. Välj **tillåt** alternativ.  
1. Välj **OK**, ange lösenordet igen för att bekräfta det, och välj sedan **OK** igen.  

## **Skydda arbetsblad med Aspose.Cells for JavaScript via C++**  
Bara behöver följande enkla koder för att implementera skydd av arbetsbokens struktur för Excel-filer.  

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

## **Avskärma arbetsblad med Aspose.Cells for JavaScript via C++**  
Att avsäkra kalkylbladet är enkelt med Aspose.Cells API. Om kalkylbladet är lösenordsskyddat krävs ett korrekt lösenord.  

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

## **Fortsatta ämnen**  
- [Avancerade skyddsinställningar sedan Excel XP](/cells/sv/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [Upptäck om arbetsbladet är lösenordsskyddat](/cells/sv/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [Skydda kalkylblad](/cells/sv/javascript-cpp/protecting-worksheets/)  
- [Avskydda ett kalkylblad](/cells/sv/javascript-cpp/unprotect-a-worksheet/)  
- [Verifiera lösenord som används för att skydda arbetsbladet](/cells/sv/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
