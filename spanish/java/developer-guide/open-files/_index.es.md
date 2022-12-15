---
title: Apertura de archivos con diferentes formatos
linktitle: Abrir archivos
type: docs
weight: 10
url: /es/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

Los desarrolladores usan Aspose.Cells para abrir archivos para diferentes propósitos. Por ejemplo, abra un archivo para recuperar datos o use un archivo de hoja de cálculo de diseñador predefinido para acelerar su proceso de desarrollo. Aspose.Cells permite a los desarrolladores abrir diferentes tipos de archivos fuente. Estos archivos de origen pueden ser Microsoft informes de Excel, SpreadsheetML, archivos de valores separados por comas (CSV), delimitados por tabuladores o archivos de valores separados por tabuladores (TSV). Este artículo analiza la apertura de estos diferentes archivos de origen utilizando Aspose.Cells.

Si necesita conocer todos los formatos de archivo admitidos, consulte las siguientes páginas:
[Formatos de archivo admitidos](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Maneras simples de abrir archivos de Excel**

### **Apertura a través de Camino**

Para abrir un archivo de Excel Microsoft usando la ruta del archivo, pase la ruta del archivo como parámetro mientras crea la instancia del**[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**clase. El siguiente código de ejemplo muestra cómo abrir un archivo de Excel utilizando la ruta del archivo.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Apertura a través de Stream**

A veces, el archivo de Excel que desea abrir se almacena como una secuencia. En ese caso, similar a abrir un archivo usando la ruta del archivo, pase la secuencia como un parámetro mientras crea una instancia del**[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**clase. El siguiente código de ejemplo muestra cómo abrir un archivo de Excel mediante stream.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Abrir archivos de diferentes versiones de Excel Microsoft**

 El usuario puede utilizar el**[Opciones de carga](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** clase para especificar el formato del archivo de Excel usando el**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumeración.

 los**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**La enumeración contiene muchos formatos de archivo predefinidos, algunos de los cuales se indican a continuación.

|**Tipos de formato**|**Descripción**|
|:- |:- |
|CSV|Representa un archivo CSV|
|Excel97To2003|Representa un archivo Excel 97 - 2003|
|xlsx|Representa un archivo Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|xlsm|Representa un archivo Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|xltx|Representa un archivo XLTX de plantilla de Excel 2007/2010/2013/2016/2019 y Office 365|
|xltm|Representa un archivo XLTM habilitado para macros de Excel 2007/2010/2013/2016/2019 y Office 365|
|xlsb|Representa un archivo XLSB binario de Excel 2007/2010/2013/2016/2019 y Office 365|
|Hoja de cálculoML|Representa un archivo SpreadsheetML|
|Tsv|Representa un archivo de valores separados por tabulaciones|
|Delimitado por tabulaciones|Representa un archivo de texto delimitado por tabulaciones|
|probabilidades|Representa un archivo ODS|
|html|Representa un archivo HTML|
|Mhtml|Representa un archivo MHTML|

### **Apertura de archivos Microsoft Excel 95/5.0**

 Para abrir archivos Microsoft Excel 95, cree una instancia del**[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**instancia con la ruta o secuencia del archivo de plantilla. El archivo de muestra para probar el código se puede descargar desde el siguiente enlace:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Abriendo Microsoft Excel 97 o versiones posteriores Archivos XLS**

 Para abrir archivos XLS de Microsoft Excel XLS 97 o versiones posteriores, cree una instancia del**[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** instancia con la ruta o secuencia del archivo de plantilla. O usa el**[Opciones de carga](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** método y seleccione el**[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)** valor en el**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumeración.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Abriendo Microsoft Excel 2007 o versiones posteriores Archivos XLSX**

 Para abrir archivos XLSX de Microsoft Excel 2007 o versiones posteriores, cree una instancia del**[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**instancia con la ruta o secuencia del archivo de plantilla. O usa el**[Opciones de carga](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** clase y seleccione la**[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)** valor en el**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumeración.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Apertura de archivos con diferentes formatos**

Aspose.Cells permite a los desarrolladores abrir archivos de hojas de cálculo con diferentes formatos, como SpreadsheetML, CSV, archivos delimitados por tabuladores. Para abrir dichos archivos, los desarrolladores pueden usar la misma metodología que usan para abrir archivos de diferentes versiones de Excel Microsoft.

### **Apertura de archivos de hoja de cálculo ML**

Los archivos SpreadsheetML son las representaciones XML de sus hojas de cálculo, incluida toda la información sobre la hoja de cálculo, como formato, fórmulas, etc. Desde Microsoft Excel XP, se agregó una opción de exportación XML a Microsoft Excel que exporta sus hojas de cálculo a archivos SpreadsheetML.

Para abrir archivos de SpreadsheetML, use el**[Opciones de carga](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** clase y seleccione la**[HOJA DE CALCULO_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#HOJA DE CALCULO_ML)** valor en el**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumeración.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Abrir archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros cuyos valores están delimitados o separados por comas. En los archivos CSV, los datos se almacenan en un formato tabular que tiene campos separados por comas y entre comillas dobles. Si el valor de un campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puede usar Microsoft Excel para exportar los datos de su hoja de cálculo a un archivo CSV.

Para abrir archivos CSV, use el**[Opciones de carga](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** clase y seleccione la**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** valor, predefinido en el**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumeración.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Abrir archivos CSV y reemplazar caracteres no válidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace Aspose.Cells API, que se demuestra en el ejemplo de código que se proporciona a continuación.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Abrir archivos CSV usando el analizador preferido**

Esto no siempre es necesario para usar la configuración predeterminada del analizador para abrir los archivos CSV. A veces, la importación de un archivo CSV no crea el resultado esperado, como que el formato de fecha no es el esperado o los campos vacíos se manejan de manera diferente. Para este propósito**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**está disponible para proporcionar su propio analizador preferido para analizar diferentes tipos de datos según el requisito. El siguiente código de ejemplo demuestra el uso del analizador preferido.

El archivo fuente de muestra y los archivos de salida se pueden descargar desde los siguientes enlaces para probar esta función.

[samplePreferredParser.csv](samplePreferredParser.csv)

[muestra de salidaPreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Apertura de archivos TSV (separados por tabuladores)**

Los archivos delimitados por tabuladores contienen datos de hojas de cálculo pero sin ningún formato. Los datos se organizan en filas y columnas, como tablas y hojas de cálculo. En resumen, un archivo delimitado por tabulaciones es un tipo especial de archivo de texto sin formato con una tabulación entre cada columna del texto.

Para abrir archivos delimitados por tabuladores, los desarrolladores deben usar el**[Opciones de carga](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** clase y seleccione la**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** valor, predefinido en el**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumeración.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Abrir archivos de Excel cifrados**

Sabemos que es posible crear archivos de Excel cifrados utilizando Microsoft Excel. Para abrir dichos archivos cifrados, los desarrolladores deben llamar a un método LoadOptions especial sobrecargado y seleccionar el valor DEFAULT, predefinido en la enumeración FileFormatType. Este método también tomaría la contraseña del archivo encriptado como se muestra a continuación en el ejemplo.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells también admite la apertura de archivos de MS Excel 2013 protegidos con contraseña.

{{% alert color="primary" %}}

Hay buenas posibilidades de que el constructor del libro de trabajo arroje System.OutOfMemoryException al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo debe cargarse mientras se habilita el[Preferencias de memoria](/cells/es/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Apertura de archivos SXC**

StarOffice Calc es similar a Microsoft Excel y admite fórmulas, gráficos, funciones y macros. Las hojas de cálculo creadas con este software se guardan con la extensión SXC. El archivo SXC también se usa para los archivos de hoja de cálculo de OpenOffice.org Calc. Aspose.Cells puede leer archivos SXC como se demuestra en el siguiente ejemplo de código.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Apertura de archivos FODS**

El archivo FODS es una hoja de cálculo guardada en OpenDocument XML sin compresión. Aspose.Cells puede leer archivos FODS como se demuestra en el siguiente ejemplo de código.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Temas avanzados**
- [Filtrar nombres definidos al cargar el libro de trabajo](/cells/es/java/filter-defined-names-while-loading-workbook/)
- [Filtrar objetos al cargar el libro de trabajo o la hoja de trabajo](/cells/es/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Recibe advertencias al cargar un archivo de Excel](/cells/es/java/get-warnings-while-loading-excel-file/)
- [Mantenga separadores para filas en blanco mientras exporta hojas de cálculo a formato CSV](/cells/es/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Cargar libro de trabajo con el tamaño de papel de impresora especificado](/cells/es/java/load-workbook-with-specified-printer-paper-size/)
- [Apertura de diferentes archivos de versiones de Excel Microsoft](/cells/es/java/opening-different-microsoft-excel-versions-files/)
- [Optimización del uso de la memoria mientras se trabaja con archivos grandes que tienen grandes conjuntos de datos](/cells/es/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Lea la hoja de cálculo de números desarrollada por Apple Inc. usando Aspose.Cells](/cells/es/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Lectura de archivos CSV con múltiples codificaciones](/cells/es/java/reading-csv-file-with-multiple-encodings/)
- [Detenga la conversión o la carga con InterruptMonitor cuando tarde demasiado](/cells/es/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Usando LightCells API](/cells/es/java/using-lightcells-api/)
