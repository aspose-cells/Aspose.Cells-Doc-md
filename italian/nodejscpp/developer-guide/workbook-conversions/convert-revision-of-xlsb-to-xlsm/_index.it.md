---  
title: Converti la Revisione di XLSB in XLSM con Node.js via C++  
linktitle: Convertire la Revisione da XLSB a XLSM  
type: docs  
weight: 290  
url: /it/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: Impara come convertire completamente le revisioni dei file XLSB nel formato XLSM utilizzando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells supporta ora la conversione completa delle revisioni dei file XLSB in file XLSM. Le revisioni si trovano all’interno del percorso \xl\revisions. Puoi visualizzarle modificando l’estensione del tuo file XLSB in ZIP. Il percorso \xl\revisions contiene file con estensione .bin.  

Quando converti il tuo file XLSB in un file XLSM usando Aspose.Cells, questi file .bin vengono convertiti correttamente in file .xml come mostrato in queste due schermate.  

{{% /alert %}}  

Il seguente esempio di codice mostra come convertire il file XLSB nel formato XLSM usando Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

