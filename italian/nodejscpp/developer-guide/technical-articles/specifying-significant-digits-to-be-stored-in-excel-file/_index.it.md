---  
title: Specifica cifre significative da memorizzare in un file Excel con Node.js via C++  
linktitle: Specifica delle cifre significative da memorizzare nel file Excel  
type: docs  
weight: 30  
url: /it/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: Impara come specificare le cifre significative da memorizzare in un file Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Per impostazione predefinita, Aspose.Cells for Node.js via C++ memorizza 17 cifre significative di valori double all'interno del file Excel, a differenza di MS-Excel che ne memorizza solo 15. Puoi cambiare il comportamento predefinito di Aspose.Cells da 17 a 15 cifre significative usando la proprietà [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--).  

## **Specifica delle cifre significative da memorizzare nel file Excel**  

Il seguente esempio di codice impone ad Aspose.Cells di usare 15 cifre significative durante la memorizzazione di valori double nel file Excel. Controlla il [file excel di output](22774105.xlsx). Cambia l'estensione in .zip, estrailo e vedrai che solo 15 cifre significative sono memorizzate nel file Excel. La seguente schermata spiega l'effetto della proprietà [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) sul file Excel di output.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
