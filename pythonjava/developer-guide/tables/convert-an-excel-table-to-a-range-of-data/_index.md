---
title: Convert an Excel Table to a Range of Data
type: docs
weight: 10
url: /python-java/convert-an-excel-table-to-a-range-of-data/
---

## **Convert an Excel Table to a Range of Data**
Aspose.Cells for Python via Java provides the option to convert Excel Table to a range of data. For this, the API provides the [ListObject.convertToRange](https://apireference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) method. The following code snippet demonstrates the use of [ListObject.convertToRange](https://apireference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) method to convert an Excel table to a range of data.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Convert an Excel Table to a Range with Options**
You may provide additional options while converting a table to a range with the [TableToRangeOptions](https://apireference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) class. You may pass an instance of the [TableToRangeOptions](https://apireference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) class to the [ListObject.convertToRange](https://apireference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) method to specify additional options. The following code snippet demonstrates the use of the [TableToRangeOptions](https://apireference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) class to set the last row index of the table. The table formatting will be retained up to the specified row index and the rest of the formatting will be removed.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
