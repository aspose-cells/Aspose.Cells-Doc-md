---
title: Convertir CSV, TSV y TXT a Excel
type: docs
weight: 50
url: /es/java/convert-csv-tsv-and-txt-to-excel/
---

## **Abriendo Archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros cuyos valores están delimitados o separados por comas. En los archivos CSV, los datos se almacenan en un formato tabular que tiene campos separados por el carácter de coma y entrecomillados por el carácter de comillas dobles. Si el valor de un campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puede usar Microsoft Excel para exportar los datos de su hoja de cálculo a un archivo CSV.

Para abrir archivos CSV, use la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y seleccione el valor [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), predefinido en la enumeración [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Abriendo Archivos CSV y reemplazando caracteres inválidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, estos se reemplazan automáticamente. Lo mismo hace la API de Aspose.Cells, que se muestra en el ejemplo de código que se muestra a continuación.

#### **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Apertura de archivos CSV utilizando un analizador preferido**

No siempre es necesario utilizar la configuración de analizador predeterminada para abrir los archivos CSV. A veces, la importación de un archivo CSV no crea la salida esperada, como el formato de fecha no es el esperado o los campos vacíos se manejan de manera diferente. Con este fin, [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) está disponible para proporcionar su propio analizador preferido para analizar diferentes tipos de datos según el requisito. El siguiente código de ejemplo demuestra el uso del analizador preferido.  

Se pueden descargar los archivos fuente de muestra y los archivos de salida de las siguientes conexiones para probar esta función.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Apertura de archivos TSV (delimitados por tabuladores)**

Los archivos delimitados por tabuladores contienen datos de hojas de cálculo pero sin ningún formato. Los datos están organizados en filas y columnas, como tablas y hojas de cálculo. En resumen, un archivo delimitado por tabuladores es un tipo especial de archivo de texto sin formato con una pestaña entre cada columna en el texto.

Para abrir archivos delimitados por tabuladores, los desarrolladores deben usar la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y seleccionar el valor [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), predefinido en la enumeración [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **Ejemplo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Temas avanzados**
- [Cargar o importar archivo CSV con fórmulas](/cells/es/java/load-or-import-csv-file-with-formulas/)
- [Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV](/cells/es/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

{{< app/cells/assistant language="java" >}}
