---
title: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/python-net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Con Aspose.Cells es sencillo abrir archivos, por ejemplo, para recuperar datos o utilizar una plantilla de diseñador para acelerar el proceso de desarrollo.

{{% /alert %}}

## **Abrir un archivo a través de una ruta**

 Los desarrolladores pueden abrir un archivo de Excel Microsoft usando su ruta de archivo en la computadora local especificándolo en el**Libro de trabajo**constructor de clases. Simplemente pase la ruta en el constructor como un*cadena*. Aspose.Cells detectará automáticamente el tipo de formato de archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Abrir un archivo a través de una secuencia**

También es sencillo abrir un archivo de Excel como una secuencia. Para hacerlo, use una versión sobrecargada del constructor que toma el*BufferStream*objeto que contiene el archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Abrir un archivo solo con datos**

 Para abrir un archivo con datos solamente, utilice el**Opciones de carga** y**Cargarfiltro**clases para establecer el atributo relacionado y las opciones de las clases para que se cargue el archivo de plantilla.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Se lanzará una excepción si intenta abrir archivos de Excel no nativos u otros formatos de archivo (por ejemplo, PPT/PPTX, DOC/DOCX, etc.) antes del Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Hay buenas posibilidades de que el**Libro de trabajo** el constructor puede lanzar*System.OutOfMemoryException* mientras se cargan hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo debe cargarse mientras se habilitan las Preferencias de memoria.

{{% /alert %}}
