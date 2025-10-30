---
title: Establecer la propiedad DefaultFont de PdfSaveOptions y ImageOrPrintOptions para tener prioridad con Node.js a través de C++
linktitle: Establecer la propiedad DefaultFont de PdfSaveOptions y ImageOrPrintOptions para tener prioridad
type: docs
weight: 30
url: /es/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Descubre cómo establecer la propiedad DefaultFont de PdfSaveOptions y ImageOrPrintOptions usando Aspose.Cells for Node.js via C++. Asegura una correcta representación de la fuente cuando faltan las fuentes.
---

## **Escenarios de uso posibles**

Al establecer la propiedad **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), podrías esperar que al guardar en PDF o imagen se establezca ese DefaultFont para todo el texto en un libro de trabajo que tiene fuente faltante (no instalada).

Por lo general, al guardar en PDF o imagen, Aspose.Cells for Node.js via C++ intentará primero establecer la fuente predeterminada del libro de trabajo (es decir, `Workbook.DefaultStyle.Font`). Si la fuente predeterminada del libro de trabajo aún no puede mostrar o renderizar el texto correctamente, entonces Aspose.Cells intentará renderizar con la fuente mencionada contra el atributo DefaultFont en [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/).

Para cumplir con tu expectativa, tenemos una propiedad booleana llamada "**CheckWorkbookDefaultFont**" en [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/). Puedes establecerla en **false** para desactivar la fuente predeterminada del libro de trabajo o permitir que la configuración **DefaultFont** en [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) tenga prioridad.

## **Establecer la propiedad DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

El siguiente código de ejemplo abre un archivo Excel. La celda A1 (en la primera hoja) tiene un texto establecido como "Texto de fuente Navidad". El nombre de la fuente es "Personal Use Navidad" que no está instalada en la máquina. Establecemos el atributo **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) en "Times New Roman". También configuramos la propiedad booleana **CheckWorkbookDefaultFont** en **"false"** lo que garantiza que el texto de la celda A1 se renderice con la fuente "Times New Roman" y no use la fuente predeterminada del libro ("Calibri" en este caso). El código renderiza la primera hoja a formatos de imagen PNG y TIFF. Finalmente, renderiza a un archivo PDF.

{{% alert color="primary" %}}

El valor predeterminado del atributo **CheckWorkbookDefaultFont** es **true**.

{{% /alert %}}

Esta es la captura de pantalla del [archivo de plantilla](49446913.xlsx) utilizado en el código de ejemplo.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Esta es la imagen PNG de salida después de establecer la propiedad [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) en "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Ver la imagen [TIFF](48496672.tiff) de salida después de establecer la propiedad [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) en "Times New Roman".

Ver el archivo [PDF](48496673.pdf) de salida después de configurar la propiedad [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) a "Times New Roman".

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open an Excel file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx"));

// Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const imgOpt = new AsposeCells.ImageOrPrintOptions();
imgOpt.setImageType(AsposeCells.ImageType.Png);
imgOpt.setCheckWorkbookDefaultFont(false);
imgOpt.setDefaultFont("Times New Roman");
const sr = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imgOpt);
sr.toImage(0, path.join(outputDir, "out1_imagePNG.png"));

// Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
imgOpt.setImageType(AsposeCells.ImageType.Tiff);
const wr = new AsposeCells.WorkbookRender(workbook, imgOpt);
wr.toImage(path.join(outputDir, "out1_imageTIFF.tiff"));

// Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setDefaultFont("Times New Roman");
saveOptions.setCheckWorkbookDefaultFont(false);
workbook.save(path.join(outputDir, "out1_pdf.pdf"), saveOptions);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
