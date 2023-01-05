---
title: Su primera solicitud Aspose.Cells - Hello World
type: docs
weight: 30
url: /es/java/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Este tema para principiantes muestra cómo los desarrolladores pueden crear una primera aplicación simple (Hello World) usando Aspose.Cells' simple API. La aplicación crea un archivo de Excel Microsoft con las palabras Hello World en una celda específica de una hoja de cálculo.

{{% /alert %}}

### **Creación de la aplicación Hello World**

Para crear la aplicación Hello World usando Aspose.Cells API:

1.  Crear una instancia de la**[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)**clase.
1. Aplicar la licencia:
1. Si ha comprado una licencia, use la licencia en su aplicación para obtener acceso a la funcionalidad completa de Aspose.Cells
 1. Si está utilizando la versión de evaluación del componente (si está utilizando Aspose.Cells sin licencia), omita este paso.
1. Cree un nuevo archivo de Excel Microsoft o abra un archivo existente en el que desee agregar/actualizar algún texto.
1. Acceda a cualquier celda de una hoja de trabajo en el archivo de Excel Microsoft.
1.  Inserta las palabras**Hello World!** en una celda accedida.
1. Genere el archivo de Excel Microsoft modificado.

Los siguientes ejemplos demuestran los pasos anteriores.

#### **Creación de un libro de trabajo**

El siguiente ejemplo crea un nuevo libro de trabajo desde cero, escribe las palabras "Hello World!" en la celda A1 de la primera hoja de cálculo y guarda el archivo.

**La hoja de cálculo generada** 

![todo:imagen_alternativa_texto](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **Abrir un archivo existente**

 El siguiente ejemplo abre un archivo de plantilla de Excel Microsoft existente llamado**libro1.xls**, escribe las palabras "Hello World!" en la celda A1 de la primera hoja de cálculo y guarda el libro de trabajo como un archivo nuevo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
