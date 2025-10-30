---  
title: Crear un Libro Compartido con Aspose.Cells en C++  
linktitle: Crear libro compartido con Aspose.Cells  
type: docs  
weight: 40  
url: /es/cpp/create-shared-workbook-with-aspose-cells/  
description: Aprenda cómo crear un libro compartido usando Aspose.Cells con C++.  
---  

## **Escenarios de uso posibles**  

Microsoft Excel le permite compartir el libro como se muestra en la siguiente captura. Cuando comparte el libro, más de un usuario puede editar el libro en la red. Aspose.Cells le permite crear un libro compartido con la propiedad [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Crear libro compartido con Aspose.Cells**  

El siguiente código de ejemplo crea un libro compartido estableciendo la propiedad [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/) como **true**. Cuando abras el [archivo de Excel de salida](55541786.xlsx) en Microsoft Excel, verás **Compartido** junto al nombre del libro de salida como se muestra en esta captura de pantalla.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Código de muestra**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create Workbook object
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>();

    // Share the Workbook
    wb->GetSettings().SetShared(true);

    // Save the Shared Workbook
    wb->Save(u"outputSharedWorkbook.xlsx");

    std::cout << "Shared workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
