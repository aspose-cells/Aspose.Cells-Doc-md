---
title: Crear tablas dinámicas y gráficos dinámicos con C++
linktitle: Crear tablas dinámicas y gráficos dinámicos
type: docs
weight: 20
url: /es/cpp/create-pivot-tables-and-pivot-charts/
description: Aprende cómo crear tablas dinámicas y gráficos dinámicos en archivos de Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Una tabla dinámica es un resumen interactivo de registros. Por ejemplo, puedes tener cientos de entradas de facturas en una lista en una hoja de cálculo. Una tabla dinámica puede sumar las facturas por cliente, producto o fecha. Con Microsoft Excel, es posible reorganizar rápidamente la información en la tabla dinámica arrastrando botones a una nueva posición.

Un gráfico dinámico es una representación gráfica interactiva de los datos en una tabla dinámica. Los gráficos dinámicos se introdujeron en Excel 2000. El uso de un gráfico dinámico facilita aún más la comprensión de los datos, ya que la tabla dinámica crea subtotales y totales automáticamente.

Aspose.Cells admite [tablas dinámicas](/cells/es/cpp/create-pivot-tables-and-pivot-charts/) y [gráficos dinámicos](/cells/es/cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Añadiendo tablas dinámicas y gráficos**

Aspose.Cells proporciona un conjunto especial de clases utilizadas para crear tablas dinámicas. Estas clases se utilizan para crear y configurar objetos PivotTable, que actúan como bloques de construcción básicos de un objeto PivotTable:

- **CampoDinámico**, un campo en un informe de tabla dinámica.
- **CamposDinámicos**, una colección de todos los objetos CampoDinámico en una tabla dinámica.
- **TablaDinámica**, un informe de TablaDinámica en una hoja de cálculo.
- **TablasDinámicas**, una colección de todos los objetos TablaDinámica en la hoja de cálculo.

### **Preparación para usar Aspose.Cells**

1. Descargue e instale Aspose.Cells:
   1. [Descarga Aspose.Cells](https://downloads.aspose.com/cells/cpp).
   1. Instálelo en su equipo de desarrollo.
      Todos los componentes de [Aspose](http://www.aspose.com/), al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos. Para trabajar con el componente en su capacidad total, necesitas tener una licencia válida.
1. Cree un proyecto:
   1. Inicia tu entorno de desarrollo C++ (por ejemplo, Visual Studio).
   1. Cree una nueva aplicación de consola.
1. Agregue referencias:
   Agrega una referencia al componente Aspose.Cells en tu proyecto, por ejemplo, `...\Archivos de programa\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Añadiendo una tabla dinámica**

Para crear una tabla dinámica usando Aspose.Cells:

1. Agrega algunos datos a las celdas de una hoja de cálculo usando el método `PutValue` de un objeto `Cell`. También puedes usar un archivo de plantilla ya llenado con datos. Los datos se usarán como fuente de datos para la tabla dinámica.
1. Agrega una tabla dinámica a la hoja llamando al método `Add` de la colección `PivotTables` (encapsulada en el objeto `Worksheet`).
1. Accede al nuevo objeto `PivotTable` desde la colección `PivotTables` pasando su índice. Usa cualquiera de los objetos de tabla dinámica encapsulados en el objeto `PivotTable` para gestionar la tabla.

A continuación se muestran ejemplos de código.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Name the sheet
    sheet.SetName(u"Data");

    // Get the cells collection
    Cells cells = sheet.GetCells();

    // Set values to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Employee");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Quarter");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Product");
    cell = cells.Get(u"D1");
    cell.PutValue(u"Continent");
    cell = cells.Get(u"E1");
    cell.PutValue(u"Country");
    cell = cells.Get(u"F1");
    cell.PutValue(u"Sale");

    // Fill employee names
    cell = cells.Get(u"A2");
    cell.PutValue(u"David");
    cell = cells.Get(u"A3");
    cell.PutValue(u"David");
    cell = cells.Get(u"A4");
    cell.PutValue(u"David");
    cell = cells.Get(u"A5");
    cell.PutValue(u"David");
    cell = cells.Get(u"A6");
    cell.PutValue(u"James");
    cell = cells.Get(u"A7");
    cell.PutValue(u"James");
    cell = cells.Get(u"A8");
    cell.PutValue(u"James");
    cell = cells.Get(u"A9");
    cell.PutValue(u"James");
    cell = cells.Get(u"A10");
    cell.PutValue(u"James");
    cell = cells.Get(u"A11");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A12");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A13");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A14");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A15");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A16");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A17");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A18");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A19");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A20");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A21");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A22");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A23");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A24");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A25");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A26");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A27");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A28");
    cell.PutValue(u"Ada");
    cell = cells.Get(u"A29");
    cell.PutValue(u"Ada");
    cell = cells.Get(u"A30");
    cell.PutValue(u"Ada");

    // Fill quarters
    cell = cells.Get(u"B2");
    cell.PutValue(1);
    cell = cells.Get(u"B3");
    cell.PutValue(2);
    cell = cells.Get(u"B4");
    cell.PutValue(3);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(1);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(3);
    cell = cells.Get(u"B9");
    cell.PutValue(4);
    cell = cells.Get(u"B10");
    cell.PutValue(4);
    cell = cells.Get(u"B11");
    cell.PutValue(1);
    cell = cells.Get(u"B12");
    cell.PutValue(1);
    cell = cells.Get(u"B13");
    cell.PutValue(2);
    cell = cells.Get(u"B14");
    cell.PutValue(2);
    cell = cells.Get(u"B15");
    cell.PutValue(3);
    cell = cells.Get(u"B16");
    cell.PutValue(4);
    cell = cells.Get(u"B17");
    cell.PutValue(4);
    cell = cells.Get(u"B18");
    cell.PutValue(1);
    cell = cells.Get(u"B19");
    cell.PutValue(1);
    cell = cells.Get(u"B20");
    cell.PutValue(2);
    cell = cells.Get(u"B21");
    cell.PutValue(3);
    cell = cells.Get(u"B22");
    cell.PutValue(3);
    cell = cells.Get(u"B23");
    cell.PutValue(4);
    cell = cells.Get(u"B24");
    cell.PutValue(4);
    cell = cells.Get(u"B25");
    cell.PutValue(1);
    cell = cells.Get(u"B26");
    cell.PutValue(2);
    cell = cells.Get(u"B27");
    cell.PutValue(3);
    cell = cells.Get(u"B28");
    cell.PutValue(1);
    cell = cells.Get(u"B29");
    cell.PutValue(2);
    cell = cells.Get(u"B30");
    cell.PutValue(3);

    // Fill products
    cell = cells.Get(u"C2");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C3");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C4");
    cell.PutValue(u"Chai");
    cell = cells.Get(u"C5");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C6");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C7");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C8");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C9");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C10");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C11");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C12");
    cell.PutValue(u"Chai");
    cell = cells.Get(u"C13");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C14");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C15");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C16");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C17");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C18");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C19");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C20");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C21");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C22");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C23");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C24");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C25");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C26");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C27");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C28");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C29");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C30");
    cell.PutValue(u"Chocolade");

    // Fill continents
    cell = cells.Get(u"D2");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D3");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D4");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D5");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D6");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D7");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D8");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D9");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D10");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D11");
    cell.PutValue(u"America");
    cell = cells.Get(u"D12");
    cell.PutValue(u"America");
    cell = cells.Get(u"D13");
    cell.PutValue(u"America");
    cell = cells.Get(u"D14");
    cell.PutValue(u"America");
    cell = cells.Get(u"D15");
    cell.PutValue(u"America");
    cell = cells.Get(u"D16");
    cell.PutValue(u"America");
    cell = cells.Get(u"D17");
    cell.PutValue(u"America");
    cell = cells.Get(u"D18");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D19");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D20");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D21");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D22");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D23");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D24");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D25");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D26");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D27");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D28");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D29");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D30");
    cell.PutValue(u"Africa");

    // Fill countries
    cell = cells.Get(u"E2");
    cell.PutValue(u"China");
    cell = cells.Get(u"E3");
    cell.PutValue(u"India");
    cell = cells.Get(u"E4");
    cell.PutValue(u"Korea");
    cell = cells.Get(u"E5");
    cell.PutValue(u"India");
    cell = cells.Get(u"E6");
    cell.PutValue(u"France");
    cell = cells.Get(u"E7");
    cell.PutValue(u"France");
    cell = cells.Get(u"E8");
    cell.PutValue(u"Germany");
    cell = cells.Get(u"E9");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E10");
    cell.PutValue(u"France");
    cell = cells.Get(u"E11");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E12");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E13");
    cell.PutValue(u"Brazil");
    cell = cells.Get(u"E14");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E15");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E16");
    cell.PutValue(u"Canada");
    cell = cells.Get(u"E17");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E18");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E19");
    cell.PutValue(u"France");
    cell = cells.Get(u"E20");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E21");
    cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E22");
    cell.PutValue(u"Australia");
    cell = cells.Get(u"E23");
    cell.PutValue(u"Australia");
    cell = cells.Get(u"E24");
    cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E25");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E26");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E27");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E28");
    cell.PutValue(u"Egypt");
    cell = cells.Get(u"E29");
    cell.PutValue(u"Egypt");
    cell = cells.Get(u"E30");
    cell.PutValue(u"Egypt");

    // Fill sales
    cell = cells.Get(u"F2");
    cell.PutValue(2000);
    cell = cells.Get(u"F3");
    cell.PutValue(500);
    cell = cells.Get(u"F4");
    cell.PutValue(1200);
    cell = cells.Get(u"F5");
    cell.PutValue(1500);
    cell = cells.Get(u"F6");
    cell.PutValue(500);
    cell = cells.Get(u"F7");
    cell.PutValue(1500);
    cell = cells.Get(u"F8");
    cell.PutValue(800);
    cell = cells.Get(u"F9");
    cell.PutValue(900);
    cell = cells.Get(u"F10");
    cell.PutValue(500);
    cell = cells.Get(u"F11");
    cell.PutValue(1600);
    cell = cells.Get(u"F12");
    cell.PutValue(600);
    cell = cells.Get(u"F13");
    cell.PutValue(2000);
    cell = cells.Get(u"F14");
    cell.PutValue(500);
    cell = cells.Get(u"F15");
    cell.PutValue(900);
    cell = cells.Get(u"F16");
    cell.PutValue(700);
    cell = cells.Get(u"F17");
    cell.PutValue(1400);
    cell = cells.Get(u"F18");
    cell.PutValue(1350);
    cell = cells.Get(u"F19");
    cell.PutValue(300);
    cell = cells.Get(u"F20");
    cell.PutValue(500);
    cell = cells.Get(u"F21");
    cell.PutValue(1000);
    cell = cells.Get(u"F22");
    cell.PutValue(1500);
    cell = cells.Get(u"F23");
    cell.PutValue(1500);
    cell = cells.Get(u"F24");
    cell.PutValue(1600);
    cell = cells.Get(u"F25");
    cell.PutValue(1000);
    cell = cells.Get(u"F26");
    cell.PutValue(1200);
    cell = cells.Get(u"F27");
    cell.PutValue(1300);
    cell = cells.Get(u"F28");
    cell.PutValue(1500);
    cell = cells.Get(u"F29");
    cell.PutValue(1400);
    cell = cells.Get(u"F30");
    cell.PutValue(1000);

    // Add a new sheet
    Worksheet sheet2 = workbook.GetWorksheets().Get(workbook.GetWorksheets().Add());
    sheet2.SetName(u"PivotTable");

    // Get the pivot tables collection
    PivotTableCollection pivotTables = sheet2.GetPivotTables();

    // Add a pivot table
    int index = pivotTables.Add(u"=Data!A1:F30", u"B3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    // Show grand totals
    pivotTable.SetShowRowGrandTotals(true);
    pivotTable.SetShowColumnGrandTotals(true);

    // Set auto format
    pivotTable.SetIsAutoFormat(true);
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report6);

    // Add fields to row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 1);

    // Add fields to column area
    pivotTable.AddFieldToArea(PivotFieldType::Column, 3);

    // Add fields to data area
    pivotTable.AddFieldToArea(PivotFieldType::Data, 5);

    // Set number format for the first data field
    pivotTable.GetDataFields().Get(0).SetNumberFormat(u"$#,##0.00");

    // Save the workbook
    workbook.Save(outDir + u"pivotTable_test.out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Añadiendo un gráfico dinámico**

Para crear un gráfico dinámico usando Aspose.Cells:

1. Agregue un gráfico.
1. Establece el `PivotSource` del gráfico para hacer referencia a una tabla dinámica existente en la hoja de cálculo.
1. Establezca otros atributos.

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivotTable_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"pivotChart_test_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Adding a new sheet
    Worksheet sheet3 = workbook.GetWorksheets().Get(workbook.GetWorksheets().Add(SheetType::Chart));

    // Naming the sheet
    sheet3.SetName(u"PivotChart");

    // Adding a column chart
    int index = sheet3.GetCharts().Add(ChartType::Column, 0, 5, 28, 16);

    // Setting the pivot chart data source
    sheet3.GetCharts().Get(index).SetPivotSource(u"PivotTable!PivotTable1");
    sheet3.GetCharts().Get(index).SetHidePivotFieldButtons(false);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
