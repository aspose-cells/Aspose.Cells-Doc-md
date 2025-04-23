---
title: Convertir Excel a Pdf, imagen y otros formatos
linktitle: Conversiones de libros de trabajo
type: docs
weight: 65
url: /es/net/convert-workbook-to-different-formats/
description: Convertir archivos de Excel a Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML y más.
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión entre muchos formatos. Técnicamente, la conversión significa cargar un libro de trabajo en un formato de archivo y guardarlo en otro.

{{% /alert %}}

## **Convertir libro de trabajo de Excel a PDF**

Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Convertir Libro de Excel a JPG**
Aspose.Cells admite la conversión de archivos de Excel a JPG.
El ejemplo de código a continuación muestra cómo guardar un libro como JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Convertir Libro de Excel a Imagen**
Aspose.Cells admite la conversión de archivos de Excel a imágenes.
El ejemplo de código a continuación muestra cómo guardar un libro como imágenes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Convirtiendo Libro de Excel a XPS**

El formato de documento XPS consta de marcado XML estructurado que define el diseño de un documento y la apariencia visual de cada página, junto con reglas de renderizado para distribuir, archivar, renderizar, procesar e imprimir documentos.

El lenguaje de marcado para XPS es un subconjunto de XAML que le permite incorporar elementos de gráficos vectoriales en documentos, utilizando XAML para marcar las primitivas de la Fundación de Presentación de Windows (WPF). Los elementos utilizados se describen en términos de rutas y otras primitivas geométricas.

Un archivo XPS es, de hecho, un archivo ZIP unicode que utiliza las Convenciones de Empaquetado Abierto, que contiene los archivos que componen el documento. Estos incluyen un archivo de marcado XML para cada página, texto, fuentes incrustadas, imágenes rasterizadas, gráficos vectoriales 2D, así como la información de gestión de derechos digitales. El contenido de un archivo XPS se puede examinar simplemente abriéndolo en una aplicación que admite archivos ZIP.

A partir de Aspose.Cells 6.0.0, se admite la conversión de Microsoft Excel a XPS.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Convertir Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells admite la conversión de archivos de Excel a archivos Ods, Sxc y Fods. El ejemplo de código a continuación muestra cómo convertir la [plantilla](book1.xlsx) a archivos Ods, Sxc y Fods.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Convirtiendo Libro de Excel a Archivos MHTML**

MHTML combina HTML normal con recursos externos (es decir, contenido que suele estar vinculado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.

Aspose.Cells admite la lectura y escritura de archivos MHTML.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo MHTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Convirtiendo Libro de Excel a HTML**

La API de Aspose.Cells proporciona soporte para exportar hojas de cálculo al formato HTML. Con este propósito, Aspose.Cells usa la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions) para proporcionar la flexibilidad de controlar varios aspectos del HTML de salida.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo HTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Configuración de las Preferencias de Imagen para HTML**

A partir de la versión 8.0.2, Aspose.Cells ha expuesto [**ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) para la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions), lo que permite a los desarrolladores especificar las preferencias de imagen al guardar las hojas de cálculo en formato HTML.

A continuación se detallan algunas de las configuraciones de imagen que se pueden aplicar:

- [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype): Especifica el tipo de imagen. Por favor, tenga en cuenta que todas las formas, incluidos los gráficos, se renderizan como imágenes en el HTML de salida.
- [**SmoothingMode**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode): Especifica el anti-aliasing para líneas, curvas y bordes de áreas rellenas.
- [**TextRenderingHint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint): Especifica la calidad de la renderización de texto.
- [**Quality**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality): Especifica la calidad de la imagen entre 0 y 100, cuando se especifica [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) como Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution): Obtiene o establece la resolución vertical de la imagen en puntos por pulgada.
- [**HorizontalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution): Obtiene o establece la resolución horizontal de la imagen en puntos por pulgada.
- [**TiffCompression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression): Obtiene o establece el tipo de compresión para las imágenes cuando se especifica [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) como Tiff.
- [**Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent): Indica si el fondo de una imagen debe ser transparente cuando se especifica ImageFormat como Png.

El siguiente código demuestra cómo utilizar [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) para especificar diferentes preferencias.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Convertir Libro de Excel a Markdown**

