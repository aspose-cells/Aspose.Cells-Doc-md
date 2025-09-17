##Excel Cell Formatting
"Excel cell formatting - apply backgrounds, borders, alignment, number formats, and cell styles with AI automation"
# Excel Cell Formatting
Apply professional **Excel cell formatting** with AI-powered automation. Style **Excel cells** with backgrounds, borders, alignment, number formats, and advanced cell properties.
## Available Tools
- `cell_format` - **Excel cell formatting** (background, borders, alignment, number format) through **Excel MCP**
- `cell_format_batch` - Apply **Excel cell formatting** to multiple ranges in batch with **AI automation**
## Single Cell Formatting
### Basic Cell Styling
```json
{
"tool": "cell_format",
"parameters": {
"filepath": "reports/formatted-report.xlsx",
"sheet_name": "Data",
"range": "A1:F1",
"background_color": "#4472C4",
"horizontal_align": "center",
"vertical_align": "middle",
"border_style": "thick",
"text_wrap": true
}
}
```
### Professional Header Formatting
```json
{
"tool": "cell_format",
"parameters": {
"filepath": "reports/sales-report.xlsx",
"sheet_name": "Sales Data",
"range": "A1:F1",
"background_color": "#2E5984",
"horizontal_align": "center",
"vertical_align": "middle",
"border_style": "thick",
"border_color": "#000000",
"text_wrap": true
}
}
```
### Number Formatting
```json
{
"tool": "cell_format",
"parameters": {
"filepath": "reports/financial.xlsx",
"sheet_name": "Budget",
"range": "C2:C10",
"number_format": "$#,##0.00",
"horizontal_align": "right"
}
}
```
## Batch Cell Formatting
### Complete Report Styling
```json
{
"tool": "cell_format_batch",
"parameters": {
"filepath": "reports/financial-report.xlsx",
"sheet_name": "Sheet1",
"format_ranges": [
{
"range": "A1:F1",
"background_color": "#2E5984",
"horizontal_align": "center",
"vertical_align": "middle",
"border_style": "thick",
"border_color": "#000000"
},
{
"range": "B2:B4",
"number_format": "$#,##0.00",
"horizontal_align": "right"
},
{
"range": "C2:C4",
"number_format": "0",
"horizontal_align": "center"
},
{
"range": "D2:F5",
"number_format": "$#,##0.00",
"horizontal_align": "right"
},
{
"range": "A5:F5",
"border_style": "thick",
"border_sides": ["top"]
}
]
}
}
```
### Advanced Border Styles
```json
{
"tool": "cell_format_batch",
"parameters": {
"filepath": "reports/border-demo.xlsx",
"sheet_name": "Sheet1",
"format_ranges": [
{
"range": "A5:A7",
"border_style": "thin",
"border_color": "#000000",
"border_sides": ["all"]
},
{
"range": "B5:B7",
"border_style": "medium",
"border_color": "#FF0000",
"border_sides": ["outline"]
},
{
"range": "C5:C7",
"border_style": "dashed",
"border_color": "#0000FF",
"border_sides": ["top", "bottom"]
},
{
"range": "D5:D7",
"border_style": "dotted",
"border_color": "#00FF00",
"border_sides": ["left", "right"]
},
{
"range": "E5:E7",
"border_style": "double",
"border_color": "#FF00FF",
"border_sides": ["all"]
}
]
}
}
```
### Text Alignment Showcase
```json
{
"tool": "cell_format_batch",
"parameters": {
"filepath": "reports/alignment-demo.xlsx",
"sheet_name": "Sheet1",
"format_ranges": [
{
"range": "A10",
"horizontal_align": "left",
"vertical_align": "top",
"background_color": "#FFE6E6"
},
{
"range": "B10",
"horizontal_align": "center",
"vertical_align": "middle",
"background_color": "#E6FFE6"
},
{
"range": "C10",
"horizontal_align": "right",
"vertical_align": "bottom",
"background_color": "#E6E6FF"
},
{
"range": "D10",
"horizontal_align": "justify",
"vertical_align": "justify",
"text_wrap": true,
"background_color": "#FFFFE6"
},
{
"range": "E10",
"horizontal_align": "fill",
"indent": 2,
"background_color": "#FFE6FF"
}
]
}
}
```
### Text Rotation Effects
```json
{
"tool": "cell_format_batch",
"parameters": {
"filepath": "reports/rotation-demo.xlsx",
"sheet_name": "Sheet1",
"format_ranges": [
{
"range": "D1",
"text_rotation": 45,
"horizontal_align": "center",
"vertical_align": "middle"
},
{
"range": "E1",
"text_rotation": -45,
"horizontal_align": "center",
"vertical_align": "middle"
},
{
"range": "F1",
"text_rotation": 90,
"horizontal_align": "center",
"vertical_align": "middle"
}
]
}
}
```
## Formatting Parameters Reference
### Background Colors
- `"#FFFFFF"` - White
- `"#4472C4"` - Professional blue
- `"#E6F3FF"` - Light blue
- `"#FFFF00"` - Yellow
- `"#FFE6E6"` - Light red
- `"#E6FFE6"` - Light green
- `"#F0F8FF"` - Alice blue
### Horizontal Alignment
- `"left"` - Left aligned
- `"center"` - Center aligned
- `"right"` - Right aligned
- `"justify"` - Justified
- `"fill"` - Fill the cell
### Vertical Alignment
- `"top"` - Top aligned
- `"middle"` - Middle aligned
- `"bottom"` - Bottom aligned
- `"justify"` - Justified vertically
### Border Styles
- `"none"` - No border
- `"thin"` - Thin line
- `"medium"` - Medium line
- `"thick"` - Thick line
- `"dashed"` - Dashed line
- `"dotted"` - Dotted line
- `"double"` - Double line
### Border Sides
- `["all"]` - All sides
- `["top", "bottom"]` - Top and bottom
- `["left", "right"]` - Left and right
- `["outline"]` - Outside borders only
- `["inside"]` - Inside borders only
### Number Formats
- `"General"` - Default format
- `"0"` - Integer
- `"0.00"` - Two decimal places
- `"0%"` - Percentage
- `"$#,##0.00"` - Currency with thousands separator
- `"yyyy-mm-dd"` - Date format
- `"h:mm AM/PM"` - Time format
### Text Properties
- `text_wrap: true` - Wrap text in cell
- `text_rotation: 45` - Rotate text (degrees)
- `indent: 2` - Indent text level
- `locked: true` - Lock cell for protection
- `hidden: true` - Hide cell formula
## Advanced Formatting Examples
### Financial Report Styling
```json
{
"tool": "cell_format_batch",
"parameters": {
"filepath": "reports/financial-complete.xlsx",
"sheet_name": "Sheet1",
"format_ranges": [
{
"range": "D2:D5",
"background_color": "#F0F8FF"
},
{
"range": "E2:E5",
"background_color": "#FFF0F0"
},
{
"range": "F2:F5",
"background_color": "#F0FFF0",
"border_style": "double",
"border_sides": ["all"]
}
]
}
}
```
### Data Validation Highlighting
```json
{
"tool": "cell_format_batch",
"parameters": {
"filepath": "reports/data-validation.xlsx",
"sheet_name": "Data",
"format_ranges": [
{
"range": "A2:A10",
"background_color": "#90EE90"
},
{
"range": "B2:B10",
"background_color": "#FFB6C1"
},
{
"range": "C2:C10",
"background_color": "#87CEEB",
"border_style": "thin",
"border_sides": ["all"]
}
]
}
}
```
### Protection Settings
```json
{
"tool": "cell_format",
"parameters": {
"filepath": "reports/protected.xlsx",
"sheet_name": "Sheet1",
"range": "B1:B5",
"locked": false,
"hidden": true
}
}
```
## Best Practices
1. **Color Harmony**: Use complementary colors for professional appearance
2. **Contrast**: Ensure text is readable against background colors
3. **Consistency**: Apply consistent formatting across similar data
4. **Borders**: Use borders to separate sections and highlight important data
5. **Number Formats**: Apply appropriate number formats for data types
## Common Use Cases
### Report Headers
- Dark background with white text
- Center alignment
- Thick borders
- Text wrapping enabled
### Financial Data
- Currency formatting
- Right alignment for numbers
- Highlighting negative values
- Thousands separators
### Status Indicators
- Color-coded backgrounds
- Center alignment
- Bold borders
- Clear visual distinction
### Data Tables
- Alternating row colors
- Consistent column widths
- Appropriate number formats
- Clear header styling
## Error Handling
### Invalid Color Code
```json
{
"tool": "cell_format",
"parameters": {
"filepath": "test.xlsx",
"sheet_name": "Sheet1",
"range": "A1",
"background_color": "invalid-color"
}
}
```
**Result**: Uses default background color
### Invalid Number Format
```json
{
"tool": "cell_format",
"parameters": {
"filepath": "test.xlsx",
"sheet_name": "Sheet1",
"range": "A1",
"number_format": "invalid-format"
}
}
```
**Result**: Uses General format as fallback
