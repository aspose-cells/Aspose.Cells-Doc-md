---
title: Abrir archivos con diferentes formatos
type: docs
weight: 30
url: /es/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API le permite abrir/leer diferentes formatos como XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Usando Aspose.Cells puedes abrir archivos con diferentes formatos.**Aspose.Cells** puede abrir una variedad de formatos de archivo, como Microsoft hojas de cálculo de Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, archivos de valores separados por comas (CSV), archivos delimitados por tabulaciones o valores separados por tabulaciones (TSV), etc.

Si necesita conocer todos los formatos de archivo admitidos, consulte las siguientes páginas:
[Formatos de archivo admitidos](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

##  **Abrir archivos con diferentes formatos**

Aspose.Cells permite a los desarrolladores abrir archivos de hojas de cálculo con diferentes formatos, como SpreadsheetML, valores separados por comas (CSV), valores delimitados por tabulaciones o separados por tabulaciones (TSV), archivos ODS. Para abrir dichos archivos, los desarrolladores pueden utilizar la misma metodología que utilizan para abrir archivos de diferentes Microsoft versiones de Excel.

###  **Apertura de archivos SpreadsheetML**

Los archivos SpreadsheetML son representaciones XML de hojas de cálculo que incluyen toda la información al respecto, como formato, fórmulas, etc. Desde Microsoft Excel XP, se agrega una opción de exportación XML a Microsoft Excel que exporta sus hojas de cálculo a archivos SpreadsheetML.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

###  **Apertura de archivos HTML**

Aspose.Cells le permite abrir el archivo HTML en el objeto Libro de trabajo. El archivo HTML debería estar orientado a Excel, es decir, MS-Excel debería poder abrirlo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

###  **Apertura de archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan como una tabla donde cada columna está separada por un carácter de coma y entre comillas dobles. Si el valor de un campo contiene un carácter de comillas dobles, se escapa con un par de caracteres de comillas dobles. También puede utilizar Microsoft Excel para exportar datos de la hoja de cálculo a CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

####  **Abrir archivos CSV y reemplazar caracteres no válidos**

En Excel, cuando se abre el archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo hace Aspose.Cells API que se demuestra en el ejemplo de código que se muestra a continuación.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Se puede descargar un archivo fuente de muestra desde los siguientes enlaces para probar esta función.

[Personajes no válidos.csv](InvalidCharacters.csv)

###  **Abrir archivos de texto con separador personalizado**

Los archivos de texto se utilizan para almacenar datos de hojas de cálculo sin formato. El archivo es una especie de archivo de texto sin formato que puede tener algunos delimitadores personalizados.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Se puede descargar un archivo fuente de muestra desde los siguientes enlaces para probar esta función.

[Separador personalizado.txt](CustomSeparator.txt)

###  **Abrir archivos delimitados por tabulaciones**

El archivo delimitado por tabulaciones (texto) contiene datos de hoja de cálculo pero sin ningún formato. Los datos se organizan en filas y columnas como en tablas y hojas de cálculo. Básicamente, un archivo delimitado por tabulaciones es un tipo especial de archivo de texto sin formato con una pestaña entre cada columna.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

###  **Abrir archivos de valores separados por tabulaciones (TSV)**

El archivo de valores separados por tabulaciones (TSV) contiene datos de hoja de cálculo pero sin ningún formato. Lo mismo ocurre con el archivo delimitado por tabulaciones, donde los datos se organizan en filas y columnas como en tablas y hojas de cálculo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

###  **Apertura de archivos SXC**

StarOffice Calc es similar a Microsoft Excel y admite fórmulas, gráficos, funciones y macros. Las hojas de cálculo creadas con este software se guardan con la extensión SXC. El archivo SXC también se utiliza para archivos de hoja de cálculo OpenOffice.org Calc. Aspose.Cells puede leer archivos SXC como lo demuestra el siguiente ejemplo de código.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

###  **Apertura de archivos FODS**

El archivo FODS es una hoja de cálculo guardada en OpenDocument XML sin ningún tipo de compresión. Aspose.Cells puede leer archivos FODS como lo demuestra el siguiente ejemplo de código.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
