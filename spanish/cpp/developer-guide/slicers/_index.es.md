---
title: Insertar Segmentador con C++
linktitle: Rebanadores
type: docs
weight: 170
url: /es/cpp/create-slicer/
description: Gestionar segmentadores de archivos de Excel con Aspose.Cells usando C++.
---

## **Escenarios de uso posibles**

Un segmentador se usa para filtrar datos rápidamente. Puede ser utilizado para filtrar datos tanto en una tabla como en una tabla dinámica. Microsoft Excel permite crear un segmentador seleccionando una tabla o tabla dinámica y luego haciendo clic en *Insertar > Segmentador*. Aspose.Cells también te permite crear un segmentador usando el método [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/).

## **Crear Cortador para una Tabla Dinámica**

Por favor, consulte el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](67338470.xlsx) que contiene la tabla dinámica. Luego crea el rebanador basado en el primer campo de la tabla pivote. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](67338471.xlsx) y [XLSB de salida](67338472.xlsb). La siguiente captura de pantalla muestra el rebanador creado por Aspose.Cells en el archivo de Excel de salida.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Crear Cortador para Tabla de Excel**

Por favor, consulte el siguiente código de ejemplo. Carga el [archivo de Excel de muestra](sampleCreateSlicerToExcelTable.xlsx) que contiene una tabla. Luego crea el rebanador basado en la primera columna. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](outputCreateSlicerToExcelTable.xlsx).

### **Código de muestra**

```cpp
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

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas Avanzados**
- [Cambiar propiedades del rebanador](/cells/es/cpp/change-slicer-properties/)
- [Dibujar un rebanador al renderizar Excel a PDF](/cells/es/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [ Formatear rebanador](/cells/es/cpp/formatting-slicer/)
- [Eliminar rebanador](/cells/es/cpp/removing-slicer/)
- [Renderización de rebanador](/cells/es/cpp/rendering-slicer/)
- [Actualización de rebanador](/cells/es/cpp/updating-slicer/)
