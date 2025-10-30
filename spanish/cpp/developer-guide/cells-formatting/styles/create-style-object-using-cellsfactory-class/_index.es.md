---  
title: Crear objeto Style usando la clase CellsFactory con C++  
description: Aspose.Cells es una biblioteca en C++ para trabajar con archivos de hojas de cálculo que proporciona un objeto estilo para dar formato a las celdas. Este artículo presentará cómo crear un objeto de estilo de celda utilizando la clase CellsFactory en la biblioteca Aspose.Cells para que los usuarios puedan personalizar la apariencia de las celdas según sea necesario.  
keywords: Aspose.Cells, biblioteca en C++, hoja de cálculo electrónica, objeto de estilo, estilo de celda, personalización  
type: docs  
weight: 70  
url: /es/cpp/create-style-object-using-cellsfactory-class/  
---  

## **Crear objeto de estilo usando la clase CellsFactory**  
El siguiente código de ejemplo crea un objeto [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style) usando la clase [CellsFactory](https://reference.aspose.com/cells/cpp/aspose.cells/cellsfactory) y luego establece el estilo predeterminado del libro de trabajo. Por favor, descargue el [archivo de Excel de salida](5115153.xlsx) para ver los resultados de este código como referencia.  

```c++
#include <iostream>
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

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
