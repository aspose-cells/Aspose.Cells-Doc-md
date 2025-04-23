---
title: Configurare i caratteri per il rendering dei fogli di calcolo con Node.js tramite C++
linktitle: Configurazione dei Font per la Visualizzazione dei Fogli di Lavoro
type: docs
weight: 10
url: /it/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Scopri come configurare i font per renderizzare i fogli di calcolo usando Aspose.Cells for Node.js via C++. Assicurati che i font siano disponibili per la massima fedeltà di conversione.
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells offrono la possibilità di rendere i fogli di calcolo in formati immagine e di convertirli in formati PDF & XPS. Per massimizzare la fedeltà della conversione, è necessario che i font usati nel foglio di calcolo siano disponibili nella directory font predefinita del sistema operativo. Se i font richiesti non sono presenti, le API di Aspose.Cells tenteranno di sostituirli con quelli disponibili.

## **Selezione dei font**

Di seguito il processo che le API di Aspose.Cells seguono dietro le quinte.

1. L'API cerca di trovare i font nel file system corrispondenti al nome esatto del font utilizzato nel foglio di calcolo.
1. Se l'API non riesce a trovare i font con lo stesso nome esatto, tenta di utilizzare il font predefinito specificato nella proprietà [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) del foglio di lavoro.
1. Se l'API non riesce a individuare il font definito nella proprietà [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) del foglio di lavoro, tenta di utilizzare il font specificato nelle proprietà [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) o [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--).
1. Se l'API non riesce a individuare il font definito nelle proprietà [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) o [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--), tenta di utilizzare il font specificato nella proprietà [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--).
1. Se l'API non riesce a individuare il font definito nella proprietà [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--), tenta di selezionare i font più adatti tra tutti i font disponibili.
1. Infine, se l'API non riesce a trovare alcun font nel file system, renderizza il foglio di calcolo utilizzando Arial.

## **Impostazione delle cartelle dei font personalizzate**

Le API di Aspose.Cells cercano i font richiesti nella directory font predefinita del sistema operativo. Se i font richiesti non sono disponibili, le API cercano nelle directory personalizzate (definite dall’utente). La classe [**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs) ha esposto diversi modi per impostare directory personalizzate dei font come dettagliato di seguito.

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): Questo metodo è utile se c'è solo una cartella da impostare.
1. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): Questo metodo è utile quando i font risiedono in più cartelle e l'utente desidera impostare tutte le cartelle separatamente anziché combinare tutti i font in una singola cartella.
1. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): Questo meccanismo è utile quando l'utente desidera caricare i font da più cartelle o un singolo file font o dati font da un array di byte.

{{% alert color="primary" %}}

Sia i metodi [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) che [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) accettano un secondo parametro di tipo Boolean. Passare **true** come secondo parametro indirizzerà le API di Aspose.Cells a cercare i file dei font nelle sottocartelle.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

Si prega di utilizzare uno qualsiasi dei metodi sopra menzionati all'inizio dell'applicazione, cioè; prima di invocare altri oggetti delle API di Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Se tutti i metodi sopra menzionati vengono utilizzati per impostare le origini dei font, solo le ultime impostazioni avranno effetto.

{{% /alert %}}

## **Meccanismo di sostituzione del font**

Le API di Aspose.Cells offrono anche la possibilità di specificare il font di sostituzione per scopi di rendering. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina utilizzata per la conversione. Gli utenti possono fornire una lista di nomi di font come alternativa al font originale. Per fare ciò, le API di Aspose.Cells hanno esposto il metodo [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-) che accetta 2 parametri. Il primo è di tipo **string**, indicante il nome del font da sostituire. Il secondo è un array di tipo **string**, nel quale gli utenti possono fornire una lista di nomi di font come sostituzione del font originale (specificato nel primo parametro).

Ecco uno scenario d'uso semplice.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **Raccolta informazioni**

Oltre ai metodi sopra menzionati, le API di Aspose.Cells forniscono anche strumenti per raccogliere informazioni sulle fonti e sostituzioni impostate.

1. Il metodo [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) restituisce un array di tipo [**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase) contenente l’elenco delle fonti specificate. Se nessuna fonte è stata impostata, il metodo [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) restituirà un array vuoto.
1. Il metodo [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) accetta un parametro di tipo **string** per specificare il nome del font per il quale è stato impostato il substitution. Se non è stato impostato alcun substitution per il nome del font specificato, il metodo [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) restituirà null.

## **Argomenti avanzati**
- [Imposta il carattere predefinito durante il rendering del foglio elettronico in immagini](/cells/it/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Imposta la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per dare priorità](/cells/it/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formati di carattere supportati](/cells/it/nodejs-cpp/supported-font-formats/)
- [Foglio elettronico in immagine - Imposta il formato pixel per l'immagine renderizzata](/cells/it/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
