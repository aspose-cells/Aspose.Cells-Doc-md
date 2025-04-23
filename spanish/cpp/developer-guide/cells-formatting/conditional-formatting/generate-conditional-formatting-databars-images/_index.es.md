---
title: Generar imágenes de barras de formato condicional con C++
linktitle: Generar imágenes de barras de datos de formato condicional
description: Aspose.Cells es una biblioteca en C++ para trabajar con archivos de hojas de cálculo. Soporta la generación de barras de datos y imágenes con formato condicional, permitiendo a los usuarios personalizar la visualización de la hoja de cálculo en función del valor de las celdas. Este artículo introducirá cómo usar la biblioteca Aspose.Cells para generar barras de datos e imágenes con formato condicional.
keywords: Aspose.Cells, Formato condicional, Barras de datos, Imágenes, Hojas de cálculo
type: docs
weight: 40
url: /es/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

A veces, necesita generar imágenes de barras de datos de formato condicional. Puede utilizar el método [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) de Aspose.Cells para generar estas imágenes. Este artículo muestra cómo generar una imagen de barra de datos usando Aspose.Cells.

{{% /alert %}}

El siguiente código de ejemplo genera la imagen DataBar de la celda C1. Primero, accede al objeto de condición de formato de la celda, y desde ese objeto, accede al objeto [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/) y usa su método [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) para generar la imagen de la celda. Finalmente, guarda la imagen en disco.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
