---
title: Sätt stark krypteringstyp med JavaScript via C++
linktitle: Ställa in stark krypteringstyp
type: docs
weight: 60
url: /sv/javascript-cpp/setting-strong-encryption-type/
description: Lär dig hur du sätter stark krypteringstyp för Excel filer med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) möjliggör kryptering och lösenordsskydd av kalkylblad. Det använder algoritmer som tillhandahålls av en kryptotjänsteleverantör. En kryptotjänsteleverantör (eller CSP) är en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är "Office 97/2000 Compatible". Detta är en CSP med vissa allmänt kända säkerhetsproblem. Kalkylblad som är säkrade med "svag kryptering (XOR)" eller med "Office 97/2000 Compatible"-krypteringstyp kan enkelt knäckas.

För att övervinna detta problem, använd en av de starka krypteringstyper som tillhandahålls av Microsoft Excel. Du kan ändra krypteringstypen till den starkaste tillgängliga CSP. För stark kryptering krävs en miniminyckellängd på 128 bitar, till exempel 'Microsoft Strong Cryptographic Provider'.

Du kan också kryptera och lösenordsskydda Excel-filer med stark krypteringstyp med hjälp av Aspose.Cells API.

{{% /alert %}}  
## **Tillämpa kryptering med Microsoft Excel**  
För att implementera filkryptering i Microsoft Excel (till exempel 2007):

1. Från menyn **Verktyg** väljer du **Alternativ**.  
1. Välj fliken **Säkerhet**.  
1. Ange ett värde för fältet **Lösenord för att öppna**.  
1. Klicka på **Avancerat**.  
1. Välj krypteringstyp och bekräfta lösenordet.  

## **Tillämpa kryptering med Aspose.Cells**  
Kodexemplen nedan tillämpar stark kryptering på en fil och anger ett lösenord.

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
