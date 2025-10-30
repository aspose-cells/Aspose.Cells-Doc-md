---
title: Impostare il tipo di crittografia forte con JavaScript via C++
linktitle: Impostazione del tipo di crittografia forte
type: docs
weight: 60
url: /it/javascript-cpp/setting-strong-encryption-type/
description: Impara come impostare tipi di crittografia forte per i file Excel usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) ti consente di crittografare e proteggere con password i fogli di calcolo. Utilizza algoritmi forniti da un Provider di servizi crittografici. Un Provider di servizi crittografici (o CSP) è un insieme di algoritmi crittografici con diverse proprietà. Il CSP predefinito è "Office 97/2000 Compatible". Questo è un CSP con alcuni problemi di sicurezza noti al pubblico. I fogli di calcolo che sono protetti con il tipo di crittografia "debole (XOR)" o con il tipo di crittografia "compatibile con Office 97/2000" possono essere facilmente violati.

Per superare questo problema, utilizzare uno dei tipi di crittografia forte forniti da Microsoft Excel. È possibile modificare il tipo di crittografia con il CSP più forte disponibile. Per la crittografia forte, è richiesta una lunghezza chiave minima di 128 bit, ad esempio 'Microsoft Strong Cryptographic Provider'.

È anche possibile crittografare e proteggere con password file di Excel con tipo di crittografia forte utilizzando l'API Aspose.Cells.

{{% /alert %}}  
## **Applicare la crittografia con Microsoft Excel**  
Per implementare la crittografia file in Microsoft Excel (ad esempio 2007):

1. Dal menu **Strumenti**, selezionare **Opzioni**.  
1. Selezionare la scheda **Sicurezza**.  
1. Immettere un valore per il campo **Password per aprire**.  
1. Fare clic su **Avanzate**.  
1. Scegliere il tipo di crittografia e confermare la password.  

## **Applicare la crittografia con Aspose.Cells**  
Gli esempi di codice di seguito applicano una crittografia forte su un file e impostano una password.

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
