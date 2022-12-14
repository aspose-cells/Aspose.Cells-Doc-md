---
title: Apertura de archivos con diferentes formatos
type: docs
weight: 30
url: /es/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API le permite abrir/leer diferentes formatos como XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Usando Aspose.Cells puede abrir archivos con diferentes formatos.**Aspose.Cells** puede abrir una variedad de formatos de archivo, como hojas de cálculo de Excel Microsoft (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valores separados por comas (CSV), archivos delimitados por tabulaciones o valores separados por tabulaciones (TSV), etc.

Si necesita conocer todos los formatos de archivo admitidos, consulte las siguientes páginas:
[Formatos de archivo admitidos](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

## **Apertura de archivos con diferentes formatos**

Aspose.Cells permite a los desarrolladores abrir archivos de hojas de cálculo con diferentes formatos, como SpreadsheetML, valores separados por comas (CSV), valores delimitados por tabuladores o separados por tabuladores (TSV), archivos ODS. Para abrir dichos archivos, los desarrolladores pueden usar la misma metodología que usan para abrir archivos de diferentes versiones de Excel Microsoft.

### **Apertura de archivos de hoja de cálculo ML**

Los archivos SpreadsheetML son representaciones XML de hojas de cálculo que incluyen toda la información al respecto, como formato, fórmulas, etc. Desde Microsoft Excel XP, se agregó una opción de exportación XML a Microsoft Excel que exporta sus hojas de cálculo a archivos SpreadsheetML.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile.cpp" >}}

### **Abrir archivos HTML**

Aspose.Cells le permite abrir un archivo HTML en el objeto Libro de trabajo. El archivo HTML debe ser Microsoft orientado a Excel, es decir, MS-Excel debería poder abrirlo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile.cpp" >}}

### **Abrir archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros en los que los valores están separados por comas. Los datos se almacenan como una tabla donde cada columna está separada por el carácter de coma y citada por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puede usar Microsoft Excel para exportar datos de hojas de cálculo a CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile.cpp" >}}

#### **Abrir archivos CSV y reemplazar caracteres no válidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace Aspose.Cells API, que se demuestra en el ejemplo de código que se proporciona a continuación.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters.cpp" >}}

El archivo fuente de muestra se puede descargar desde los siguientes enlaces para probar esta función.

[Caracteres no válidos.csv](InvalidCharacters.csv)

### **Apertura de archivos de texto con separador personalizado**

Los archivos de texto se utilizan para contener datos de hojas de cálculo sin formato. El archivo es una especie de archivo de texto sin formato que puede tener algunos delimitadores personalizados.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator.cpp" >}}

El archivo fuente de muestra se puede descargar desde los siguientes enlaces para probar esta función.

[CustomSeparator.txt](CustomSeparator.txt)

### **Apertura de archivos delimitados por tabulaciones**

El archivo delimitado por tabuladores (texto) contiene datos de hoja de cálculo pero sin ningún formato. Los datos se organizan en filas y columnas como en tablas y hojas de cálculo. Básicamente, un archivo delimitado por tabulaciones es un tipo especial de archivo de texto sin formato con una tabulación entre cada columna.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile.cpp" >}}

### **Apertura de archivos de valores separados por tabuladores (TSV)**

El archivo de valores separados por tabuladores (TSV) contiene datos de hoja de cálculo pero sin ningún formato. Es lo mismo con el archivo delimitado por tabuladores donde los datos se organizan en filas y columnas como en tablas y hojas de cálculo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile.cpp" >}}

### **Apertura de archivos SXC**

StarOffice Calc es similar a Microsoft Excel y admite fórmulas, gráficos, funciones y macros. Las hojas de cálculo creadas con este software se guardan con la extensión SXC. El archivo SXC también se utiliza para los archivos de hoja de cálculo de OpenOffice.org Calc. Aspose.Cells puede leer archivos SXC como se demuestra en el siguiente ejemplo de código.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile.cpp" >}}

### **Apertura de archivos FODS**

El archivo FODS es una hoja de cálculo guardada en OpenDocument XML sin compresión. Aspose.Cells puede leer archivos FODS como se demuestra en el siguiente ejemplo de código.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile.cpp" >}}
