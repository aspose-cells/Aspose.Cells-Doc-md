---
title: Specifying the Absolute Position of the Pivot Item with Python via .NET
linktitle: Specifying the Absolute Position of the Pivot Item
type: docs
weight: 50
url: /python-net/specifying-the-absolute-position-of-the-pivot-item/
description: Learn how to specify absolute positions of pivot items in Excel using Aspose.Cells for Python via .NET API with code examples.
---

{{% alert color="primary" %}}

Sometimes users need to specify the absolute position of pivot items. Aspose.Cells API provides properties and methods to achieve this:

- Added [**PivotItem.position**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotitem/#position) property to specify position index across all PivotItems regardless of parent node
- Added [**PivotItem.position_in_same_parent_node**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotitem/#position_in_same_parent_node) property to specify position index under the same parent node
- Added [**PivotItem.move(count, is_same_parent)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotitem/#move(int,bool)) method to move items up/down based on count value
- The legacy `move(count)` method is deprecated - use `move(count, is_same_parent)` instead

{{% /alert %}}

This sample code creates a pivot table and specifies pivot item positions under the same parent node. Download [source Excel](5112632.xlsx) and [output Excel](5112619.xlsx) files for reference. The output shows:
- "4H12" at position 0 under parent "K11"
- "DIF400" at position 3
- "CA32" at position 1
- "AAA3" at position 2

```python
import os
from aspose.cells import Workbook, PivotFieldType, PivotFieldSubtotalType

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

wb = Workbook(os.path.join(data_dir, "source.xlsx"))
ws_pivot = wb.worksheets.add("pvtNew Hardware")
ws_data = wb.worksheets["New Hardware - Yearly"]

# Get the pivottables collection for the pivot sheet
pivot_tables = ws_pivot.pivot_tables

# Add PivotTable to the worksheet
index = pivot_tables.add("='New Hardware - Yearly'!A1:D621", "A3", "HWCounts_PivotTable")

# Get the PivotTable object
pvt_table = pivot_tables[index]

# Add vendor row field
pvt_table.add_field_to_area(PivotFieldType.ROW, "Vendor")

# Add item row field
pvt_table.add_field_to_area(PivotFieldType.ROW, "Item")

# Add data field
pvt_table.add_field_to_area(PivotFieldType.DATA, "2014")

# Turn off the subtotals for the vendor row field
pivot_field = pvt_table.row_fields["Vendor"]
pivot_field.set_subtotals(PivotFieldSubtotalType.NONE, True)

# Turn off grand total
pvt_table.column_grand = False

# Refresh and calculate data before position manipulation
pvt_table.refresh_data()
pvt_table.calculate_data()

pvt_table.row_fields["Item"].pivot_items["4H12"].position_in_same_parent_node = 0
pvt_table.row_fields["Item"].pivot_items["DIF400"].position_in_same_parent_node = 3

# Recalculate after first position changes
pvt_table.calculate_data()

pvt_table.row_fields["Item"].pivot_items["CA32"].position_in_same_parent_node = 1
pvt_table.row_fields["Item"].pivot_items["AAA3"].position_in_same_parent_node = 2

# Save file
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb.save(os.path.join(output_dir, "output_out.xlsx"))
```

{{% alert color="primary" %}}

Important: Always call [**pivot_table.refresh_data()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/#refresh_data()) and [**pivot_table.calculate_data()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/#calculate_data()) before using position properties or move methods.

{{% /alert %}}