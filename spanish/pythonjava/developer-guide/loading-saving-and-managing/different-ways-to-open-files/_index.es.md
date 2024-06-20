---
title: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Con Aspose.Cells es simple abrir archivos, por ejemplo, para obtener datos, o para utilizar una plantilla de diseñador para acelerar el proceso de desarrollo.

{{% /alert %}}

## **Apertura de un archivo a través de una ruta**

Los desarrolladores pueden abrir un archivo de Microsoft Excel utilizando su ruta de archivo en la computadora local especificándola en el constructor de la clase [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). Simplemente pase la ruta en el constructor como un *string*. Aspose.Cells detectará automáticamente el tipo de formato del archivo.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Apertura de un archivo a través de un flujo**

También es simple abrir un archivo de Excel como un flujo. Para hacerlo, use una versión sobrecargada del constructor que toma el objeto *BufferStream* que contiene el archivo.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Apertura de un archivo con solo datos**

Para abrir un archivo solo con datos, use las clases [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) y [**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter) para establecer el atributo y las opciones relacionadas de las clases para cargar el archivo de plantilla.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Se lanzará una excepción si intenta abrir archivos de Excel que no son nativos u otros formatos de archivo (por ejemplo, PPT/PPTX, DOC/DOCX, etc.) con Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Existe una gran probabilidad de que el constructor [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) arroje *System.OutOfMemoryException* al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo debe cargarse habilitando las Preferencias de memoria.

{{% /alert %}}