La API de Aspose.Cells proporciona soporte para exportar hojas de cálculo a formato Markdown. Para exportar la hoja de cálculo activa a Markdown, pase [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) como segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). También puedes usar la clase [**MarkdownSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions) para especificar ajustes adicionales para exportar la hoja de cálculo a Markdown.

El siguiente ejemplo de código demuestra la exportación de una hoja de cálculo activa a Markdown usando el miembro de enumeración [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Consulte el [archivo Markdown de salida](md_sample.txt) generado por el código para referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Convertir Libro de Excel a JSON**

Aspose.Cells admite la conversión de un libro de trabajo a un archivo Json (JavaScript Object Notation).

El siguiente ejemplo de código demuestra la exportación de una hoja de cálculo activa a Json utilizando el miembro de enumeración [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Consulte el código para convertir el [archivo fuente](Book1.xlsx) al [archivo Json de salida](Book1.Json) generado por el código para referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Convertir Excel a XML**
Aspose.Cells admite la conversión de un libro de trabajo a XML de Hoja de Cálculo Excel 2003 y datos XML sin formato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Convertir libro de Excel a TIFF**
Aspose.Cells admite la conversión de un libro de trabajo a un archivo TIFF.

El fragmento de código a continuación muestra cómo convertir Excel a TIFF:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Convertir libro de Excel a DOCX**

La API Aspose.Cells proporciona soporte para convertir hojas de cálculo al formato DOCX. Para exportar el libro de trabajo a DOCX, pase [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). También puede utilizar la clase [**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a DOCX.

El siguiente ejemplo de código demuestra la exportación de la hoja de cálculo activa a DOCX mediante el uso del miembro de la enumeración [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Consulta el [archivo DOCX de salida] (Book1.docx) generado por el código para más referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Convertir libro de Excel a PPTX**

La API Aspose.Cells proporciona soporte para convertir hojas de cálculo al formato PPTX. Para exportar el libro de trabajo a PPTX, pase [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). También puede utilizar la clase [**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a PPTX.

El siguiente ejemplo de código demuestra la exportación de la hoja de cálculo activa a PPTX mediante el uso del miembro de la enumeración [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Consulta el [archivo PPTX de salida] (Book1.pptx) generado por el código para más referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Convertir Libro de Excel a EPUB**

La API de Aspose.Cells proporciona soporte para convertir hojas de cálculo al formato EPUB. Para exportar el libro de trabajo a EPUB, pasa [**SaveFormat.Epub**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). También puedes usar la clase [**EBookSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/ebooksaveoptions) para especificar configuraciones adicionales para exportar la hoja de trabajo a Epub.

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a EPUB usando el miembro de enumeración [**SaveFormat.Epub**](https://reference.aspose.com/cells/net/aspose.cells/saveformat).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToEPUB-1.cs" >}}

## **Convertir Libro de Excel a AZW3**

La API de Aspose.Cells proporciona soporte para convertir hojas de cálculo al formato AZW3. Para exportar el libro a AZW3, pasa [**SaveFormat.Azw3**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). También puedes usar la clase [**EBookSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/ebooksaveoptions) para especificar configuraciones adicionales para exportar la hoja de trabajo a AZW3.

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a AZW3 usando el miembro de enumeración [**SaveFormat.Azw3**](https://reference.aspose.com/cells/net/aspose.cells/saveformat).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToAZW3-1.cs" >}}

## **Temas avanzados**
- [Convertir Revisión de XLSB a XLSM](/cells/es/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/es/net/convert-excel-to-html/)
- [Imagen](/cells/es/net/convert-excel-to-image/)
- [Json](/cells/es/net/convert-workbook-to-json/)
- [Convertir libro de trabajo de Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice calc).](/cells/es/net/convert-excel-to-ods/)
- [Pdf](/cells/es/net/convert-excel-workbook-to-pdf/)
- [Convertir Excel a CSV, TSV y Txt](/cells/es/net/convert-excel-to-csv-tsv-and-txt/)
- [Seguimiento del progreso de conversión de documentos](/cells/es/net/track-document-conversion-progress/)
- [Convertir CSV, TSV y TXT a Excel](/cells/es/net/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="csharp" >}}
