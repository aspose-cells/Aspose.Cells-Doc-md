---  
title: Mostrar página en blanco cuando no hay nada que imprimir con C++  
linktitle: Página en Blanco de Salida cuando no hay Nada que Imprimir  
type: docs  
weight: 90  
url: /es/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Manejar hojas de cálculo vacías y imprimir páginas en blanco con Aspose.Cells usando C++.  
---  

## **Escenarios de uso posibles**  

Si la hoja está vacía, entonces Aspose.Cells no imprimirá nada cuando exportes la hoja a imagen. Puedes cambiar este comportamiento usando la propiedad [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/). Cuando la configures en **true**, imprimirá la página en blanco.  

## **Página en Blanco de Salida cuando no hay Nada que Imprimir**  

El siguiente ejemplo de código crea el libro de trabajo vacío que tiene una hoja vacía y renderiza la hoja vacía a una imagen después de establecer la propiedad [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) en **true**. En consecuencia, genera la página en blanco ya que no hay nada que imprimir, como puedes ver en la imagen a continuación.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **Código de muestra**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Output directory
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet - it is an empty sheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify image or print options
    // Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
    // So that an empty page gets printed
    ImageOrPrintOptions opts;
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetOutputBlankPageWhenNothingToPrint(true);

    // Render empty sheet to png image
    SheetRender sr(ws, opts);
    sr.ToImage(0, outputDir + u"OutputBlankPageWhenNothingToPrint.png");

    std::cout << "Blank page rendered to PNG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  
{{< app/cells/assistant language="cpp" >}}
