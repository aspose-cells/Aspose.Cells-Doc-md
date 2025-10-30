---
title: Bloccare o sbloccare forme con JavaScript tramite C++
linktitle: Bloccare o sbloccare forme
type: docs
weight: 200
url: /it/javascript-cpp/lock-or-unlock-shapes/
description: Questo articolo mostra come bloccare o sbloccare le forme per proteggerle usando la libreria Aspose.Cells per JavaScript tramite C++.
keywords: JavaScript tramite C++ Bloccare forme per proteggerle, come bloccare o sbloccare forme usando JavaScript tramite C++, bloccare o sbloccare forme per proteggerle in JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**

A volte è necessario proteggere tutte le forme in determinati fogli di lavoro per evitare che vengano distrutte da situazioni indesiderate. In questo caso, è necessario bloccare tutte le forme nel foglio di lavoro specificato. 

Bloccare le forme in un foglio di calcolo o in un documento può essere vantaggioso per diversi motivi:
1. Evitare modifiche accidentali: Bloccare le forme assicura che non vengano accidentalmente spostate, ridimensionate o eliminate dagli utenti. Questo è particolarmente importante in documenti complessi dove le forme possono essere usate per annotazioni, illustrazioni o come parte del progetto del documento.
1. Mantenere layout e design: Le forme spesso giocano un ruolo cruciale nel layout e nel design visivo di un documento. Bloccarle preserva l'aspetto intenzionato, assicurando che il documento rimanga professionale e visivamente attraente.
1. Integrità dei dati: Nei fogli di calcolo, le forme possono essere usate per evidenziare punti dati importanti, aggiungere commenti o fornire spiegazioni visive. Bloccare queste forme assicura che le informazioni contestuali che forniscono rimangano accurate e integra.
1. Coerenza nei documenti condivisi: Quando si collaborano sui documenti, diversi utenti possono avere livelli di competenza differenti. Bloccare le forme aiuta a mantenere la coerenza nel documento impedendo alterazioni indesiderate.
1. Sicurezza: In documenti sensibili, bloccare le forme può essere parte di una strategia più ampia per proteggere le informazioni. Ad esempio, nei rapporti finanziari o nei documenti legali, le forme bloccate possono essere usate per salvaguardare annotazioni o evidenziazioni specifiche che forniscono un contesto critico.

A volte, hai bisogno di poter modificare alcune forme in certi fogli di lavoro protetti, in tal caso, devi sbloccare queste forme. Questo articolo introdurrà in dettaglio come bloccare e sbloccare forme specificate.

## **Come Bloccare le Forme per Proteggerle in Excel**

Ecco come puoi bloccare le celle in Microsoft Excel:

1. Apri il tuo file Excel: Apri il file Excel che contiene le forme che vuoi bloccare.

1. Seleziona la forma: fai clic sulla forma che desideri bloccare. Puoi anche selezionare più forme tenendo premuto il tasto Ctrl e facendo clic su ciascuna forma.

1. Apri il riquadro Formato Shape: clicca con il tasto destro sulla (s) forma (e) selezionata e scegli "Dimensioni e Proprietà". In alternativa, puoi andare alla scheda "Formato" sulla barra multifunzione, e nel gruppo "Dimensione", clicca sull'icona di lancio della finestra di dialogo (una piccola freccia) per aprire il riquadro "Formato Forma".
1. Blocca la forma: nel riquadro "Formato Forma", vai alla scheda "Dimensioni e Proprietà" (l'icona sembra un quadrato con frecce). Nella sezione "Proprietà", spunta la casella "Bloccato".
<br>
<img src="1.png" width=60% />
1. Proteggi il foglio di lavoro: Vai alla scheda "Revision" sulla barra multifunzione. Clicca su "Proteggi foglio." Imposta una password (opzionale) e scegli le autorizzazioni che desideri consentire (ad esempio, selezionare celle bloccate, formattare celle, ecc.). Clicca "OK."
<br>
<img src="2.png" width=60% />

## **Come bloccare tutte le forme in un foglio di lavoro specificato**

Per proteggere tutte le forme in un foglio di lavoro specificato, usa il metodo `worksheet.protect(ProtectionType.Objects)`, come mostrato nel seguente esempio di codice.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Lock Shapes Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const text = "This is a test";
            const worksheet = workbook.worksheets.get(0);

            let shape = worksheet.shapes.addTextBox(1, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addRectangle(5, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addButton(9, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addOval(13, 0, 1, 0, 50, 100);
            shape.text = text;

            // Protect all shapes in the specified worksheet
            shape.worksheet.protect(ProtectionType.Objects);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Come sbloccare forme specificate in un foglio di lavoro protetto**

Per sbloccare una forma specificata in un foglio di lavoro protetto, usa `shape.isLocked`, come mostrato nel seguente esempio di codice.

Nota: `shape.isLocked` è significativo solo quando il foglio di lavoro è protetto.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unlock Shape</title>
    </head>
    <body>
        <h1>Unlock Shape Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get protected worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the specified shape to be unlocked
            const shape = worksheet.shapes.get("TextBox 1");

            if (!shape) {
                resultDiv.innerHTML = '<p style="color: red;">Shape "TextBox 1" not found.</p>';
                return;
            }

            // Unlock the specified shape
            if (!worksheet.protection.allowEditingObject && shape.isLocked) {
                shape.isLocked = false;
            }

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'UnLocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape unlocked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
