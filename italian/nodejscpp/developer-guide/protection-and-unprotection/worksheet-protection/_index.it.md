---  
title: Proteggi e Rimuovi la protezione dal Foglio di Lavoro con Node.js tramite C++  
linktitle: Proteggere e Difendere il Foglio di Lavoro  
type: docs  
weight: 40  
url: /it/nodejs-cpp/protect-and-unprotect-worksheets/  
description: Proteggi e rimuovi la protezione dal foglio di lavoro di file Excel con Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Per impedire ad altri utenti di modificare, spostare o eliminare accidentalmente o deliberatamente i dati in un foglio di lavoro, è possibile bloccare le celle nel foglio di lavoro di Excel e quindi proteggere il foglio con una password.  
{{% /alert %}}  

## **Proteggere e proteggere il foglio di lavoro in MS Excel**  

**![proteggere e proteggere il foglio di lavoro](protect-and-unprotect-worksheet.png)**  

1. Fare clic su **Revisione > Proteggi foglio di lavoro**.  
1. Inserire una password nella **casella di Password**.  
1. Selezionare le opzioni **consenti**.  
1. Selezionare **OK**, reinserire la password per confermarla e quindi selezionare di nuovo **OK**.  

## ** Proteggi il Foglio di Lavoro usando Aspose.Cells for Node.js via C++**  
È sufficiente utilizzare le seguenti linee di codice per implementare la protezione della struttura della cartella di lavoro dei file di Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **Rimuovi la protezione dal Foglio di Lavoro usando Aspose.Cells for Node.js via C++**  
Rimuovere la protezione dal foglio di lavoro è facile con l'API Aspose.Cells. Se il foglio di lavoro è protetto da password, è richiesta la password corretta.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **Argomenti avanzati**  
- [Impostazioni di protezione avanzate da Excel XP in poi](/cells/it/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [Verificare se il foglio di lavoro è protetto da password](/cells/it/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [Protezione dei fogli di lavoro](/cells/it/nodejs-cpp/protecting-worksheets/)  
- [Sblocca un foglio di lavoro](/cells/it/nodejs-cpp/unprotect-a-worksheet/)  
- [Verificare la password utilizzata per proteggere il foglio di lavoro](/cells/it/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
