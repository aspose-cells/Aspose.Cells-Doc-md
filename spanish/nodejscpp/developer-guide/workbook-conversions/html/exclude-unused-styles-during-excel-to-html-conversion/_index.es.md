---  
title: Excluir estilos no utilizados durante la conversión de Excel a HTML con Node.js a través de C++  
linktitle: Excluir Estilos No Utilizados durante la conversión de Excel a HTML  
type: docs  
weight: 30  
url: /es/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: Aprende cómo excluir estilos no utilizados al convertir Excel en HTML usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Los archivos de Microsoft Excel pueden contener muchos estilos no utilizados. Al exportar el archivo a HTML, estos estilos también se exportan, lo que puede aumentar el tamaño del HTML. Puedes excluir los estilos no utilizados durante la conversión configurando la propiedad [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) a **true**. Cuando lo hagas, se excluirán todos los estilos no utilizados del HTML de salida. La captura muestra un ejemplo de estilo no utilizado en el HTML generado.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Excluir estilos no utilizados durante la conversión de Excel a HTML**  

El siguiente código de ejemplo crea un libro de trabajo y también crea un estilo nombrado no utilizado. Dado que [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) está en **true**, este estilo no utilizado no se exportará a [HTML de salida](61767778.zip). Si lo configuras en **false**, este estilo no utilizado aparecerá en el HTML de salida, visible en la marca de marcado HTML como en la captura.  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
