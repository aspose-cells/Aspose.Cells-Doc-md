---  
title: Disabilita il Controllo di Compatibilità in Excel con Node.js tramite C++  
linktitle: Disabilitare il verificatore di compatibilità in Excel  
type: docs  
weight: 170  
url: /it/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: Scopri come disabilitare il controllo di compatibilità tramite le API Aspose.Cells for Node.js via C++.  
keywords: Node.js Disabilita il Controllo di Compatibilità, Disabilita il Controllo di Compatibilità in Excel tramite Node.js con C++, Disabilita il Controllo di Compatibilità nel Workbook.  
---  

## Disabilitare il Controllo di Compatibilità nei fogli di lavoro di Excel in Node.js  

{{% alert color="primary" %}}  
Il controllo di compatibilità di Microsoft Excel segnala quando il salvataggio di un file in un formato precedente potrebbe causare problemi di funzionalità o perdita di fedeltà. Il Controllo di compatibilità è una funzionalità di Microsoft Office Excel 2007 e Microsoft Excel 2010.  

Quando si salva una cartella di lavoro in una versione precedente, da Excel 2007 o Excel 2010 a Excel 97 attraverso Excel 2003, il Verificatore di Compatibilità analizza la cartella di lavoro per vedere se contiene funzionalità non supportate dalla versione precedente. Per aiutarti a prendere decisioni su come gestire problemi di compatibilità, il Verificatore di Compatibilità visualizza finestre di dialogo con opzioni. Può anche essere utilizzato per creare un rapporto su eventuali problemi nella cartella di lavoro, o disabilitare la funzione.  

A volte, è necessario disabilitare il controllo di compatibilità per un determinato foglio di calcolo. Con le API di Aspose.Cells, puoi farlo programmaticamente in modo che gli utenti non si frustrino o si confondano con la finestra di dialogo del Controllo di Compatibilità che appare quando risalvano manualmente il file in Microsoft Excel.  
{{% /alert %}}  

## **Come disabilitare il Controllo di compatibilità utilizzando Microsoft Excel**  

Per disabilitare il Verificatore di compatibilità in Microsoft Excel (ad esempio Microsoft Excel 2007/2010):  

- (Excel 2007) Fare clic sul pulsante Office, quindi su **Prepara**, poi su **Esegui controllo compatibilità**, e infine deselezionare l'opzione **Esegui controllo compatibilità al salvataggio di questo foglio di lavoro**.  
- (Excel 2010) Nella scheda File, fare clic su **Informazioni**, quindi su **Verifica problemi**, fare clic su **Verifica compatibilità** e, infine, deselezionare l'opzione **Verifica compatibilità quando si salva questa cartella di lavoro**.  

## **Come disabilitare il Controllo di compatibilità utilizzando le API di Aspose.Cells**  

Imposta la proprietà [**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--) a **false** per disabilitare il Controllo di Compatibilità di Microsoft Excel.  

### **Esempi di codice**  

Gli esempi di codice successivi mostrano come disabilitare il Controllo di Compatibilità con Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

