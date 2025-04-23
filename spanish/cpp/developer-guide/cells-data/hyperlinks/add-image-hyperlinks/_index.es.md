---
title: Agregar Hiperenlaces de Imagen con C++
linktitle: Agregar hipervínculos de imagen
type: docs
weight: 140
url: /es/cpp/add-image-hyperlinks/
description: Aprende cómo agregar Hiperenlaces de Imagen usando la API Aspose.Cells for C++.
keywords: Agregar hipervínculos de imagen, insertar hipervínculos de imagen
---

{{% alert color="primary" %}} 

Los hipervínculos son útiles para acceder a información en otras hojas de cálculo o en sitios web. Microsoft Excel permite a los usuarios agregar hipervínculos en texto en celdas y en imágenes. Los hipervínculos de imagen pueden facilitar la navegación en una hoja de cálculo, por ejemplo, como botones de siguiente y anterior, o logotipos que enlazan a sitios particulares. Este documento explica cómo insertar hipervínculos de imagen en una hoja de cálculo usando Aspose.Cells.

{{% /alert %}} 

Aspose.Cells te permite agregar hipervínculos a imágenes en hojas de cálculo en tiempo de ejecución. Es posible establecer y modificar la sugerencia en pantalla y la dirección del enlace. El siguiente código de ejemplo ilustra cómo agregar un hipervínculo de imagen a una hoja de cálculo.

```c++
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

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
