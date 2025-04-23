---
title: Crittografare file Excel con Node.js tramite C++
linktitle: Crittografare file Excel
type: docs
weight: 90
url: /it/nodejs-cpp/encrypting-excel-files/
description: Impara come cifrare e proteggere con password i file Excel usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) ti consente di crittare e proteggere con password i tuoi fogli di calcolo. Utilizza algoritmi forniti da un fornitore di servizi crittografici, o CSP, un insieme di algoritmi crittografici con proprietà diverse. Il CSP predefinito è 'Office 97/2000 Compatible' o 'Crittografia debole (XOR)'. È importante scegliere la corretta lunghezza della chiave di crittografia. Alcuni CSP non supportano più di 40 o 56 bit. Questo è considerato una crittografia debole. Per una crittografia forte, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene CSP che offrono tipi di crittografia forte, ad esempio il 'Microsoft Strong Cryptographic Provider'. Per darti un'idea, la crittografia a 128 bit è ciò che le banche usano per crittografare la connessione con i loro sistemi di Internet Banking.

Aspose.Cells consente di crittografare e proteggere con password file Microsoft Excel con il tipo di crittografia desiderato.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per impostare le impostazioni di crittografia del file in Microsoft Excel (qui Microsoft Excel 2003):

1. Dal menu **Strumenti**, seleziona **Opzioni**. Verrà visualizzata una finestra di dialogo.
1. Selezionare la scheda **Sicurezza**.
1. Immetti una password e clicca su **Avanzate**
1. Scegliere il tipo di crittografia e confermare la password.

## **Crittografia con Aspose.Cells for Node.js via C++**

L'esempio seguente mostra come crittare e proteggere con password un file excel utilizzando l'API Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```

### **Specificare la password per modificare l'opzione**

L'esempio seguente mostra come impostare l'opzione **Password per modificare** per un file esistente utilizzando l'API Aspose.Cells di Microsoft Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```

## **Verifica la password del file crittografato**

Per verificare la password del file criptato, Aspose.Cells for Node.js via C++ fornisce il metodo [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-). Questi metodi accettano due parametri, il flusso del file e la password da verificare.
Il seguente frammento di codice dimostra l'uso del metodo [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) per verificare se la password fornita è valida o meno.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is Valid: " + isPasswordValid);
```

## **Crittografia/Decrittografia del file ODS con Aspose.Cells**

Aspose.Cells ti permette di cifrare e decifrare i file ODS. Il file ODS decriptato può essere aperto sia in Excel che in OpenOffice, tuttavia il file ODS criptato può essere aperto solo in OpenOffice previa inserimento della password. Excel non può aprire il file ODS criptato e potrebbe mostrare un messaggio di avviso. Le opzioni di crittografia non sono applicabili ai file ODS, a differenza di altri tipi di file. Per cifrare un file ODS, carica il file e imposta il valore [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) con la password reale prima di salvarlo. Il file ODS crittografato in output può essere aperto solo in OpenOffice.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

Per decifrare un file ODS, caricare il file fornendo una password in [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). Una volta caricato il file, impostare la stringa [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) su null.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an encrypted ODS file
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Ods);

// Set original password
loadOptions.setPassword("1234");

// Load the encrypted ODS file with the appropriate load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleEncryptedODSFile.ods"), loadOptions);

// Set the password to null
workbook.getSettings().setPassword(null);

// Save the decrypted ODS file
workbook.save(outputDir + "outputDecryptedODSFile.ods");
```
