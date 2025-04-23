---
title: Apertura de archivos con diferentes formatos
type: docs
weight: 30
url: /es/python-net/opening-files-with-different-formats/
description: Aspose.Cells para Python via .NET API te permite abrir/leer diferentes formatos como XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: abrir archivos xlsx, abrir archivos html, leer archivos fods, leer archivos ods, leer archivos sxc, abrir archivos csv, Delimitado por tabulaciones, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Usando Aspose.Cells para Python via .NET, puedes abrir archivos con diferentes formatos. Aspose.Cells para Python via .NET puede abrir una variedad de formatos de archivo como hojas de cálculo de Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valores separados por comas (CSV), archivos delimitados por tabulaciones (TSV), etc.

Si necesitas conocer todos los formatos de archivo admitidos, consulta las siguientes páginas:
[Formatos de archivo admitidos](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Abriendo Archivos con Diferentes Formatos**

Aspose.Cells para Python via .NET permite a los desarrolladores abrir archivos de hojas de cálculo con diferentes formatos como SpreadsheetML, valores separados por comas (CSV), delimitados por tabulaciones o valores delimitados por tabulaciones (TSV), archivos ODS. Para abrir estos archivos, los desarrolladores pueden usar la misma metodología que usan para abrir archivos de diferentes versiones de Microsoft Excel.

### **Abriendo Archivos de SpreadsheetML**

Los archivos de SpreadsheetML son representaciones XML de hojas de cálculo que incluyen toda la información sobre ellas, como formato, fórmulas, etc. Desde Microsoft Excel XP, se añadió una opción de exportación XML a Microsoft Excel que exporta tus hojas de cálculo a archivos de SpreadsheetML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **Abriendo Archivos HTML**

Aspose.Cells para Python via .NET permite abrir archivos HTML en un objeto Workbook. El archivo HTML debe estar orientado a Microsoft Excel, es decir, Excel debe poder abrirlo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **Abriendo Archivos CSV**

Los archivos de Valores Separados por Comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan en una tabla donde cada columna está separada por el carácter de coma y entre comillas por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puedes usar Microsoft Excel para exportar datos de hoja de cálculo a CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **Abriendo Archivos CSV y reemplazando caracteres inválidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace la API Aspose.Cells para Python via .NET, como se demuestra en el ejemplo de código a continuación.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **Apertura de archivos con formato de pestañas**

El archivo con formato de pestañas (Texto) contiene datos de hojas de cálculo pero sin ningún formato. Los datos están organizados en filas y columnas como en tablas y hojas de cálculo. Básicamente, un archivo con formato de pestañas es un tipo especial de archivo de texto plano con una pestaña entre cada columna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **Apertura de archivos de Valores Separados por Comas y con pestañas (TSV)**

El archivo de valores separados por comas y con pestañas (TSV) contiene datos de hojas de cálculo pero sin ningún formato. Es lo mismo que un archivo con formato de pestañas donde los datos están organizados en filas y columnas como en tablas y hojas de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **Apertura de archivos SXC**

StarOffice Calc es similar a Microsoft Excel y soporta fórmulas, gráficos, funciones y macros. Las hojas de cálculo creadas con este software se guardan con la extensión SXC. El archivo SXC también se usa para archivos de hojas de cálculo de OpenOffice.org Calc. Aspose.Cells para Python via .NET puede leer archivos SXC, como se demuestra en el siguiente ejemplo de código.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **Apertura de archivos FODS**

El archivo FODS es una hoja de cálculo guardada en XML de OpenDocument sin compresión. Aspose.Cells para Python via .NET puede leer archivos FODS, como se muestra en el ejemplo de código siguiente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
