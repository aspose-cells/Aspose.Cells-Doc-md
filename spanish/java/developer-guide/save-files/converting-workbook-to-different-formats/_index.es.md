---
title: Conversión de libros de trabajo a diferentes formatos
type: docs
weight: 20
url: /es/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells admite la conversión entre muchos formatos. Técnicamente, la conversión significa cargar un libro de trabajo en un formato de archivo y guardarlo en otro.

{{% /alert %}}

## **Conversión de Excel a XPS**

El formato de documento XPS consta de marcado XML estructurado que define el diseño de un documento y la apariencia visual de cada página, junto con reglas de representación para distribuir, archivar, representar, procesar e imprimir documentos.

El lenguaje de marcado para XPS es un subconjunto de XAML que le permite incorporar elementos gráficos vectoriales en documentos, utilizando XAML para marcar las primitivas Windows Presentation Foundation (WPF). Los elementos utilizados se describen en términos de caminos y otras primitivas geométricas.

Un archivo XPS es, de hecho, un archivo ZIP Unicodificado que utiliza las convenciones de empaquetado abierto y contiene los archivos que componen el documento. Estos incluyen un archivo de marcado XML para cada página, texto, fuentes incrustadas, imágenes rasterizadas, gráficos vectoriales 2D, así como la información de gestión de derechos digitales. El contenido de un archivo XPS se puede examinar simplemente abriéndolo en una aplicación que admita archivos ZIP.

Desde Aspose.Cells 6.0.0, Microsoft se admite la conversión de Excel a XPS.

### **Conversión de una sola hoja de trabajo a XPS**

El siguiente ejemplo muestra cómo convertir una sola hoja de trabajo en un archivo de Excel a XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Exportar todo el libro de trabajo a XPS**

El siguiente ejemplo muestra cómo convertir todo el libro de trabajo al formato XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Conversión rápida de Excel a XPS**

El siguiente ejemplo muestra una forma sencilla de convertir directamente el archivo de Excel al formato XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Conversión de archivos de Excel a MHTML**

