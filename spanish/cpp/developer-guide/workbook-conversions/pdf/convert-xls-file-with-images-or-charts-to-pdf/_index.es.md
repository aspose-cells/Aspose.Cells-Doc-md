---
title: Convertir archivo XLS con imágenes o gráficos a PDF con C++
linktitle: Convertir archivo XLS con imágenes o gráficos a PDF
type: docs
weight: 50
url: /es/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Convertir archivos XLS que contienen imágenes o gráficos a documentos PDF usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

 Aspose.Cells soporta convertir archivos XLS que contienen imágenes y gráficos a documentos PDF. Aspose.Cells for C++ puede funcionar de forma independiente para convertir una hoja de cálculo a PDF: no es necesario Aspose.PDF para C++ para la conversión. El proceso se puede realizar en memoria ya que no depende de archivos XML temporales o intermedios. Esto significa que archivos de Excel grandes, por ejemplo, que contienen imágenes, gráficos y otros objetos de dibujo, pueden convertirse rápida y eficientemente.

{{% /alert %}} 
## **Código de muestra**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String designerFile = srcDir + u"SampleInput.xls";

    // Path of output pdf file
    U16String pdfFile = outDir + u"Output.out.pdf";

    try
    {
        // Open the template excel file
        std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(designerFile);

        // Save the pdf file
        wb->Save(pdfFile, SaveFormat::Pdf);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}} 

 Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [Calculate(CalculationData data)](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) justo antes de renderizar a PDF. Esto asegura que los valores dependientes de las fórmulas se vuelvan a calcular y que los valores correctos se muestren en el PDF.

{{% /alert %}}
