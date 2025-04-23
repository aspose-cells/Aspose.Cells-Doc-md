---  
title: Aggiorna i valori delle forme collegate con Node.js tramite C++  
linktitle: Aggiorna i valori delle forme collegate  
type: docs  
weight: 3200  
url: /it/nodejs-cpp/refresh-values-of-linked-shapes/  
description: Impara come aggiornare i valori delle forme collegate in Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

A volte, nel tuo file Excel, hai una forma collegata a una cella. In Microsoft Excel, modificare il valore della cella collegata modifica anche il valore della forma collegata. Questo funziona anche con Aspose.Cells for Node.js via C++ se vuoi salvare il documento in formato XLS o XLSX. Tuttavia, se desideri salvarlo in formato PDF o HTML, dovrai chiamare il metodo [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) per aggiornare il valore della forma collegata.  

{{% /alert %}}  

## Esempio  

Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice di esempio qui sotto. Ha un'immagine collegata collegata alle celle A1 a E4. Modificheremo il valore della cella B4 con Aspose.Cells e poi chiameremo il metodo [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) per aggiornare il valore dell'immagine e salvarlo in formato PDF.  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

Puoi scaricare il [file Excel di origine](95584291.xlsx) e il [PDF di output](95584292.pdf) dai link forniti.  

### Codice Node.js per aggiornare i valori delle forme collegate  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
