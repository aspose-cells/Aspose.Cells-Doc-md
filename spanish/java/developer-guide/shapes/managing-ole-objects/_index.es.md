---
title: Gestión de objetos OLE
type: docs
weight: 30
url: /es/java/managing-ole-objects/
---
## **Introducción**

OLE (Vinculación e incrustación de objetos) es el marco de trabajo de Microsoft para una tecnología de documentos compuestos. Brevemente, un documento compuesto es algo así como un escritorio de visualización que puede contener objetos visuales y de información de todo tipo: texto, calendarios, animaciones, sonido, video en movimiento, 3D, noticias continuamente actualizadas, controles, etc. Cada objeto de escritorio es una entidad de programa independiente que puede interactuar con un usuario y también comunicarse con otros objetos en el escritorio.

 OLE (Vinculación e incrustación de objetos) es compatible con muchos programas diferentes y se utiliza para hacer que el contenido creado en un programa esté disponible en otro. Por ejemplo, puede insertar un documento de Word Microsoft en Excel Microsoft. Para ver qué tipos de contenido puede insertar, haga clic en**Objeto** sobre el**Insertar** menú. Solo los programas que están instalados en la computadora y que admiten objetos OLE aparecen en el**Tipo de objeto** caja.

## **Insertar objetos OLE en una hoja de trabajo**

Aspose.Cells admite agregar, extraer y manipular objetos OLE en hojas de trabajo. Por esta razón, Aspose.Cells tiene la[**OleObjectCollectionOleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)clase, utilizada para agregar un nuevo objeto OLE a la lista de recopilación. Otra clase,[**Objeto OLE**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), representa un objeto OLE. Tiene algunos miembros importantes:

- [**Datos de imagen**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData)especifica los datos de la imagen (icono) del tipo de matriz de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de trabajo.
- [**ObjetoDatos**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData)especifica los datos del objeto en forma de matriz de bytes. Estos datos se mostrarán en su programa relacionado cuando haga doble clic en el icono Objeto OLE.

El siguiente ejemplo muestra cómo agregar un objeto OLE a una hoja de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Extracción de objetos OLE en el libro de trabajo**

El siguiente ejemplo muestra cómo extraer objetos OLE en un libro de trabajo. El ejemplo obtiene diferentes objetos OLE de un archivo XLS existente y guarda diferentes archivos (DOC, XLS, PPT, PDF, etc.) según el tipo de formato de archivo del objeto OLE.

Aquí está la captura de pantalla del archivo XLS de plantilla, tiene diferentes objetos OLE incrustados en la primera hoja de trabajo.

**El archivo de plantilla contiene cuatro objetos OLE** 

![todo:imagen_alternativa_texto](managing-ole-objects_1.png)

Después de ejecutar el código, podemos guardar diferentes archivos en función de sus respectivos tipos de formato de objetos OLE. Las siguientes son capturas de pantalla de algunos de los archivos creados.

**El archivo XLS extraído** 

![todo:imagen_alternativa_texto](managing-ole-objects_2.png)

**El archivo PPT extraído** 

![todo:imagen_alternativa_texto](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Extracción de archivos MOL integrados**

Aspose.Cells admite la extracción de objetos de tipos poco comunes como MOL (archivo de datos moleculares que contiene información sobre átomos y enlaces). El siguiente fragmento de código muestra cómo extraer un archivo MOL incrustado y guardarlo en el disco usando este[ejemplo de archivo de Excel](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Temas avanzados**
- [Acceder y modificar la etiqueta de visualización del objeto Ole vinculado](/cells/es/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Actualizar automáticamente el objeto OLE a través de Microsoft Excel usando Aspose.Cells](/cells/es/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraer objetos OLE del libro de trabajo](/cells/es/java/extract-ole-objects-from-workbook/)
- [Obtener o establecer el identificador de clase del objeto OLE incrustado](/cells/es/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
