---
title: Come formattare un numero come valuta
type: docs
weight: 10
url: /it/javascript-cpp/format-number-to-currency/
description: Questo articolo introdurrà come formattare un numero in valuta usando Aspose.Cells for JavaScript via C++ API.
keywords: formattare numero come valuta, impostazioni numero cella, formattare numero come valuta, impostazioni valuta, formato valuta.
---

## **Possibili Scenari di Utilizzo**
La formattazione dei numeri come valuta in Excel è importante per diversi motivi, in particolare quando si lavora con dati finanziari. Ecco perché la formattazione in valuta è vantaggiosa:

1. Chiarisce i valori finanziari: formattare un numero come valuta rende chiaro che il valore rappresenta denaro. Per esempio, invece di vedere 1000, che potrebbe significare qualsiasi cosa, $1.000 indica chiaramente che si tratta di un importo monetario.
1. Include simboli di valuta: quando si tratta di valute internazionali o multiple, formattare i numeri con il simbolo di valuta appropriato (ad esempio $, €, £) chiarisce il tipo di valuta utilizzata, riducendo la confusione nei rapporti finanziari multinazionali o nelle transazioni.
1. Migliora la presentazione professionale: valori in valuta ben formattati appaiono curati e professionali, il che è particolarmente importante per relazioni, presentazioni e documenti aziendali. $10.000,00 appare più credibile e organizzato rispetto a un semplice 10000.
1. Migliora la leggibilità: la formattazione in valuta aggiunge le virgole come separatori di migliaia e i decimali, rendendo più facile leggere numeri grandi. Per esempio, 1000000 diventa $1.000.000,00, più leggibile e facile da capire a colpo d'occhio.
1. Garantisce la coerenza: applicando una formattazione in valuta coerente, si assicura che tutti i valori monetari in un insieme di dati siano visualizzati nello stesso formato. Questa coerenza è importante per l'accuratezza finanziaria e per una comunicazione professionale, specialmente in fogli di calcolo grandi con molti numeri.
1. Mostra precisione: la formattazione in valuta di solito include due decimali, rendendo facile vedere importi monetari precisi. Per esempio, $100.50 è chiaramente diverso da $100.00, cosa importante nei rapporti finanziari dove la precisione conta.
1. Semplifica i calcoli finanziari: quando si eseguono calcoli finanziari (come sommare totali o media dei costi), la formattazione in valuta aiuta Excel e gli utenti a comprendere che i dati sono in termini monetari. Aiuta Excel ad applicare una formattazione appropriata nelle formule e funzioni, assicurando che i risultati rimangano coerenti.
1. Riduce interpretazioni errate: senza la formattazione in valuta, i numeri potrebbero essere fraintesi come valori numerici generali piuttosto che somme di denaro. Per esempio, 500 potrebbe essere scambiato come conteggio di articoli o unità, mentre $500.00 rappresenta chiaramente un importo finanziario.
1. Funziona con le funzioni di contabilità: la formattazione in valuta si allinea bene con le funzioni di contabilità in Excel, come bilanci o rapporti di flusso di cassa. Rende più facile usare i valori nelle dichiarazioni finanziarie dove il denaro è il focus principale.
<br>
In sintesi, la formattazione dei numeri come valuta aiuta a distinguere i valori monetari da altri tipi di numeri, aumenta la chiarezza e rende più facile interpretare i dati, specialmente in contesti finanziari.

## **Come formattare un numero come valuta in Excel**
Per formattare i numeri come valuta in Excel, segui questi passaggi:

### **Utilizzo dell'opzione Formato Valuta**
1. Seleziona le celle che desideri formattare come valuta.
1. Vai alla scheda Home sulla barra multifunzione.
1. Nel gruppo Numero, clicca sulla freccia a discesa accanto alla casella di formato numero (questo potrebbe visualizzare "Generale" di default).
<br>
<img src="1.png" width=60% />
1. Seleziona Valuta dall'elenco.

### **Utilizzo della finestra di dialogo Formato celle**
1. Seleziona le celle che desideri formattare.
1. Fai clic con il tasto destro sulle celle selezionate e scegli Format Cells per aprire la finestra di dialogo Format Cells.
1. Nella scheda Numero, seleziona Valuta dall’elenco a sinistra.
<br>
<img src="2.png" width=60% />
1. Puoi personalizzare quanto segue: Decimali, Simbolo, Numeri negativi.
1. Fai clic su OK per applicare la formattazione.

## **Come formattare un numero come valuta in Aspose.Cells**

Per formattare i numeri come valuta nella libreria Aspose.Cells for JavaScript via C++ per lavorare con file Excel, puoi applicare la formattazione in valuta alle celle in modo programmato. Ecco come farlo usando Aspose.Cells for JavaScript via C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Currency Formatting Example</h1>
        <p>Optionally select an Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value to the cell
            a1.value = 1234.56;

            // Create a style object to apply the currency format
            const a1Style = a1.style;
            // "7" is the currency format in Excel
            a1Style.number = 7;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 3456.78;

            // Create a style object to apply the currency format
            const a2Style = a2.style;
            // Custom format for dollar currency
            a2Style.custom = "$#,##0.00";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CurrencyFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CurrencyFormatted.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