[MHTML](https://en.wikipedia.org/wiki/MHTML) combina HTML normal con recursos externos; es decir, contenido que generalmente está vinculado como imágenes, animaciones, audio, etc. en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.

{{% alert color="primary" %}}

Aspose.Cells admite la lectura y escritura de archivos MHTML.

{{% /alert %}}

Convertir una hoja de cálculo a MHTML es una operación rápida, como se muestra a continuación.

El siguiente ejemplo de código muestra cómo guardar un libro de trabajo como un archivo MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Convertir archivos de Excel a HTML**

 Las API Aspose.Cells brindan soporte para exportar hojas de cálculo a formato HTML. Para ello, Aspose.Cells utiliza el**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**clase que permite a los desarrolladores controlar varios aspectos del HTML de salida.

El siguiente código muestra cómo usar el**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**clase para exportar Microsoft archivos de Excel a formato HTML sin especificar parámetros adicionales.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

 Puede lograr los mismos resultados pasando el**[Guardar formato.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)** hacia**[Libro de trabajo.guardar](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** método.

{{% /alert %}}

### **Configuración de preferencias de imagen para HTML**

 A partir de 8.0.2, Aspose.Cells ha expuesto**[Opciones de imagen](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**Para el**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**class, que permite a los desarrolladores especificar preferencias de imagen al guardar hojas de cálculo en formato HTML.

Los ajustes de imagen que se pueden aplicar son:

- **[Tipo de imagen] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: Obtiene o establece el tipo de imagen. Tenga en cuenta que todas las formas, incluidos los gráficos, se representan como imágenes en el HTML de salida.
- **[Calidad](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: Obtiene o establece la calidad de las imágenes entre 0 y 100, cuando ImageFormat se especifica como Jpeg.
- **[Resolución vertical](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Resoluciónvertical)**: Obtiene o establece la resolución vertical de la imagen en puntos por pulgada.
- **[Resolución horizontal](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Resoluciónhorizontal)**: Obtiene o establece la resolución horizontal de la imagen en puntos por pulgada.
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**: Obtiene o establece el tipo de compresión de las imágenes cuando ImageFormat se especifica como Tiff.
- **[Transparente](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**indica si el fondo de una imagen debe ser transparente cuando ImageFormat se especifica como Png.

 El siguiente código demuestra cómo usar**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)** para especificar diferentes preferencias.

|**Vista de hoja de cálculo antes de exportar**|**Vista HTML después de la exportación**|
|:- |:- |
|![Vista de hoja de cálculo antes de exportar](converting-workbook-to-different-formats_1.png)|![Vista HTML después de la exportación](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Conversión de archivos de Excel a PDF**

Los documentos PDF se utilizan ampliamente como formato estándar para el intercambio de documentos entre organizaciones, sectores gubernamentales e individuos. A los desarrolladores de software a menudo se les pide que busquen una forma de convertir fácilmente Microsoft archivos de Excel en documentos PDF. Aspose.Cells admite estas funciones. Este artículo muestra cómo.

### **Convertir Excel a PDF**

 Microsoft La conversión de Excel a PDF se introdujo con Aspose.Cells for Java 2.3.0. A partir de ese lanzamiento, Aspose.Cells puede[convertir hojas de cálculo a PDF directamente](#direct-conversion) (incluido[PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), sin otro producto. Para convertir hojas de cálculo con versiones anteriores de Aspose.Cells,[use Aspose.PDF para la conversión](#conversion-with-asposepdf-asposecells-prior-to-230).

 Aspose.Cell convierte hojas de cálculo a PDF con un alto grado de precisión y fidelidad. Sin embargo, hay algunos[limitaciones](/cells/es/java/converting-workbook-to-different-formats/#conversion-attributes), enumerados al final de este artículo.

{{% alert color="primary" %}}

 Aspose.Cells for Java escribe directamente la información sobre API y el número de versión en los documentos de salida. Por ejemplo, al renderizar Documento a PDF, Aspose.Cells for Java se completa**Solicitud** campo con valor 'Aspose.Cells' y**Productor de PDF** campo con un valor, por ejemplo, 'Aspose.Cells for Java v17.9'.

Tenga en cuenta que no puede indicar al Aspose.Cells for Java que cambie o elimine esta información de los documentos de salida.

{{% /alert %}}

#### **Conversión Directa**

Guarde un archivo de Excel directamente en PDF usando el**[Libro de trabajo.guardar](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** método, y proporcionar el**[Guardar formato.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**miembro de la interfaz. La conversión directa como esta es el método de conversión más eficiente. No pierde datos ni formato, pero mantiene el PDF de salida con el mismo aspecto que el archivo Excel de entrada.

 Para especificar las opciones de seguridad al guardar en PDF, use**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Conversión avanzada**

También puede optar por utilizar el**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** class para establecer diferentes atributos para la conversión. Establecer diferentes propiedades de**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**class le dará el control sobre las configuraciones de Impresión, Fuente, Seguridad y Compresión para el archivo PDF resultante. La propiedad más notable es la**[Cumplimiento](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Cumplimiento)**que le permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A.

##### **Guardar hojas de cálculo de Excel en archivos compatibles con PDF/A**

El fragmento de código proporcionado a continuación demuestra el uso de la**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** class para guardar los archivos de Excel en formato PDF compatible con PDF/A.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Conversión con Aspose.Pdf: Aspose.Cells Antes de 2.3.0**

 Para las versiones Aspose.Cells anteriores a la versión 2.3.0, debe usar un componente como[Aspose.PDF for Java](/pdf/java/) para convertir hojas de cálculo a archivos PDF. Aspose.Cells y Aspose.PDF funcionan juntos para convertir una hoja de cálculo a PDF a través de un paso intermedio.

Para convertir hojas de cálculo a PDF con Aspose.Cells y Aspose.PDF:

1.  Instanciar un objeto de la**[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**clase llamando a su constructor vacío.
1. Realice el trabajo deseado en la hoja de cálculo utilizando el Aspose.Cells API.
1. Llama a**[Libro de trabajo.guardar](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**Método para guardar la hoja de cálculo:
1. Establezca el formato de archivo en XML.
 1. Seleccione Aspose_Pdf (un valor predefinido) en la interfaz FileFormatType. Esto indica al método de guardado que genere una hoja de cálculo en formato XML compatible con el esquema Aspose.PDF para que Aspose.PDF for Java pueda generar un documento PDF.
1. Cuando se haya creado el archivo XML, cree un objeto de la clase Pdf en el paquete aspose.pdf.
1. Llame al método bindXML de la clase Pdf y pase el nombre del archivo XML de salida.
1. Llame al método de guardado de la clase Pdf para generar el documento PDF.

Los pasos anteriores se implementan a continuación en un ejemplo.

{{% alert color="primary" %}}

 Si su hoja de cálculo contiene fórmulas, es mejor llamar**[Libro de trabajo.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())** justo antes de convertir la hoja de cálculo en formato PDF. Si lo hace, se asegurará de que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}

#### **Atributos de conversión**

Trabajamos duro para mejorar la conversión y otros aspectos de Aspose.Cells con cada lanzamiento. La conversión de Excel a PDF tiene algunas limitaciones. Algunas configuraciones de formato especificadas en una hoja de cálculo pueden perderse y no todos los objetos de dibujo son compatibles.

La siguiente tabla enumera todas las funciones que son total o parcialmente compatibles al exportar a PDF usando Aspose.Cells. Esta tabla no es definitiva y no cubre todos los atributos de la hoja de cálculo. También puede identificar aquellas funciones que pueden no ser compatibles o que son parcialmente compatibles con la conversión.

{{% alert color="primary" %}}

|**Elemento de documento**|**Atributo**|**Red admitida**|**notas**|
|:- |:- |:- |:- |
|Alineación||Sí||
|Rotación||Parcialmente|Solo admite 90 y -90.|
|Configuración de fondo||Sí||
|Borde|Color|Sí||
|Borde|Estilo de línea|Sí||
|Borde|Ancho de línea|Sí||
|Cell Datos||Sí||
|Comentarios||No||
|Formato condicional||Sí||
|Propiedades del documento||Sí||
|Objetos de dibujo||Sí||
|Fuente|Tamaño|Sí||
|Fuente|Color|Sí||
|Fuente|Estilo|Sí||
|Fuente|Subrayar|Sí||
|Fuente|Efectos|Parcialmente|Solo se admite el efecto de tachado|
|Imágenes||Sí||
|Hipervínculo||Sí||
|Gráficos||Sí||
|Fusionado Cells||Sí||
|Salto de página||Sí||
|Configuración de página|Encabezado/Pie de página|Sí||
|Configuración de página|Márgenes|Sí||
|Configuración de página|Orientación de la página|Sí||
|Configuración de página|Tamaño de página|Sí||
|Configuración de página|Área de impresión|Sí||
|Configuración de página|Imprimir títulos|Sí||
|Configuración de página|Escalada|Sí||
|Altura de fila/Ancho de columna||Sí||
{{% /alert %}}
