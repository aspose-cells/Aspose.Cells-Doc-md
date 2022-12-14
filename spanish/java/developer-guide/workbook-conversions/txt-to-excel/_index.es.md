---
title: Convierta CSV, TSV y TXT a Excel
type: docs
weight: 50
url: /es/java/convert-csv-tsv-and-txt-to-excel/
---
## **Abrir archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros cuyos valores están delimitados o separados por comas. En los archivos CSV, los datos se almacenan en un formato tabular que tiene campos separados por comas y entre comillas dobles. Si el valor de un campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puede usar Microsoft Excel para exportar los datos de su hoja de cálculo a un archivo CSV.

Para abrir archivos CSV, use el**[Opciones de carga](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** clase y seleccione la**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** valor, predefinido en el**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumeración.

## **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Abrir archivos CSV y reemplazar caracteres no válidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace Aspose.Cells API, que se demuestra en el ejemplo de código que se proporciona a continuación.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Abrir archivos CSV usando el analizador preferido**

Esto no siempre es necesario para usar la configuración predeterminada del analizador para abrir los archivos CSV. A veces, la importación de un archivo CSV no crea el resultado esperado, como que el formato de fecha no es el esperado o los campos vacíos se manejan de manera diferente. Para este propósito**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**está disponible para proporcionar su propio analizador preferido para analizar diferentes tipos de datos según el requisito. El siguiente código de ejemplo demuestra el uso del analizador preferido.

El archivo fuente de muestra y los archivos de salida se pueden descargar desde los siguientes enlaces para probar esta función.

[samplePreferredParser.csv](samplePreferredParser.csv)

[muestra de salidaPreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Apertura de archivos TSV (separados por tabuladores)**

Los archivos delimitados por tabuladores contienen datos de hojas de cálculo pero sin ningún formato. Los datos se organizan en filas y columnas, como tablas y hojas de cálculo. En resumen, un archivo delimitado por tabulaciones es un tipo especial de archivo de texto sin formato con una tabulación entre cada columna del texto.

Para abrir archivos delimitados por tabuladores, los desarrolladores deben usar el**[Opciones de carga](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** clase y seleccione la**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** valor, predefinido en el**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumeración.

## **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Temas avanzados**
- [Cargue o importe un archivo CSV con fórmulas](/cells/es/java/load-or-import-csv-file-with-formulas/)
- [Recorte las filas y columnas en blanco iniciales mientras exporta hojas de cálculo a formato CSV](/cells/es/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

