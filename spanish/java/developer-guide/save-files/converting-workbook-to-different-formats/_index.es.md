---
title: Convertir libro de trabajo a diferentes formatos
type: docs
weight: 20
url: /es/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión entre muchos formatos. Técnicamente, la conversión significa cargar un libro de trabajo en un formato de archivo y guardarlo en otro.

{{% /alert %}}

## **Convertir Excel a XPS**

El formato de documento XPS consiste en marcado XML estructurado que define el diseño de un documento y la apariencia visual de cada página, junto con reglas de representación para distribuir, archivar, representar, procesar e imprimir documentos.

El lenguaje de marcado para XPS es un subconjunto de XAML que le permite incorporar elementos gráficos vectoriales en documentos, utilizando XAML para marcar los elementos primitivos de Windows Presentation Foundation (WPF). Los elementos utilizados se describen en términos de rutas y otros elementos geométricos.

Un archivo XPS es en realidad un archivo ZIP codificado en Unicode que utiliza las Convenciones de Empaquetado Abierto, y contiene los archivos que conforman el documento. Estos incluyen un archivo de marcado XML para cada página, texto, fuentes incrustadas, imágenes de mapa de bits, gráficos vectoriales 2D, así como la información de administración de derechos digitales. El contenido de un archivo XPS se puede examinar simplemente abriéndolo en una aplicación que admite archivos ZIP.

Desde Aspose.Cells 6.0.0, se admite la conversión de Microsoft Excel a XPS.

### **Convertir una sola hoja de cálculo a XPS**

El siguiente ejemplo muestra cómo convertir una sola hoja de cálculo en un archivo de Excel a XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Exportar el libro completo a XPS**

El siguiente ejemplo muestra cómo convertir todo el libro a formato XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Conversión rápida de Excel a XPS**

El siguiente ejemplo muestra una forma sencilla de convertir directamente un archivo de Excel a formato XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Convertir Excel a archivos MHTML**

[**MHTML**](https://en.wikipedia.org/wiki/MHTML) combina HTML normal con recursos externos; es decir, contenido que generalmente se vincula como imágenes, animaciones, audio, etc., en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.

{{% alert color="primary" %}}

Aspose.Cells admite la lectura y escritura de archivos MHTML.

{{% /alert %}}

Convertir una hoja de cálculo a MHTML es una operación rápida, como se muestra a continuación.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Convertir archivos de Excel a HTML**

Las API de Aspose.Cells brindan soporte para exportar hojas de cálculo a formato HTML. Para este propósito, Aspose.Cells utiliza la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) que permite a los desarrolladores controlar varios aspectos de la salida HTML.

El siguiente código demuestra cómo utilizar la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) para exportar archivos de Microsoft Excel a formato HTML sin especificar parámetros adicionales.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

Puede lograr los mismos resultados pasando el [**SaveFormat.HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML) al método [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-).

{{% /alert %}}

### **Configuración de preferencias de imagen para HTML**

A partir de la versión 8.0.2, Aspose.Cells ha expuesto [**ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) para la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions), lo que permite a los desarrolladores especificar preferencias de imagen al guardar hojas de cálculo en formato HTML.

Las configuraciones de imagen que se pueden aplicar son:

- [**ImageType**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType): Obtiene o establece el tipo de imagen. Tenga en cuenta que todas las formas, incluidos los gráficos, se representan como imágenes en la salida HTML.
- [**Quality**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality): Obtiene o establece la calidad de las imágenes entre 0 y 100, cuando se especifica ImageFormat como Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution): Obtiene o establece la resolución vertical de la imagen en puntos por pulgada.
- [**HorizontalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution): Obtiene o establece la resolución horizontal de la imagen en puntos por pulgada.
- [**TiffCompression**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression): Obtiene o establece el tipo de compresión para las imágenes cuando se especifica ImageFormat como Tiff.
- [**Transparent**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent): Indica si el fondo de una imagen debe ser transparente cuando se especifica ImageFormat como Png.

El código a continuación demuestra cómo usar [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) para especificar diferentes preferencias.

