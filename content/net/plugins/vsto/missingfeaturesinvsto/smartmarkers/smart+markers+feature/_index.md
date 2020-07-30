---
title : "Smart Markers feature" 
description : "" 
weight : 20839 
toc : false
type: docs
url: /net/plugins/vsto/missingfeaturesinvsto/smartmarkers/smart+markers+feature/
---

# Aspose.Cells for .NET : Smart Markers feature


**Smart markers** are used to let Aspose.Cells know what information to place in an Microsoft Excel designer spreadsheet. Smart markers allow you to create templates that contain only specific information and formatting.

### Designer Spreadsheet & Smart Markers

Designer spreadsheets are standard Excel files that contain visual formatting, formulas and smart markers. They can contain smart markers that reference one or more data source, such as information from a project and information for related contacts. Smart markers are written into the cells where you want the information.

All smart markers start with &=. An example of a data marker is &=Party.FullName. If the data marker results in more than one item, for example, a complete row, then the following rows are moved down automatically to make room for all of the new information. Thus sub-totals and totals can be placed on the row immediately after the data marker to make calculations based on the inserted data. To make calculations on the inserted rows, use dynamic formulas.

Smart markers consist of the **data source** and **field name** parts for most information. Special information may also be passed with variables and variable arrays. Variables always fill only one cell whereas variable arrays may fill several. Only use one data marker per cell. Unused smart markers are removed.

Smart marker may also contain parameters. Parameters allow you to modify how the information will be laid out. They are appended to the end of smart marker in parenthesis as a comma separated list.

### Smart Marker Options

*   &=DataSource.FieldName
*   &=Data Source.Field Name
*   &=$VariableName
*   &=$VariableArray
*   &==DynamicFormula
*   &=&=RepeatDynamicFormula

### Parameters

The following parameters are allowed:

*   noadd - Do not add extra rows to fit data.
*   skip:n - Skip n number of rows for each row of data.
*   ascending:n or descending:n - Sort data in smart markers. If n is 1, then the column is the first key of the sorter. The data is sorted after processing the data source. E.g &=Table1.Field3(ascending:1).
*   horizontal - Write data left-to-right, instead of top-to-bottom.
*   numeric - Convert text to number if possible.Only supported in .NET version.
*   shift - Shift down or right, creating extra rows or columns to fit data. The shift parameter works the same way as in Microsoft Excel. For example in MS Excel, when you select a range of cells, right-click and select Insert and specify shift cells down, shift cells right and other options. In short, the shift parameter fills the same function for vertical/normal (top to bottom) or horizontal (left to right) smart markers.
*   copystyle - Copy the base cell's style to all the cells in that column.

The parameters **noadd** and skip can be combined to insert data on alternating rows. Because the template is processed from bottom to top, you should add noadd on the first row to avoid extra rows from being inserted before the alternate row.

