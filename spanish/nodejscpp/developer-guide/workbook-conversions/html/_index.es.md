---
title: HTML con Node.js a través de C++
linktitle: HTML
type: docs
weight: 230
url: /es/nodejs-cpp/convert-excel-to-html/
---

## **Convirtiendo Libro de Excel a HTML**
La API de Aspose.Cells ofrece soporte para exportar hojas de cálculo a formato HTML. Para esto, Aspose.Cells usa la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) para ofrecer flexibilidad en el control de varios aspectos del HTML de salida.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo HTML usando Node.js:

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


## **Convirtiendo Libro de Excel a Archivos MHTML**
MHTML combina HTML normal con recursos externos (es decir, contenido que normalmente está enlazado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se usan para correos electrónicos con extensión de archivo .mht. Aspose.Cells soporta la lectura y escritura de archivos MHTML.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo MHTML usando Node.js:

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

## **Temas avanzados**
- [Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo](/cells/es/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Evita la notación exponencial de números grandes al importar desde HTML](/cells/es/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Cambiar el tipo de destino del enlace HTML](/cells/es/nodejs-cpp/change-the-html-link-target-type/)
- [Convertir Excel a HTML con tooltip](/cells/es/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/es/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [Eliminar espacios redundantes después de salto de línea al importar HTML](/cells/es/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML](/cells/es/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Deshabilitar la exportación de scripts de marco y propiedades del documento](/cells/es/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel a HTML - Utilice la opción PresentationPreference para un mejor diseño](/cells/es/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Excluir estilos no utilizados durante la conversión de Excel a HTML](/cells/es/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Expandir texto de derecha a izquierda al exportar archivo Excel a HTML](/cells/es/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Exportar Formato Condicional DataBar, ColorScale e IconSet al convertir Excel a HTML](/cells/es/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Exportar comentarios al guardar archivo de Excel como HTML](/cells/es/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [Exportar propiedades del libro y la hoja de cálculo del documento en la conversión de Excel a HTML](/cells/es/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Exportar Excel a HTML con Líneas de Cuadrícula](/cells/es/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [Exportar rango del área de impresión a HTML](/cells/es/nodejs-cpp/export-print-area-range-to/)
- [Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web](/cells/es/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Exportar la hoja de estilos CSS por separado en el HTML de salida](/cells/es/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [Ocultar Contenido Superpuesto con CrossHideRight al guardar en HTML](/cells/es/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Prefijo de estilos de elementos de tabla con la propiedad HtmlSaveOptions.TableCssId](/cells/es/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Evitar la exportación del contenido oculto de la hoja de cálculo al guardar en HTML](/cells/es/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Proporcionar la ruta del archivo HTML de la hoja de cálculo exportada a través de la interfaz IFilePathProvider](/cells/es/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Reconocer etiquetas auto-cierre](/cells/es/nodejs-cpp/recognise-self-closing-tags/)
- [Renderizar relleno de degradado para WordArt al convertir hojas de cálculo a HTML](/cells/es/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Establecer el ancho de la columna a una unidad escalable como em o porcentaje](/cells/es/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Establecer fuente predeterminada al renderizar la hoja de cálculo a HTML](/cells/es/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Especifica cómo cruzar la cadena en HTML de salida utilizando HtmlCrossType](/cells/es/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Soportar el diseño de etiquetas DIV al cargar HTML en un libro de Excel](/cells/es/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Habilitar Propiedades Personalizadas de CSS al guardar en HTML](/cells/es/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
