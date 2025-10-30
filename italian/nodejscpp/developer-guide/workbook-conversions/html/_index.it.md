---
title: HTML con Node.js via C++
linktitle: HTML
type: docs
weight: 230
url: /it/nodejs-cpp/convert-excel-to-html/
---

## **Conversione di un Workbook Excel in HTML**
L’API Aspose.Cells supporta l’esportazione di fogli di calcolo in formato HTML. Per questo scopo, Aspose.Cells utilizza la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) per fornire la flessibilità di controllare vari aspetti dell’HTML di output.

L’esempio di codice seguente mostra come salvare una cartella di lavoro come file HTML usando Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to HTML format
workbook.save("out.html");
```


## **Conversione della cartella di lavoro Excel in file MHTML**
MHTML combina HTML normale con risorse esterne (ovvero contenuti collegati come immagini, animazioni, audio, ecc.) in un unico file. Sono usati per email con estensione .mht. Aspose.Cells supporta la lettura e la scrittura di file MHTML.

L’esempio di codice seguente mostra come salvare una cartella di lavoro come file MHTML usando Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```

## **Argomenti avanzati**
- [Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook](/cells/it/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Evitare la notazione esponenziale per i grandi numeri durante l'importazione da HTML](/cells/it/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Modifica il Tipo di Destinazione del Link HTML](/cells/it/nodejs-cpp/change-the-html-link-target-type/)
- [Convertire Excel in HTML con tooltip](/cells/it/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/it/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [Eliminare gli spazi ridondanti dopo un'interruzione di riga durante l'importazione di HTML](/cells/it/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML](/cells/it/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Disabilita l'Esportazione di Script Frame e Proprietà del Documento](/cells/it/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel to HTML - Utilizzare l'Opzione PresentationPreference per una Migliore Impaginazione](/cells/it/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Escludere Stili Non Utilizzati durante la conversione da Excel a HTML](/cells/it/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Espansione del testo da destra a sinistra durante l'esportazione di un file Excel in HTML](/cells/it/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Esportazione di formattazioni condizionali DataBar, ColorScale e IconSet durante la conversione da Excel in HTML](/cells/it/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Esporta commenti durante il salvataggio del file di Excel in HTML](/cells/it/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [Esportare le Proprietà del Documento Workbook e del Foglio di Lavoro nella conversione da Excel a HTML](/cells/it/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Esportare Excel in HTML con linee della griglia](/cells/it/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [Esportare l'intervallo dell'area di stampa in HTML](/cells/it/nodejs-cpp/export-print-area-range-to/)
- [Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser Web](/cells/it/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Esportare il Foglio di Stile CSS Separatamente nell'HTML di Output](/cells/it/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [Nascondere il Contenuto Sovrapposto con CrossHideRight durante il salvataggio in HTML](/cells/it/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Prefisso degli stili degli elementi della tabella con la proprietà HtmlSaveOptions.TableCssId](/cells/it/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Impedire l'Esportazione dei Contenuti dei Fogli Nascosti al Salvataggio in HTML](/cells/it/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Fornire il percorso del file HTML del foglio di lavoro esportato tramite l'interfaccia IFilePathProvider](/cells/it/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Riconoscere i Tag di Chiusura Automatica](/cells/it/nodejs-cpp/recognise-self-closing-tags/)
- [Rendere il Riempimento a Gradiente per WordArt durante la Conversione di Fogli di Calcolo in HTML](/cells/it/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Imposta la larghezza della colonna su un'unità scalabile come em o percentuale](/cells/it/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Imposta il carattere predefinito durante la rendering del foglio di calcolo in HTML](/cells/it/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Specifica come attraversare la stringa nell'output HTML utilizzando HtmlCrossType](/cells/it/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Supporta il layout dei tag DIV durante il caricamento di HTML nell'oggetto foglio di calcolo Excel](/cells/it/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Abilita le Proprietà CSS Personalizzate durante il salvataggio in HTML](/cells/it/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
