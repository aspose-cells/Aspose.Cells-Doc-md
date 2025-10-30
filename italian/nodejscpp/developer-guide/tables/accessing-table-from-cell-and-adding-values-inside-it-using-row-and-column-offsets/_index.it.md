---  
title: Accesso a una tabella da una cella e aggiunta di valori al suo interno usando offset di riga e colonna con Node.js tramite C++  
linktitle: Accesso alla Tabella da una Cella e Aggiunta di Valori al suo Interno utilizzando Offset di Riga e Colonna  
type: docs  
weight: 230  
url: /it/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

Normalmente, si aggiungono valori all'interno della Tabella o dell'oggetto Lista utilizzando il metodo [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-). Ma a volte potresti dover aggiungere valori all'interno della Tabella o dell'oggetto Lista utilizzando gli offset di riga e colonna.  

Per accedere a una tabella o oggetto Lista da una cella, utilizza il metodo [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--). Per aggiungere valori al suo interno usando offset di riga e colonna, utilizza il metodo [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

{{% /alert %}}  

Il seguente screenshot mostra il file Excel di origine usato nel codice. Contiene la tabella vuota e evidenzia la cella D5 che si trova all’interno della tabella. Accederemo a questa tabella dalla cella D5 usando il metodo [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--) e poi aggiungeremo i valori al suo interno usando entrambi i metodi [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) e [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

## Esempio  

### Screenshots che confrontano i file di origine e di output  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Lo screenshot seguente mostra il file Excel di output generato dal codice. Come puoi vedere, la cella D5 ha un valore e la cella F6 che si trova all'offset 2,2 della tabella ha un valore.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Codice Node.js per accedere a una tabella da una cella e aggiungere valori al suo interno usando offset di riga e colonna  

Il codice di esempio seguente carica il file Excel di origine come mostrato nello screenshot precedente e aggiunge valori all'interno della tabella e genera il file Excel di output come mostrato sopra.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
