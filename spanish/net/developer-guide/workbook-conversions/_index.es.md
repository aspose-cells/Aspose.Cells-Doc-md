---
title: Convierta Excel a PDF, imagen y otros formatos
linktitle: Conversiones de libros
type: docs
weight: 65
url: /es/net/convert-workbook-to-different-formats/
description: Convierta archivos de Excel a Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, 0761934110, 4 XML y más.
---
{{% alert color="primary" %}}

Aspose.Cells admite la conversión entre muchos formatos. Técnicamente, la conversión significa cargar un libro de trabajo en un formato de archivo y guardarlo en otro.

{{% /alert %}}

## **Convertir libro de Excel a PDF**

Los archivos PDF se utilizan ampliamente para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se les pide a los desarrolladores de software que encuentren una forma de convertir archivos Excel Microsoft en documentos PDF.

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Convertir libro de trabajo de Excel a JPG**
Aspose.Cells admite la conversión de archivos de Excel a JPG.
El siguiente ejemplo de código muestra cómo guardar un libro de trabajo como JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Convertir libro de Excel en imagen**
Aspose.Cells admite la conversión de archivos de Excel a imágenes.
El siguiente ejemplo de código muestra cómo guardar un libro de trabajo como imágenes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Conversión de libro de Excel a XPS**

El formato de documento XPS consta de marcado XML estructurado que define el diseño de un documento y la apariencia visual de cada página, junto con reglas de representación para distribuir, archivar, representar, procesar e imprimir documentos.

El lenguaje de marcado para XPS es un subconjunto de XAML que le permite incorporar elementos de gráficos vectoriales en documentos, utilizando XAML para marcar las primitivas de Presentation Foundation (WPF) de Windows. Los elementos utilizados se describen en términos de caminos y otras primitivas geométricas.

Un archivo XPS es, de hecho, un archivo ZIP Unicode que utiliza las Convenciones de empaquetado abierto y contiene los archivos que componen el documento. Estos incluyen un archivo de marcado XML para cada página, texto, fuentes incrustadas, imágenes rasterizadas, gráficos vectoriales 2D, así como la información de gestión de derechos digitales. El contenido de un archivo XPS se puede examinar simplemente abriéndolo en una aplicación que admita archivos ZIP.

Desde Aspose.Cells 6.0.0, Microsoft Excel a XPS se admite la conversión.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Convierta Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice Calc)**
 Aspose.Cells admite la conversión de archivos de Excel a archivos Ods, Sxc y Fods. El siguiente ejemplo de código muestra cómo convertir el[templada](book1.xlsx) al archivo Ods, Sxc y Fods.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Conversión de libro de Excel a archivos MHTML**

