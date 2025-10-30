---
title: Aggiornare lo Slicer con JavaScript tramite C++
linktitle: Aggiornamento Slicer
type: docs
weight: 50
url: /it/javascript-cpp/updating-slicer/
description: Questo articolo mostra come aggiornare tabelle pivot collegate aggiornando lo slicer usando Aspose.Cells for JavaScript tramite C++.
keywords: Aspose.Cells JavaScript tramite C++, Aggiorna lo slicer JavaScript, come cambiare lo slicer JavaScript, come regolare lo slicer in JavaScript, come selezionare o deselezionare gli elementi dello slicer JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**

Se vuoi aggiornare uno slicer in Microsoft Excel, seleziona o deseleziona i suoi elementi, e aggiornará di conseguenza la tabella dello slicer o la tabella pivot. Per favore usa [**Slicer.slicerCacheItems**](https://reference.aspose.com/cells/javascript-cpp/slicercache/#slicerCacheItems--) per selezionare o deselezionare gli elementi dello slicer con Aspose.Cells e poi chiama il metodo [**Slicer.refresh()**](https://reference.aspose.com/cells/javascript-cpp/slicer/#refresh--) per aggiornare la tabella dello slicer o la tabella pivot.

## **Come aggiornare il riquadro di selezione**

Il seguente codice di esempio carica il [file Excel di esempio](67338475.xlsx) che contiene un filtro esistente. Deseleziona il 2° e 3° elemento del filtro e aggiorna il filtro. Quindi salva il lavoro come [file Excel di output](67338476.xlsx). La seguente schermata mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, l'aggiornamento del filtro con gli elementi selezionati ha anche aggiornato la tabella pivot di conseguenza.

![todo:image_alt_text](updating-slicer_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Access the slicer items via slicer cache
            const items = slicer.slicerCache.slicerCacheItems;

            // Iterate items and deselect "Pink" and "Green"
            for (let i = 0; i < items.count; i++) {
                const item = items.get(i);
                if (item.value === "Pink" || item.value === "Green") {
                    item.selected = false;
                }
            }

            // Refresh slicer to apply changes
            slicer.refresh();

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
