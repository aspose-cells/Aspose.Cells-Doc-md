##Excel Row and  Column Operations
"Excel row and column operations - insert, delete, resize, hide/unhide rows and columns with AI automation"
# Excel Row and  Column Operations
Manage **Excel row and column operations** with AI-powered automation. Insert, delete, resize, hide/unhide **Excel rows** and **columns** for perfect spreadsheet layout management.
## Available Tools
- `row_column_operations` - **Excel row/column operations** (insert, delete, resize, hide/unhide) with **AI Excel**
- `row_column_operations_batch` - Perform multiple **Excel row/column operations** in batch using **Excel MCP**
## Single Operations
### Insert Rows
```json
{
"tool": "row_column_operations",
"parameters": {
"filepath": "reports/layout-test.xlsx",
"sheet_name": "Data",
"operation": "insert_rows",
"rows": "5",
"count": 2
}
}
```
### Delete Columns
```json
{
"tool": "row_column_operations",
"parameters": {
"filepath": "reports/cleanup.xlsx",
"sheet_name": "Sheet1",
"operation": "delete_columns",
"columns": "C:D"
}
}
```
### Set Row Height
```json
{
"tool": "row_column_operations",
"parameters": {
"filepath": "reports/formatted.xlsx",
"sheet_name": "Report",
"operation": "set_row_height",
"rows": "1",
"height": 30
}
}
```
### Set Column Width
```json
{
"tool": "row_column_operations",
"parameters": {
"filepath": "reports/formatted.xlsx",
"sheet_name": "Report",
"operation": "set_column_width",
"columns": "A:F",
"width": 15
}
}
```
## Batch Operations
### Comprehensive Layout Setup
```json
{
"tool": "row_column_operations_batch",
"parameters": {
"filepath": "reports/professional-layout.xlsx",
"sheet_name": "Summary Report",
"operations": [
{
"operation": "set_row_height",
"rows": "3",
"height": 30
},
{
"operation": "set_row_height",
"rows": "4:6",
"height": 20
},
{
"operation": "set_column_width",
"columns": "C",
"width": 20
},
{
"operation": "set_column_width",
"columns": "D:G",
"width": 15
},
{
"operation": "auto_fit_rows",
"rows": "7:10"
}
]
}
}
```
### Insert and Delete Operations
```json
{
"tool": "row_column_operations_batch",
"parameters": {
"filepath": "reports/restructure.xlsx",
"sheet_name": "Sheet1",
"operations": [
{
"operation": "insert_rows",
"rows": "5",
"count": 2
},
{
"operation": "insert_columns",
"columns": "D",
"count": 1
},
{
"operation": "delete_rows",
"rows": "8:9"
}
]
}
}
```
### Hide and Unhide Operations
```json
{
"tool": "row_column_operations_batch",
"parameters": {
"filepath": "reports/visibility.xlsx",
"sheet_name": "Sheet1",
"operations": [
{
"operation": "hide_rows",
"rows": "15:16"
},
{
"operation": "hide_columns",
"columns": "H:I"
},
{
"operation": "unhide_rows",
"rows": "15"
},
{
"operation": "unhide_columns",
"columns": "H"
}
]
}
}
```
### Auto-Fit Operations
```json
{
"tool": "row_column_operations_batch",
"parameters": {
"filepath": "reports/auto-sized.xlsx",
"sheet_name": "Data",
"operations": [
{
"operation": "auto_fit_columns",
"columns": "A:F"
},
{
"operation": "auto_fit_rows",
"rows": "1:20"
}
]
}
}
```
## Operation Types Reference
### Insert Operations
- `insert_rows` - Insert new rows at specified position
- `insert_columns` - Insert new columns at specified position
### Delete Operations
- `delete_rows` - Delete specified rows
- `delete_columns` - Delete specified columns
### Resize Operations
- `set_row_height` - Set specific row height in points
- `set_column_width` - Set specific column width in characters
- `auto_fit_rows` - Auto-fit rows to content height
- `auto_fit_columns` - Auto-fit columns to content width
### Visibility Operations
- `hide_rows` - Hide specified rows
- `unhide_rows` - Show hidden rows
- `hide_columns` - Hide specified columns
- `unhide_columns` - Show hidden columns
## Range Specifications
### Row Ranges
- `"1"` - Single row (row 1)
- `"1:3"` - Range of rows (rows 1 to 3)
- `"5:10"` - Multiple consecutive rows
### Column Ranges
- `"A"` - Single column (column A)
- `"A:C"` - Range of columns (columns A to C)
- `"D:F"` - Multiple consecutive columns
## Advanced Examples
### Report Header Setup
```json
{
"tool": "row_column_operations_batch",
"parameters": {
"filepath": "reports/header-setup.xlsx",
"sheet_name": "Report",
"operations": [
{
"operation": "set_row_height",
"rows": "1:2",
"height": 35
},
{
"operation": "set_column_width",
"columns": "A",
"width": 25
},
{
"operation": "set_column_width",
"columns": "B:E",
"width": 12
},
{
"operation": "set_column_width",
"columns": "F",
"width": 18
}
]
}
}
```
### Data Table Layout
```json
{
"tool": "row_column_operations_batch",
"parameters": {
"filepath": "reports/data-table.xlsx",
"sheet_name": "Data",
"operations": [
{
"operation": "insert_rows",
"rows": "1",
"count": 1
},
{
"operation": "set_row_height",
"rows": "1",
"height": 25
},
{
"operation": "auto_fit_columns",
"columns": "A:J"
},
{
"operation": "set_row_height",
"rows": "2:100",
"height": 18
}
]
}
}
```
### Presentation Layout
```json
{
"tool": "row_column_operations_batch",
"parameters": {
"filepath": "reports/presentation.xlsx",
"sheet_name": "Summary",
"operations": [
{
"operation": "hide_columns",
"columns": "B:C"
},
{
"operation": "hide_rows",
"rows": "10:15"
},
{
"operation": "set_column_width",
"columns": "A",
"width": 30
},
{
"operation": "set_column_width",
"columns": "D:G",
"width": 15
}
]
}
}
```
## Measurement Guidelines
### Row Heights (Points)
- `15` - Default row height
- `20` - Slightly taller for readability
- `25` - Good for headers
- `30` - Large headers
- `40` - Extra large for titles
### Column Widths (Characters)
- `8` - Narrow columns (dates, codes)
- `12` - Standard data columns
- `15` - Medium text columns
- `20` - Wide text columns
- `25` - Extra wide for descriptions
- `30` - Very wide for long text
## Best Practices
1. **Header Sizing**: Make headers taller and wider for emphasis
2. **Data Consistency**: Use consistent row heights for data rows
3. **Auto-Fit**: Use auto-fit for dynamic content sizing
4. **Hide Unused**: Hide empty rows/columns for cleaner appearance
5. **Logical Grouping**: Group related resize operations in batches
## Common Patterns
### Report Setup Pattern
1. Insert title rows at top
2. Set header row height
3. Auto-fit data columns
4. Set standard data row height
5. Hide unused areas
### Data Import Pattern
1. Insert rows for new data
2. Auto-fit columns to content
3. Standardize row heights
4. Hide calculation columns
### Presentation Pattern
1. Hide detail rows/columns
2. Enlarge summary areas
3. Set presentation-friendly dimensions
4. Show only relevant data
## Error Handling
### Invalid Row Range
```json
{
"tool": "row_column_operations",
"parameters": {
"filepath": "test.xlsx",
"sheet_name": "Sheet1",
"operation": "set_row_height",
"rows": "0",
"height": 20
}
}
```
**Result**: Error - row numbers start from 1
### Invalid Column Range
```json
{
"tool": "row_column_operations",
"parameters": {
"filepath": "test.xlsx",
"sheet_name": "Sheet1",
"operation": "set_column_width",
"columns": "ZZ",
"width": 10
}
}
```
**Result**: May succeed but beyond typical usage
### Missing Required Parameters
```json
{
"tool": "row_column_operations",
"parameters": {
"filepath": "test.xlsx",
"sheet_name": "Sheet1",
"operation": "set_row_height",
"rows": "1"
}
}
```
**Result**: Error - height parameter required
