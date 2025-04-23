---
title: Apertura de archivos con diferentes formatos
linktitle: Abrir archivos
type: docs
weight: 10
url: /es/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

Los desarrolladores utilizan Aspose.Cells para abrir archivos con diferentes propósitos. Por ejemplo, abrir un archivo para recuperar datos de él, o utilizar un archivo de hoja de cálculo predefinido para acelerar el proceso de desarrollo. Aspose.Cells permite a los desarrolladores abrir diferentes tipos de archivos fuente. Estos archivos fuente pueden ser informes de Microsoft Excel, SpreadsheetML, valores separados por comas (CSV), archivos delimitados por tabulaciones (TSV). Este artículo trata sobre la apertura de estos diferentes archivos fuente utilizando Aspose.Cells.

Si necesitas conocer todos los formatos de archivo admitidos, consulta las siguientes páginas:
[Formatos de archivo admitidos](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Formas sencillas de abrir archivos de Excel**

### **Apertura a través de la Ruta**

Para abrir un archivo de Microsoft Excel utilizando la ruta del archivo, pase la ruta del archivo como parámetro al crear la instancia de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). El siguiente código de ejemplo demuestra la apertura de un archivo de Excel utilizando la ruta del archivo.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Apertura a través de un flujo**

A veces, el archivo de Excel que desea abrir se almacena como un flujo. En ese caso, de manera similar a la apertura de un archivo utilizando la ruta del archivo, pase el flujo como parámetro al instanciar la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). El siguiente código de ejemplo demuestra la apertura de un archivo de Excel utilizando un flujo.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Apertura de archivos de diferentes versiones de Microsoft Excel**

