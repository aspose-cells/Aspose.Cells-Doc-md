---  
title: Esporta le formattazioni condizionali DataBar, ColorScale e IconSet durante la conversione di Excel in HTML con Node.js tramite C++  
linktitle: Esportazione di formattazioni condizionali DataBar, ColorScale e IconSet durante la conversione da Excel in HTML  
type: docs  
weight: 30  
url: /it/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

Puoi esportare le formattazioni condizionali DataBar, ColorScale e IconSet durante la conversione del tuo file Excel in HTML. Questa funzione è parzialmente supportata da Microsoft Excel, ma Aspose.Cells for Node.js via C++ la supporta completamente.

{{% /alert %}}  

## **Esportazione di formattazioni condizionali DataBar, ColorScale e IconSet durante la conversione da Excel in HTML**  
La seguente schermata mostra il [file di esempio Excel](5115558.xlsx) con formattazione condizionale DataBar, ColorScale e IconSet. Puoi scaricare il [file di esempio Excel](5115558.xlsx) dal link fornito.  

![todo:image_alt_text](conversion_1.png)  

La seguente schermata mostra il file HTML di output di Aspose.Cells che mostra la formattazione condizionale DataBar, ColorScale e IconSet. Come puoi vedere, appare esattamente come il [file di esempio di Excel](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Codice di Esempio**  
Il codice di esempio seguente converte il file Excel di esempio in HTML, che rappresenta semplicemente una conversione normale [Excel in HTML](/cells/it/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  


