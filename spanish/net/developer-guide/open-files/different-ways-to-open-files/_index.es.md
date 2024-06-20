---
title: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/net/different-ways-to-open-files/
description: Este artículo explica cómo abrir un archivo de Excel usando la API Aspose.Cells for .NET.
keywords: C# Abrir un archivo de Excel sin Excel, ¿Cómo abro un archivo de Excel?
---

{{% alert color="primary" %}}

Con Aspose.Cells es simple abrir archivos, por ejemplo, para obtener datos, o para utilizar una plantilla de diseñador para acelerar el proceso de desarrollo.

{{% /alert %}}

## **Cómo abrir un archivo de Excel a través de una ruta**

Los desarrolladores pueden abrir un archivo de Microsoft Excel utilizando su ruta de archivo en la computadora local especificándola en el constructor de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Simplemente pase la ruta en el constructor como un *string*. Aspose.Cells detectará automáticamente el tipo de formato del archivo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Cómo abrir un archivo de Excel via un Stream**

También es sencillo abrir un archivo de Excel como un stream. Para hacerlo, use una versión sobrecargada del constructor que toma el objeto *Stream* que contiene el archivo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Cómo abrir un archivo con solo datos**

Para abrir un archivo solo con datos, use las clases [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) y [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) para establecer el atributo y las opciones relacionadas de las clases para cargar el archivo de plantilla.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Cómo cargar solo las hojas visibles**

Al cargar un [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) a veces solo necesita los datos en hojas visibles en un libro de trabajo. Aspose.Cells le permite omitir datos en hojas invisibles al cargar un libro de trabajo. Para hacerlo, cree una función personalizada que herede la clase [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) y pase su instancia a la propiedad [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Aquí está la implementación de la clase *CustomnLoad* referenciada en el fragmento anterior.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Se lanzará una excepción si intenta abrir archivos de Excel que no son nativos u otros formatos de archivo (por ejemplo, PPT/PPTX, DOC/DOCX, etc.) con Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Existe una gran probabilidad de que el constructor [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) arroje *System.OutOfMemoryException* al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo debe cargarse habilitando las Preferencias de memoria.

{{% /alert %}}
