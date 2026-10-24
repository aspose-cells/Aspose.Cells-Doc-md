---
title: Proteggi e Sblocca con Node.js tramite C++
linktitle: Crittografia e protezione
type: docs
weight: 68
url: /it/nodejs-cpp/protect-and-unprotect/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/nodejs-cpp/security-features/]
description: Questa sezione spiega come crittografare e decrittografare i file Excel e proteggere i dati Excel, trattando crittografia dei file, protezione in sola lettura, protezione della struttura della cartella di lavoro, protezione dei fogli di lavoro e firme digitali utilizzando codice JavaScript
keywords: Aspose.Cells, Node.js, C++, crittografare, decrittografare, password, proteggere, rimuovere la protezione, protezione cartella di lavoro, protezione foglio di lavoro, sola lettura, firma digitale, JavaScript
---

Le cartelle di lavoro di Excel spesso contengono informazioni sensibili di natura finanziaria, aziendale o personale che devono essere protette dagli accessi non autorizzati. Aspose.Cells for Node.js via C++ fornisce un insieme completo di funzionalità di protezione che rispecchia le capacità di Microsoft Excel, consentendo di proteggere i dati a livello di file, di cartella di lavoro e di foglio di lavoro.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ offre un'ampia gamma di funzionalità di protezione, dal livello di file al livello di dati, in modo simile a MS Excel. Queste funzionalità includono la crittografia dei file con una password, l'applicazione dell'accesso in sola lettura tramite una password per modificare, la protezione della struttura della cartella di lavoro, la protezione dei fogli di lavoro e la firma digitale delle cartelle di lavoro.
{{% /alert %}}

