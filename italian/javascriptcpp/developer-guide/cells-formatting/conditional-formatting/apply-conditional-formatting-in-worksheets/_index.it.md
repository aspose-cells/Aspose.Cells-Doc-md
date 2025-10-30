---
title: Applicare la formattazione condizionale nei fogli di lavoro
linktitle: Applicare la formattazione condizionale nei fogli di lavoro
description: Come usare la libreria Aspose.Cells in JavaScript tramite C++ per applicare la formattazione condizionale nei fogli di lavoro per un migliore controllo sull aspetto delle celle.
keywords: Aspose.Cells, Formattazione condizionale, JavaScript tramite C++, Foglio di lavoro, Formattazione
type: docs
weight: 130
url: /it/javascript-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Questo articolo è progettato per fornire una comprensione dettagliata di come aggiungere la formattazione condizionale a un intervallo di celle in un foglio di lavoro.

La formattazione condizionale è una funzionalità avanzata di Microsoft Excel che consente di applicare formati a un intervallo di celle e di far sì che la formattazione cambi a seconda del valore della cella o del valore di una formula. Ad esempio, lo sfondo di una cella può essere rosso per evidenziare un valore negativo, o il colore del testo potrebbe essere verde per un valore positivo. Quando il valore della cella soddisfa la condizione di formattazione, la formattazione viene applicata. Se il valore della cella non soddisfa la condizione di formattazione, viene utilizzata la formattazione predefinita della cella.

È possibile applicare la formattazione condizionale con la Automazione di Office di Microsoft ma ciò comporta alcuni svantaggi. Sono coinvolte diverse ragioni e problemi: ad esempio, sicurezza, stabilità, scalabilità e velocità. Il motivo principale per trovare un'altra soluzione è che Microsoft stessa sconsiglia vivamente l'Automazione di Office per le soluzioni software.

Questo articolo spiega come creare un'applicazione web, aggiungere formattazione condizionale alle celle con poche righe di codice usando l'API Aspose.Cells.

{{% /alert %}}

## **Utilizzare Aspose.Cells per Applicare la Formattazione Condizionale in Base al Valore della Cella**

1. **Scarica e installa Aspose.Cells**.
   1. Scarica Aspose.Cells for JavaScript tramite C++.
1. Installalo sul tuo computer di sviluppo.
   Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. **Crea un progetto**.
   Inizia il tuo progetto JavaScript inizializzandolo. Questo esempio dimostra l'uso in un'applicazione web basata su browser.
1. **Aggiungi riferimenti**.
   Aggiungi un riferimento a Aspose.Cells nel tuo progetto, ad esempio includendo la libreria come segue:
   ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Conditional Formatting Example</title>
    </head>
    <body>
        <h1>Apply Conditional Formatting Based on Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormatConditionType, OperatorType, CellArea, Color } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add conditional formatting collection
            const cfCollection = worksheet.conditionalFormattings;
            const idx = cfCollection.add();
            const formatConditionCollection = cfCollection.get(idx);

            // Define the cell area to apply conditional formatting (A1)
            const area = CellArea.createCellArea(0, 0, 0, 0); // fromRow, fromCol, toRow, toCol
            formatConditionCollection.addArea(area);

            // Add a condition: Cell Value > 100
            const conditionIndex = formatConditionCollection.addCondition(
                FormatConditionType.CellValue,
                OperatorType.Greater,
                "100",
                null
            );

            const formatCondition = formatConditionCollection.get(conditionIndex);

            // Modify the style for the condition: bold and red font
            const style = formatCondition.style;
            if (!style.font) {
                style.font = {};
            }
            style.font.bold = true;
            style.font.color = Color.fromArgb(255, 255, 0, 0); // ARGB red

            // Assign modified style back (property assignment pattern)
            formatCondition.style = style;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'conditional_formatting_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied to cell A1 (value &gt; 100). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Quando viene eseguito il codice sopra, viene applicata una formattazione condizionale alla cella "A1" nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata ad A1 dipende dal valore della cella. Se il valore di A1 è tra 50 e 100, lo sfondo diventa rosso grazie alla formattazione condizionale applicata.

## **Utilizzare Aspose.Cells per Applicare la Formattazione Condizionale in Base a una Formula**

1. Applicare la formattazione condizionale in base alla formula (Snippet di codice)
   Di seguito è riportato il codice per completare il compito. Si applica la formattazione condizionale su B3.
