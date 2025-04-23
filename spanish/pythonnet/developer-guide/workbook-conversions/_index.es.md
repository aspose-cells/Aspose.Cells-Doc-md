---
title: Convertir Excel a Pdf, imagen y otros formatos
linktitle: Conversiones de libros de trabajo
type: docs
weight: 65
url: /es/python-net/convert-workbook-to-different-formats/
description: Convertir archivos de Excel a Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML y más mediante la API de Aspose.Cells para Python via .NET.
keywords: Convertir libro de trabajo de Excel a PDF en Python, Convertir libro de trabajo de Excel a JPG en Python, Convertir libro de trabajo de Excel a imagen en Python, Convertir libro de trabajo de Excel a XPS usando Python, Convertir Excel a Ods, Sxc y Fods a través de Python, Convertir libro de trabajo de Excel a HTML en Python, Convertir libro de trabajo de Excel a JSON en Python, Convertir libro de trabajo de Excel a DOCX en Python, Convertir libro de trabajo de Excel a TIFF o MARKDOWN con Python.
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET admite la conversión entre muchos formatos. Técnicamente, la conversión significa cargar un libro de trabajo en un formato de archivo y guardarlo en otro.

{{% /alert %}}

## **Convertir libro de trabajo de Excel a PDF**

Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.

Aspose.Cells para Python via .NET admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-PDF.py" >}}

## **Convertir Libro de Excel a JPG**
Aspose.Cells para Python via .NET admite la conversión de archivos de Excel a JPG.
El ejemplo de código a continuación muestra cómo guardar un libro como JPG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JPG.py" >}}

## **Convertir Libro de Excel a Imagen**
Aspose.Cells para Python via .NET admite la conversión de archivos de Excel a imágenes.
El ejemplo de código a continuación muestra cómo guardar un libro como imágenes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Image.py" >}}

## **Convirtiendo Libro de Excel a XPS**

El formato de documento XPS consta de marcado XML estructurado que define el diseño de un documento y la apariencia visual de cada página, junto con reglas de renderizado para distribuir, archivar, renderizar, procesar e imprimir documentos.

El lenguaje de marcado para XPS es un subconjunto de XAML que le permite incorporar elementos de gráficos vectoriales en documentos, utilizando XAML para marcar las primitivas de la Fundación de Presentación de Windows (WPF). Los elementos utilizados se describen en términos de rutas y otras primitivas geométricas.

Un archivo XPS es, de hecho, un archivo ZIP unicode que utiliza las Convenciones de Empaquetado Abierto, que contiene los archivos que componen el documento. Estos incluyen un archivo de marcado XML para cada página, texto, fuentes incrustadas, imágenes rasterizadas, gráficos vectoriales 2D, así como la información de gestión de derechos digitales. El contenido de un archivo XPS se puede examinar simplemente abriéndolo en una aplicación que admite archivos ZIP.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XPS.py" >}}

## **Convertir Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells para Python via .NET admite la conversión de archivos de Excel a archivos Ods, Sxc y Fods. El ejemplo de código a continuación muestra cómo convertir la [plantilla](book1.xlsx) a archivos Ods, Sxc y Fods.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-ODS.py" >}}


## **Convirtiendo Libro de Excel a Archivos MHTML**

MHTML combina HTML normal con recursos externos (es decir, contenido que suele estar vinculado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.

Aspose.Cells para Python via .NET admite la lectura y escritura de archivos MHTML.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo MHTML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-MHTML.py" >}}

## **Convirtiendo Libro de Excel a HTML**

La API de Aspose.Cells para Python via .NET proporciona soporte para exportar hojas de cálculo a formato HTML. Para este propósito, Aspose.Cells para Python via .NET utiliza la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/) para proporcionar la flexibilidad de controlar varios aspectos de la salida HTML.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo HTML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML.py" >}}

## **Configuración de las Preferencias de Imagen para HTML**

Aspose.Cells for Python via .NET ha expuesto [**image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/) para la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions), permitiendo a los desarrolladores especificar las preferencias de imagen al guardar hojas de cálculo en formato HTML.

A continuación se detallan algunas de las configuraciones de imagen que se pueden aplicar:

