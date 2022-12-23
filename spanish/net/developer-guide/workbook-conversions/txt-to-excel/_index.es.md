---
title: Convierta CSV, TSV y TXT a Excel
type: docs
weight: 30
url: /es/net/convert-csv-tsv-and-txt-to-excel/
---
{{% alert color="primary" %}}

Con Aspose.Cells, puede convertir el archivo CSV a Excel, OpenOffice, Pdf, Json y muchos formatos diferentes.

{{% /alert %}}


## **Apertura de archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan como una tabla donde cada columna está separada por el carácter de coma y citada por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puede usar Microsoft Excel para exportar datos de hojas de cálculo a CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Abrir archivos CSV y reemplazar caracteres no válidos**

En Excel, cuando se abre el archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace Aspose.Cells API, que se demuestra en el ejemplo de código que se proporciona a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Usando el analizador preferido**

Esto no siempre es necesario para usar la configuración predeterminada del analizador para abrir los archivos CSV. A veces, la importación del archivo CSV no crea el resultado esperado, como que el formato de fecha no es el esperado o los campos vacíos se manejan de manera diferente. Para este propósito**TxtLoadOptions.PreferredParsers**está disponible para proporcionar su propio analizador preferido para analizar diferentes tipos de datos según el requisito. El siguiente código de ejemplo demuestra el uso del analizador preferido.

El archivo fuente de muestra y los archivos de salida se pueden descargar desde los siguientes enlaces para probar esta función.

[samplePreferredParser.csv](samplePreferredParser.csv)

[muestra de salidaPreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Apertura de archivos de texto con separador personalizado**

Los archivos de texto se utilizan para contener datos de hojas de cálculo sin formato. El archivo es una especie de archivo de texto sin formato que puede tener algunos delimitadores personalizados.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Apertura de archivos delimitados por tabulaciones**

El archivo delimitado por tabuladores (texto) contiene datos de hoja de cálculo pero sin ningún formato. Los datos se organizan en filas y columnas como en tablas y hojas de cálculo. Básicamente, un archivo delimitado por tabulaciones es un tipo especial de archivo de texto sin formato con una tabulación entre cada columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Abrir archivos de valores separados por tabuladores (TSV)**

El archivo de valores separados por tabuladores (TSV) contiene datos de hoja de cálculo pero sin ningún formato. Es lo mismo con el archivo delimitado por tabuladores donde los datos se organizan en filas y columnas como en tablas y hojas de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Temas avanzados**
- [Cargue o importe el archivo CSV con fórmulas](/cells/es/net/load-or-import-csv-file-with-formulas/)
- [Lectura del archivo CSV con múltiples codificaciones](/cells/es/net/reading-csv-file-with-multiple-encodings/)