El usuario puede usar la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) para especificar el formato del archivo de Excel utilizando la enumeración [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

La enumeración [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) contiene muchos formatos de archivo predefinidos, algunos de los cuales se muestran a continuación.

| **Tipos de formato** | **Descripción** |
| :- | :- |
|Csv|Representa un archivo CSV|
|Excel97To2003|Representa un archivo de Excel 97 - 2003|
|Xlsx|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|Xlsm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|Xltx|Representa una plantilla de Excel 2007/2010/2013/2016/2019 y Office 365 XLTX|
|Xltm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 habilitado para macros XLTM|
|Xlsb|Representa un archivo binario XLSB de Excel 2007/2010/2013/2016/2019 y Office 365|
|SpreadsheetML|Representa un archivo de SpreadsheetML|
|Tsv|Representa un archivo de valores separados por tabulaciones|
|TabDelimited|Representa un archivo de texto delimitado por tabulaciones|
|Ods|Representa un archivo ODS|
|Html|Representa un archivo HTML|
|Mhtml|Representa un archivo MHTML|

### **Apertura de archivos de Microsoft Excel 95/5.0**

Para abrir archivos de Microsoft Excel 95, instancie la instancia [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) con la ruta o el flujo del archivo de plantilla. El archivo de muestra para probar el código se puede descargar desde el siguiente enlace:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Apertura de archivos de Microsoft Excel 97 o versiones posteriores XLS**

Para abrir archivos XLS de Microsoft Excel XLS de las versiones 97 o posteriores, instancie la instancia [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) con la ruta o el flujo del archivo de plantilla. O utilice el método [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y seleccione el valor [**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL-97-TO-2003) en la enumeración [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Apertura de archivos XLSX de Microsoft Excel 2007 o versiones posteriores**

Para abrir archivos XLSX de Microsoft Excel 2007 o versiones posteriores, instancie la instancia [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) con la ruta o el flujo del archivo de plantilla. O utilice la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y seleccione el valor [**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX) en la enumeración [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Abriendo Archivos con Diferentes Formatos**

Aspose.Cells permite a los desarrolladores abrir archivos de hojas de cálculo con diferentes formatos, como SpreadsheetML, CSV, archivos delimitados por tabuladores. Para abrir dichos archivos, los desarrolladores pueden usar la misma metodología que utilizan para abrir archivos de diferentes versiones de Microsoft Excel.

### **Abriendo Archivos de SpreadsheetML**

Los archivos de SpreadsheetML son las representaciones XML de sus hojas de cálculo, incluyendo toda la información sobre la hoja de cálculo, como el formato, las fórmulas, etc. Desde Microsoft Excel XP, se añadió una opción de exportación XML a Microsoft Excel que exporta sus hojas de cálculo a archivos de SpreadsheetML.

Para abrir archivos de SpreadsheetML, use la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y seleccione el valor [**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET-ML) en la enumeración [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Abriendo Archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros cuyos valores están delimitados o separados por comas. En los archivos CSV, los datos se almacenan en un formato tabular que tiene campos separados por el carácter de coma y entrecomillados por el carácter de comillas dobles. Si el valor de un campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puede usar Microsoft Excel para exportar los datos de su hoja de cálculo a un archivo CSV.

Para abrir archivos CSV, use la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y seleccione el valor [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), predefinido en la enumeración [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Abriendo Archivos CSV y reemplazando caracteres inválidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, estos se reemplazan automáticamente. Lo mismo hace la API de Aspose.Cells, que se muestra en el ejemplo de código que se muestra a continuación.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Apertura de archivos CSV utilizando un analizador preferido**

No siempre es necesario utilizar la configuración de analizador predeterminada para abrir los archivos CSV. A veces, la importación de un archivo CSV no crea la salida esperada, como el formato de fecha no es el esperado o los campos vacíos se manejan de manera diferente. Con este fin, [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) está disponible para proporcionar su propio analizador preferido para analizar diferentes tipos de datos según el requisito. El siguiente código de ejemplo demuestra el uso del analizador preferido.  

Se pueden descargar los archivos fuente de muestra y los archivos de salida de las siguientes conexiones para probar esta función.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Apertura de archivos TSV (delimitados por tabuladores)**

Los archivos delimitados por tabuladores contienen datos de hojas de cálculo pero sin ningún formato. Los datos están organizados en filas y columnas, como tablas y hojas de cálculo. En resumen, un archivo delimitado por tabuladores es un tipo especial de archivo de texto sin formato con una pestaña entre cada columna en el texto.

Para abrir archivos delimitados por tabuladores, los desarrolladores deben usar la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y seleccionar el valor [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), predefinido en la enumeración [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Apertura de archivos de Excel encriptados**

Sabemos que es posible crear archivos de Excel encriptados utilizando Microsoft Excel. Para abrir tales archivos encriptados, los desarrolladores deben llamar a un método LoadOptions sobrecargado y seleccionar el valor DEFAULT, predefinido en la enumeración FileFormatType. Este método también tomaría la contraseña del archivo encriptado como se muestra a continuación en el ejemplo.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells también admite la apertura de archivos de MS Excel 2013 protegidos por contraseña.

{{% alert color="primary" %}}

Existe la posibilidad de que el constructor de Workbook pueda generar System.OutOfMemoryException al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo debe cargarse habilitando las [Preferencias de memoria](/cells/es/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Apertura de archivos SXC**

StarOffice Calc es similar a Microsoft Excel y admite fórmulas, gráficos, funciones y macros. Las hojas de cálculo creadas con este software se guardan con la extensión SXC. El archivo SXC también se utiliza para los archivos de hojas de cálculo de OpenOffice.org Calc. Aspose.Cells puede leer archivos SXC como se muestra en el siguiente ejemplo de código.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Apertura de archivos FODS**

El archivo FODS es una hoja de cálculo guardada en OpenDocument XML sin compresión. Aspose.Cells puede leer archivos FODS como se muestra en el siguiente ejemplo de código.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Temas avanzados**
- [Filtrar nombres definidos al cargar el libro de trabajo](/cells/es/java/filter-defined-names-while-loading-workbook/)
- [Filtrar objetos al cargar el libro de trabajo o de la hoja de cálculo](/cells/es/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Obtener advertencias al cargar archivo de Excel](/cells/es/java/get-warnings-while-loading-excel-file/)
- [Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV](/cells/es/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Cargar libro de trabajo con tamaño de papel de impresora especificado](/cells/es/java/load-workbook-with-specified-printer-paper-size/)
- [Abrir archivos de diferentes versiones de Microsoft Excel](/cells/es/java/opening-different-microsoft-excel-versions-files/)
- [Optimización del uso de memoria al trabajar con archivos grandes que contengan conjuntos de datos extensos](/cells/es/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Leer Hojas de cálculo Numbers desarrolladas por Apple Inc. usando Aspose.Cells](/cells/es/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Lectura de archivo CSV con múltiples codificaciones](/cells/es/java/reading-csv-file-with-multiple-encodings/)
- [Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado](/cells/es/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Usar la API LightCells](/cells/es/java/using-lightcells-api/)
{{< app/cells/assistant language="java" >}}
