---
title: Gestión de objetos OLE
type: docs
weight: 50
url: /es/python-net/managing-ole-objects/
---

## **Introducción**

OLE (Object Linking and Embedding) es el marco de Microsoft para una tecnología de documento compuesto. En resumen, un documento compuesto es algo similar a un escritorio de visualización que puede contener objetos visuales e informativos de todo tipo: texto, calendarios, animaciones, sonido, video en movimiento, 3D, noticias actualizadas continuamente, controles, y mucho más. Cada objeto de escritorio es una entidad de programa independiente que puede interactuar con un usuario y también comunicarse con otros objetos en el escritorio.

OLE (Object Linking and Embedding) es compatible con muchos programas diferentes y se utiliza para hacer que el contenido creado en un programa esté disponible en otro. Por ejemplo, puedes insertar un documento de Microsoft Word en Microsoft Excel. Para ver qué tipos de contenido puedes insertar, haz clic en **Objeto** en el menú **Insertar**. Solo aparecen en el cuadro **Tipo de objeto** los programas instalados en el equipo y que admiten objetos OLE.

### **Inserción de objetos OLE en la hoja de cálculo**

Aspose.Cells para Python via .NET soporta añadir, extraer y manipular objetos OLE en hojas de cálculo. Por ello, Aspose.Cells para Python via .NET tiene la clase [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection), utilizada para agregar un nuevo objeto OLE a la lista de colección. Otra clase, [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), representa un objeto OLE. Tiene algunos miembros importantes:

- La propiedad [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) especifica los datos de imagen (icono) de tipo matriz de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de cálculo.
- La propiedad [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) especifica los datos del objeto en forma de matriz de bytes. Estos datos se mostrarán en su programa relacionado cuando hagas doble clic en el ícono del objeto OLE.

El siguiente ejemplo muestra cómo agregar un objeto(s) OLE a una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **Extracción de objetos OLE en el libro de trabajo**

El siguiente ejemplo muestra cómo extraer objetos OLE en un libro de trabajo. El ejemplo obtiene diferentes objetos OLE de un archivo XLS existente y guarda diferentes archivos (DOC, XLS, PPT, PDF, etc.) basándose en el tipo de formato de archivo del objeto OLE.

Después de ejecutar el código, podemos guardar diferentes archivos basados en sus respectivos tipos de formato de objetos OLE.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **Extrayendo archivo MOL incrustado**

Aspose.Cells para Python via .NET admite extraer objetos de tipos poco comunes como MOL (archivo de datos molecular que contiene información sobre átomos y enlaces). El siguiente fragmento de código demuestra cómo extraer un archivo MOL incrustado y guardarlo en disco usando este [archivo de Excel de ejemplo](94896196.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **Temas avanzados**
- [Acceder y Modificar la Etiqueta de Visualización del Objeto Ole Vinculado](/cells/es/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Actualizar automáticamente el objeto OLE](/cells/es/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraer objetos OLE del libro de trabajo](/cells/es/python-net/extract-ole-objects-from-workbook/)
- [Obtener o establecer el identificador de clase del objeto OLE incrustado](/cells/es/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Insertar un archivo WAV como un objeto OLE](/cells/es/python-net/inserting-a-wav-file-as-an-ole-object/)

{{< app/cells/assistant language="python-net" >}}
