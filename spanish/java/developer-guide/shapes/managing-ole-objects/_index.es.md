---
title: Gestión de objetos OLE
type: docs
weight: 30
url: /es/java/managing-ole-objects/
---

## **Introducción**

OLE (Object Linking and Embedding) es el marco de Microsoft para una tecnología de documento compuesto. En resumen, un documento compuesto es algo similar a un escritorio de visualización que puede contener objetos visuales e informativos de todo tipo: texto, calendarios, animaciones, sonido, video en movimiento, 3D, noticias actualizadas continuamente, controles, y mucho más. Cada objeto de escritorio es una entidad de programa independiente que puede interactuar con un usuario y también comunicarse con otros objetos en el escritorio.

OLE (Object Linking and Embedding) es compatible con muchos programas diferentes y se utiliza para hacer que el contenido creado en un programa esté disponible en otro. Por ejemplo, puedes insertar un documento de Microsoft Word en Microsoft Excel. Para ver qué tipos de contenido puedes insertar, haz clic en **Objeto** en el menú **Insertar**. Solo aparecen en el cuadro **Tipo de objeto** los programas instalados en el equipo y que admiten objetos OLE.

## **Insertar objetos OLE en una hoja de cálculo**

Aspose.Cells admite agregar, extraer y manipular objetos OLE en hojas de cálculo. Por esta razón, Aspose.Cells tiene la clase [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection), utilizada para agregar un nuevo objeto OLE a la lista de colección. Otra clase, [**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), representa un objeto OLE. Tiene algunos miembros importantes:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) especifica los datos de la imagen (ícono) de tipo matriz de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de cálculo.
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData) especifica los datos del objeto en forma de una matriz de bytes. Estos datos se mostrarán en su programa relacionado cuando haga doble clic en el ícono del objeto OLE.

El siguiente ejemplo muestra cómo agregar un objeto OLE a una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Extracción de objetos OLE en el libro de trabajo**

El siguiente ejemplo muestra cómo extraer objetos OLE en un libro de trabajo. El ejemplo obtiene diferentes objetos OLE de un archivo XLS existente y guarda diferentes archivos (DOC, XLS, PPT, PDF, etc.) basándose en el tipo de formato de archivo del objeto OLE.

Aquí está la captura de pantalla del archivo XLS de plantilla, que tiene diferentes objetos OLE incrustados en la primera hoja de cálculo.

**El archivo de plantilla contiene cuatro objetos OLE** 

![todo:image_alt_text](managing-ole-objects_1.png)

Después de ejecutar el código, podemos guardar diferentes archivos basados en sus respectivos tipos de formato de objetos OLE. A continuación se muestran capturas de pantalla de algunos de los archivos creados.

**El archivo XLS extraído** 

![todo:image_alt_text](managing-ole-objects_2.png)

**El archivo PPT extraído** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Extrayendo archivo MOL incrustado**

Aspose.Cells soporta la extracción de objetos de tipos poco comunes como MOL (archivo de datos moleculares que contiene información sobre átomos y enlaces). El siguiente fragmento de código demuestra extraer un archivo MOL incrustado y guardarlo en el disco utilizando este [archivo de Excel de muestra](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Temas avanzados**
- [Acceder y Modificar la Etiqueta de Visualización del Objeto Ole Vinculado](/cells/es/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Actualizar automáticamente el objeto OLE a través de Microsoft Excel usando Aspose.Cells](/cells/es/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraer objetos OLE del libro de trabajo](/cells/es/java/extract-ole-objects-from-workbook/)
- [Obtener o establecer el identificador de clase del objeto OLE incrustado](/cells/es/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
