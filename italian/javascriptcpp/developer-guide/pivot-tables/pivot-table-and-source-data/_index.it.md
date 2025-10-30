---
title: Tabella Pivot e Dati di Origine
type: docs
weight: 30
url: /it/javascript-cpp/pivot-table-and-source-data/
---

## **Dati di Origine della Tabella Pivot**

Ci sono momenti in cui si desidera creare report di Microsoft Excel con tabelle pivot che prendono dati da diverse fonti di dati (come un database) che non sono noti al momento della progettazione. Questo articolo fornisce un approccio per cambiare dinamicamente la fonte dati di una tabella pivot.

### **Cambiare i Dati di Origine di una Tabella Pivot**

1. Creazione di un nuovo modello di design.
   1. Creare un nuovo file di modello di design come nella schermata qui sotto.
   1. Definire quindi un intervallo nominato, **DataSource**, che si riferisce a questo intervallo di celle.

      **Creazione di un modello di design e definizione di un intervallo nominato, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Creazione di una Tabella Pivot basata su questo intervallo nominato.
   1. In Microsoft Excel, scegliere **Dati**, quindi **Tabella Pivot** e **Rapporto Tabella Pivot**.
   1. Creare una tabella pivot basata sull'intervallo nominato creato nel primo passaggio.

      **Creazione di una tabella pivot basata sull'intervallo nominato, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Trascinare il campo corrispondente sulla riga e sulla colonna della tabella pivot, quindi creare la tabella pivot risultante come nella schermata qui sotto.

   **Creazione di una tabella pivot basata su un campo corrispondente** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Fare clic con il tasto destro sulla tabella pivot e selezionare **Opzioni Tabella**.
   1. Seleziona **Aggiorna all'apertura** nelle impostazioni delle **Opzioni dati**.

      **Impostare le opzioni della tabella pivot** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Ora puoi salvare questo file come il file del modello del tuo designer.

1. Popolazione di nuovi dati e modifica dei dati di origine di una tabella pivot.
   1. Una volta creato il modello del designer, utilizza il codice seguente per modificare i dati di origine della tabella pivot.

Eseguendo il codice di esempio sottostante si cambia il dato di origine della tabella pivot.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Instantiating a Workbook object using uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Populating new data to the worksheet cells
            worksheet.cells.get("A9").value = "Golf";
            worksheet.cells.get("B9").value = "Qtr4";
            worksheet.cells.get("C9").value = 7000;

            // Changing named range "DataSource"
            const range = worksheet.cells.createRange(0, 0, 9, 3);
            range.name = "DataSource";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
