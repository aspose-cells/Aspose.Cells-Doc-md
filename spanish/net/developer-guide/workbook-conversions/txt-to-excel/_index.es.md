---
title: Convertir CSV, TSV y TXT a Excel
type: docs
weight: 30
url: /es/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

Usando Aspose.Cells, puede convertir el archivo CSV a Excel, OpenOffice, Pdf, Json y muchos formatos diferentes.

{{% /alert %}}


## **Abriendo Archivos CSV**

Los archivos de Valores Separados por Comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan en una tabla donde cada columna está separada por el carácter de coma y entre comillas por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puedes usar Microsoft Excel para exportar datos de hoja de cálculo a CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Abriendo Archivos CSV y reemplazando caracteres inválidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace la API de Aspose.Cells, como se demuestra en el ejemplo de código que se muestra a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Usando analizador preferido**

No siempre es necesario utilizar la configuración de analizador predeterminada para abrir los archivos CSV. A veces, al importar un archivo CSV, no se crea la salida esperada, como el formato de fecha no es el esperado o los campos vacíos se manejan de manera diferente. Con este propósito, se dispone de **TxtLoadOptions.PreferredParsers** para proporcionar un analizador preferido propio para analizar diferentes tipos de datos según el requisito. El siguiente código de muestra demuestra el uso del analizador preferido.  

Se pueden descargar los archivos fuente de muestra y los archivos de salida de las siguientes conexiones para probar esta función.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Abriendo Archivos de Texto con Separador Personalizado**

Los archivos de texto se usan para contener datos de hojas de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Apertura de archivos con formato de pestañas**

El archivo con formato de pestañas (Texto) contiene datos de hojas de cálculo pero sin ningún formato. Los datos están organizados en filas y columnas como en tablas y hojas de cálculo. Básicamente, un archivo con formato de pestañas es un tipo especial de archivo de texto plano con una pestaña entre cada columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Apertura de archivos de Valores Separados por Comas y con pestañas (TSV)**

El archivo de valores separados por comas y con pestañas (TSV) contiene datos de hojas de cálculo pero sin ningún formato. Es lo mismo que un archivo con formato de pestañas donde los datos están organizados en filas y columnas como en tablas y hojas de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Temas avanzados**
- [Cargar o importar archivo CSV con fórmulas](/cells/es/net/load-or-import-csv-file-with-formulas/)
- [Lectura de archivo CSV con múltiples codificaciones](/cells/es/net/reading-csv-file-with-multiple-encodings/)

{{< app/cells/assistant language="csharp" >}}
