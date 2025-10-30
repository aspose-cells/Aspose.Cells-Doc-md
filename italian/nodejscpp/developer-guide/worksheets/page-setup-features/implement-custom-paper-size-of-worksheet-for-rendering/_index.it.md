---  
title: Implementa una dimensione carta personalizzata del foglio di lavoro per il rendering con Node.js tramite C++  
linktitle: Implementa la dimensione della carta personalizzata del foglio di lavoro per la resa  
type: docs  
weight: 70  
url: /it/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: Questo articolo spiega come usare l API Node.js tramite C++ per impostare una dimensione carta personalizzata per i fogli desiderati durante il rendering di un file Excel in formato PDF programmaticamente.  
keywords: Imposta una dimensione carta personalizzata durante la conversione di Excel in PDF con Node.js tramite C++  
---  

## **Possibili Scenari di Utilizzo**  

Non esiste un'opzione diretta per creare dimensioni carta personalizzate in MS Excel, tuttavia, puoi impostare una dimensione carta personalizzata per i fogli desiderati durante il rendering di un file Excel in formato PDF. Questo documento spiega come impostare una dimensione carta personalizzata di un foglio di lavoro usando le API Aspose.Cells.  

## **Implementare un formato carta personalizzato del foglio di lavoro per il rendering**  

 Aspose.Cells consente di impostare la dimensione di carta desiderata del foglio di lavoro. Puoi usare il metodo [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-) della classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) per specificare una dimensione personalizzata della pagina. Il seguente esempio illustra come specificare una dimensione personalizzata della carta per il primo foglio di lavoro nel workbook. Vedi anche [output PDF](45056028.pdf) generato con questo codice come riferimento.  

## **Screenshot**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
