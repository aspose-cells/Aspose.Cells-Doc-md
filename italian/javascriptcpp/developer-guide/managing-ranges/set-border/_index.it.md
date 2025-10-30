---
title: Imposta il bordo dell intervallo con JavaScript tramite C++
linktitle: Imposta il bordo dell intervallo
type: docs
weight: 600
url: /it/javascript-cpp/set-range-border/
---

## **Possibili Scenari di Utilizzo**  
Quando si desidera impostare il bordo di un intervallo, non è necessario impostare ogni cella singolarmente. È possibile impostare il bordo sull'intervallo. Aspose.Cells for JavaScript tramite C++ offre questa funzione.  
Questo articolo fornisce un esempio di codice che utilizza Aspose.Cells for JavaScript tramite C++ per impostare il bordo dell'intervallo.  

## **Imposta il bordo dell'intervallo in Excel**  
Per impostare il bordo di un intervallo in Excel, puoi seguire questi passaggi:  
1. Seleziona l'intervallo di celle a cui desideri applicare il bordo.  
2. Nella scheda "Home" del menu, individua il gruppo "Carattere".  
3. All'interno del gruppo "Carattere", fai clic sul pulsante a discesa "Bordi".  
<br>  
<img src="border.png" />  
4. Scegli il tipo di bordo che desideri applicare dalle opzioni nel menu a discesa. Puoi scegliere tra stili di bordi predefiniti o personalizzare il tuo bordo.  
5. Una volta selezionato lo stile di bordo desiderato, il bordo sarà applicato all'intervallo selezionato di celle.  

## **Imposta il bordo dell'intervallo usando Aspose.Cells for JavaScript tramite C++**  
Questo esempio mostra come:  

1. Crea un libro di lavoro.  
2. Aggiungi dati alle celle nel primo foglio di lavoro.  
3. Crea un [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).  
4. Imposta il bordo interno dell'intervallo.  
5. Imposta il bordo esterno dell'intervallo.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Instantiate a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Create a range (A1:C5).
            const range = cells.createRange("A1", "C5");

            // set inner border of range
            const innerColor = workbook.createCellsColor();
            innerColor.color = AsposeCells.Color.Red;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Vertical,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };
            innerColor.color = AsposeCells.Color.Green;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Horizontal,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };

            // set outer border of range
            const outerColor = workbook.createCellsColor();
            outerColor.color = AsposeCells.Color.Blue;
            range.outlineBorders = {
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: outerColor
            };

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
