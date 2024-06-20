---
title: Diferentes formas de abrir archivos
linktitle: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

Con Aspose.Cells es posible abrir archivos, por ejemplo para recuperar datos, o usar una plantilla de diseñador para acelerar el proceso de desarrollo. Aspose.Cells puede abrir una variedad de archivos diferentes, como hojas de cálculo de Microsoft Excel (XLS, XLSX, XLSM, XLSB), archivos CSV o TabDelimited.

{{% /alert %}} 
## **Apertura de un archivo a través de una ruta**
Los desarrolladores pueden abrir un archivo de Microsoft Excel usando su ruta de archivo en la computadora local al especificarla en el constructor de la clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Simplemente pasa la ruta en el constructor como String. Aspose.Cells detectará automáticamente el tipo de formato de archivo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **Abriendo un Archivo usando un Stream**
También es posible abrir un archivo de Excel como un flujo. Para hacerlo, utiliza una versión sobrecargada del constructor que toma el objeto *Stream* que contiene el archivo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

