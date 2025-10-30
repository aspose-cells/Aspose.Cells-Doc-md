---
title: Apertura de archivos con diferentes formatos
type: docs
weight: 30
url: /es/go-cpp/opening-files-with-different-formats/

description: La API Aspose.Cells for Go via C++ permite abrir/leer diferentes formatos como XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: abrir archivos xlsx, abrir archivos html, leer archivos fods, leer archivos ods, leer archivos sxc, abrir archivos csv, Delimitado por tabulaciones, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Usando Aspose.Cells, puedes abrir archivos con diferentes formatos. **Aspose.Cells** puede abrir una variedad de formatos de archivos como hojas de cálculo de Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valores separados por comas (CSV), archivos con tabulaciones (TSV), etc.

Si necesitas conocer todos los formatos de archivo admitidos, consulta las siguientes páginas:
[Formatos de archivo soportados](https://docs.aspose.com/cells/go-cpp/supported-file-formats/)

{{% /alert %}}

## **Abriendo Archivos con Diferentes Formatos**

Aspose.Cells permite a los desarrolladores abrir archivos de hojas de cálculo con diferentes formatos como SpreadsheetML, valores separados por comas (CSV), archivos con tabulaciones (TSV), archivos ODS, etc. Para abrir tales archivos, los desarrolladores pueden usar la misma metodología que utilizan para abrir archivos de diferentes versiones de Microsoft Excel.

### **Abriendo Archivos de SpreadsheetML**

Los archivos SpreadsheetML son representaciones XML de hojas de cálculo que incluyen toda la información sobre ellas, como formato, fórmulas, etc. Desde Microsoft Excel XP, se agregó una opción de exportación XML a Microsoft Excel que exporta tus hojas a archivos SpreadsheetML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **Abriendo Archivos HTML**

Aspose.Cells te permite abrir archivos HTML en un objeto Workbook. El archivo HTML debe estar orientado a Microsoft Excel, es decir, MS-Excel debería poder abrirlo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **Abriendo Archivos CSV**

Los archivos de Valores Separados por Comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan en una tabla donde cada columna está separada por el carácter de coma y entre comillas por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puedes usar Microsoft Excel para exportar datos de hoja de cálculo a CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

### **Abriendo Archivos de Texto con Separador Personalizado**

Los archivos de texto se usan para contener datos de hojas de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

Los archivos de origen de ejemplo se pueden descargar desde los siguientes enlaces para probar esta función.

[CustomSeparator.txt](CustomSeparator.txt)

### **Apertura de archivos con formato de pestañas**

Los archivos de texto delimitados por tabulaciones (Texto) contienen datos de hojas de cálculo pero sin ningún formato. Los datos están organizados en filas y columnas, como en tablas y hojas de cálculo. Básicamente, un archivo delimitado por tabulaciones es un tipo especial de archivo de texto plano con una tabulación entre cada columna.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **Apertura de archivos de Valores Separados por Comas y con pestañas (TSV)**

Un archivo de valores separados por tabulaciones (TSV) contiene datos de hojas de cálculo pero sin ningún formato. Es lo mismo que un archivo delimitado por tabulaciones donde los datos están organizados en filas y columnas, como en tablas y hojas de cálculo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **Apertura de archivos SXC**

StarOffice Calc es similar a Microsoft Excel y soporta fórmulas, gráficos, funciones y macros. Las hojas de cálculo creadas con este software se guardan con la extensión SXC. El archivo SXC también se usa para archivos de hojas de cálculo de OpenOffice.org Calc. Aspose.Cells puede leer archivos SXC, como se demuestra en el siguiente ejemplo de código.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **Apertura de archivos FODS**

El archivo FODS es una hoja de cálculo guardada en XML de OpenDocument sin compresión. Aspose.Cells puede leer archivos FODS, como se demuestra en el siguiente ejemplo de código.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}
