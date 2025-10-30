---  
title: Formato intervalli con Node.js tramite C++  
linktitle: Formato intervalli  
type: docs  
weight: 105  
url: /it/nodejs-cpp/how-to-format-a-range/  
description: Impara come formattare un intervallo di celle in Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  
Quando hai bisogno di applicare uno stile a un intervallo, puoi utilizzare la formattazione dell'intervallo.  

## **Come formattare un intervallo in Excel**  

Per formattare un intervallo di celle in Excel, puoi utilizzare le opzioni di formattazione integrate fornite da Excel. Ecco come puoi formattare direttamente un intervallo di celle in Excel:  

1. Apri Excel e apri il foglio di lavoro che contiene l'intervallo che desideri formattare.  

2. Seleziona l'intervallo di celle che desideri formattare. Puoi fare clic e trascinare per selezionare l'intervallo, oppure puoi utilizzare scorciatoie da tastiera come Maiusc + frecce per estendere la selezione.  

3. Una volta selezionato l'intervallo, fai clic con il pulsante destro del mouse sull'intervallo selezionato e scegli "Formatta celle" dal menu contestuale. In alternativa, puoi andare alla scheda Home nella barra dei menu di Excel, fare clic sulla voce "Formato" nel gruppo "Celle" e selezionare "Formatta celle".  

4. La finestra di dialogo "Formatta celle" apparirà. Qui puoi scegliere varie opzioni di formattazione da applicare all'intervallo selezionato. Ad esempio, puoi cambiare lo stile del carattere, la dimensione del carattere, il colore del carattere, il formato numero, i bordi, il colore di sfondo, ecc. Esplora le diverse schede nella finestra di dialogo per accedere a varie opzioni di formattazione.  

5. Dopo aver apportato le modifiche di formattazione desiderate, fai clic sul pulsante "OK" per applicare la formattazione all'intervallo selezionato.  

## **Come formattare un intervallo usando Node.js**  

Per formattare un intervallo usando Aspose.Cells for Node.js via C++, puoi usare i seguenti metodi:  
1. [Range.applyStyle(stile, flag)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(stile)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(stile)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **Codice di Esempio**  
In questo esempio, creiamo un foglio di lavoro Excel, aggiungiamo alcuni dati di esempio, accediamo al primo foglio di lavoro e definiamo due intervalli("A1:C3" e "A4:C5"). Poi, creiamo nuovi stili, impostiamo varie opzioni di formattazione (ad esempio, colore del carattere, grassetto) e applichiamo lo stile all'intervallo. Infine, salviamo il foglio di lavoro in un nuovo file.  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
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

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
