---
title: Configuration Parameters
type: docs
weight: 10
url: /jasperreports/configuration-parameters/
---

{{% alert color="primary" %}} 

The following table lists the configuration parameters. 

{{% /alert %}} 

|**Parameter name** |**Description** |
| :- | :- |
|FORMAT_TYPE |Can be set to "EXCEL97TO2003" or "EXCEL2007" to generate Microsoft Excel 79 0 2003 or Excel 2007 format files. |
|IS_ONE_PAGE_PER_SHEET |A Boolean value specifying whether each report page should be written to a different XLS worksheet. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_ROWS |A Boolean value specifying whether the empty spaces that may appear between rows should be removed or not. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_COLUMNS |A Boolean value specifying whether the empty spaces that may appear between columns should be removed or not. |
|IS_WHITE_PAGE_BACKGROUND |A Boolean value specifying whether the page background should be white or the default XLS background color. What the XLS background colour is may vary depending on the XLS viewer properties or the operating system color scheme. |
|IS_DETECT_CELL_TYPE |Flag used to indicate whether the exporter should take into consideration the type of the original text field expressions and set the cell types and values accordingly. |
|SHEET_NAMES |An array of strings representing custom sheet names. This is useful when used with the IS_ONE_PAGE_PER_SHEET parameter. |
|IS_FONT_SIZE_FIX_ENABLED |Flag for decreasing font size so that text fits into the specified cell height. |
|MAXIMUM_ROWS_PER_SHEET |An integer value specifying the maximum number of rows allowed to be shown in a sheet. When set, a new sheet is created for the remaining rows to be displayed. Negative values or zero means no limit has been set. |
|IS_IGNORE_GRAPHICS |Flag for ignoring graphical elements and exporting text elements only. |
|IS_COLLAPSE_ROW_SPAN |Flag for collapsing row span and avoid merging cells across rows. |
|IS_IGNORE_CELL_BORDER |Flag for ignoring the cell border. |
|IS_USE_EXCEL_CHART |Flag for using editable chart in Microsoft Excel format rather than static pictures. The default value is true. |