|**Vista de la hoja de cálculo antes de exportar**|**Vista HTML después de la exportación**|
| :- | :- |
|![Vista de la hoja de cálculo antes de exportar](converting-workbook-to-different-formats_1.png)|![Vista HTML después de la exportación](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Convirtiendo Excel a Archivos PDF**

Los documentos PDF son ampliamente utilizados como formato estándar para el intercambio de documentos entre organizaciones, sectores gubernamentales e individuos. A menudo se pide a los desarrolladores de software que diseñen una forma de convertir fácilmente los archivos de Microsoft Excel en documentos PDF. Aspose.Cells admite estas funciones. Este artículo muestra cómo hacerlo.

### **Convirtiendo Excel a PDF**

La conversión de Microsoft Excel a PDF se introdujo con Aspose.Cells for Java 2.3.0. A partir de ese lanzamiento, Aspose.Cells puede [convertir hojas de cálculo a PDF directamente](#direct-conversion) (incluido [PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), sin necesidad de otro producto. Para convertir hojas de cálculo con versiones anteriores de Aspose.Cells, [utilice Aspose.PDF para la conversión](#conversion-with-asposepdf-asposecells-prior-to-230).

Aspose.Cells convierte hojas de cálculo a PDF con un alto grado de precisión y fidelidad. Sin embargo, hay algunas [limitaciones](/cells/es/java/converting-workbook-to-different-formats/#conversion-attributes), que se enumeran al final de este artículo.

{{% alert color="primary" %}}

Aspose.Cells for Java escribe directamente la información sobre la API y el número de versión en los documentos de salida. Por ejemplo, al renderizar el Documento a PDF, Aspose.Cells for Java completa el campo de **Aplicación** con el valor 'Aspose.Cells' y el campo de **Productor de PDF** con un valor, por ejemplo 'Aspose.Cells for Java v17.9'.

Tenga en cuenta que no puede instruir a Aspose.Cells for Java para cambiar o eliminar esta información de los Documentos de salida.

{{% /alert %}}

#### **Conversión Directa**

Guarde un archivo de Excel directamente en PDF utilizando el método [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-), y proporcione el miembro de interfaz [**SaveFormat.PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF). La conversión directa como esta es el método de conversión más eficiente. No pierde datos ni formato, pero mantiene el PDF de salida parecido al archivo de Excel de entrada.

Para especificar opciones de seguridad al guardar en PDF, use [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Conversión Avanzada**

También puede optar por usar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) para establecer diferentes atributos para la conversión. El establecimiento de diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) le dará control sobre la configuración de Impresión, Fuente, Seguridad y Compresión para el archivo PDF resultante. La propiedad más notable es [**Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) que le permite guardar los archivos de Excel como archivos PDF/A compatibles.

##### **Guardando Hojas de Cálculo de Excel en Archivos PDF/A Compilados**

A continuación se proporciona un fragmento de código que demuestra el uso de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) para guardar los archivos de Excel en PDF/A compatible formato PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Conversión con Aspose.Pdf: Aspose.Cells antes de la versión 2.3.0**

Para versiones de Aspose.Cells anteriores a la versión 2.3.0, necesitas usar un componente como [Aspose.PDF para Java](/pdf/java/) para convertir hojas de cálculo a archivos PDF. Aspose.Cells y Aspose.PDF trabajan juntos para convertir una hoja de cálculo a PDF a través de un paso intermedio.

Para convertir hojas de cálculo a PDF con Aspose.Cells y Aspose.PDF:

1. Instancia un objeto de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) llamando a su constructor vacío.
1. Realiza el trabajo deseado en la hoja de cálculo utilizando la API de Aspose.Cells.
1. Llama al método [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-) para guardar la hoja de cálculo:
   1. Establece el formato de archivo a XML.
   1. Selecciona Aspose_Pdf (un valor predefinido) de la interfaz FileFormatType. Esto dirige al método de guardado a generar una hoja de cálculo en forma XML compatible con el Esquema Aspose.PDF para que Aspose.PDF para Java pueda luego generar un documento PDF.
1. Cuando se haya creado el archivo XML, crea un objeto de la clase Pdf en el paquete aspose.pdf.
1. Llama al método bindXML de la clase Pdf y pasa el nombre del archivo XML de salida.
1. Llama al método save de la clase Pdf para generar el documento PDF.

Los pasos anteriores se implementan a continuación en un ejemplo.

{{% alert color="primary" %}}

Si tu hoja de cálculo contiene fórmulas, es mejor llamar al método [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) justo antes de renderizar la hoja de cálculo en formato PDF. Hacerlo garantizará que los valores dependientes de la fórmula sean recalculados y que se muestren los valores correctos en el PDF.

{{% /alert %}}

#### **Atributos de Conversión**

Trabajamos duro para mejorar la conversión y otros aspectos de Aspose.Cells con cada lanzamiento. La conversión de Excel a PDF tiene algunas limitaciones. Algunos ajustes de formato especificados en una hoja de cálculo pueden perderse, y no todos los objetos de dibujo son compatibles.

La tabla a continuación enumera todas las características que son completamente o parcialmente compatibles al exportar a PDF utilizando Aspose.Cells. Esta tabla no es definitiva y no cubre todos los atributos de la hoja de cálculo. También puede identificar aquellas características que pueden no ser compatibles o que son parcialmente compatibles para la conversión.

{{% alert color="primary" %}}

|Elemento del Documento|Atributo|Neto Compatible|Notas|
| :- | :- | :- | :- |
|Alineación| |Sí| |
|Rotación| |Parcialmente| Solo admite 90 y -90.|
|Configuraciones de fondo| |Sí| |
|Borde|Color|Sí| |
|Borde|Estilo de línea|Sí| |
|Borde|Ancho de línea|Sí| |
|Datos de celda| |Sí| |
|Comentarios| |No| |
|Formato condicional| |Sí| |
|Propiedades del documento| |Sí| |
|Objetos de dibujo| |Sí| |
|Fuente|Tamaño|Sí| |
|Fuente|Color|Sí| |
|Fuente|Estilo|Sí| |
|Fuente|Subrayado|Sí| |
|Fuente|Efectos|Parcialmente|Solo se admite el efecto de tachado|
|Imágenes| |Sí| |
|Hipervínculo| |Sí| |
|Gráficos| |Sí| |
|Celdas fusionadas| |Sí| |
|Salto de página| |Sí| |
|Configuración de página|Encabezado/Pie de página|Sí| |
|Configuración de página|Márgenes|Sí| |
|Configuración de página|Orientación de la página|Sí| |
|Configuración de página|Tamaño de la página|Sí| |
|Configuración de página|Área de impresión|Sí| |
|Configuración de página|Títulos de impresión|Sí| |
|Configuración de página|Escalado|Sí| |
|Altura de fila/Ancho de columna| |Sí| |
{{% /alert %}}
{{< app/cells/assistant language="java" >}}
