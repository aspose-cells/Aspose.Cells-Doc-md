---
title: Come Bloccare le Celle per Proteggerle
type: docs
weight: 130
url: /it/javascript-cpp/how-to-lock-cells-to-protect-them/
description: Questo articolo mostra come scrivere codice per bloccare le celle per proteggerle usando lo Script Aspose.Cells for Java tramite C++.
keywords: Blocca le celle con JavaScript per proteggerle, Come bloccare celle per proteggerle usando JavaScript, Blocca celle per proteggerle in JavaScript.
---

## **Possibili Scenari di Utilizzo**
Bloccare le celle per proteggerle è una pratica comune nelle applicazioni di fogli di calcolo, come Microsoft Excel o Google Sheets, per diverse ragioni importanti:

1. Prevenire modifiche accidentali: Bloccare le celle può impedire agli utenti di modificare accidentalmente dati o formule importanti. Questo è particolarmente utile in fogli complessi dove modifiche involontarie possono causare errori significativi.

1. Mantenere l'integrità dei dati: Bloccando le celle, puoi garantire che i dati critici rimangano coerenti e accurati. Questo è fondamentale per documenti finanziari, report e qualsiasi altro documento in cui l'integrità dei dati sia essenziale.

1. Accesso controllato: In ambienti collaborativi, bloccare le celle permette di controllare chi può modificare determinate parti di un foglio di calcolo. Per esempio, potresti voler consentire solo a certi membri del team di modificare celle specifiche mentre il resto del foglio è protetto.

1. Proteggere le formule: Le formule sono spesso cruciali per i calcoli e l'analisi dei dati. Bloccare le celle che contengono formule garantisce che queste non vengano modificate o eliminate accidentalmente, il che potrebbe interrompere la funzionalità dell'intero foglio.

1. Applicare regole aziendali: In alcuni casi, regole aziendali specifiche o normative possono richiedere che determinati dati siano protetti dalle modifiche. Bloccare le celle aiuta a rispettare questi requisiti.

1. Guidare gli utenti: Bloccare le celle e fornire istruzioni chiare su quali celle possono essere modificate, puoi guidare gli utenti su come interagire con il foglio, riducendo confusione ed errori.

## **Come Bloccare le Celle per Proteggerle in Excel**
Ecco come puoi bloccare le celle in Microsoft Excel:

1. Seleziona le Celle da Bloccare: Seleziona le celle che desideri bloccare. Se vuoi bloccare l'intero foglio, puoi saltare questo passaggio.
1. Apri la finestra di dialogo formato celle: Fai clic con il tasto destro sulle celle selezionate e scegli "Formato celle," o premi Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Blocca le Celle: Nella finestra di dialogo formato celle, vai alla scheda "Protezione." Seleziona la casella "Bloccato." Clicca "OK."
1. Proteggi il foglio di lavoro: Vai alla scheda "Revision" sulla barra multifunzione. Clicca su "Proteggi foglio." Imposta una password (opzionale) e scegli le autorizzazioni che desideri consentire (ad esempio, selezionare celle bloccate, formattare celle, ecc.). Clicca "OK."
<br>
<img src="2.png" width=60% />

## **Come Bloccare Celle per Proteggerle Usando JavaScript**

Aspose.Cells è una libreria potente per lavorare con file Excel programmaticamente. Per bloccare le celle usando lo Script Aspose.Cells for Java tramite C++, devi seguire questi passaggi: caricare [file di esempio](sample.xlsx), sbloccare tutte le celle prima (dato che, di default, tutte le celle sono bloccate ma non vengono applicate fino a quando il foglio di lavoro non viene protetto), quindi bloccare le celle specifiche che desideri proteggere, e infine proteggere il foglio di lavoro per applicare il blocco.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unlock all cells first
            const unlockStyle = workbook.createStyle();
            unlockStyle.isLocked = false;

            const styleFlag = new StyleFlag();
            styleFlag.locked = true;
            sheet.cells.applyStyle(unlockStyle, styleFlag);

            // Lock specific cells (e.g., A1 and B2)
            const lockStyle = workbook.createStyle();
            lockStyle.isLocked = true;

            sheet.cells.get("A1").style = lockStyle;
            sheet.cells.get("B2").style = lockStyle;

            // Protect the worksheet to enforce the locking
            sheet.protect(ProtectionType.All);

            // Save the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet protected and cells locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Risultato dell'Output**
Questo codice garantisce che solo le celle specificate (A1 e B2 in questo esempio) siano bloccate, e il foglio sia protetto per applicare queste impostazioni. Tutte le altre celle nel foglio rimangono sbloccate e modificabili.

<br>
<img src="3.png" width=60% />
