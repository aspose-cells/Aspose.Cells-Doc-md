---
title: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Con Aspose.Cells es simple abrir archivos, por ejemplo, para obtener datos, o para utilizar una plantilla de diseñador para acelerar el proceso de desarrollo.

{{% /alert %}}

## **Apertura de un archivo a través de una ruta**

Los desarrolladores pueden abrir un archivo de Microsoft Excel usando su ruta de archivo en la computadora local al especificarlo en el constructor de la clase **Workbook**. Simplemente pase la ruta en el constructor como *string*. Aspose.Cells detectará automáticamente el tipo de formato del archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Apertura de un archivo a través de un flujo**

También es simple abrir un archivo de Excel como un flujo. Para hacerlo, use una versión sobrecargada del constructor que toma el objeto *BufferStream* que contiene el archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Apertura de un archivo con solo datos**

Para abrir un archivo con solo datos, use las clases **LoadOptions** y **LoadFilter** para configurar el atributo relacionado y las opciones de las clases para que se cargue el archivo de plantilla.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Se lanzará una excepción si intenta abrir archivos de Excel que no son nativos u otros formatos de archivo (por ejemplo, PPT/PPTX, DOC/DOCX, etc.) con Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Existen posibilidades de que el constructor de **Workbook** arroje *System.OutOfMemoryException* al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo que la hoja de cálculo tiene que cargarse mientras se habilitan las Preferencias de memoria.

{{% /alert %}}
