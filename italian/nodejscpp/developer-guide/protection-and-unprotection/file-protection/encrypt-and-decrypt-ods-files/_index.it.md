---
title: Cifrare e decifrare file ODS con Node.js tramite C++
linktitle: Crittografa e decritta i file ODS
type: docs
weight: 10
url: /it/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: Protegge con password e cifra i file ODS usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
OpenOffice.org è una suite per ufficio completa che supporta la protezione con password e la cifratura dei file. Tuttavia, un file ODS cifrato può essere aperto solo da OpenOffice dopo aver fornito la password. Excel non può aprire il file ODS criptato e potrebbe mostrare messaggi di avviso. Le opzioni di cifratura non sono applicabili ai file ODS, a differenza di altri tipi di file. 
Aspose.Cells permette di cifrare e decifrare file ODS. I file ODS decifrati possono essere aperti sia in Excel che in OpenOffice.
{{% /alert %}}

## **Crittografa con OpenOffice Calc**
1. Seleziona **Salva come** e clicca sulla casella **Salva con password**.
1. Fai clic sul pulsante **Salva**.
1. Digita la password desiderata nei campi **Inserisci password per aprire** e **Conferma password** nella finestra Imposta password che si apre. 
1. Fare clic sul pulsante **OK** per salvare il file.

## **Cifra il file ODS con Aspose.Cells for Node.js via C++**
Per crittografare un file ODS, caricare il file e impostare il valore [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) sulla password effettiva prima di salvarlo. Il file ODS crittografato in output può essere aperto solo in OpenOffice.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "source");
const outputDir = path.join(__dirname, "output");

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

## **Decrittografare file ODS con Aspose.Cells for Node.js via C++**
Per decriptare un file ODS, caricare il file fornendo una password in [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). Una volta caricato, impostare la stringa [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) su null.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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
