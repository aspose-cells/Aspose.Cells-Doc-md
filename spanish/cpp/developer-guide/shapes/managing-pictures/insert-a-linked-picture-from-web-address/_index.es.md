---
title: Insertar una imagen vinculada desde una dirección web con C++
linktitle: Insertar una imagen vinculada desde una dirección web
type: docs
weight: 450
url: /es/cpp/insert-a-linked-picture-from-web-address/
description: Aprende cómo insertar una imagen vinculada desde una dirección web en una hoja de trabajo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces necesitas insertar una imagen desde la web (http://) en una hoja de cálculo. Para hacerlo, especifica la URL de la imagen y la imagen se descargará cada vez que se abra la hoja de cálculo en Microsoft Excel. La imagen no se incrusta físicamente en el documento de Excel, sino que apunta a un recurso web.

{{% /alert %}}

## **Usar Microsoft Excel**

En Microsoft Excel (por ejemplo, 2007):

1. Haz clic en el menú **Insertar** y selecciona **Imagen**.
1. Especifica la dirección web de la imagen en el cuadro de diálogo Insertar Imagen.

## **Usando Aspose.Cells for C++**

Aspose.Cells for C++ soporta agregar una imagen vinculada usando el método [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/). El método devuelve un objeto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

El siguiente ejemplo muestra cómo agregar una imagen vinculada desde una dirección web a una hoja de trabajo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Insert a linked picture (from Web Address) to B2 Cell
    U16String imageUrl(u"http://www.aspose.com/Images/aspose-logo.jpg");
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddLinkedPicture(1, 1, 100, 100, imageUrl);

    // Set the height and width of the inserted image
    pic.SetHeightInch(1.04);
    pic.SetWidthInch(2.6);

    // Save the Excel file
    U16String outputPath = outDir + u"outLinkedPicture.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Linked picture inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
