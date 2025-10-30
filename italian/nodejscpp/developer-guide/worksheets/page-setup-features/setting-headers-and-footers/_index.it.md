---
title: Impostare intestazioni e piè di pagina con Node.js tramite C++
linktitle: Impostazione Intestazioni e piè di pagina
type: docs
weight: 30
url: /it/nodejs-cpp/setting-headers-and-footers/
description: Questo articolo spiega come inserire programmaticamente un immagine nell intestazione e nel piè di pagina dei fogli di lavoro Excel usando Aspose.Cells for Node.js via C++. 
keywords: inserire immagine in intestazione e piè di pagina di Excel Node.js tramite C++, comandi script per intestazione e piè di pagina di Excel Node.js tramite C++
---

{{% alert color="primary" %}}

Le intestazioni e i piè di pagina sono le linee di testo visualizzate sotto il margine superiore o sopra il margine inferiore rispettivamente. È possibile aggiungere intestazioni e piè di pagina anche ai fogli di lavoro. Le intestazioni e i piè di pagina possono essere utilizzati per visualizzare informazioni utili come il numero di pagina, il nome dell'autore, il nome del tema o la data e l'ora. Le intestazioni e i piè di pagina sono gestiti utilizzando le impostazioni della pagina di setup.

{{% /alert %}}

## **Impostazione di intestazioni e piè di pagina**

Aspose.Cells for Node.js via C++ consente di aggiungere intestazioni e piè di pagina ai fogli di lavoro durante l'esecuzione, ma consigliamo di impostarli manualmente in un file pre-progettato per la stampa. Puoi usare Microsoft Excel come strumento GUI per impostare intestazioni e piè di pagina per risparmiare sforzo e tempo di sviluppo. Aspose.Cells può importare il file e salvare le impostazioni.

Per aggiungere intestazioni e piè di pagina in fase di esecuzione, Aspose.Cells fornisce chiamate API speciali e comandi di script per formattare intestazioni e piè di pagina.

### **Comandi di script**

I comandi di script sono comandi speciali che consentono di impostare la formattazione di intestazioni e piè di pagina.

|**Comandi di script**|**Descrizione**|
| :- | :- |
|&P|Numero di pagina corrente|
|&G|Un'immagine|
|&N|Il numero totale di pagine|
|&D|La data corrente|
|&T|L'orario corrente|
|&A|Il nome del foglio di lavoro|
|&F|Il nome del file senza percorso|
|&&Testo|Mostra &Testo. Per esempio: &&WO sarà visualizzato come &WO|
|&"\<FontName>"|Rappresenta un nome di carattere. Ad esempio: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Rappresenta il nome del carattere con lo stile. Ad esempio: &"Arial,Grassetto"|
|&\<FontSize>|Rappresenta la dimensione del carattere. Ad esempio: “&14abc”. Ma, se questo comando è seguito da un numero normale da stampare nell'intestazione, questo dovrebbe essere separato da un carattere spazio dalla dimensione del carattere. Ad esempio: “&14 123”.|

### **Imposta Intestazioni e Piè di Pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) fornisce due metodi, [**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) e [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-), usati per aggiungere intestazioni e piè di pagina a un foglio di lavoro. Questi metodi accettano solo due parametri:

- **Sezione** – la sezione in cui dovrebbe essere posizionata l'intestazione o il piè di pagina. Ci sono tre sezioni: sinistra, centro e destra, rappresentate rispettivamente da 0, 1 e 2.
- **Script** – lo script da utilizzare per l'intestazione o il piè di pagina. Questo script contiene comandi di script per formattare l'intestazione o il piè di pagina.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **Inserire un'immagine nell'intestazione o nel piè di pagina**

La classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) ha altri due metodi, [**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) e [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-), usati per inserire immagini nelle intestazioni e nei piè di pagina. Questi metodi accettano i parametri:

- **Sezione** – la sezione dell'intestazione o del piè di pagina in cui verrà posizionata l'immagine. Ci sono tre sezioni, sinistra, centro e destra, rappresentate dai valori 0, 1 e 2 rispettivamente.
- **Array di byte** – i dati grafici (i dati binari devono essere scritti nel buffer di un array di byte).

Dopo aver eseguito il codice sottostante e aperto il file, controlla l'intestazione del foglio di lavoro:

1. Nel menu **File**, seleziona **Imposta pagina**. Verrà visualizzata una finestra di dialogo.
1. Seleziona la scheda **Intestazione/Piè di pagina**.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
