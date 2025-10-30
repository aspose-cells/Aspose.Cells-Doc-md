---  
title: Imposta i Bordo dell Intervallo con Node.js tramite C++  
linktitle: Imposta il bordo dell intervallo  
type: docs  
weight: 600  
url: /it/nodejs-cpp/set-range-border/  
---  

## **Possibili Scenari di Utilizzo**  
Quando si desidera impostare il bordo di un intervallo, non è necessario impostare ogni cella singolarmente. Puoi impostare il bordo sull'intervallo. Aspose.Cells for Node.js via C++ offre questa funzionalità.  
Questo articolo fornisce un esempio di codice che utilizza Aspose.Cells for Node.js via C++ per impostare il bordo dell'intervallo.  

## **Imposta il bordo dell'intervallo in Excel**  
Per impostare il bordo di un intervallo in Excel, puoi seguire questi passaggi:  
1. Seleziona l'intervallo di celle a cui desideri applicare il bordo.  
2. Nella scheda "Home" del menu, individua il gruppo "Carattere".  
3. All'interno del gruppo "Carattere", fai clic sul pulsante a discesa "Bordi".  
<br>  
<img src="border.png" />  
4. Scegli il tipo di bordo che desideri applicare dalle opzioni nel menu a discesa. Puoi scegliere tra stili di bordi predefiniti o personalizzare il tuo bordo.  
5. Una volta selezionato lo stile di bordo desiderato, il bordo sarà applicato all'intervallo selezionato di celle.  

## **Imposta il bordo dell'intervallo usando Aspose.Cells for Node.js via C++**  
Questo esempio mostra come:  

1. Crea un libro di lavoro.  
2. Aggiungi dati alle celle nel primo foglio di lavoro.  
3. Crea un [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
4. Imposta il bordo interno dell'intervallo.  
5. Imposta il bordo esterno dell'intervallo.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

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
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
