---
title: Diferentes formas de abrir archivos
type: docs
weight: 10
url: /es/net/different-ways-to-open-files/
description: Este artículo explica cómo abrir un archivo de Excel usando Aspose.Cells for .NET API.
keywords: C# Open an Excel file without Excel, How do I open an Excel File.
---
{{% alert color="primary" %}}

Con Aspose.Cells es sencillo abrir archivos, por ejemplo, para recuperar datos o utilizar una plantilla de diseñador para acelerar el proceso de desarrollo.

{{% /alert %}}

##  **Cómo abrir un archivo de Excel a través de una ruta**

 Los desarrolladores pueden abrir un archivo Excel Microsoft utilizando su ruta de archivo en la computadora local especificándola en el**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)**constructor de clases. Simplemente pase la ruta en el constructor como una *cadena*. Aspose.Cells detectará automáticamente el tipo de formato de archivo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

##  **Cómo abrir un archivo de Excel a través de una secuencia**

 También es sencillo abrir un archivo de Excel como una secuencia. Para hacerlo, use una versión sobrecargada del constructor que toma el*Arroyo*objeto que contiene el archivo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

##  **Cómo abrir un archivo solo con datos**

 Para abrir un archivo sólo con datos, utilice el**[Opciones de carga](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** y**[Filtro de carga](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**clases para establecer el atributo relacionado y las opciones de las clases para que se cargue el archivo de plantilla.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

##  **Cómo cargar sólo hojas visibles**

 Mientras carga un**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)**A veces es posible que solo necesite datos en hojas de trabajo visibles en un libro. Aspose.Cells le permite omitir datos en hojas de trabajo invisibles mientras carga un libro. Para hacer esto, cree una función personalizada que herede el**[Filtro de carga](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**clase y pasar su instancia a**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Aquí está la implementación del*Carga personalizada*clase a la que se hace referencia en el fragmento anterior.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Se generará una excepción si intenta abrir archivos Excel no nativos u otros formatos de archivo (por ejemplo, PPT/PPTX, DOC/DOCX, etc.) mediante Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Hay buenas posibilidades de que el**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)**el constructor puede tirar*System.OutOfMemoryException* mientras carga hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo debe cargarse mientras se habilitan las Preferencias de memoria.

{{% /alert %}}
