---
title: Convertir una tabla de Excel en un rango de datos
type: docs
weight: 10
url: /es/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **Convertir una tabla de Excel en un rango de datos**
 Aspose.Cells para Python a través de Java brinda la opción de convertir la tabla de Excel en un rango de datos. Para esto, el API proporciona el[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ) método. El siguiente fragmento de código demuestra el uso de[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)para convertir una tabla de Excel en un rango de datos.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Convertir una tabla de Excel en un rango con opciones**
Puede proporcionar opciones adicionales al convertir una tabla en un rango con el[TableToRangeOptionsTableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) clase. Puede pasar una instancia de la[TableToRangeOptionsTableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)clase a la[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) para especificar opciones adicionales. El siguiente fragmento de código demuestra el uso de la[TableToRangeOptionsTableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)class para establecer el índice de la última fila de la tabla. El formato de la tabla se mantendrá hasta el índice de fila especificado y el resto del formato se eliminará.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
