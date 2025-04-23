---
title: Proteggere i fogli di lavoro con Node.js tramite C++
linktitle: Protezione dei fogli di lavoro
type: docs
weight: 10
url: /it/nodejs-cpp/protecting-worksheets/
description: Impara come proteggere i fogli di lavoro in Excel usando Aspose.Cells for Node.js via C++, inclusa la protezione di righe, colonne e celle specifiche.
---


{{% alert color="primary" %}}

Quando un foglio di lavoro è protetto, le azioni che l'utente può eseguire sono limitate. Ad esempio, non può inserire dati, inserire o eliminare righe o colonne, ecc.

{{% /alert %}}

## **Proteggere i fogli di lavoro**

### **Introduzione**

Le opzioni generali di protezione in Microsoft Excel sono:

- Contenuti
- Oggetti
- Scenari

I fogli di lavoro protetti non nascondono o proteggono dati sensibili, quindi è diverso dalla crittografia dei file. In generale, la protezione del foglio di lavoro è adatta per scopi di presentazione. Impedisce all'utente finale di modificare i dati, il contenuto e la formattazione nel foglio di lavoro.

### **Proteggere un foglio di lavoro**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce il metodo [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) che viene utilizzato per applicare la protezione sul foglio di lavoro. Il metodo [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) accetta i seguenti parametri:

- Tipo di Protezione, il tipo di protezione da applicare al foglio di lavoro. Il tipo di protezione è applicato con l'aiuto dell'enumerazione [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype).
- Nuova password, la nuova password utilizzata per proteggere il foglio di lavoro.
- Vecchia password, la vecchia password, se il foglio di lavoro è già protetto da password. Se il foglio di lavoro non è già protetto, passare semplicemente null.

L'enumerazione [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype) contiene i seguenti tipi di protezione predefiniti:

|**Tipi di protezione**|**Descrizione**|
| :- | :- |
|All|L'utente non può modificare nulla in questo foglio di lavoro|
|Contents|L'utente non può inserire dati in questo foglio di lavoro|
|Objects|L'utente non può modificare oggetti disegno|
|Scenarios|L'utente non può modificare scenari salvati|
|Structure|L'utente non può modificare la struttura|
|Windows|La protezione è applicata alle finestre|
|None|Nessuna protezione è applicata|

L'esempio seguente mostra come proteggere un foglio di lavoro con una password.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file buffer
const excel = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = excel.getWorksheets().get(0);

// Protecting the worksheet with a password
worksheet.protect(AsposeCells.ProtectionType.All, "aspose", null);

// Saving the modified Excel file in default format
excel.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

Dopo che il codice sopra è utilizzato per proteggere il foglio di lavoro, è possibile verificare la protezione sul foglio di lavoro aprendolo. Una volta aperto il file e tentato di aggiungere alcuni dati al foglio di lavoro, si vedrà il seguente dialogo:

|**Un avviso di dialogo che l'utente non può modificare il foglio di lavoro**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Per lavorare sul foglio di lavoro, sblocca il foglio di lavoro selezionando **Protezione**, poi **Sblocca foglio** dal menu **Strumenti**.

Dopo aver selezionato Sblocca foglio nel menu, si aprirà una finestra di dialogo che richiederà di inserire la password in modo da poter lavorare sul foglio di lavoro come mostrato di seguito:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Proteggere alcune celle nel foglio di lavoro utilizzando Microsoft Excel**

Potrebbero esserci scenari in cui è necessario bloccare solo alcune celle del foglio di lavoro. Se si desidera bloccare alcune celle specifiche, bisogna sbloccare tutte le altre. Tutte le celle di un foglio di lavoro sono già inizializzate per essere bloccate; è possibile verificare aprendo un file Excel con MS Excel e cliccando su **Formato | Celle...** per mostrare la finestra di dialogo **Formato celle** e poi cliccare sulla scheda **Protezione** e vedere che la casella di controllo "Bloccato" è selezionata di default.

I punti seguenti descrivono come bloccare alcune celle usando MS Excel. Questo metodo si applica a Microsoft Office Excel 97, 2000, 2002, 2003 e versioni successive.