MHTML combina HTML normal con recursos externos (es decir, contenido que suele estar vinculado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.

Aspose.Cells admite la lectura y escritura de archivos MHTML.

El siguiente ejemplo de código muestra cómo guardar un libro de trabajo como un archivo MHTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Conversión de libro de Excel a HTML**

 El Aspose.Cells API brinda soporte para exportar hojas de cálculo al formato HTML. Para ello, Aspose.Cells utiliza el**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**clase para proporcionar la flexibilidad para controlar varios aspectos de la salida HTML.

El siguiente ejemplo de código muestra cómo guardar un libro de trabajo como un archivo HTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Configuración de las preferencias de imagen para HTML**

 A partir de 8.0.2, Aspose.Cells ha expuesto**[Opciones de imagen](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)** Para el**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**clase, lo que permite a los desarrolladores especificar preferencias de imagen al guardar hojas de cálculo en formato HTML.

A continuación se detallan algunos de los ajustes de imagen que se pueden aplicar,

- **[Tipo de imagen] (https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**: Especifica el tipo de imagen. Tenga en cuenta que todas las formas, incluidos los gráficos, se representan como imágenes en la salida HTML.
- **[Modo de suavizado] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)**: especifica el suavizado de líneas, curvas y bordes de áreas rellenas.
- **[Sugerencia de representación de texto] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint)**: especifica la calidad de la representación del texto.
- **[Calidad](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)** : Especifica la calidad de la imagen entre 0 y 100, cuando**[Tipo de imagen] (https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**se especifica como JPEG.
- **[Resolución vertical](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalsolution)**: Obtiene o establece la resolución vertical de la imagen en puntos por pulgada.
- **[Resolución horizontal](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/resoluciónhorizontal)**Obtiene o establece la resolución horizontal de la imagen en puntos por pulgada.
- **[TiffCompression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)** : Obtiene o establece el tipo de compresión para las imágenes cuando**[Tipo de imagen] (https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**se especifica como Tiff.
- **[Transparente](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)**: indica si el fondo de una imagen debe ser transparente cuando ImageFormat se especifica como Png.

 El siguiente código demuestra cómo usar**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**para especificar diferentes preferencias.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Convertir libro de Excel a Markdown**

El Aspose.Cells API brinda soporte para exportar hojas de cálculo al formato Markdown. Para exportar la hoja de trabajo activa a Markdown, pase**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** como segundo parámetro de**[Libro de trabajo.Guardar](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)** método. También puede usar**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)**class para especificar configuraciones adicionales para exportar la hoja de trabajo a Markdown.

 El siguiente ejemplo de código muestra cómo exportar una hoja de trabajo activa a Markdown usando**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** miembro de la enumeración. Por favor vea el[salida de archivo Markdown](md_sample.txt)generado por el código como referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Convertir libro de Excel a JSON**

Aspose.Cells admite la conversión de un libro de trabajo a un archivo Json (notación de objetos de JavaScript).

El siguiente ejemplo de código muestra cómo exportar una hoja de trabajo activa a Json mediante el uso[**GuardarFormato.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) miembro de la enumeración. Por favor vea el código para convertir[archivo fuente](Book1.xlsx) al[archivo Json de salida](Book1.Json)generado por el código como referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Convertir Excel a XML**
Aspose.Cells admite la conversión de un libro de trabajo a XML de hoja de cálculo de Excel 2003 y datos XML sin formato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Convertir libro de Excel a TIFF**
Aspose.Cells admite la conversión de un libro de trabajo a un archivo TIFF.

El fragmento de código a continuación muestra cómo convertir Excel a TIFF:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Convertir libro de Excel a DOCX**

El Aspose.Cells API brinda soporte para convertir hojas de cálculo al formato DOCX. Para exportar el libro de trabajo a DOCX, pase[**GuardarFormato.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) como segundo parámetro de[**Libro de trabajo.Guardar**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) método. También puede usar[**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions) class para especificar configuraciones adicionales para exportar la hoja de trabajo a DOCX.

 El siguiente ejemplo de código muestra la exportación de la hoja de trabajo activa a DOCX mediante el uso[**GuardarFormato.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) miembro de la enumeración. Por favor vea el[archivo de salida DOCX](Book1.docx)generado por el código como referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Convertir libro de Excel a PPTX**

El Aspose.Cells API brinda soporte para convertir hojas de cálculo al formato PPTX. Para exportar el libro de trabajo a PPTX, pase[**GuardarFormato.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) como segundo parámetro de[**Libro de trabajo.Guardar**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) método. También puede usar[**PptxGuardarOpciones**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) class para especificar configuraciones adicionales para exportar la hoja de trabajo a PPTX.

 El siguiente ejemplo de código muestra la exportación de la hoja de trabajo activa a PPTX mediante el uso[**GuardarFormato.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) miembro de la enumeración. Por favor vea el[archivo de salida PPTX](Book1.pptx)generado por el código como referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Temas avanzados**
- [Convertir Revisión de XLSB a XLSM](/cells/es/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/es/net/convert-excel-to-html/)
- [Imagen](/cells/es/net/convert-excel-to-image/)
- [json](/cells/es/net/convert-workbook-to-json/)
- [Convierta el libro de trabajo de Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice calc).](/cells/es/net/convert-excel-to-ods/)
- [pdf](/cells/es/net/convert-excel-workbook-to-pdf/)
- [Convierta Excel a CSV,TSV y Txt](/cells/es/net/convert-excel-to-csv-tsv-and-txt/)
- [Seguimiento del progreso de la conversión de documentos](/cells/es/net/track-document-conversion-progress/)
- [Convierta CSV, TSV y TXT a Excel](/cells/es/net/convert-csv-tsv-and-txt-to-excel/)
