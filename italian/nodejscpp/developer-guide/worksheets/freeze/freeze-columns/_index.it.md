---  
title: Blocca la prima colonna o le prime colonne del foglio di lavoro Excel con Node.js tramite C++  
linktitle: Congelare le colonne  
type: docs  
weight: 190  
url: /it/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: Impara come bloccare le colonne a sinistra dei fogli di lavoro Excel in modo programmato usando Aspose.Cells for Node.js via C++.  
keywords: Blocca le colonne a sinistra, Blocca le prime colonne, Blocca le colonne  
---  

## **Introduzione**  

In questo articolo, impareremo come bloccare le colonne a sinistra. Quando hai una grande quantità di dati in una riga, potresti non riuscire a vedere le colonne di sinistra quando scorri orizzontalmente il foglio di lavoro. Puoi bloccare e fissare le prime colonne in modo che tu possa vederle anche quando il resto dei dati viene scorrendo. Puoi facilmente vedere le intestazioni nelle colonne di sinistra.  

## **Congela le colonne In Excel**  

**![Congelare la/e colonna/e di sinistra in Excel](freeze-columns.png)**  

1. Se vuoi bloccare le colonne a sinistra, seleziona prima la colonna sotto la colonna che deve essere bloccata.
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Congela la prima colonna.
4. Se scorri verso il basso, la prima colonna rimane sempre visibile a sinistra.

**![Colonna bloccata](frozen-columns.png)**  

Come puoi vedere, la prima colonna è bloccata, e questa rimane sempre ancorata in alto durante lo scorrimento orizzontale.

Blocca le colonne, permette di visualizzare i tuoi dati lunghi senza problemi di mantenere traccia della prima colonna.

## **Blocca colonne con Aspose.Cells for Node.js via C++**  
 È semplice congelare la/e prima/e colonna/e con Aspose.Cells for Node.js via C++.  
Usa il metodo [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) per bloccare le colonne alla colonna selezionata.  
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.
2. Congela la prima colonna con il metodo Worksheet.freezePanes().
3. Salvare il file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

File Excel di esempio allegato (Freeze.xlsx).  

