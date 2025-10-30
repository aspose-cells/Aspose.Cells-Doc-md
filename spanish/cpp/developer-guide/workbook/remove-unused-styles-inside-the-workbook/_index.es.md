---  
title: Eliminar estilos no utilizados dentro del libro con C++  
linktitle: Eliminar Estilos No Utilizados dentro del Libro de Trabajo  
type: docs  
weight: 340  
url: /es/cpp/remove-unused-styles-inside-the-workbook/  
description: Eliminar estilos no utilizados en un libro de Excel usando Aspose.Cells con C++.  
---  

{{% alert color="primary" %}}  

Los estilos no utilizados en archivos de Excel no solo ocupan espacio, sino que también causan problemas de rendimiento al convertir a diferentes formatos como PDF, HTML, etc. Aspose.Cells proporciona el método [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) para eliminar todos los estilos no utilizados dentro del libro.  

{{% /alert %}}  

El siguiente código explica el uso de [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/). El código carga el [archivo de plantilla de Excel](5115520.xlsx) que puedes descargar desde el enlace proporcionado. Contiene un estilo no utilizado llamado **AsposeStyle**; este estilo y todos los demás estilos no utilizados serán eliminados después de la ejecución del código.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load template Excel file containing unused styles
    U16String templateFilePath = srcDir + u"Template-With-Unused-Custom-Style.xlsx";
    Workbook workbook(templateFilePath);

    // Remove all unused styles inside the template
    // This will also remove AsposeStyle which is an unused style inside the template
    workbook.RemoveUnusedStyles();

    // Save the file
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Unused styles removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
