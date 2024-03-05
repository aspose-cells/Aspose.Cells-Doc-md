---
title: Su primera solicitud Aspose.Cells - Hello World
type: docs
weight: 30
url: /es/net/your-first-aspose-cells-application-hello-world/
description: Cree, edite y guarde su primer archivo de Excel en cualquier formato compatible usando Aspose.Cells for .NET para experimentar su simplicidad y potencia en C#.
keywords: C# Hello World, Aspose.Cells for .NET Hello World, The first application using Aspose.Cells for .NET, The first program via Aspose.Cells for .NET.
---
{{% alert color="primary" %}}

Este tutorial muestra cómo crear una primera aplicación (Hello World) usando Aspose.Cells' simple API. Esta sencilla aplicación crea un archivo Excel Microsoft con el texto 'Hello World' en una celda de hoja de cálculo especificada.

{{% /alert %}}

##  **Cómo crear la aplicación Hello World**

Los pasos siguientes crean la aplicación Hello World utilizando Aspose.Cells API:

1.  Crear una instancia del[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase.
1.  Si tiene una licencia, entonces[apliquelo](/cells/es/net/licensing/).
 Si está utilizando la versión de evaluación, omita las líneas de código relacionadas con la licencia.
1. Cree un nuevo archivo de Excel o abra un archivo de Excel existente.
1. Acceda a cualquier celda deseada de una hoja de trabajo en el archivo de Excel.
1.  Inserta las palabras**Hello World!** en una celda a la que se accede.
1. Genere el archivo Excel Microsoft modificado.

La implementación de los pasos anteriores se demuestra en los ejemplos siguientes.

###  **Cómo crear un nuevo libro de trabajo**

El siguiente ejemplo crea un nuevo libro desde cero, escribe Hello World. en la celda A1 de la primera hoja de trabajo y guarda el archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Cómo abrir un archivo existente**

El siguiente ejemplo abre un archivo de plantilla de Excel Microsoft existente llamado "Sample.xlsx", ingresa "Hello World!" texto en la celda A1 de la primera hoja de trabajo y guarda el libro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
