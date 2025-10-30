---  
title: Establecer fuente predeterminada al renderizar hoja de cálculo a HTML con Node.js mediante C++  
linktitle: Establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML  
type: docs  
weight: 370  
url: /es/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/  
---  

{{% alert color="primary" %}}  
Aspose.Cells te permite establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML. Utiliza [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--) para este propósito. Esta propiedad es útil cuando hay celdas en una hoja de cálculo que tienen fuentes inválidas o que no existen. Entonces esas celdas se renderizarán en una fuente especificada con la propiedad [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  
{{% /alert %}}  

## Establecer la fuente predeterminada al renderizar la hoja de cálculo en HTML  

El siguiente código de ejemplo crea un libro de trabajo, agrega algo de texto en la celda B4 de la primera hoja de cálculo y establece su fuente en una fuente desconocida o inexistente. Luego guarda el libro en HTML estableciendo diferentes nombres de fuente predeterminada como Courier New, Arial, Times New Roman, etc.  

La captura de pantalla muestra el efecto de establecer diferentes nombres de fuentes predeterminadas mediante la propiedad [**HtmlSaveOptions.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDefaultFontName--).  

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)  

El código genera el [archivo HTML de salida con Courier New](5115516), el [archivo HTML de salida con Arial](5115518), y el [archivo HTML de salida con Times New Roman](5115517).  

## Código de Muestra  

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
