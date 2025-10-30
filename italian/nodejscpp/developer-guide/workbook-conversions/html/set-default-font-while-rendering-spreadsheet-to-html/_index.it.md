---  
title: Imposta il font predefinito durante il rendering di un foglio di calcolo in HTML con Node.js tramite C++  
linktitle: Imposta il carattere predefinito durante la conversione del foglio di calcolo in HTML  
type: docs  
weight: 370  
url: /it/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
Aspose.Cells ti consente di impostare il carattere predefinito durante la conversione del foglio di calcolo in HTML. Si prega di utilizzare [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) a questo scopo. Questa proprietà è utile quando alcune celle in un foglio di calcolo hanno caratteri non validi o inesistenti. Quindi quelle celle verranno renderizzate con un carattere specificato con la proprietà [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  
{{% /alert %}}  

## Imposta il carattere predefinito durante la conversione del foglio di calcolo in HTML  

Il seguente codice di esempio crea un workbook e aggiunge del testo nella cella B4 del primo foglio di lavoro e imposta il suo carattere su un font sconosciuto/inesistente. Quindi salva il workbook in HTML impostando diversi nomi di carattere predefinito come Courier New, Arial, Times New Roman, ecc.  

Lo screenshot mostra l'effetto di impostare nomi di font predefiniti diversi tramite la proprietà [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

Il codice genera [file HTML di output con Courier New](5115516), il [file HTML con Arial](5115518) e il [file HTML di output con Times New Roman](5115517).  

## Codice di esempio  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object and access first worksheet.
const wb = new AsposeCells.Workbook();
const ws = wb.getWorksheets().get(0);

// Access cell B4 and add some text inside it.
const cell = ws.getCells().get("B4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell B4 which is unknown.
const st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
cell.setStyle(st);

// Now save the workbook in html format and set the default font to Courier New.
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDefaultFontName("Courier New");
wb.save(path.join(dataDir, "out_courier_new_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Arial.
opts.setDefaultFontName("Arial");
wb.save(path.join(dataDir, "out_arial_out.htm"), opts);

// Now save the workbook in html format once again but set the default font to Times New Roman.
opts.setDefaultFontName("Times New Roman");
wb.save(path.join(dataDir, "times_new_roman_out.htm"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
