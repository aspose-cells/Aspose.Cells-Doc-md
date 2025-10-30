---  
title: Crea una linea di firma in un workbook Excel usando Aspose.Cells for Node.js via C++  
linktitle: Crea LINEA FIRMA in un workbook Excel utilizzando Aspose.Cells  
type: docs  
weight: 150  
url: /it/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: Questo articolo descrive come creare una linea di firma in un workbook Excel usando il codice Node.js con Aspose.Cells for Node.js via C++.  
keywords: Crea una linea di firma in un workbook Excel Node.js tramite C++, come creare una linea di firma in un workbook Excel, come aggiungere la linea di firma, come aggiungere la linea di firma al file Excel.  
---  

## **Introduzione**  

Microsoft Excel fornisce la funzionalità di aggiungere **Linea firma** in workbook Excel. È possibile aggiungere una linea di firma facendo clic sulla scheda **Inserisci** e quindi selezionando **Linea firma** dal gruppo **Testo**.  

## **Come Creare una Linea di Firma per Excel**  

Aspose.Cells for Node.js via C++ fornisce anche questa funzionalità e ha esposto la proprietà [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) a questo scopo. Questo articolo spiega come usare questa proprietà per aggiungere una linea di firma usando Aspose.Cells.  

Il codice di esempio seguente aggiunge una linea di firma usando la proprietà [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) e salva il workbook.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
