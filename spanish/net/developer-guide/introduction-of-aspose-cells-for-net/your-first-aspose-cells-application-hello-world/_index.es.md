---
title: Su primera solicitud Aspose.Cells - Hello World
type: docs
weight: 30
url: /es/net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Este tutorial muestra cómo crear una primera aplicación (Hello World) usando Aspose.Cells' simple API. Esta aplicación simple crea un archivo de Excel Microsoft con el texto 'Hello World' en una celda de hoja de cálculo específica.

{{% /alert %}}

## **Creación de la aplicación Hello World**

Los pasos a continuación crean la aplicación Hello World usando el Aspose.Cells API:

1.  Crear una instancia de la[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase.
1.  Si tiene una licencia, entonces[apliquelo](/cells/es/net/licensing/).
 Si está utilizando la versión de evaluación, omita las líneas de código relacionadas con la licencia.
1. Cree un nuevo archivo de Excel o abra un archivo de Excel existente.
1. Acceda a cualquier celda deseada de una hoja de trabajo en el archivo de Excel.
1.  Inserta las palabras**Hello World!** en una celda accedida.
1. Genere el archivo de Excel Microsoft modificado.

La implementación de los pasos anteriores se demuestra en los siguientes ejemplos.

### **Ejemplo de código: creación de un nuevo libro de trabajo**

El siguiente ejemplo crea un nuevo libro de trabajo desde cero, ¡escribe Hello World! en la celda A1 de la primera hoja de cálculo y guarda el archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Ejemplo de código: abrir un archivo existente**

El siguiente ejemplo abre un archivo de plantilla de Excel Microsoft existente llamado "Sample.xlsx", ingresa "Hello World!" texto en la celda A1 en la primera hoja de trabajo y guarda el libro de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
