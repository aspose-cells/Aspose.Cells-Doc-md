---
title: Applicare Filtro Avanzato di Microsoft Excel per Visualizzare Record che Soddisfano Criteri Complessi
type: docs
weight: 280
url: /it/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Impara come applicare il filtro avanzato di Microsoft Excel per visualizzare record che soddisfano criteri complessi usando lo script Aspose.Cells for Java tramite API C++.
keywords: Applica il filtro avanzato JavaScript tramite C++, Imposta il filtro avanzato JavaScript tramite C++, Aggiungi il filtro avanzato JavaScript tramite C++, Crea il filtro avanzato JavaScript tramite C++, Come aggiungere il filtro avanzato a un intervallo JavaScript tramite C++
---

## **Possibili Scenari di Utilizzo**  

Microsoft Excel ti permette di applicare *Filtro Avanzato* sui dati del foglio di lavoro per visualizzare record che soddisfano criteri complessi. Puoi applicare il filtro avanzato con Microsoft Excel tramite il comando *Dati > Avanzate* come mostrato in questo screenshot.  

![todo:image_alt_text](1.png)  

Lo script Aspose.Cells for Java tramite C++ ti consente anche di applicare il filtro avanzato usando il metodo [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). Proprio come in Microsoft Excel, accetta i seguenti parametri.  

**isFilter**  

Indica se filtrare l'elenco sul posto.  

**listRange**  

L'intervallo dell'elenco.  

**criteriaRange**  

L'intervallo dei criteri.  

**copyTo**  

L'intervallo in cui copiare i dati.  

**uniqueRecordOnly**  

Mostra o copia solo le righe uniche.  

## **Applicare il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi**  

Il seguente esempio di codice applica il filtro avanzato sul [File Excel di esempio](48496692.xlsx) e genera il [File Excel di output](48496691.xlsx). Lo screenshot mostra entrambi i file per confronto. Come si può vedere nello screenshot, i dati sono stati filtrati all'interno del file Excel di output secondo criteri complessi.  

![todo:image_alt_text](2.png)  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
