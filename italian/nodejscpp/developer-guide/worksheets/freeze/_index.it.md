---  
title: Blocca i riquadri del Foglio di Excel con Node.js tramite C++  
linktitle: Blocca riquadri  
type: docs  
weight: 190  
url: /it/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: In questo articolo, imparerai come bloccare i riquadri dei Fogli di Excel programmaticamente usando Aspose.Cells for Node.js via C++.  
keywords: Blocca pannelli, Blocca finestra.  
---  

## **Introduzione**  

In questo articolo, impareremo Come Bloccare i Pannelli. Quando hai una grande quantità di dati sotto un'intestazione comune, non riesci a vedere l'intestazione quando scorri verso il basso il foglio. E ogni record contiene molti dati. Puoi bloccare i pannelli in modo da poter vedere quella parte bloccata anche quando il resto dei dati viene scrollato. Puoi facilmente vedere gli intestazioni nelle righe superiori o nelle prime colonne. Bloccare e sbloccare i pannelli cambia solo la visualizzazione dei dati senza modificare i dati stessi.  

## **In Excel**  

**![Blocca riquadri in Excel](Freeze-panes.png)**  

1. Se vuoi bloccare i pannelli, blocca righe e colonne, allora prima seleziona una cella (come B2).  
2. Fare clic su Visualizza > Blocca riquadri.  
3. Nel menu a discesa, fare clic su Blocca riquadri.  
4. Se scorri verso il basso o a destra, la prima riga e colonna sono bloccate.  

**![Pannelli bloccati](Frozen-Panes.png)**  

Come puoi vedere, la prima riga e la colonna A sono bloccate, la seconda riga è la 32 e la seconda colonna visibile è D.  

Bloccare i riquadri consente di visualizzare grandi quantità di dati senza dover tenere traccia di etichette di Righe o Colonne.  

## **Blocca i riquadri con Aspose.Cells for Node.js via C++**  
È semplice bloccare i riquadri con Aspose.Cells for Node.js via C++. Si prega di usare il metodo [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) per bloccare i riquadri alla cella selezionata.  
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.  
2. Blocca i riquadri con il metodo Worksheet.freezePanes()  
3. Salvare il file.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

File Excel di esempio allegato (Freeze.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
