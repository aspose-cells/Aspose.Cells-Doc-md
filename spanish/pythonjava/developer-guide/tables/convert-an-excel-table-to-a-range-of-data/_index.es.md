---
title: Convertir una Tabla de Excel a un Rango de Datos
type: docs
weight: 10
url: /es/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **Convertir una Tabla de Excel a un Rango de Datos**
Aspose.Cells for Python via Java proporciona la opción de convertir una tabla de Excel en un rango de datos. Para ello, la API proporciona el método [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)). El siguiente fragmento de código demuestra el uso del método [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) para convertir una tabla de Excel en un rango de datos.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Convertir una tabla de Excel a un rango con opciones**
Puede proporcionar opciones adicionales al convertir una tabla a un rango con la clase [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions). Puede pasar una instancia de la clase [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) al método [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) para especificar opciones adicionales. El siguiente fragmento de código muestra el uso de la clase [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) para establecer el índice de la última fila de la tabla. El formato de la tabla se mantendrá hasta el índice de fila especificado y el resto del formato se eliminará.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