## Crittografare e decrittografare i file Excel
Una password impostata su un file Excel impedisce agli utenti non autorizzati di aprire o visualizzare il contenuto della cartella di lavoro. Per crittografare una cartella di lavoro, assegnare una stringa di password a `workbook.getSettings().setPassword()` e quindi salvare la cartella di lavoro. Aspose.Cells scrive il file in forma crittografata. Per aprire una cartella di lavoro crittografata a scopo di decrittografia, creare un'istanza di un oggetto `LoadOptions`, impostare `loadOptions.setPassword()` sulla stessa password utilizzata durante la crittografia e passarlo al costruttore `Workbook`. Aspose.Cells applica la password fornita in modo trasparente, così che il resto del codice possa interagire con il contenuto decrittografato come se il file fosse una normale cartella di lavoro.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Protezione in sola lettura (password per modificare)
Excel supporta due distinti livelli di password. Il primo è la password di apertura, che crittografa il file stesso ed è trattato nella sezione precedente. Il secondo è la password per modificare, che non impedisce agli utenti di aprire la cartella di lavoro; al contrario, Excel consiglia di aprire il file in modalità di sola lettura a meno che non venga fornita la password di modifica. Configurare questo comportamento in Aspose.Cells tramite `workbook.getSettings().getWriteProtection()`. Impostare la proprietà `password` sulla password di modifica e la proprietà `author` per identificare chi ha applicato la protezione. Utilizzare il metodo `writeProtection.validatePassword(string)` per verificare se la password di modifica fornita è corretta, restituendo `true` in caso di corrispondenza e `false` altrimenti.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Configura la protezione da scrittura: imposta la password di modifica e l'autore
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Salva la cartella di lavoro in modo che la protezione da scrittura venga mantenuta
workbook.save("WriteProtectedWorkbook.xlsx");
// Verifica la password di modifica utilizzando la password corretta
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Verifica la password di modifica utilizzando una password errata per dimostrare l'altro ramo
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Proteggere e rimuovere la protezione della struttura della cartella di lavoro
La protezione della struttura della cartella di lavoro impedisce ad altri utenti di visualizzare fogli di lavoro nascosti, aggiungere nuovi fogli di lavoro, spostare fogli di lavoro, eliminare fogli di lavoro, nascondere fogli di lavoro o rinominare i fogli di lavoro. Lo stato protetto si applica alla struttura del foglio anziché al contenuto delle celle all'interno di qualsiasi foglio. Per applicare la protezione della struttura, chiamare `workbook.protect(ProtectionType.Structure, "password")`. Per rimuovere la protezione, chiamare `workbook.unprotect("password")` fornendo la password corretta. Il valore enum `ProtectionType.Structure` viene utilizzato qui ed è distinto da altri tipi di protezione come `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Aggiungi un secondo foglio di lavoro
workbook.getWorksheets().add();
// Scrivi un valore di esempio nella cella A1 del primo foglio di lavoro
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Proteggi la struttura della cartella di lavoro
workbook.protect(AsposeCells.ProtectionType.Structure, "StructPwd");
// Salva la cartella di lavoro come structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Ricarica il file in una nuova istanza di Workbook
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Rimuovi la protezione della struttura
loadedWorkbook.unprotect("StructPwd");
// Stampa il messaggio di conferma
console.log("Structure protection has been successfully removed from the workbook.");
```

## Proteggere e rimuovere la protezione dei fogli di lavoro
La protezione del foglio di lavoro blocca le celle di un foglio di lavoro contro modifiche accidentali o intenzionali. Gli utenti non possono modificare le celle bloccate senza fornire la password. Questa è la tipica protezione utilizzata per tutelare formule, intestazioni o aree designate per l'immissione dei dati nei fogli di calcolo condivisi. Per proteggere un foglio di lavoro, chiamare `worksheet.protect(ProtectionType.All, "password")`. L'utilizzo di `ProtectionType.All` abilita ogni opzione di protezione disponibile, come la selezione delle celle bloccate, la formattazione delle celle, l'inserimento di righe e colonne e l'eliminazione di righe e colonne. Per rimuovere la protezione, chiamare `worksheet.unprotect("password")` con la password corretta. È disponibile un controllo più granulare combinando altri tipi di protezione come `Contents`, `Objects` e `Scenarios` tramite l'OR bit per bit.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.All, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Aggiungere e convalidare le firme digitali
Una firma digitale garantisce ai destinatari che il contenuto della cartella di lavoro è autentico e non è stato alterato da quando è stato firmato. Aspose.Cells fornisce il supporto per le firme digitali attraverso il namespace `Aspose.Cells.DigitalSignatures`. Il flusso di lavoro tipico prevede il caricamento di un file di certificato `.pfx` utilizzando le utility crypto di Node.js, il suo incapsulamento in un `Aspose.Cells.DigitalSignatures.DigitalSignature`, l'aggiunta della firma a un `DigitalSignatureCollection` e l'applicazione della raccolta alla cartella di lavoro tramite `workbook.addDigitalSignature(digitalSignatureCollection)`. La proprietà `digitalSignature.comments` consente di registrare il contesto della firma, come l'ora e lo scopo della firma. Qualsiasi modifica apportata alla cartella di lavoro dopo la firma invalida la firma stessa, pertanto una fase di convalida sul lato ricevente può rilevare eventuali manomissioni.

```javascript
const AsposeCells = require("aspose.cells.node");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

## Related Articles
- [Crittografare e decrittografare i file Excel](/cells/it/nodejs-cpp/encrypt-and-decrypt-excel-files/)
- [Proteggere e rimuovere la protezione della struttura della cartella di lavoro](/cells/it/nodejs-cpp/protect-and-unprotect-workbook-structure/)
- [Proteggere e rimuovere la protezione del foglio di lavoro](/cells/it/nodejs-cpp/protect-and-unprotect-worksheets/)
- [Proteggere con password o rimuovere la protezione della cartella di lavoro condivisa](/cells/it/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Assegnare e convalidare le firme digitali](/cells/it/nodejs-cpp/assign-and-validate-digital-signatures/)
- [Verificare la password per modificare utilizzando Aspose.Cells](/cells/it/nodejs-cpp/check-password-to-modify-using-aspose-cells/)
- [Rilevare il formato di file di Office Open XML crittografati - file OOXML](/cells/it/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Crittografia dei file Excel](/cells/it/nodejs-cpp/encrypting-excel-files/)
- [Come rilevare un formato di file e verificare se il file è crittografato](/cells/it/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="nodejs-cpp" >}}