---
title: Kryptera och dekryptera Excel filer med JavaScript via C++
linktitle: Kryptera och dekryptera Excel filer
type: docs
weight: 10
url: /sv/javascript-cpp/encrypt-and-decrypt-excel-files/
description: Hur man krypterar och dekrypterar Excel filer med JavaScript via C++. Lås och lås upp Excel filer.
---

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) gör det möjligt för dig att kryptera och lösenordsskydda dina kalkylblad. Det använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning krypteringsalgoritmer med olika egenskaper. Standard-CSP är 'Kontors 97/2000-kompatibel' eller 'Svag kryptering (XOR)'. Det är viktigt att välja rätt krypteringsnyckellängd. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller också CSP:er som erbjuder starka krypteringstyper, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en uppfattning, 128 bitar kryptering är vad banker använder för att kryptera anslutningen med sina internetbankssystem.  

Aspose.Cells gör det möjligt för dig att kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.  
{{% /alert %}}  

## **Använda Microsoft Excel**  

För att ställa in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):  

1. Från menyn **Verktyg**, välj **Alternativ**. En dialogruta kommer att visas.  
2. Välj fliken **Säkerhet**.  
3. Skriv in ett lösenord och klicka på **Avancerat**  
4. Välj krypteringstyp och bekräfta lösenordet.  

## **Kryptera Excel-filer med Aspose.Cells for JavaScript via C++**  

Följande exempel visar hur man krypterar och lösenordsskyddar en Excel-fil med Aspose.Cells API.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Encrypt Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded excel file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify XOR encryption type.
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.XOR, keyLength: 40 };

            // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.StrongCryptographicProvider, keyLength: 128 };

            // Password protect the file.
            workbook.settings.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook encrypted and ready for download.</p>';
        });
    </script>
</html>
```  

### **Anger Lösenord för att ändra alternativ**  

Följande exempel visar hur man ställer in alternativet **Lösenord för att ändra** i Microsoft Excel för en befintlig fil med hjälp av Aspose.Cells API.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Password To Modify Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set the password for modification.
            workbook.settings.writeProtection.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SpecifyPasswordToModifyOption.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password-to-modify set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


## **Dekryptera Excel-fil med Aspose.Cells for JavaScript via C++**  
Det är mycket enkelt att öppna en lösenordsskyddad Excel-fil och dekryptera den med Aspose.Cells API som visas i följande kod:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Excel and Remove Password</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an encrypted Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Prepare load options with password to open encrypted file
            const loadOptions = new LoadOptions();
            loadOptions.password = "password";

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Remove password from workbook settings
            workbook.settings.password = null;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            // Use original filename with suffix to indicate password removed
            const originalName = file.name || 'output.xlsx';
            const baseName = originalName.replace(/(\.xls[xm]?|\.csv)$/i, '') || 'output';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unlocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unlocked Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password removed successfully! Click the download link to get the unlocked file.</p>';
        });
    </script>
</html>
```  


## **Fortsatta ämnen**  
- [Kryptera och dekryptera ODS-filer](/cells/sv/javascript-cpp/encrypt-and-decrypt-ods-files/)  
- [Ange stark krypterings typ](/cells/sv/javascript-cpp/setting-strong-encryption-type/)  
- [Ange författare vid skrivskydd av arbetsbok](/cells/sv/javascript-cpp/specify-author-while-write-protecting-workbook/)  
- [Verifiera lösenord för krypterade filer](/cells/sv/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/)
