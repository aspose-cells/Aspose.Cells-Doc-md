---
title: Guardar archivos de Excel en CSV, PDF y otros formatos
linktitle: Guardar archivos
type: docs
weight: 20
url: /es/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells** permite a los desarrolladores crear archivos de Excel desde cero utilizando su flexible API. Una vez que cree archivos de Excel, también necesitará guardar su libro de trabajo (archivo). Aspose.Cells proporciona una variedad de formas de guardar estos archivos. En este tema, discutiremos todas las formas posibles que los desarrolladores pueden adoptar para guardar sus archivos.

{{% /alert %}}

## **Diferentes formas de guardar sus archivos**

 Aspose.Cells API proporciona una clase denominada[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)que representa un archivo de Excel y proporciona todas las propiedades y métodos necesarios que los desarrolladores pueden necesitar para trabajar con sus archivos de Excel. Él[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la clase proporciona un[**ahorrar**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) método que se utiliza para guardar archivos de Excel. Él[**ahorrar**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) tiene muchas sobrecargas que se utilizan para guardar archivos de Excel de diferentes maneras.

 Los desarrolladores también pueden especificar el formato de archivo en el que deben guardarse sus archivos. Los archivos se pueden guardar en varios formatos, como XLS, SpreadsheetML, CSV, delimitado por tabuladores, valores separados por tabuladores TSV, XPS y muchos más. Estos formatos de archivo se especifican utilizando el[**Guardar formato**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumeración.

[**Guardar formato**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)La enumeración contiene muchos formatos de archivo predefinidos (que usted puede elegir) de la siguiente manera:

|**Tipos de formato de archivo**|**Descripción**|
|:- |:- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API intenta detectar el formato apropiado desde la extensión de archivo especificada en el primer parámetro hasta el método de guardar|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Representa un archivo CSV|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Representa un archivo Office Open XML SpreadsheetML|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Representa el archivo XLSM basado en XML|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Representa un archivo de plantilla de Excel|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Representa un archivo de plantilla habilitado para macros de Excel|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Representa un archivo Excel XLAM|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Representa un archivo de valores separados por tabulaciones|
|[**DELIMITADO POR TABULACIONES**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Representa un archivo de texto delimitado por tabulaciones|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Representa un archivo(s) HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Representa un archivo(s) MHTML|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Representa un archivo de hoja de cálculo de OpenDocument|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Representa un archivo XLS que es el formato predeterminado para las revisiones de Excel 1997 a 2003|
|[**HOJA DE CALCULO_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Representa un archivo SpreadSheetML|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Representa un archivo binario XLSB de Excel 2007|
|[**DESCONOCIDO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Representa un formato no reconocido, no se puede guardar.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Representa un documento PDF|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Representa un archivo de especificación de papel XML (XPS)|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Representa un archivo de formato de archivo de imagen etiquetado (TIFF)|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Representa un archivo de gráficos vectoriales escalables basado en XML (SVG)|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Representa el formato de intercambio de datos.|
|[**NÚMEROS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Representa un archivo de números.|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Representa un documento de descuento.|
**Normalmente, hay dos formas de guardar archivos de Excel de la siguiente manera:**

1. **Guardar el archivo en alguna ubicación**
1. **Guardar el archivo en una secuencia**

## **Guardar archivo en alguna ubicación**

Si los desarrolladores necesitan guardar sus archivos en alguna ubicación de almacenamiento, simplemente pueden especificar el nombre del archivo (con su ruta de almacenamiento completa) y el formato de archivo deseado (usando el[**Guardar formato**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumeración) mientras llama al[**ahorrar**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) método de[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)objeto.

**Ejemplo:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Guardar libro de trabajo en formato de texto o CSV**

A veces, desea convertir o guardar un libro de trabajo con varias hojas de trabajo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), de forma predeterminada, tanto Microsoft Excel como Aspose.Cells guardan solo el contenido de la hoja de trabajo activa.

El siguiente ejemplo de código explica cómo guardar un libro completo en formato de texto. Cargue el libro de origen, que podría ser cualquier archivo de hoja de cálculo de Excel u OpenOffice Microsoft (por ejemplo, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puede modificar el mismo ejemplo para guardar su archivo en CSV. De forma predeterminada,[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) es una coma, así que no especifique un separador si guarda en formato CSV.

**Ejemplo:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Guardar archivos de texto con separador personalizado**

Los archivos de texto contienen datos de hojas de cálculo sin formato. El archivo es una especie de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Guardar archivo en una secuencia**

 Si los desarrolladores necesitan guardar sus archivos en un**Arroyo** entonces deben crear un**FileOutputStream** objeto y luego guarde el archivo en ese**Arroyo** objeto llamando al[**ahorrar**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) método de[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) objeto. Los desarrolladores también pueden especificar el formato de archivo deseado (usando el[**Guardar formato**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumeración) mientras llama al[**ahorrar**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) método.

**Ejemplo:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Guardar archivo en otro formato**

### **XLS archivos**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX archivos**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF archivos**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Establecer la opción ContentCopyForAccessibility**

 Con el[**PdfGuardarOpciones**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) clase, puede obtener o configurar el PDF[**AccesibilidadExtraerContenido**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent)opción para controlar el acceso al contenido en el PDF convertido. Significa que permite que el software del lector de pantalla utilice el texto dentro del archivo PDF para leer el archivo PDF. Puede desactivarlo aplicando una contraseña de cambio de permisos y anulando la selección de los dos elementos en la captura de pantalla[aquí](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Exportar propiedades personalizadas al PDF**

Con el[**PdfGuardarOpciones**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) clase, puede exportar las propiedades personalizadas en el libro de origen al PDF.[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) El enumerador se proporciona para especificar la forma en que se exportan las propiedades. Estas propiedades se pueden observar en Adobe Acrobat Reader haciendo clic en Archivo y luego en la opción de propiedades como se muestra en la siguiente imagen. Se puede descargar el archivo de plantilla "sourceWithCustProps.xlsx"[aquí](sourceWithCustProps.xlsx)para pruebas y salida PDF el archivo "outSourceWithCustProps" está disponible[aquí](outSourceWithCustProps.pdf)para analizar.

![todo:imagen_alternativa_texto](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Convertir libro de Excel a Markdown**

El Aspose.Cells API brinda soporte para exportar hojas de cálculo al formato Markdown. Para exportar la hoja de trabajo activa a Markdown, pase[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)como segundo parámetro de[**Libro de trabajo.Guardar**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) método. También puede usar[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)class para especificar configuraciones adicionales para exportar la hoja de trabajo a Markdown.

El siguiente ejemplo de código muestra cómo exportar una hoja de trabajo activa a Markdown usando[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)miembro de la enumeración. Por favor vea el[salida de archivo Markdown](Book1.txt)generado por el código como referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Temas avanzados**
- [Ajustar el nivel de compresión del libro](/cells/es/java/adjust-workbook-compression-level/)
- [Conversión de libros de trabajo a diferentes formatos](/cells/es/java/converting-workbook-to-different-formats/)
- [Guardar libro de trabajo en formato de hoja de cálculo XML abierto estricto](/cells/es/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Seguimiento del progreso de conversión de Excel a TIFF](/cells/es/java/track-conversion-progress-of-excel-to-tiff/)
- [Seguimiento del progreso de la conversión de documentos](/cells/es/java/track-document-conversion-progress/)
