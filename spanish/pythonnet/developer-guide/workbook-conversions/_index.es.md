---
title: Convertir Excel a Pdf, Imagen y otros formatos
linktitle: Conversiones de libros de trabajo
type: docs
weight: 65
url: /es/python-net/convert-workbook-to-different-formats/
description: Convierta archivos de Excel a Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML y más usando Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel Workbook to PDF, Convert Excel Workbook to JPG in Python, Python Convert Excel Workbook to Image, Converting Excel Workbook to XPS using Python, Convert Excel to Ods,Sxc and Fods via Python, Python Convert Excel Workbook to HTML, Convert Excel Workbook to JSON in Python, Python Convert Excel Workbook to DOCX, Convert Excel Workbook to TIFF or MARKDOWN with Ptyhon.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET admite la conversión entre muchos formatos. Técnicamente, conversión significa cargar un libro en un formato de archivo y guardarlo en otro.

{{% /alert %}}

##  **Convertir libro de Excel a PDF**

Los archivos PDF se utilizan ampliamente para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se les pide a los desarrolladores de software que encuentren una manera de convertir archivos de Excel Microsoft en documentos PDF.

Aspose.Cells for Python via .NET admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-PDF.py" >}}

##  **Convertir libro de Excel a JPG**
Aspose.Cells for Python via .NET admite la conversión de archivos de Excel a JPG.
El siguiente ejemplo de código muestra cómo guardar un libro como JPG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JPG.py" >}}

##  **Convertir libro de Excel a imagen**
Aspose.Cells for Python via .NET admite la conversión de archivos de Excel a imágenes.
El siguiente ejemplo de código muestra cómo guardar un libro como imágenes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Image.py" >}}

##  **Conversión de libro de Excel a XPS**

El formato de documento XPS consta de un marcado XML estructurado que define el diseño de un documento y la apariencia visual de cada página, junto con reglas de representación para distribuir, archivar, representar, procesar e imprimir documentos.

El lenguaje de marcado para XPS es un subconjunto de XAML que le permite incorporar elementos de gráficos vectoriales en documentos, utilizando XAML para marcar las primitivas de Presentation Foundation (WPF) de Windows. Los elementos utilizados se describen en términos de caminos y otras primitivas geométricas.

Un archivo XPS es, de hecho, un archivo ZIP Unicode que utiliza las convenciones de empaquetado abierto y que contiene los archivos que componen el documento. Estos incluyen un archivo de marcado XML para cada página, texto, fuentes incrustadas, imágenes rasterizadas, gráficos vectoriales 2D, así como información de gestión de derechos digitales. El contenido de un archivo XPS se puede examinar simplemente abriéndolo en una aplicación que admita archivos ZIP.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XPS.py" >}}

##  **Convierta Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice Calc)**
 Aspose.Cells for Python via .NET admite la conversión de archivos Excel a archivos Ods, Sxc y Fods. El siguiente ejemplo de código muestra cómo convertir el[templar](book1.xlsx) al archivo Ods, Sxc y Fods.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-ODS.py" >}}


##  **Conversión de libro de Excel a archivos MHTML**

