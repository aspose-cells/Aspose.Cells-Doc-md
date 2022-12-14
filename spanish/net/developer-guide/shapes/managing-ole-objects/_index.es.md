---
title: Gestión de objetos OLE
type: docs
weight: 50
url: /es/net/managing-ole-objects/
---
## **Introducción**

OLE (Vinculación e incrustación de objetos) es el marco de trabajo de Microsoft para una tecnología de documentos compuestos. Brevemente, un documento compuesto es algo así como un escritorio de visualización que puede contener objetos visuales y de información de todo tipo: texto, calendarios, animaciones, sonido, video en movimiento, 3D, noticias continuamente actualizadas, controles, etc. Cada objeto de escritorio es una entidad de programa independiente que puede interactuar con un usuario y también comunicarse con otros objetos en el escritorio.

 OLE (Vinculación e incrustación de objetos) es compatible con muchos programas diferentes y se utiliza para hacer que el contenido creado en un programa esté disponible en otro. Por ejemplo, puede insertar un documento de Word Microsoft en Excel Microsoft. Para ver qué tipos de contenido puede insertar, haga clic en**Objeto** sobre el**Insertar** menú. Solo los programas que están instalados en la computadora y que admiten objetos OLE aparecen en el**Tipo de objeto** caja.

### **Insertar objetos OLE en la hoja de trabajo**

Aspose.Cells admite agregar, extraer y manipular objetos OLE en hojas de trabajo. Por esta razón, Aspose.Cells tiene la[**OleObjectCollectionOleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) clase, utilizada para agregar un nuevo objeto OLE a la lista de recopilación. Otra clase,[**Objeto OLE**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), representa un objeto OLE. Tiene algunos miembros importantes:

-  los[**Datos de imagen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)La propiedad especifica los datos de la imagen (icono) del tipo de matriz de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de trabajo.
-  los[**ObjetoDatos**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)La propiedad especifica los datos del objeto en forma de una matriz de bytes. Estos datos se mostrarán en su programa relacionado cuando haga doble clic en el icono Objeto OLE.

El siguiente ejemplo muestra cómo agregar objetos OLE a una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Extracción de objetos OLE en el libro de trabajo**

El siguiente ejemplo muestra cómo extraer objetos OLE en un libro de trabajo. El ejemplo obtiene diferentes objetos OLE de un archivo XLS existente y guarda diferentes archivos (DOC, XLS, PPT, PDF, etc.) según el tipo de formato de archivo del objeto OLE.

Después de ejecutar el código, podemos guardar diferentes archivos en función de sus respectivos tipos de formato de objetos OLE.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Extracción de archivos MOL integrados**

Aspose.Cells admite la extracción de objetos de tipos poco comunes como MOL (archivo de datos moleculares que contiene información sobre átomos y enlaces). El siguiente fragmento de código muestra cómo extraer un archivo MOL incrustado y guardarlo en el disco usando este[ejemplo de archivo de Excel](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Temas avanzados**
- [Acceder y modificar la etiqueta de visualización del objeto Ole vinculado](/cells/es/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Actualizar automáticamente el objeto OLE a través de Microsoft Excel usando Aspose.Cells](/cells/es/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraer objetos OLE del libro de trabajo](/cells/es/net/extract-ole-objects-from-workbook/)
- [Obtener o establecer el identificador de clase del objeto OLE incrustado](/cells/es/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Insertar un archivo WAV como un objeto Ole](/cells/es/net/inserting-a-wav-file-as-an-ole-object/)

