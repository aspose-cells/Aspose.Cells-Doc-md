---
title: Impostazioni bordo
linktitle: Impostazioni bordo
description: Come usare la libreria Aspose.Cells in JavaScript in C++ per impostare lo stile e il colore dei bordi delle celle. Regolando larghezza, stile e colore del bordo, hai un controllo maggiore sull’aspetto delle celle.
keywords: Aspose.Cells, Impostazioni del bordo della cella, JavaScript tramite C++, Larghezza bordo, Stile bordo, Colore bordo
type: docs
weight: 40
url: /it/javascript-cpp/cells-border-settings/
---

## **Aggiungere Bordi alle Celle**

Microsoft Excel permette agli utenti di formattare le celle aggiungendo i bordi. Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore viene aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile di linea e il colore dei bordi.

Con Script via C++, Aspose.Cells for Java, gli sviluppatori possono aggiungere bordi e personalizzare il loro aspetto nello stesso modo flessibile di Microsoft Excel.

### **Aggiungere Bordi alle Celle**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che consente di accedere a ogni foglio di calcolo nel file Excel. Un foglio di calcolo viene rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fornisce la collezione [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Ogni elemento nella collezione [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

Aspose.Cells fornisce la proprietà [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) nella classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). La proprietà [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) viene utilizzata per impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) fornisce proprietà per aggiungere bordi alle celle.

#### **Aggiunta di bordi a una cella**

Gli sviluppatori possono aggiungere bordi a una cella utilizzando la raccolta [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) dell'oggetto [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--). Il tipo di bordo viene passato come indice alla raccolta [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--). Tutti i tipi di bordo sono predefiniti nell'enumerazione [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).

**Enumerazione Border**

|**Tipi di bordi**|**Descrizione**|
| :- | :- |
|BottomBorder|Una linea di bordo inferiore|
|DiagonalDown|Una linea diagonale dall'angolo in alto a sinistra all'angolo in basso a destra|
|DiagonalUp|Una linea diagonale dall'angolo in basso a sinistra all'angolo in alto a destra|
|LeftBorder|Una linea di bordo sinistro|
|RightBorder|Una linea di bordo destro|
|TopBorder|Una linea di bordo superiore|

La raccolta [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) memorizza tutti i bordi. Ogni bordo nella raccolta [**borders**](https://reference.aspose.com/cells/javascript-cpp/style/#borders--) è rappresentato da un oggetto [**Border**](https://reference.aspose.com/cells/javascript-cpp/border) che fornisce due proprietà, [**color**](https://reference.aspose.com/cells/javascript-cpp/border/#color-color-) e [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-), per impostare rispettivamente colore e stile della linea del bordo.

Per impostare il colore della linea di un bordo, seleziona un colore usando l'enumerazione Color (parte di JavaScript) e assegna il valore alla proprietà color dell'oggetto Border.

Lo stile della linea del bordo viene impostato selezionando uno stile di linea dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).

**Enumerazione CellBorderType**

|**Stili di linea**|**Descrizione**|
| :- | :- |
|DashDot|Linea tratteggiata sottile a punti|
|DashDotDot|Linea sottile a punti e trattini|
|Dashed|Linea tratteggiata|
|Dotted|Linea a punti|
|Double|Linea doppia|
|Hair|Linea sottilissima|
|MediumDashDot|Linea media tratteggiata a punti|
|MediumDashDotDot|Linea media a punti e trattini|
|MediumDashed|Linea tratteggiata media|
|None|Nessuna linea|
|Medium|Linea media|
|SlantedDashDot|Linea tratteggiata sottile a punti inclinata|
|Thick|Linea spessa|
|Thin|Linea sottile|
Seleziona uno degli stili di linea e assegnalo alla proprietà [**lineStyle**](https://reference.aspose.com/cells/javascript-cpp/border/#lineStyle-cellbordertype-) dell'oggetto [**Border**](https://reference.aspose.com/cells/javascript-cpp/border).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Borders to A1 Cell Example</h1>
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
            // This example creates a new workbook and adds borders to cell A1.
            // No try/catch is used so errors propagate for testing.

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Create a style object
            const style = cell.style;

            // Setting the line style and color of the top border
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the bottom border
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the left border
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;

            // Setting the line style and color of the right border
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thick;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;

            // Apply the border styles to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Dovresti impostare sia lo stile di linea che il colore contemporaneamente. Le due linee diagonali del bordo dovrebbero avere lo stesso stile e colore.
{{% /alert %}}

#### **Aggiunta di bordi a un intervallo di celle**

È anche possibile aggiungere bordi a un intervallo di celle piuttosto che a una singola cella. Per farlo, prima crea un intervallo di celle chiamando il metodo [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) della raccolta [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Accetta i seguenti parametri:

- Prima riga, la prima riga dell'intervallo.
- Prima colonna, rappresenta la prima colonna dell'intervallo.
- Numero di righe, il numero di righe nell'intervallo.
- Numero di colonne, il numero di colonne nell'intervallo.

Il metodo [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) restituisce un oggetto [**Range**](https://reference.aspose.com/cells/javascript-cpp/range), che contiene l'intervallo di celle specificato. L'oggetto [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) fornisce un metodo [**outlineBorder**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-) che prende i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- **Tipo di Bordi**, il tipo di bordo, selezionato dall'enumerazione [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype).
- **Stile di Linea**, lo stile della linea del bordo, selezionato dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype).
- **Colore**, il colore della linea, selezionato dall'enumerazione Colore.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Apply Borders</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, writes to A1, creates a range and applies borders, then offers the file for download.
            const workbook = new Workbook();

            const worksheet = workbook.worksheets.get(0);

            const cell = worksheet.cells.get("A1");

            cell.putValue("Hello World From Aspose");

            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Applying borders using property assignment conversions for setter methods
            range.outlineBorder = [BorderType.TopBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.BottomBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.LeftBorder, CellBorderType.Thick, Color.Blue];
            range.outlineBorder = [BorderType.RightBorder, CellBorderType.Thick, Color.Blue];

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and borders applied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
