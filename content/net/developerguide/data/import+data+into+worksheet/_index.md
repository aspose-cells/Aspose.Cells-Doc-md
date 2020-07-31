---
title : "Import Data into Worksheet" 
description : "" 
weight : 12205 
toc : false
type: docs
url: /net/developerguide/data/import+data+into+worksheet/
---

# Aspose.Cells for .NET : Import Data into Worksheet


This article discusses some data import techniques that developers have access to through Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Import Data into Worksheet](#import-data-into-worksheet)
    *   1.1 [Importing from Array](#importing-from-array)
    *   1.2 [Importing from ArrayList](#importing-from-arraylist)
    *   1.3 [Importing from Custom Objects](#importing-from-custom-objects)
    *   1.4 [Importing from Custom Objects to merged area](#importing-from-custom-objects-to-merged-area)
    *   1.5 [Importing from DataTable](#importing-from-datatable)
    *   1.6 [Importing from dynamic object as data source](#importing-from-dynamic-object-as-data-source)
    *   1.7 [Importing from DataColumn (.NET)](#importing-from-datacolumn-(.net)))
    *   1.8 [Importing from DataView (.NET)](#importing-from-dataview-(.net)))
    *   1.9 [Importing from DataGrid (.NET)](#importing-from-datagrid-(.net)))
    *   1.10 [Importing from GridView](#importing-from-gridview)
    *   1.11 [Importing HTML formatted data](#importing-html-formatted-data)
    *   1.12 [Importing Data from JSON](#importing-data-from-json)
{{< /panel >}}
 

## Import Data into Worksheet

When you open an Excel file with Aspose.Cells, all data in the file is automatically imported. Aspose.Cells can also import data from other data sources.

Aspose.Cells provides a [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet)class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection provides useful methods to import data from different data sources. This article explains how these methods can be used.

### Importing from Array

To import data to a spreadsheet from an array, call the [ImportArray](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importarray/index) method of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells)collection. There are many overloaded versions of the [ImportArray](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importarray/index) method but a typical overload takes the following parameters:

*   **Array**, the array object that you're importing content from.
*   **Row number**, the row number of the first cell that the data will be imported to.
*   **Column number**, the column number of the first cell that the data will be imported to.
*   **Is vertical**, a Boolean value that specifies whether to import data vertically or horizontally.

### Importing from ArrayList

To import data from an *ArrayList *to worksheets, call the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection's [ImportArrayList](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importarraylist) method. The `ImportArray` method takes the following parameters:

*   **Array list**, represents the *ArrayList *object you're importing.
*   **Row number**, represents the row number of the first cell that the data will be imported to.
*   **Column number**, represents the column number of the first cell that the data will be imported to.
*   **Is vertical**, a Boolean value that specifies whether to import data vertically or horizontally.

### Importing from Custom Objects

To import data from a collection of objects to a worksheet, use [ImportCustomObjects](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importcustomobjects/index). Provide a list of columns/properties to the method to display your desired list of objects.

### Importing from Custom Objects to merged area

To import data from a collection of objects to a worksheet containing merged cells, use [ImportTableOptions.CheckMergedCells](https://apireference.aspose.com/net/cells/aspose.cells/importtableoptions/properties/checkmergedcells) property. If the Excel template has merged cells, set the value of [ImportTableOptions.CheckMergedCells](https://apireference.aspose.com/net/cells/aspose.cells/importtableoptions/properties/checkmergedcells) property to true. Pass the [ImportTableOptions](https://apireference.aspose.com/net/cells/aspose.cells/importtableoptions) object along with the list of columns/properties to the method to display your desired list of objects. The following code sample demonstrates the use of [ImportTableOptions.CheckMergedCells](https://apireference.aspose.com/net/cells/aspose.cells/importtableoptions/properties/checkmergedcells) property to import data from Custom Objects to merged cells. Please see the attached [source Excel](https://docs2.aspose.com/cells/net/attachments/5025402/90112033.xlsx) file and the [output Excel](https://docs2.aspose.com/cells/net/attachments/5025402/90112034.xlsx) file for reference.

### Importing from DataTable

To import data from a *DataTable*, call the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection's [ImportDataTable](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importdatatable/index) method. There are many overloaded versions of the [ImportDataTable](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importdatatable/index) method but a typical overload takes the following parameters:

*   **Data table**, the *DataTable* object that you're importing the content from.
*   **Is field name shown**, specifies whether the names of the *DataTable *columns should be imported to the worksheet as a first row or not.
*   **Start cell**, represents the name of the start cell (for example "A1") from where to import the contents of the *DataTable*.

### Importing from dynamic object as data source

Aspose.Cells provides features to work with dynamic objects as datasource. It helps in using datasource where properties are added dynamically to the objects. Once the properties are added to the object, Aspose.Cells considers the first entry as the template and handles the rest accordingly. It means if some dynamic property is added to a first item only and not to other objects, Aspose.Cells considers that all items in the collection should be the same.

In this example, a template model is used which initially contains two variables only. This List is converted to List of dynamic objects. Then some additional field is added into it and finally loaded into the workbook. The workbook picks only those values which are in the template XLSX file. This template workbook uses Smart Markers which also contain parameters. Parameters allow you to modify how the information is laid out. Details about the Smart Markers can be obtained from the following article:

[Using Smart Markers](https://docs2.aspose.com/cells/net/developerguide/smartmarkers/using+smart+markers#usingsmartmarkers-designerspreadsheet&smartmarkers)

### Importing from DataColumn (.NET)

A *DataTable *or *DataView *object is composed of one or more columns. Developers can also import data from any Column/Columnsof the *DataTable *or *DataView *by calling the [ImportData](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importdata/index) method of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. The [ImportData](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importdata/index) method accepts a parameter of type [ImportTableOptions](https://apireference.aspose.com/net/cells/aspose.cells/importtableoptions). The [ImportTableOptions](https://apireference.aspose.com/net/cells/aspose.cells/importtableoptions) class provides a [ColumnIndexes](https://apireference.aspose.com/net/cells/aspose.cells/importtableoptions/properties/columnindexes) property that accepts an array of columns indexes. 

The sample code given below demonstrates the use of [ImportTableOptions.ColumnIndexes ](https://apireference.aspose.com/net/cells/aspose.cells/importtableoptions/properties/columnindexes)to import selective columns.

### Importing from DataView (.NET)

To import data from a *DataView*, call the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection's [ImportData](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importdata/index) method. There are many overloaded versions of the [ImportData](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importdata/index) method but the one for DataView takes the following parameters:

*   **DataView:** The *DataView *object that you're about to import content from.
*   **First Row:** the row number of the first cell that the data will be imported to.
*   **First Column:** the column number of the first cell that the data will be imported to.
*   **ImportTableOptions:** The import options.

### Importing from DataGrid (.NET)

It is possible to import data from a *DataGrid *by calling the [ImportDataGrid](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importdatagrid/index) method of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection. There are many overloaded versions of the [ImportDataGrid](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importdatagrid/index) method but a typical overload takes the following parameters:

*   **Data grid**, the *DataGrid *object that you're importing content from.
*   **Row Number**, the row number of the first cell that the data will be imported to.
*   **Column Number**, the column number of the first cell that the data will be imported to.
*   **Insert Rows**, a Boolean property that indicates whether extra rows should be added to the worksheet to fit data or not.

### Importing from GridView

To import data from a *GridView* control, call the [ImportGridView](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/importgridview) method of the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/cells) collection.

Aspose.Cells allows us to respect HTML formatted values while importing data to the spreadsheet. When HTML parsing is enabled while importing data, Aspose.Cells converts the HTML into corresponding cell formatting.

### Importing HTML formatted data

Aspose.Cells provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) class that provides very useful methods for importing data from external data sources. This article shows how to parse HTML formatted text while importing data and convert the HTML into formatted cell values.

### Importing Data from JSON

Aspose.Cells provides a [JsonUtility](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonutility) class for processing JSON. [JsonUtility](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonutility) class has an [ImportData](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonutility/methods/importdata) method for importing JSON data. Aspose.Cells also provides a [JsonLayoutOptions](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions) class that represents the options of JSON layout. The [ImportData](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonutility/methods/importdata) method accepts [JsonLayoutOptions](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions) as a parameter. The [JsonLayoutOptions](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions) class provides the following properties.

*   [ArrayAsTable](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Indicates in the array should be processed as a table or not.
*   [ConvertNumericOrDate](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Gets or sets a value that indicates whether the string in JSON is to be converted to numeric or date.
*   [DateFormat](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Gets and sets the format of the date value.  
    
*   [IgnoreArrayTitle](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indicates whether to ignore the title if the property of the object is an array  
    
*   [IgnoreNull](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indicates whether the null value should be ignored or not.  
    
*   [IgnoreObjectTitle](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indicates whether to ignore the title if the property of the object is an object.  
    
*   [NumberFormat](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Gets and sets the format of numeric value.  
    
*   [TitleStyle](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Gets and sets the style of the title.  
    

The sample code given below demonstrates the use of the [JsonUtility](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonutility) and [JsonLayoutOptions](https://apireference.aspose.com/net/cells/aspose.cells.utility/jsonlayoutoptions) classes to import JSON data.

