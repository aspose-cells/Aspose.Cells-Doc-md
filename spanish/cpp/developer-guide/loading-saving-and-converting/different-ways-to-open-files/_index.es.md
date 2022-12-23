---
title: Diferentes formas de abrir archivos
linktitle: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Con Aspose.Cells es posible abrir archivos, por ejemplo para recuperar datos, o usar una plantilla de diseñador para acelerar el proceso de desarrollo. Aspose.Cells puede abrir una variedad de archivos diferentes, como Microsoft hojas de cálculo de Excel (XLS, XLSX, XLSM, XLSB), CSV o TabDelimited archivos.

{{% /alert %}} 
## **Abrir un archivo a través de una ruta**
 Los desarrolladores pueden abrir un archivo de Excel Microsoft usando su ruta de archivo en la computadora local especificándolo en el[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)constructor de clases. Simplemente pase la ruta en el constructor como String. Aspose.Cells detectará automáticamente el tipo de formato de archivo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath.cpp" >}}

## **Abrir un archivo usando una secuencia**
 También es posible abrir un archivo de Excel como flujo. Para hacerlo, use una versión sobrecargada del constructor que toma el*Arroyo*objeto que contiene el archivo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream.cpp" >}}