- [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/): Especifica el tipo de imagen. Por favor, tenga en cuenta que todas las formas, incluidos los gráficos, se renderizan como imágenes en el HTML de salida.
- [**smoothing_mode**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/smoothing_mode/): Especifica el anti-aliasing para líneas, curvas y bordes de áreas rellenas.
- [**text_rendering_hint**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/text_rendering_hint/): Especifica la calidad de la renderización de texto.
- [**quality**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/quality/): Especifica la calidad de la imagen entre 0 y 100, cuando se especifica [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/) como Jpeg.
- [**vertical_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/): Obtiene o establece la resolución vertical de la imagen en puntos por pulgada.
- [**horizontal_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/): Obtiene o establece la resolución horizontal de la imagen en puntos por pulgada.
- [**tiff_compression**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/): Obtiene o establece el tipo de compresión para las imágenes cuando se especifica [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/) como Tiff.
- [**transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent/): Indica si el fondo de una imagen debe ser transparente cuando se especifica ImageFormat como Png.

El siguiente código demuestra cómo utilizar [**HtmlSaveOptions.image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/) para especificar diferentes preferencias.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML-SettingImagePrefrencesforHTML-1.py" >}}

## **Convertir Libro de Excel a Markdown**

La API de Aspose.Cells for Python via .NET brinda soporte para exportar hojas de cálculo a formato Markdown. Para exportar la hoja de cálculo activa a Markdown, pase [**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) como segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.saveformat). También puede utilizar la clase [**MarkdownSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/markdownsaveoptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a Markdown.

El siguiente ejemplo de código demuestra la exportación de una hoja de cálculo activa a Markdown usando el miembro de enumeración [**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/). Consulte el [archivo Markdown de salida](md_sample.txt) generado por el código para referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Markdown-1.py" >}}

## **Convertir Libro de Excel a JSON**

Aspose.Cells for Python via .NET admite la conversión de un libro de trabajo a un archivo Json (Notación de Objetos de JavaScript).

El siguiente ejemplo de código demuestra la exportación de una hoja de cálculo activa a Json utilizando el miembro de enumeración [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/). Consulte el código para convertir el [archivo fuente](Book1.xlsx) al [archivo Json de salida](Book1.Json) generado por el código para referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

## **Convertir Excel a XML**
Aspose.Cells for Python via .NET admite la conversión de un libro de trabajo a XML de Hoja de Cálculo 2003 y datos XML sin formato.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XML.py" >}}

## **Convertir libro de Excel a TIFF**
Aspose.Cells for Python via .NET es compatible con la conversión de un libro de trabajo a un archivo TIFF.

El fragmento de código a continuación muestra cómo convertir Excel a TIFF:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-TIFF.py" >}}

## **Convertir libro de Excel a DOCX**

La API Aspose.Cells for Python via .NET brinda soporte para convertir hojas de cálculo al formato DOCX. Para exportar el libro de trabajo a DOCX, pase [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) como segundo parámetro del método [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions). También puedes usar la clase [**DocxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/docxsaveoptions/) para especificar configuraciones adicionales para la exportación de la hoja de cálculo a DOCX.

El siguiente ejemplo de código demuestra la exportación de la hoja de cálculo activa a DOCX mediante el uso del miembro de la enumeración [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/). Consulta el [archivo DOCX de salida] (Book1.docx) generado por el código para más referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Docx-1.py" >}}

## **Convertir libro de Excel a PPTX**

La API Aspose.Cells for Python via .NET brinda soporte para convertir hojas de cálculo al formato PPTX. Para exportar el libro de trabajo a PPTX, pase [**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) como segundo parámetro del método [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions). También puedes usar la clase [**PptxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pptxsaveoptions) para especificar configuraciones adicionales para la exportación de la hoja de cálculo a PPTX.

El siguiente ejemplo de código demuestra la exportación de la hoja de cálculo activa a PPTX mediante el uso del miembro de la enumeración [**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/). Consulta el [archivo PPTX de salida] (Book1.pptx) generado por el código para más referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-File-To-Pptx-1.py" >}}

## **Temas avanzados**
- [Json](/cells/es/python-net/convert-workbook-to-json/)
- [Pdf](/cells/es/python-net/convert-excel-to-pdf/)
- [Convertir CSV, TSV y TXT a Excel](/cells/es/python-net/convert-csv-tsv-and-txt-to-excel/)
