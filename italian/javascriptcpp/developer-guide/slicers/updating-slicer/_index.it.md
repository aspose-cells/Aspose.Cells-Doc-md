---
title: Aggiornamento dello slicer con JavaScript tramite C++
linktitle: Aggiornamento dello slicer
type: docs
weight: 50
url: /it/javascript-cpp/updating-slicer/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Questo articolo mostra come aggiornare uno slicer per filtrare i dati della Tabella Pivot o della tabella collegata utilizzando Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells JavaScript via C++, Aggiorna slicer JavaScript, come cambiare lo slicer in JavaScript, come filtrare una Tabella Pivot tramite slicer in JavaScript, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
---

## **Possibili Scenari di Utilizzo**
Aggiornare uno slicer significa filtrare i dati della Tabella Pivot o della tabella a cui lo slicer è collegato. Quando si selezionano o si deselezionano gli elementi dello slicer in Microsoft Excel, la Tabella Pivot o la tabella collegata viene ricalcolata di conseguenza. Con Aspose.Cells for JavaScript via C++, non è necessario iterare gli elementi della cache dello slicer e aggiornare manualmente lo slicer — il metodo [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/javascript-cpp/slicer/) aggiorna lo slicer e ricalcola la Tabella Pivot o la tabella collegata direttamente dagli elementi del filtro:
- `Slicer.selectItems(labels, append)` — seleziona le etichette specificate e ricalcola la Tabella Pivot o la tabella collegata. Quando `append` è `true`, le etichette originariamente selezionate vengono mantenute e le etichette specificate vengono aggiunte alla selezione; quando `append` è `false`, tutte le selezioni originali vengono cancellate e solo le etichette specificate restano selezionate.
- `Slicer.unselectItems(labels)` — deseleziona parte degli elementi attualmente selezionati.
- `Slicer.clearFilter()` — rimuove il filtro e seleziona tutti gli elementi.

{{% alert color="primary" %}}
A partire da Aspose.Cells for JavaScript via C++ 26.10, la proprietà `SlicerCacheItem.selected` diventa di sola lettura e il relativo setter non è più supportato. Utilizzare i metodi `Slicer.selectItems`, `Slicer.unselectItems` e `Slicer.clearFilter` anziché impostare `SlicerCacheItem.selected` elemento per elemento.
{{% /alert %}}

## **Come aggiornare lo slicer**
Il seguente codice di esempio carica il [file Excel di esempio](67338475.xlsx) che contiene uno slicer esistente collegato a una Tabella Pivot. Seleziona solo gli elementi "Blue" e "Pink" dello slicer con `Slicer.selectItems(labels, false)` — la Tabella Pivot viene ricalcolata direttamente dagli elementi del filtro, senza una chiamata manuale a `Slicer.refresh()`. Salva quindi la cartella di lavoro come [file Excel di output](67338476.xlsx). La schermata seguente mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, la Tabella Pivot mostra solo gli elementi filtrati.
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

            // Select only "Blue" and "Pink"; the linked pivot table or table
            // is recalculated directly from the filter items
            slicer.selectItems(["Blue", "Pink"], false);

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

Mantenere le etichette attualmente selezionate e selezionare ulteriori elementi:

```javascript
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Deselezionare parte degli elementi selezionati:

```javascript
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Rimuovere il filtro (selezionare tutti gli elementi):

```javascript
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="javascript-cpp" >}}