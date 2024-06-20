---
title: Tu primera aplicación Aspose.Cells  Hola Mundo
type: docs
weight: 30
url: /es/java/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

Este tema para principiantes muestra cómo los desarrolladores pueden crear una aplicación simple (Hola Mundo) utilizando la API simple de Aspose.Cells. La aplicación crea un archivo de Microsoft Excel con las palabras Hola Mundo en una celda especificada de una hoja de cálculo.

{{% /alert %}}

### **Creación de la aplicación Hola Mundo**

Para crear la aplicación Hola Mundo utilizando la API de Aspose.Cells:

1. Crear una instancia de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).
1. Aplicar la licencia:
   1. Si has comprado una licencia, entonces úsala en tu aplicación para acceder a la funcionalidad completa de Aspose.Cells.
   1. Si estás usando la versión de evaluación del componente (si estás usando Aspose.Cells sin una licencia), omite este paso.
1. Crear un nuevo archivo de Microsoft Excel o abrir un archivo existente en el cual quieras agregar/actualizar algún texto.
1. Acceder a cualquier celda de una hoja de cálculo en el archivo de Microsoft Excel.
1. Inserte las palabras **¡Hola, mundo!** en una celda accesada.
1. Genere el archivo modificado de Microsoft Excel.

Los ejemplos a continuación demuestran los pasos anteriores.

#### **Creando un Libro de trabajo**

El siguiente ejemplo crea un nuevo libro de trabajo desde cero, escribe las palabras "¡Hola, mundo!" en la celda A1 en la primera hoja de trabajo, y guarda el archivo.

**La hoja de cálculo generada** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **Apertura de un Archivo Existente**

El siguiente ejemplo abre un archivo de plantilla de Microsoft Excel existente llamado **book1.xls**, escribe las palabras "¡Hola, mundo!" en la celda A1 en la primera hoja de trabajo, y guarda el libro de trabajo como un nuevo archivo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