1. Selezionare l'intero foglio di lavoro facendo clic sul pulsante **Seleziona tutto** (il rettangolo grigio direttamente sopra il numero di riga per la riga 1 e alla sinistra della lettera della colonna A).
2. Clicca su **Celle** nel menu **Formato**, clicca sulla scheda **Protezione** e poi deseleziona la casella **Bloccato**.
   Questo sblocca tutte le celle del foglio di lavoro.
   Se il comando **Celle** non è disponibile, parti del foglio di lavoro potrebbero già essere bloccate. Nel menu **Strumenti**, posizionarsi su **Protezione**, e quindi fare clic su **Sblocca foglio**.
3. Seleziona solo le celle che desideri bloccare e ripeti il passaggio 2, ma questa volta seleziona la casella **Bloccato**.
4. Dal menu **Strumenti**, punta su **Protezione**, clicca su **Proteggi foglio** e poi su **OK**.
5. Nella finestra di dialogo **Proteggi foglio**, puoi specificare una password e selezionare gli elementi che desideri che gli utenti possano modificare.

### **Proteggi alcune celle nel foglio di lavoro usando Aspose.Cells**

In questo metodo, utilizziamo l'API Aspose.Cells esclusivamente per eseguire il compito.

Esempio: il seguente esempio mostra come proteggere alcune celle del foglio di lavoro. Sblocca tutte le celle del foglio prima e poi blocca 3 celle (A1, B1, C1). Infine, protegge il foglio di lavoro. L'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) contiene una proprietà booleana, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Puoi impostare la proprietà [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) su true o false e applicare il metodo *Column/Row.applyStyle()* per bloccare o sbloccare la riga/colonna con gli attributi desiderati.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get((i)).getStyle();
style.setIsLocked(false);
styleflag.setLocked(true);
sheet.getCells().getColumns().get((i)).applyStyle(style, styleflag);
}

// Lock the three cells...i.e. A1, B1, C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);
style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);
style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, Protect the sheet now.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Proteggere una riga nel foglio di lavoro**

Aspose.Cells permette di bloccare facilmente qualsiasi riga nel foglio di lavoro. Qui, possiamo utilizzare il metodo [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) della classe [**Aspose.Cells.Row**](https://reference.aspose.com/cells/nodejs-cpp/row) per applicare [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) a una riga specifica del foglio. Questo metodo accetta due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) e un oggetto [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) che contiene tutti i membri relativi alla formattazione applicata.

Il seguente esempio mostra come proteggere una riga nel foglio di lavoro. Sblocca tutte le celle del foglio prima e poi blocca la prima riga. Infine, protegge il foglio. L'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) contiene una proprietà booleana, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Puoi impostare [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) su true o false per bloccare o sbloccare la riga/colonna usando l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first row style.
style = sheet.getCells().getRows().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Set the lock setting.
flag.setLocked(true);

// Apply the style to the first row.
sheet.getCells().applyRowStyle(0, style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Proteggere una colonna nel foglio di lavoro**

Aspose.Cells permette di bloccare facilmente qualsiasi colonna nel foglio di lavoro. Qui, possiamo utilizzare il metodo [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/column/#applyStyle-style-styleflag-) della classe [**Aspose.Cells.Column**](https://reference.aspose.com/cells/nodejs-cpp/column) per applicare [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) a una colonna specifica del foglio. Questo metodo accetta due argomenti: un oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) e un oggetto [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) che contiene tutti i membri relativi alla formattazione applicata.

Il seguente esempio mostra come proteggere una colonna nel foglio di lavoro. Sblocca tutte le celle del foglio prima e poi blocca la prima colonna. Infine, protegge il foglio. L'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) contiene una proprietà booleana, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Puoi impostare [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) su true o false per bloccare o sbloccare la riga/colonna usando l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first column style.
style = sheet.getCells().getColumns().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Apply the style to the first column.
sheet.getCells().getColumns().get(0).applyStyle(style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Consenti agli utenti di modificare intervalli**

L'esempio seguente mostra come consentire agli utenti di modificare un intervallo in un foglio di lavoro protetto.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges
const allowRanges = sheet.getAllowEditRanges();

// Define ProtectedRange
let protected_range;

// Create the range
const idx = allowRanges.add("r2", 1, 1, 3, 3);
protected_range = allowRanges.get(idx);

// Specify the password
protected_range.setPassword("123");

// Protect the sheet
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file
book.save(path.join(dataDir, "protectedrange.out.xls"));
```
