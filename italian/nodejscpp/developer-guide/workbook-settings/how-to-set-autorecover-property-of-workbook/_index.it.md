---  
title: Come impostare la proprietà AutoRecupero del Workbook con Node.js tramite C++  
linktitle: Come impostare la proprietà AutoRecupero del Workbook  
type: docs  
weight: 220  
url: /it/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: Scopri come impostare la proprietà AutoRecupero di un libro di lavoro usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Puoi usare Aspose.Cells per impostare la proprietà AutoRecupero del workbook. Il valore predefinito di questa proprietà è **true**. Quando la imposti a **false** in un workbook, Microsoft Excel disabilita AutoRecupero (Autosave) su quel file Excel.  

Aspose.Cells fornisce la proprietà [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) per abilitare o disabilitare questa opzione.  
{{% /alert %}}  

Il seguente esempio di codice spiega come usare la proprietà [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) del workbook. Il codice prima legge il valore predefinito di questa proprietà, che è **true**, poi la imposta a **false** e salva il file. Quindi rilegge il workbook e legge di nuovo il valore di questa proprietà, che sarà **false** in quel momento.  

## Codice Node.js per impostare la proprietà AutoRecupero del Workbook  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **Output**  

Ecco l'output della console del codice di esempio sopra.  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
