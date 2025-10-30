---
title: Ottenere intestazioni o piè di pagina con Node.js via C++
linktitle: Ottenere Intestazioni o Piè di Pagina
type: docs
weight: 30
url: /it/nodejs-cpp/get-headers-or-footers/
description: Questo articolo spiega come ottenere programmaticamente intestazioni e piè di pagina da file Excel o OpenOffice usando l API Node.js via C++.
---

{{% alert color="primary" %}}

Le intestazioni e i piè di pagina vengono visualizzati solo nella visualizzazione Layout di pagina, Anteprima di stampa e sulle pagine stampate. 

È inoltre possibile utilizzare la finestra di dialogo Imposta pagina se si desidera visualizzare le intestazioni o i piè di pagina per più di un foglio di lavoro alla volta. 

Per altri tipi di fogli, come fogli grafico o grafici, è possibile inserire solo intestazioni e piè di pagina utilizzando la finestra di dialogo Imposta pagina.

{{% /alert %}}

## **Ottenere Intestazioni e Piè di Pagina in MS Excel**
1. Fare clic sul foglio di lavoro dove si desidera visualizzare o modificare le intestazioni o i piè di pagina.
2. Nella scheda Visualizza, nel gruppo Visualizzazioni cartella di lavoro, clicca su Layout di pagina.
   Excel visualizza il foglio di lavoro in vista Layout di pagina.
3. Per visualizzare o modificare un'intestazione o un piè di pagina, fare clic sulla casella di testo intestazione o piè di pagina a sinistra, al centro o a destra nella parte superiore o inferiore della pagina del foglio di lavoro (sotto Intestazione o sopra Piè di pagina).


## **Ottenere intestazioni e piè di pagina usando Aspose.Cells for Node.js via C++**
Con i metodi [**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) e [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-), gli sviluppatori Node.js possono semplicemente ottenere intestazioni o piè di pagina dal file.

1. Costruisci una cartella di lavoro per aprire il file.
2. Ottieni il foglio di lavoro in cui vuoi ottenere intestazioni o piè di pagina.
3. Ottieni l'intestazione o il piè di pagina con un ID di sezione specifico.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **Analizza Intestazioni e Piè di Pagina in elenco di comandi**
Il testo dell'intestazione o del piè di pagina può contenere comandi speciali, ad esempio un segnaposto per il numero di pagina, la data corrente o attributi di formattazione del testo.

I comandi speciali sono rappresentati da una singola lettera con un carattere 'e commerciale' iniziale ("&").

Le stringhe di intestazione e piè di pagina sono costruite usando la grammatica ABNF. Non è facile da capire senza un visualizzatore.

Aspose.Cells for Node.js via C++ fornisce il metodo [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) per analizzare intestazioni e piè di pagina come lista di comandi.

I seguenti codici mostrano come analizzare l'intestazione o il piè di pagina come lista di comandi e processare i comandi:

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
