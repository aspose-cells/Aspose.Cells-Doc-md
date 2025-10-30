---
title: Skydda och avskärma arbetsboksstruktur med JavaScript via C++
linktitle: Skydda och avskydda arbetsbokens struktur
type: docs
weight: 40
url: /sv/javascript-cpp/protect-and-unprotect-workbook-structure/
description: Skydda och avskärma arbetsboksstruktur i Excel filer med JavaScript via C++.
---


{{% alert color="primary" %}}  
För att förhindra att andra användare ser dolda kalkylblad, lägger till, flyttar, tar bort eller gömmer kalkylbladen, och döper om kalkylbladen, kan du skydda strukturen för din Excel-arbetsbok med ett lösenord.  
{{% /alert %}}  


## **Skydda och avskydda arbetsbokens struktur i MS Excel**  

**![skydda och avskydda arbetsbokens struktur](skydda-och-avskydda-arbetsbokens-struktur.png)**  

1. Klicka på **Granska > Skydda arbetsbok**.  
1. Ange ett lösenord i **Lösenordsrutan**.  
1. Välj **OK**, ange lösenordet igen för att bekräfta det, och välj sedan **OK** igen.  


## **Skydda arbetsboksstruktur med Aspose.Cells for JavaScript via C++**  
Bara behöver följande enkla koder för att implementera skydd av arbetsbokens struktur för Excel-filer.  

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

## **Avskärma arbetsboksstruktur med Aspose.Cells for JavaScript via C++**  
Det är enkelt att avskydda arbetsbokens struktur med Aspose.Cells API.  

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
Observera: Ett korrekt lösenord krävs.  
{{% /alert %}}
