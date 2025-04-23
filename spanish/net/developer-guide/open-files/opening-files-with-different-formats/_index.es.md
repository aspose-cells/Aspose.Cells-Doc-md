---
title: Apertura de archivos con diferentes formatos
type: docs
weight: 30
url: /es/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET La API le permite abrir/leer diferentes formatos como XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: abrir archivos xlsx, abrir archivos html, leer archivos fods, leer archivos ods, leer archivos sxc, abrir archivos csv, Delimitado por tabulaciones, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Con Aspose.Cells puedes abrir archivos con diferentes formatos. **Aspose.Cells** puede abrir una variedad de formatos de archivo como hojas de cálculo de Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valores separados por comas (CSV), archivos de valores delimitados por tabuladores (TSV), etc.

Si necesitas conocer todos los formatos de archivo admitidos, consulta las siguientes páginas:
[Formatos de archivo admitidos](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **Abriendo Archivos con Diferentes Formatos**

Aspose.Cells permite a los desarrolladores abrir archivos de hoja de cálculo con diferentes formatos como SpreadsheetML, valores separados por comas (CSV), valores delimitados por tabuladores (TSV), archivos ODS. Para abrir tales archivos, los desarrolladores pueden usar la misma metodología que usan para abrir archivos de diferentes versiones de Microsoft Excel.

### **Abriendo Archivos de SpreadsheetML**

Los archivos de SpreadsheetML son representaciones XML de hojas de cálculo que incluyen toda la información sobre ellas, como formato, fórmulas, etc. Desde Microsoft Excel XP, se añadió una opción de exportación XML a Microsoft Excel que exporta tus hojas de cálculo a archivos de SpreadsheetML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **Abriendo Archivos HTML**

Aspose.Cells te permite abrir archivos HTML en un objeto Workbook. El archivo HTML debe estar orientado a Microsoft Excel, es decir, MS-Excel debería poder abrirlo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **Abriendo Archivos CSV**

Los archivos de Valores Separados por Comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan en una tabla donde cada columna está separada por el carácter de coma y entre comillas por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puedes usar Microsoft Excel para exportar datos de hoja de cálculo a CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **Abriendo Archivos CSV y reemplazando caracteres inválidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace la API de Aspose.Cells, como se demuestra en el ejemplo de código que se muestra a continuación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **Usando analizador preferido**

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

### **Apertura de archivos SXC**

StarOffice Calc es similar a Microsoft Excel y admite fórmulas, gráficos, funciones y macros. Las hojas de cálculo creadas con este software se guardan con la extensión SXC. El archivo SXC también se utiliza para los archivos de hojas de cálculo de OpenOffice.org Calc. Aspose.Cells puede leer archivos SXC como se muestra en el siguiente ejemplo de código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **Apertura de archivos FODS**

El archivo FODS es una hoja de cálculo guardada en OpenDocument XML sin ninguna compresión. Aspose.Cells puede leer archivos FODS como se muestra en el siguiente ejemplo de código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
