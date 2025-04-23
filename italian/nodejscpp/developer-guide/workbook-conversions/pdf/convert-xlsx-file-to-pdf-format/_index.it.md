---
title: Converti file XLSX in formato PDF con Node.js tramite C++
linktitle: Converti il file XLSX nel Formato PDF
type: docs
weight: 30
url: /it/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: Questa guida spiega come convertire un file Excel (XLSX) in formato PDF usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Il formato PDF (Portable Document Format) rappresenta documenti in modo indipendente dal software, dall'hardware e dal sistema operativo utilizzati per crearli. Un file PDF può contenere una combinazione qualsiasi di testo, grafica e immagini in maniera indipendente dal dispositivo e dalla risoluzione. I file PDF sono spesso compressi, quindi occupano meno spazio rispetto al file originale.

A volte, è necessario convertire un file Microsoft Excel in PDF. Per questo, è richiesta una soluzione veloce, sicura, accurata e affidabile che consenta di distribuire documenti PDF in tutto il mondo. Esistono numerosi strumenti di conversione che possono eseguire questa operazione. Ma devi assicurarti che il layout del documento Excel originale sia conservato nel file PDF di output. Immagini, grafici, forme, formattazione dei dati, font, attributi, colori, impostazioni di pagina, orientamento del testo, bordi, grafici ecc. devono essere renderizzati in modo accurato e preciso. [Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/) assicura una conversione di alta fedeltà.

Questo documento è progettato per fornire una comprensione completa di come un documento di Microsoft Excel (contenente immagini, grafici, formattazioni, ecc.) possa essere convertito in PDF. A tal fine, mostra come creare una semplice applicazione console in Node.js che converte un file Excel in PDF utilizzando l’API di Aspose.Cells. La conversione viene eseguita con un alto grado di precisione e accuratezza.

{{% /alert %}}

## **Conversione di Excel in PDF**

Questo esempio utilizza un file Excel (SampleInput.xlsx) come modello. Il libro contiene fogli di lavoro con grafici e immagini. Ogni foglio contiene diversi tipi di formattazione utilizzando font, attributi, colori, effetti di ombreggiatura e bordi. Nel primo foglio c’è un grafico a colonne e nell’ultimo un’immagine.

### **Il file Excel di modello**

Il file modello ha tre fogli di lavoro, inclusi grafici e immagini come sezioni multimediali. Il primo foglio ha grafici e l’ultimo un’immagine come mostrato nelle schermate.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|

### **Processo di conversione**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) proprio prima di esportare in PDF. In questo modo si garantisce che i valori dipendenti dalle formule siano ricalcolati e corretti nel PDF.

{{% /alert %}}

### **Risultato**

Quando il codice sopra è stato eseguito, viene creato un file PDF nella cartella Files della directory dell'applicazione.
Gli screenshot seguenti mostrano le pagine PDF. Nota che gli header e i footer sono mantenuti anche nel file PDF di output.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|
