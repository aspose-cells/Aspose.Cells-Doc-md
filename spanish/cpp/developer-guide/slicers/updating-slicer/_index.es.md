---
title: Actualización del Segmentador con C++
linktitle: Actualización de Slicer
type: docs
weight: 50
url: /es/cpp/updating-slicer/
description: Este artículo muestra cómo actualizar tablas dinámicas vinculadas actualizando el segmentador usando la API Aspose.Cells for C++.
keywords: Aspose.Cells C++ Actualizar segmentador, C++ cómo cambiar el segmentador, cómo ajustar el segmentador en C++, cómo seleccionar o deseleccionar los elementos del segmentador.
---

## **Escenarios de uso posibles**

Si desea actualizar un segmentador en Microsoft Excel, selecciónelo o deseleccione sus elementos, y luego actualizará la tabla del segmentador o la tabla dinámica en consecuencia. Utilice [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercache/getslicercacheitems/) para seleccionar o deseleccionar elementos del segmentador con Aspose.Cells y luego llame al método [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) para actualizar la tabla del segmentador o la tabla dinámica.

## **Cómo actualizar filtro**

El siguiente código de muestra carga el [archivo Excel de muestra](67338475.xlsx) que contiene un filtro existente. Desactiva los elementos 2 y 3 del filtro y actualiza el filtro. Luego guarda el libro de trabajo como [archivo Excel de salida](67338476.xlsx). La captura de pantalla siguiente muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, al actualizar el filtro con los elementos seleccionados también se ha actualizado la tabla dinámica correspondientemente.

![todo:image_alt_text](updating-slicer_1.png)

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);

    // Access the slicer items.
    SlicerCacheItemCollection scItems = slicer.GetSlicerCache().GetSlicerCacheItems();

    SlicerCacheItemCollection items = slicer.GetSlicerCache().GetSlicerCacheItems();

    for (int i = 0; i < items.GetCount(); ++i)
    {
        SlicerCacheItem item = items.Get(i);
        if (item.GetValue() == u"Pink" || item.GetValue() == u"Green")
        {
            item.SetSelected(false);
        }
    }

    slicer.Refresh();

    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
