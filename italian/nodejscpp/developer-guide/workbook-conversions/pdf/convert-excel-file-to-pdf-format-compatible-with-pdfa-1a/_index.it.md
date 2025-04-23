---  
title: Converti file Excel in formato PDF compatibile con PDF/A 1a con Node.js tramite C++  
linktitle: Converti file Excel in formato PDF compatibile con PDF/A 1a  
type: docs  
weight: 130  
url: /it/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: Impara come convertire file Excel in PDF conforme a PDF/A utilizzando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

PDF/A è una variante unica del PDF progettata per la conservazione a lungo termine dei documenti. PDF/A è una versione standardizzata ISO del Formato di Documento Portatile (PDF) che è un formato archivistico di PDF che incorpora tutti i font utilizzati nel documento all'interno del file PDF. PDF/A si differenzia dal PDF proibendo funzionalità come il collegamento dei font (a differenza dell'incorporamento dei font) e la crittografia. Aspose.Cells for Node.js via C++ ti consente di salvare i file Excel come file PDF conformi a PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, e PDF/A-3u sono supportati). Questo argomento descrive come salvare la cartella di lavoro Excel come file PDF conforme a PDF/A (PDF/A-1a).  

## **Convertire file Excel nel formato PDF compatibile con PDF/A-1a**  

Gli sviluppatori possono usare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) per impostare attributi diversi per la conversione. Impostare proprietà diverse della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) ti dà il controllo su impostazioni di stampa, font, sicurezza e compressione per il PDF di output. La proprietà più importante è [**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) che permette di salvare i file Excel come file PDF conformi a PDF/A.  

Il codice di esempio seguente spiega come convertire un file Excel in formato PDF compatibile con PDF/A-1a. Per favore, consulta il [PDF di output](outputCompliancePdfA1a.pdf) e lo screenshot come riferimento.  

## **Screenshot**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

