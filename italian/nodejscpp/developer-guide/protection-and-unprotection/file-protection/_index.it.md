---  
title: Cripta e Decripta file Excel con Node.js tramite C++  
linktitle: Crittografa e Decrittografa file Excel  
type: docs  
weight: 10  
url: /it/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: Come criptare e decriptare file Excel usando Node.js tramite C++. Blocco e sblocco di file Excel.  
---  

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) ti consente di crittare e proteggere con password i tuoi fogli di calcolo. Utilizza algoritmi forniti da un fornitore di servizi crittografici, o CSP, un insieme di algoritmi crittografici con proprietà diverse. Il CSP predefinito è 'Office 97/2000 Compatible' o 'Crittografia debole (XOR)'. È importante scegliere la corretta lunghezza della chiave di crittografia. Alcuni CSP non supportano più di 40 o 56 bit. Questo è considerato una crittografia debole. Per una crittografia forte, è richiesta una lunghezza minima della chiave di 128 bit. Microsoft Windows contiene CSP che offrono tipi di crittografia forte, ad esempio il 'Microsoft Strong Cryptographic Provider'. Per darti un'idea, la crittografia a 128 bit è ciò che le banche usano per crittografare la connessione con i loro sistemi di Internet Banking.  

Aspose.Cells consente di crittografare e proteggere con password file Microsoft Excel con il tipo di crittografia desiderato.  
{{% /alert %}}  

## **Utilizzando Microsoft Excel**  

Per impostare le impostazioni di crittografia del file in Microsoft Excel (qui Microsoft Excel 2003):  

1. Dal menu **Strumenti**, seleziona **Opzioni**. Verrà visualizzata una finestra di dialogo.  
2. Seleziona la scheda **Sicurezza**.  
3. Inserisci una password e fai clic su **Avanzate**  
4. Scegli il tipo di crittografia e conferma la password.  

## **Criptare il file Excel con Aspose.Cells for Node.js via C++**  

Il seguente esempio mostra come criptare e proteggere con password un file Excel usando l'API Aspose.Cells.  

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

### **Specificare l'opzione Password per modificare**  

L'esempio seguente mostra come impostare l'opzione **Password per modificare** per un file esistente utilizzando l'API Aspose.Cells di Microsoft Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  


## **Decriptare file Excel con Aspose.Cells for Node.js via C++**  
È molto facile aprire un file Excel protetto da password e decriptarlo usando l'API Aspose.Cells come mostrato nel codice seguente:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);

// Remove password.
workbook.getSettings().setPassword(null);

// Save the file.
workbook.save(filePath);
```  


## **Argomenti avanzati**  
- [Crittografa e Decrittografa file ODS](/cells/it/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [Impostazione del tipo di crittografia forte](/cells/it/nodejs-cpp/setting-strong-encryption-type/)  
- [Specificare l'autore durante la protezione in scrittura del workbook](/cells/it/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [Verifica password dei file crittografati](/cells/it/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
