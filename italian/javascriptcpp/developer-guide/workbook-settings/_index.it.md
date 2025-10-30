---
title: Gestisci le impostazioni dei file di fogli di calcolo Excel con JavaScript tramite C++
linktitle: Impostazioni del foglio di lavoro
type: docs
weight: 185
url: /it/javascript-cpp/workbook-settings/
description: Gestisci le impostazioni dei file Excel usando Aspose.Cells for JavaScript tramite C++.
---

## **Panoramica delle impostazioni del workbook**
Lavorare con i file Excel comporta varie impostazioni che possono essere manipolate programmativamente usando Aspose.Cells for JavaScript tramite C++. Questo documento descrive come gestire efficacemente queste impostazioni.

## **Possibili Scenari di Utilizzo**
Gli scenari seguenti illustrano quando potresti aver bisogno di gestire le impostazioni del workbook:
- Regolazione delle opzioni di visualizzazione
- Impostare la modalità di calcolo
- Configurare i parametri di imposta pagina

## **Gestione delle impostazioni del workbook usando Aspose.Cells for JavaScript tramite C++**
Questo esempio dimostra come gestire le impostazioni del workbook come le opzioni di calcolo e le impostazioni di visualizzazione.

1. Crea un nuovo workbook o carica uno esistente.
2. Modifica le impostazioni del workbook secondo le tue esigenze.
3. Salva il workbook per mantenere le modifiche.

### **Codice di esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook Settings Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the settings of the workbook
            const settings = workbook.settings;
            settings.calculationMode = 1; // Manual calculation

            // Display options
            settings.showGridLines = false; // Disable gridlines

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookSettingsExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Proprietà e Metodi Chiave delle Impostazioni del Workbook**
Aspose.Cells for JavaScript tramite C++ fornisce un certo numero di proprietà e metodi per regolare le impostazioni del workbook:
- **Workbook.settings**: Accede alle impostazioni del workbook.
- **Settings.calculationMode**: Imposta la modalità di calcolo del workbook.
- **Settings.showGridLines**: Abilita o disabilita le linee di griglia sulla visualizzazione.

## **Conclusioni**
Gestire le impostazioni del workbook in Aspose.Cells for JavaScript tramite C++ è semplice e offre numerose opzioni per personalizzare i comportamenti dei file Excel. Utilizzando le impostazioni disponibili, puoi adattare il workbook alle tue esigenze specifiche.
