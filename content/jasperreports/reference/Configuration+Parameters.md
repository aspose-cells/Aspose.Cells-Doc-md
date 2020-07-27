+++
title = "Configuration Parameters" 
description = "" 
weight = 8027 
+++

Aspose.Cells for JasperReports : Configuration Parameters  

# Aspose.Cells for JasperReports : Configuration Parameters


The following table lists the configuration parameters.

{{< table style="table-striped" >}}
|Parameter name|Description|
|:----|:----|
|FORMAT\_TYPE|Can be set to "EXCEL97TO2003" or "EXCEL2007" to generate Microsoft Excel 79 0 2003 or Excel 2007 format files.|
|IS\_ONE\_PAGE\_PER\_SHEET|A Boolean value specifying whether each report page should be written to a different XLS worksheet.|
|IS\_REMOVE\_EMPTY\_SPACE\_BETWEEN\_ROWS|A Boolean value specifying whether the empty spaces that may appear between rows should be removed or not.|
|IS\_REMOVE\_EMPTY\_SPACE\_BETWEEN\_COLUMNS|A Boolean value specifying whether the empty spaces that may appear between columns should be removed or not.|
|IS\_WHITE\_PAGE\_BACKGROUND|A Boolean value specifying whether the page background should be white or the default XLS background color. What the XLS background colour is may vary depending on the XLS viewer properties or the operating system color scheme.|
|IS\_DETECT\_CELL\_TYPE|Flag used to indicate whether the exporter should take into consideration the type of the original text field expressions and set the cell types and values accordingly.|
|SHEET\_NAMES|An array of strings representing custom sheet names. This is useful when used with the IS\_ONE\_PAGE\_PER\_SHEET parameter.|
|IS\_FONT\_SIZE\_FIX\_ENABLED|Flag for decreasing font size so that text fits into the specified cell height.|
|MAXIMUM\_ROWS\_PER\_SHEET|An integer value specifying the maximum number of rows allowed to be shown in a sheet. When set, a new sheet is created for the remaining rows to be displayed. Negative values or zero means no limit has been set.|
|IS\_IGNORE\_GRAPHICS|Flag for ignoring graphical elements and exporting text elements only.|
|IS\_COLLAPSE\_ROW\_SPAN|Flag for collapsing row span and avoid merging cells across rows.|
|IS\_IGNORE\_CELL\_BORDER|Flag for ignoring the cell border.|
|IS\_USE\_EXCEL\_CHART|Flag for using editable chart in Microsoft Excel format rather than static pictures. The default value is true.|
{{< /table >}}

