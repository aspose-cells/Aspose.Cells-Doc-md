---
title: Convertir Excel a PDF, Imagen y otros formatos con Golang a través de C++
linktitle: Conversiones de libros de trabajo
type: docs
weight: 65
url: /es/go-cpp/convert-workbook-to-different-formats/
description: Convertir archivos de Excel a Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML y más usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells soporta la conversión entre muchos formatos. Técnicamente, la conversión implica cargar un libro en un formato de archivo y guardarlo en otro.

{{% /alert %}}

## **Convertir libro de trabajo de Excel a PDF**

Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales y particulares. Es un formato estándar de documento, y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions.go" >}}
## **Convertir Libro de Excel a JPG**
Aspose.Cells admite la conversión de archivos de Excel a JPG.
El ejemplo de código a continuación muestra cómo guardar un libro como JPG.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-1.go" >}}
## **Convertir Libro de Excel a Imagen**
Aspose.Cells admite la conversión de archivos de Excel a imágenes.
El ejemplo de código a continuación muestra cómo guardar un libro como imágenes.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-2.go" >}}
## **Convirtiendo Libro de Excel a XPS**

El formato de documento XPS consta de marcado XML estructurado que define el diseño de un documento y la apariencia visual de cada página, junto con reglas de renderizado para distribuir, archivar, renderizar, procesar e imprimir documentos.

El lenguaje de marcado para XPS es un subconjunto de XAML, lo que permite incorporar elementos gráficos vectoriales en los documentos, usando XAML para marcar las primitivas de Windows Presentation Foundation (WPF). Los elementos utilizados se describen en términos de rutas y otras primitivas geométricas.

Un archivo XPS es, en realidad, un archivo ZIP en formato Unicode que utiliza las Normas de Empaquetado Abierto, que contiene los archivos que conforman el documento. Estos incluyen un archivo de marcado XML para cada página, texto, fuentes incrustadas, imágenes rasterizadas, gráficos vectoriales 2D, así como información de gestión de derechos digitales. El contenido de un archivo XPS se puede examinar simplemente abriéndolo en una aplicación que soporte archivos ZIP.

A partir de Aspose.Cells 6.0.0, se admite la conversión de Microsoft Excel a XPS.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-3.go" >}}
## **Convertir Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells soporta la conversión de archivos de Excel a archivos Ods, Sxc y Fods. El ejemplo de código a continuación muestra cómo convertir la [plantilla](book1.xlsx) a archivos Ods, Sxc y Fods.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-4.go" >}}
## **Convirtiendo Libro de Excel a Archivos MHTML**

MHTML combina HTML normal con recursos externos (es decir, contenido que suele estar vinculado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.

Aspose.Cells admite la lectura y escritura de archivos MHTML.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo MHTML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-5.go" >}}
## **Convirtiendo Libro de Excel a HTML**

La API de Aspose.Cells ofrece soporte para exportar hojas de cálculo a formato HTML. Para esto, Aspose.Cells usa la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/) para ofrecer flexibilidad en el control de varios aspectos del HTML de salida.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo HTML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-6.go" >}}
## **Configuración de las Preferencias de Imagen para HTML**

A partir de la versión 8.0.2, Aspose.Cells ha expuesto [**GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) para la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/), permitiendo a los desarrolladores especificar preferencias de imagen al guardar hojas de cálculo en formato HTML.

A continuación, se detallan algunos de los ajustes de imagen que se pueden aplicar:

