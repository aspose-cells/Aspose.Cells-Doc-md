---
title: Usar partes de XML personalizado en Aspose.Cells con C++
linktitle: Usar partes de XML personalizado
type: docs
weight: 390
url: /es/cpp/use-custom-xml-parts-in-aspose-cells/
description: Aprende cómo usar partes de XML personalizadas en archivos de Excel de forma programática usando Aspose.Cells con C++.
---

## Usando Partes XML Personalizadas en Aspose.Cells

Las partes de XML personalizadas son datos XML almacenados por diferentes aplicaciones como SharePoint dentro de un archivo de Excel. Estos datos son consumidos por varias aplicaciones que lo requieren. Microsoft Excel no utiliza estos datos, por lo que no hay interfaz gráfica para agregarlos. Puedes ver estos datos cambiando la extensión de **.xlsx** a **.zip** y abriéndolos con **WinZip**. También puedes abrir el archivo ZIP usando cualquier utilidad de compresión de Windows de terceros como WinRAR o WinZip. Los datos están presentes dentro de la carpeta **customXml**.

Puedes agregar partes XML personalizadas usando Aspose.Cells a través del método [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/).

El siguiente código de ejemplo usa el método [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) para agregar el **XML del Catálogo de Libros**, y su nombre es **BookStore**. La siguiente imagen muestra el resultado de este código. Como puedes ver, el XML del Catálogo de Libros se añadió dentro del nodo BookStore, que es el nombre de esta propiedad.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Código C++ para usar partes de XML personalizado

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // The sample XML that will be injected to Workbook
    U16String booksXML = uR"(<catalog>
   <book>
      <title>Complete C#</title>
      <price>44</price>
   </book>
   <book>
      <title>Complete Java</title>
      <price>76</price>
   </book>
   <book>
      <title>Complete SharePoint</title>
      <price>55</price>
   </book>
   <book>
      <title>Complete PHP</title>
      <price>63</price>
   </book>
   <book>
      <title>Complete VB.NET</title>
      <price>72</price>
   </book>
</catalog>)";

    // Create an instance of Workbook class
    Workbook workbook;

    // Add Custom XML Part to ContentTypePropertyCollection
    workbook.GetContentTypeProperties().Add(u"BookStore", booksXML);

    // Save the resultant spreadsheet
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Custom XML part added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Artículo Relacionado

- [Agregar propiedades personalizadas visibles en el panel de información del documento](/cells/es/cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="cpp" >}}
