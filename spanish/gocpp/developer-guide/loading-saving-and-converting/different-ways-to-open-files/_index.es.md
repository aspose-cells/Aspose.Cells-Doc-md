---
title: Diferentes formas de abrir archivos
linktitle: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Con Aspose.Cells, puedes abrir archivos, por ejemplo, para recuperar datos o para usar una plantilla de diseñador para acelerar el proceso de desarrollo. Aspose.Cells puede abrir una variedad de archivos diferentes, como hojas de cálculo de Microsoft Excel (XLS, XLSX, XLSM, XLSB), CSV o archivos delimitados por tabulaciones.

{{% /alert %}}

## **Apertura de un archivo a través de una ruta**

Los desarrolladores pueden abrir un archivo de Microsoft Excel usando su ruta en la computadora local especificándola en el constructor de la clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Pase la ruta en el constructor como una cadena. Aspose.Cells detectará automáticamente el tipo de formato del archivo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **Abrir un archivo usando un stream**

También es posible abrir un archivo de Excel como un flujo. Para hacerlo, utiliza una versión sobrecargada del constructor que toma el objeto *Stream* que contiene el archivo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
