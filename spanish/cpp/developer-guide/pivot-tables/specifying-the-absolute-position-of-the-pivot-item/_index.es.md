---
title: Especificando la posición absoluta del ítem de pivote con C++
linktitle: Especificar la posición absoluta del elemento de la tabla dinámica
type: docs
weight: 50
url: /es/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Aprende cómo especificar la posición absoluta de los ítems de pivote en C++ usando Aspose.Cells.
---

{{% alert color="primary" %}}

A veces, los usuarios necesitan especificar la posición absoluta de los ítems de pivote. La API de Aspose.Cells ha expuesto algunas propiedades nuevas y un método para lograr este requisito.

- Se agregó la propiedad [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/) que se puede usar para especificar el índice de posición en todos los PivotItems independientemente del nodo padre. Se agregó la propiedad [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) que se puede utilizar para especificar el índice de posición en los PivotItems bajo el mismo nodo padre.
- Se añadió el método [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) para mover el ítem hacia arriba o abajo basado en un valor de conteo, donde el contador es la cantidad de posiciones para mover el PivotItem hacia arriba o abajo. Si el valor del conteo es menor que cero, el ítem se moverá hacia arriba; si el valor es mayor que cero, el PivotItem se moverá hacia abajo. El parámetro booleano `isSameParent` especifica si la operación de movimiento debe realizarse en el mismo nodo padre o no.
- El método `PivotItem.Move(int count)` ha quedado obsoleto; por lo tanto, se recomienda usar el método [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) recién añadido.

{{% /alert %}}

El siguiente código de ejemplo crea una tabla dinámica y luego especifica las posiciones de los ítems de pivote en el mismo nodo padre. Puedes descargar los archivos de Excel [original](5112632.xlsx) y [de salida](5112619.xlsx) para referencia. Si abres el archivo Excel de salida, verás que el ítem de pivote "4H12" está en la posición 0 en el padre "K11" y "DIF400" está en la posición 3. De manera similar, CA32 está en la posición 1 y AAA3 en la posición 2.

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

    // Create workbook
    Workbook wb(srcDir + u"source.xlsx");

    // Add new worksheet for pivot table
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet wsPivot = worksheets.Add(u"pvtNew Hardware");
    Worksheet wsData = worksheets.Get(u"New Hardware - Yearly");

    // Get the pivot tables collection for the pivot sheet
    PivotTableCollection pivotTables = wsPivot.GetPivotTables();

    // Add PivotTable to the worksheet
    int index = pivotTables.Add(u"='New Hardware - Yearly'!A1:D621", u"A3", u"HWCounts_PivotTable");

    // Get the PivotTable object
    PivotTable pvtTable = pivotTables.Get(index);

    // Add vendor row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Vendor");

    // Add item row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Item");

    // Add data field
    pvtTable.AddFieldToArea(PivotFieldType::Data, u"2014");

    // Turn off the subtotals for the vendor row field
    PivotField pivotField = pvtTable.GetRowFields().Get(u"Vendor");
    pivotField.SetSubtotals(PivotFieldSubtotalType::None, true);

    // Turn off grand total
    pvtTable.SetShowColumnGrandTotals(false);

    // Refresh and calculate data before modifying pivot items
    pvtTable.RefreshData();
    pvtTable.CalculateData();

    // Set positions for specific pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"4H12").SetPositionInSameParentNode(0);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"DIF400").SetPositionInSameParentNode(3);

    // Recalculate data after modifying pivot items
    pvtTable.CalculateData();

    // Set positions for additional pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"CA32").SetPositionInSameParentNode(1);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"AAA3").SetPositionInSameParentNode(2);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Ten en cuenta que es necesario llamar a los métodos `PivotTable.RefreshData` y `PivotTable.CalculateData` antes de usar [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) y [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
