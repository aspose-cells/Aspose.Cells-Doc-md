---  
title: Impostare la modalità di calcolo delle formule del Workbook con Node.js via C++  
linktitle: Impostazione della modalità di calcolo delle formule di Workbook  
description: Questo articolo introduce come impostare la modalità di calcolo delle formule di un workbook in Microsoft Excel con Aspose.Cells for Node.js via C++. Caricando un file Excel esistente o creando un nuovo file, è possibile utilizzare il metodo fornito da Aspose.Cells per impostare la modalità di calcolo delle formule e ottenere il risultato. Infine, si salva il file Excel modificato su disco.  
keywords: Aspose.Cells, Excel, workbook, modalità di calcolo delle formule, impostazioni, Node.js via C++  
type: docs  
weight: 110  
url: /it/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
---  

{{% alert color="primary" %}}  
Microsoft Excel consente di impostare la modalità di calcolo delle formule, cioè il modo in cui le formule vengono calcolate. Ci sono tre possibili valori:  

- Automatico - ricalcola ogni volta che qualcosa viene modificato e ogni volta che viene aperto un workbook.  
- Automatico tranne per le tabelle dati - ricalcola ogni volta che qualcosa viene modificato, ma tralasciando le tabelle dati.  
- Manuale - ricalcola solo quando l'utente lo richiede esplicitamente premendo F9 o CTRL+ALT+F9, o quando il workbook viene salvato.  
{{% /alert %}}  

Per impostare la modalità di calcolo delle formule in Microsoft Excel:  

1. Selezionare **Formule** e quindi **Opzioni di calcolo**.  
1. Seleziona una delle opzioni.  

Aspose.Cells for Node.js via C++ consente anche di impostare la **Modalità di calcolo delle formule** utilizzando la proprietà [**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--). Puoi assegnarle l'enumerazione [**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype) con uno dei seguenti valori:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