- [**ImageType**](https://reference.aspose.com/cells/go-cpp/imagetype/): Especifica el tipo de imagen. Por favor, tenga en cuenta que todas las formas, incluidos los gráficos, se renderizan como imágenes en el HTML de salida.
- [**GetQuality()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getquality/): Especifica la calidad de la imagen entre 0 y 100 cuando [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) se especifica como Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getverticalresolution/): Obtiene o establece la resolución vertical de la imagen en puntos por pulgada.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gethorizontalresolution/): Obtiene o establece la resolución horizontal de la imagen en puntos por pulgada.
- [**TiffCompression**](https://reference.aspose.com/cells/go-cpp/tiffcompression/): Obtiene o establece el tipo de compresión para las imágenes cuando [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) se especifica como Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gettransparent/): Indica si el fondo de una imagen debe ser transparente cuando se especifica ImageFormat como Png.

El código a continuación demuestra cómo usar [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) para especificar diferentes preferencias.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-7.go" >}}
## **Convertir Libro de Excel a Markdown**

La API de Aspose.Cells soporta la exportación de hojas de cálculo a formato Markdown. Para exportar la hoja de cálculo activa a Markdown, pase [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) para especificar configuraciones adicionales para exportar la hoja a Markdown.

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a Markdown usando el miembro del enumerador [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/). Por favor, consulte el [archivo Markdown de salida](md_sample.txt) generado por el código como referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-8.go" >}}
## **Convertir Libro de Excel a JSON**

Aspose.Cells soporta convertir un libro en un archivo JSON (JavaScript Object Notation).

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a JSON usando el miembro del enumerador [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/). Por favor, consulte el código para convertir el [archivo fuente](Book1.xlsx) al [archivo JSON de salida](Book1.Json) generado por el código como referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-9.go" >}}
## **Convertir Excel a XML**
Aspose.Cells admite la conversión de un libro de trabajo a XML de Hoja de Cálculo Excel 2003 y datos XML sin formato.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-10.go" >}}
## **Convertir libro de Excel a TIFF**
Aspose.Cells admite la conversión de un libro de trabajo a un archivo TIFF.

El fragmento de código a continuación muestra cómo convertir Excel a TIFF:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-11.go" >}}
## **Convertir libro de Excel a DOCX**

La API de Aspose.Cells proporciona soporte para convertir hojas de cálculo a formato DOCX. Para exportar el libro de trabajo a DOCX, pase [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) para especificar configuraciones adicionales para exportar la hoja a DOCX.

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a DOCX usando el miembro del enumerador [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/). Por favor, consulte el [archivo DOCX de salida](Book1.docx) generado por el código como referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-12.go" >}}
## **Convertir libro de Excel a PPTX**

La API de Aspose.Cells proporciona soporte para convertir hojas de cálculo a formato PPTX. Para exportar el libro de trabajo a PPTX, pase [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) para especificar configuraciones adicionales para exportar la hoja a PPTX.

El siguiente ejemplo de código demuestra cómo exportar la hoja de trabajo activa a PPTX usando [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) miembro de enumeración. Por favor, consulte el [archivo PPTX de salida](Book1.pptx) generado por el código como referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-13.go" >}}
## **Convertir Libro de Excel a EPUB**

La API Aspose.Cells ofrece soporte para convertir hojas de cálculo a formato EPUB. Para exportar el libro a EPUB, pase [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) para especificar configuraciones adicionales para exportar la hoja de trabajo a EPUB.

El siguiente ejemplo de código demuestra cómo exportar la hoja de trabajo activa a EPUB usando [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) miembro de enumeración.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-14.go" >}}
## **Convertir Libro de Excel a AZW3**

La API Aspose.Cells proporciona soporte para convertir hojas de cálculo a formato AZW3. Para exportar el libro a AZW3, pase [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) para especificar configuraciones adicionales para exportar la hoja de trabajo a AZW3.

El siguiente ejemplo de código demuestra cómo exportar la hoja de trabajo activa a AZW3 usando [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) miembro de enumeración.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-15.go" >}}
## **Temas avanzados**
- [Convertir Revisión de XLSB a XLSM](/cells/es/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/es/cpp/convert-excel-to-html/)
- [Imagen](/cells/es/cpp/convert-excel-to-image/)
- [Json](/cells/es/cpp/convert-workbook-to-json/)
- [Convertir libro de Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice calc).](/cells/es/cpp/convert-excel-to-ods/)
- [Pdf](/cells/es/cpp/convert-excel-workbook-to-pdf/)
- [Convertir Excel a CSV, TSV y Txt](/cells/es/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Seguimiento del progreso de conversión de documentos](/cells/es/cpp/track-document-conversion-progress/)
- [Convertir CSV, TSV y TXT a Excel](/cells/es/cpp/convert-csv-tsv-and-txt-to-excel/)