MHTML combina HTML normal con recursos externos (es decir, contenido que normalmente está vinculado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.

Aspose.Cells for Python via .NET admite la lectura y escritura de archivos MHTML.

El siguiente ejemplo de código muestra cómo guardar un libro como un archivo MHTML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-MHTML.py" >}}

##  **Conversión de libro de Excel a HTML**

 Aspose.Cells for Python via .NET API brinda soporte para exportar hojas de cálculo al formato HTML. Para ello, Aspose.Cells for Python via .NET utiliza el**[HtmlSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/)**clase para proporcionar la flexibilidad de controlar varios aspectos de la salida HTML.

El siguiente ejemplo de código muestra cómo guardar un libro como un archivo HTML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML.py" >}}

##  **Configuración de las preferencias de imagen para HTML**

 Aspose.Cells for Python via .NET ha expuesto**[opciones_imagen](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/)** Para el**[HtmlSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions)**clase, que permite a los desarrolladores especificar preferencias de imagen al guardar hojas de cálculo en formato HTML.

A continuación se detallan algunas de las configuraciones de imagen que se pueden aplicar.

- *[Tipo de imagen](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/)**: Especifica el tipo de imagen. Tenga en cuenta que todas las formas, incluidos los gráficos, se representan como imágenes en el resultado HTML.
- *[modo_suavizado](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/smoothing_mode/)**: Especifica el suavizado de líneas, curvas y bordes de áreas rellenas.
- *[pista_rendering_texto](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/text_rendering_hint/)**: Especifica la calidad de la representación del texto.
- **[calidad](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/quality/)**: Especifica la calidad de la imagen entre 0 y 100, cuando **[ImageType ](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/)**se especifica como Jpeg.
- *[resolución_vertical](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)**: Obtiene o establece la resolución vertical de la imagen en puntos por pulgada.
- *[resolucion horizontal](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/)**: Obtiene o establece la resolución horizontal de la imagen en puntos por pulgada.
- **[tiff_compression](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/)**: Obtiene o establece el tipo de compresión de las imágenes cuando **[ImageType]( https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/)**se especifica como Tiff.
- *[transparente](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent/)**: Indica si el fondo de una imagen debe ser transparente cuando ImageFormat se especifica como Png.

 El siguiente código demuestra cómo utilizar**[HtmlSaveOptions.image_options](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/)**para especificar diferentes preferencias.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML-SettingImagePrefrencesforHTML-1.py" >}}

##  **Convertir un libro de Excel a Markdown**

Aspose.Cells for Python via .NET API brinda soporte para exportar hojas de cálculo al formato Markdown. Para exportar la hoja de trabajo activa a Markdown, pase**[Guardar formato.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** como segundo parámetro de**[Libro de trabajo.Guardar](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)** método. También puedes usar**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)** clase para especificar configuraciones adicionales para exportar la hoja de trabajo a Markdown.

 El siguiente ejemplo de código demuestra la exportación de la hoja de trabajo activa a Markdown mediante el uso**[SaveFormat.MARKDOWN](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)** miembro de enumeración. Por favor vea el[salida del archivo Markdown](md_sample.txt)generado por el código como referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Markdown-1.py" >}}

##  **Convertir libro de Excel a JSON**

Aspose.Cells for Python via .NET admite la conversión de un libro de trabajo a un archivo Json (notación de objetos JavaScript).

El siguiente ejemplo de código demuestra la exportación de una hoja de trabajo activa a Json mediante el uso[**Guardar formato.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) miembro de enumeración. Por favor vea el código para convertir[archivo fuente](Book1.xlsx) hacia[archivo Json de salida](Book1.Json)generado por el código como referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

##  **Convertir Excel a XML**
Aspose.Cells for Python via .NET admite la conversión de un libro a hoja de cálculo XML de Excel 2003 y datos XML simples.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XML.py" >}}

##  **Convertir libro de Excel a TIFF**
Aspose.Cells for Python via .NET admite la conversión de un libro de trabajo a un archivo TIFF.

El siguiente fragmento de código muestra cómo convertir Excel a TIFF:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-TIFF.py" >}}

##  **Convertir libro de Excel a DOCX**

Aspose.Cells for Python via .NET API proporciona soporte para convertir hojas de cálculo al formato DOCX. Para exportar el libro a DOCX, pase[**Guardar formato.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) como segundo parámetro de[**Libro de trabajo.guardar**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions) método. También puedes usar[**Opciones de DocxSave**](https://reference.aspose.com/cells/python-net/aspose.cells/docxsaveoptions/) clase para especificar configuraciones adicionales para exportar la hoja de trabajo a DOCX.

 El siguiente ejemplo de código demuestra la exportación de la hoja de trabajo activa a DOCX mediante el uso[**Guardar formato.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) miembro de enumeración. Por favor vea el[salida del archivo DOCX](Book1.docx)generado por el código como referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Docx-1.py" >}}

##  **Convertir libro de Excel a PPTX**

Aspose.Cells for Python via .NET API proporciona soporte para convertir hojas de cálculo al formato PPTX. Para exportar el libro a PPTX, pase[**Guardar formato.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) como segundo parámetro de[**Libro de trabajo.guardar**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions) método. También puedes usar[**PptxGuardarOpciones**](https://reference.aspose.com/cells/python-net/aspose.cells/pptxsaveoptions) clase para especificar configuraciones adicionales para exportar la hoja de trabajo a PPTX.

 El siguiente ejemplo de código demuestra la exportación de la hoja de trabajo activa a PPTX mediante el uso[**Guardar formato.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) miembro de enumeración. Por favor vea el[salida del archivo PPTX](Book1.pptx)generado por el código como referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-File-To-Pptx-1.py" >}}

##  **Temas avanzados**
- [json](/cells/es/python-net/convert-workbook-to-json/)
- [Pdf](/cells/es/python-net/convert-excel-to-pdf/)
- [Convertir CSV, TSV y TXT a Excel](/cells/es/python-net/convert-csv-tsv-and-txt-to-excel/)
