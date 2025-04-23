---  
title: Espandere il testo da destra a sinistra durante l esportazione di un file Excel in HTML con Node.js tramite C++  
linktitle: Espansione del testo da destra a sinistra durante l esportazione di un file Excel in HTML  
type: docs  
weight: 60  
url: /it/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
---  

{{% alert color="primary" %}}  

Aspose.Cells ora supporta l'espansione del testo da destra a sinistra durante l'esportazione di un file Excel in HTML. Questa funzionalità è stata implementata dalla versione 8.9.0.0. Ora, se il tuo file Excel di origine contiene del testo che si espande da destra a sinistra, allora Aspose.Cells lo esporterà correttamente in HTML.  

{{% /alert %}}  
## **Espansione del testo da destra a sinistra durante l'esportazione di un file Excel in HTML**  
Il codice di esempio seguente converte il [file di esempio Excel](5115502.xlsx) in HTML. Questa schermata mostra come appare il file Excel di esempio in Microsoft Excel 2013.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

Questa schermata mostra l'[output HTML generato con la versione precedente](5115509).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

Questa schermata mostra l'[output HTML generato con la versione più recente](5115508).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

Come puoi vedere negli screenshot, la nuova versione espande correttamente il testo allineato a destra a sinistra, proprio come Microsoft Excel.  


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load source excel file inside the workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save workbook in html format
wb.save(path.join(dataDir, `ExpandTextFromRightToLeft_out_${AsposeCells.CellsHelper.getVersion()}.html`), AsposeCells.SaveFormat.Html);
```  

