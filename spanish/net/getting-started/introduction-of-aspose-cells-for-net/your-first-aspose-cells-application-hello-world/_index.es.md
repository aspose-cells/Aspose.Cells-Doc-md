---
title: Tu primera aplicación Aspose.Cells  Hola Mundo
type: docs
weight: 30
url: /es/net/your-first-aspose-cells-application-hello-world/
description: Cree, edite y guarde su primer archivo de Excel en cualquier formato admitido usando Aspose.Cells for .NET para experimentar su simplicidad y potencia en C#.
keywords: C# Hola Mundo, Aspose.Cells for .NET Hola Mundo, La primera aplicación usando Aspose.Cells for .NET, El primer programa via Aspose.Cells for .NET.
---

{{% alert color="primary" %}}

Este tutorial muestra cómo crear una primera aplicación (Hola Mundo) utilizando la API simple de Aspose.Cells. Esta sencilla aplicación crea un archivo de Microsoft Excel con el texto 'Hola Mundo' en una celda de hoja de cálculo especificada.

{{% /alert %}}

## **Cómo crear la aplicación Hola Mundo**

Los siguientes pasos crean la aplicación Hola Mundo utilizando la API de Aspose.Cells:

1. Crea una instancia de la clase [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Si tienes una licencia, entonces [aplícala](/cells/es/net/licensing/).
   Si estás usando la versión de evaluación, omite las líneas de código relacionadas con la licencia.
1. Crea un nuevo archivo de Excel, o abre un archivo de Excel existente.
1. Accede a cualquier celda deseada de una hoja de cálculo en el archivo de Excel.
1. Inserte las palabras **¡Hola, mundo!** en una celda accesada.
1. Genere el archivo modificado de Microsoft Excel.

La implementación de los pasos anteriores se muestra en los ejemplos a continuación.

### **Cómo crear un nuevo Workbook**

El siguiente ejemplo crea un nuevo workbook desde cero, escribe ¡Hola Mundo! en la celda A1 en la primera hoja de cálculo y guarda el archivo Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Cómo abrir un archivo existente**

El siguiente ejemplo abre un archivo de plantilla de Microsoft Excel existente llamado "Sample.xlsx", ingresa el texto "¡Hola Mundo!" en la celda A1 en la primera hoja de cálculo y guarda el workbook.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
