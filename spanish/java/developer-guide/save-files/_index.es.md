---
title: Guardar archivos Excel en formato CSV, PDF y otros formatos
linktitle: Guardar archivos
type: docs
weight: 20
url: /es/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** permite a los desarrolladores crear archivos de Excel desde cero utilizando su API flexible. Una vez que se crean los archivos de Excel, también es necesario guardar su libro de trabajo (archivo). Aspose.Cells proporciona una variedad de formas de guardar estos archivos. En este tema, discutiremos todas esas posibles formas que pueden ser adoptadas por los desarrolladores para guardar sus archivos.

{{% /alert %}}

## **Diferentes formas de guardar tus archivos**

La API de Aspose.Cells proporciona una clase llamada [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que representa un archivo de Excel y proporciona todas las propiedades y métodos necesarios que los desarrolladores puedan necesitar para trabajar con sus archivos de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) proporciona un método [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) que se utiliza para guardar archivos de Excel. El método [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) tiene muchas sobrecargas que se utilizan para guardar archivos de Excel de diferentes maneras.

Los desarrolladores también pueden especificar el formato de archivo en el que deben guardarse sus archivos. Los archivos se pueden guardar en varios formatos como XLS, SpreadsheetML, CSV, Delimitado por tabulaciones, Valores separados por tabulaciones TSV, XPS y muchos más. Estos formatos de archivo se especifican utilizando la enumeración [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat).

La enumeración [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) contiene muchos formatos de archivo predefinidos (que pueden ser elegidos por usted) de la siguiente manera:

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|La API intenta detectar el formato apropiado a partir de la extensión de archivo especificada en el primer parámetro del método de guardado.
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Representa un archivo CSV.
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Representa un archivo de Office Open XML SpreadsheetML|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Representa un archivo XLSM basado en XML|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Representa un archivo de plantilla de Excel|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Representa un archivo de plantilla habilitado para macros de Excel|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Representa un archivo XLAM de Excel|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Representa un archivo de valores separados por tabulaciones|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Representa un archivo de texto delimitado por tabulaciones|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Representa un archivo HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Representa un archivo MHTML|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Representa un archivo de hoja de cálculo de OpenDocument|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Representa un archivo XLS que es el formato predeterminado para las revisiones de Excel 1997 a 2003|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Representa un archivo de SpreadSheetML|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Representa un archivo XLSB binario de Excel 2007|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Representa un formato no reconocido, no se puede guardar|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Representa un documento PDF|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Representa un archivo de especificación de papel XML (XPS)|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Representa un archivo TIFF (Tagged Image File Format)|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Representa un archivo SVG (Scalable Vector Graphics) basado en XML|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Representa un formato de intercambio de datos|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Representa un archivo de números|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Representa un documento de markdown.
**Normalmente, hay dos formas de guardar archivos de Excel de la siguiente manera:**

1. **Guardar el archivo en alguna ubicación**
1. **Guardar el archivo en un flujo (stream)**

## **Guardar archivo en alguna ubicación**

Si los desarrolladores necesitan guardar sus archivos en alguna ubicación de almacenamiento, pueden simplemente especificar el nombre del archivo (con su ruta de almacenamiento completa) y el formato de archivo deseado (usando la enumeración [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) al llamar al método [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) del objeto [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook).

**Ejemplo:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Guardar libro de trabajo en formato de texto o CSV**

A veces, es posible que desee convertir o guardar un libro de trabajo con varias hojas de cálculo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), tanto Microsoft Excel como Aspose.Cells guardan por defecto el contenido de la hoja de cálculo activa únicamente.

El siguiente ejemplo de código explica cómo guardar un libro de trabajo completo en formato de texto. Cargue el libro de trabajo fuente que podría ser cualquier archivo de hoja de cálculo de Microsoft Excel u OpenOffice (por ejemplo, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando el código se ejecuta, convierte los datos de todas las hojas en el libro de trabajo al formato TXT.

Puedes modificar el mismo ejemplo para guardar tu archivo en CSV. Por defecto, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) es una coma, así que no especifiques un separador al guardar en formato CSV. Ten en cuenta: Si estás usando la versión de evaluación e incluso si el parámetro del método [**TxtSaveOptions.setExportAllSheets(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions/#setExportAllSheets-boolean-) está configurado en true, el programa seguirá exportando solo una hoja de trabajo.

**Ejemplo:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Guardar archivos de texto con separador personalizado**

Los archivos de texto contienen datos de la hoja de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Guardar archivo en un flujo (stream)**

Si los desarrolladores necesitan guardar sus archivos en un **Flujo (Stream)**, deberían crear un objeto **FileOutputStream** y luego guardar el archivo en ese objeto **Flujo (Stream)** llamando al método [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) del objeto [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Los desarrolladores también pueden especificar el formato de archivo deseado (usando la enumeración [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) al llamar al método [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)).

**Ejemplo:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Guardar archivo en otro formato**

### **Archivos XLS**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **Archivos XLSX**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **Archivos PDF**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Establecer la opción ContentCopyForAccessibility**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions), puedes obtener o establecer la opción de PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) para controlar el acceso al contenido en el PDF convertido. Esto significa que permite que el software de lectura de pantalla utilice el texto dentro del archivo PDF para leerlo. Puedes desactivarlo aplicando una contraseña para cambiar permisos y deseleccionando los dos elementos en la captura de pantalla [aquí](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Exportar Propiedades Personalizadas a PDF**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions), puedes exportar las propiedades personalizadas en la hoja de cálculo fuente al PDF. Se proporciona un enumerador [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) para especificar la forma en que se exportan las propiedades. Estas propiedades se pueden ver en Adobe Acrobat Reader haciendo clic en Archivo y luego en la opción de propiedades como se muestra en la siguiente imagen. El archivo de plantilla "sourceWithCustProps.xlsx" se puede descargar [aquí](sourceWithCustProps.xlsx) para probarlo y el archivo PDF de salida "outSourceWithCustProps" está disponible [aquí](outSourceWithCustProps.pdf) para el análisis.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Convertir Libro de Excel a Markdown**

La API de Aspose.Cells brinda soporte para exportar hojas de cálculo al formato Markdown. Para exportar la hoja de cálculo activa a Markdown, pasa [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) como segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)). También puedes usar la clase [**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions) para especificar configuraciones adicionales para exportar la hoja de cálculo a Markdown.

El siguiente ejemplo de código muestra cómo exportar la hoja de cálculo activa a Markdown utilizando el miembro de enumeración [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN). Consulta el [archivo de Markdown de salida](Book1.txt) generado por el código como referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Temas avanzados**
- [Ajustar el nivel de compresión del libro de trabajo](/cells/es/java/adjust-workbook-compression-level/)
- [Convertir Libro de Trabajo a Diferentes Formatos](/cells/es/java/converting-workbook-to-different-formats/)
- [Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto](/cells/es/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Seguir el progreso de conversión de Excel a TIFF](/cells/es/java/track-conversion-progress-of-excel-to-tiff/)
- [Seguimiento del progreso de conversión de documentos](/cells/es/java/track-document-conversion-progress/)
