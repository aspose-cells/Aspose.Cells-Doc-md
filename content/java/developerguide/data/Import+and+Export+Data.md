+++
title = "Import and Export Data" 
description = "" 
weight = 12172 
+++

Aspose.Cells for Java : Import and Export Data  

# Aspose.Cells for Java : Import and Export Data



This article discusses some data import and export techniques that developers have access to through Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Import Data into Worksheet](#ImportandExportData-ImportDataintoWorksheet)
    *   1.1 [Importing Data Using Aspose.Cells](#ImportandExportData-ImportingDataUsingAspose.Cells)
        *   1.1.1 [Importing from Array](#ImportandExportData-ImportingfromArray)
        *   1.1.2 [Importing from Multi-dimensional Arrays](#ImportandExportData-ImportingfromMulti-dimensionalArrays)
        *   1.1.3 [Importing from an ArrayList](#ImportandExportData-ImportingfromanArrayList)
        *   1.1.4 [Importing from Custom Objects to merged area](#ImportandExportData-ImportingfromCustomObjectstomergedarea)
        *   1.1.5 [Importing Data from JSON](#ImportandExportData-ImportingDatafromJSON)
*   2 [Export Data from Worksheet](#ImportandExportData-ExportDatafromWorksheet)
    *   2.1 [Exporting Data Using Aspose.Cells - Exporting Data to Array](#ImportandExportData-ExportingDataUsingAspose.Cells-ExportingDatatoArray)
        *   2.1.1 [Columns Containing Strongly Typed Data](#ImportandExportData-ColumnsContainingStronglyTypedData)
{{< /panel >}}
 

## Import Data into Worksheet

Data represents the world as it is. To make sense of data, we analyze it and gain an understanding of the world. Data turns into information.

There are many ways of performing analysis: putting data into spreadsheets and manipulating it in different ways is one common method. With Aspose.Cells, it is easy to create spreadsheets that take data from a range of external sources and prepare them for analysis.

This article discusses some data import techniques that developers have access to through Aspose.Cells.

### Importing Data Using Aspose.Cells

When you open an Excel file with Aspose.Cells, all data in the file is automatically imported. Aspose.Cells can also import data from other data sources:

*   [Array](https://docs2.aspose.com/cells/java/developerguide/data/import+and+export+data).
*   [Array list](https://docs2.aspose.com/cells/java/developerguide/data/import+and+export+data).
*   [Result set](https://docs2.aspose.com/cells/java/developerguide/data/import+and+export+data).
*   [JSON](https://docs2.aspose.com/cells/java/developerguide/data/import+and+export+data)

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook) class contains the collection [WorksheetCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#Worksheets) which allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection. [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection provides very useful methods for importing data from other data sources. This article explains how these methods can be used.

#### Importing from Array

To import data to a spreadsheet from an array, call the importArray method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection. There are many overloaded versions of the importArray method but a typical overload takes the following parameters:

*   **Array**, the array object that you're importing content from.
*   **Row number**, the row number of the first cell that the data will be imported to.
*   **Column number**, the column number of the first cell that the data will be imported to.
*   **Is vertical**, a Boolean value that specifies whether to import data vertically or horizontally.

#### Importing from Multi-dimensional Arrays

To import data to a spreadsheet from multi-dimensional arrays, call the relevant importArray overload of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection:

#### Importing from an ArrayList

To import data from an *ArrayList* to worksheets, call the [ImportArrayList](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) method of the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection. The [ImportArrayList](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) method takes the following parameters:

*   **ArrayList**, the *ArrayList* object whose contents will be imported.
*   **Row Number**, the row number of the first cell of the cell range from which contents will be imported.
*   **Column Number**, the column number of the first cell from which data will be imported.
*   **Is Vertical**, is a Boolean value that specifies whether to import data vertically or horizontally.

#### Importing from Custom Objects to merged area

To import data from a collection of objects to a worksheet containing merged cells, use [ImportTableOptions.CheckMergedCells](https://apireference.aspose.com/java/cells/com.aspose.cells/importtableoptions#CheckMergedCells) property. If the Excel template has merged cells, set the value of [ImportTableOptions.CheckMergedCells](https://apireference.aspose.com/java/cells/com.aspose.cells/importtableoptions#CheckMergedCells) property to true. Pass the [ImportTableOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/ImportTableOptions) object along with the list of columns/properties to the method to display your desired list of objects. The following code sample demonstrates the use of [ImportTableOptions.CheckMergedCells](https://apireference.aspose.com/java/cells/com.aspose.cells/importtableoptions#CheckMergedCells) property to import data from Custom Objects to merged cells. Please see the attached [source Excel](https://docs2.aspose.com/cells/java/attachments/5276213/90112035.xlsx) file and the [output Excel](https://docs2.aspose.com/cells/java/attachments/5276213/90112036.xlsx) file for reference.

</script<p>The following is the code for the Product class used in the above code snippet.</p><p> </p><script src="https://gist.github.com/aspose-com-gists/439a68a5e4305388c50ca306ef238de5.js?file=Examples-src-AsposeCellsExamples-HelperClasses-Product-1.java"></script<p><br /><span class="confluence-anchor-link" id="ImportandExportData-resultSet"></span></p><h4 id="ImportandExportData-ImportingfromResultSet">Importing from ResultSet</h4><p>To import data from a <em>ResultSet</em> to worksheets, call the <a href="https://apireference.aspose.com/java/cells/com.aspose.cells/cells#importResultSet(java.sql.ResultSet,%20int,%20int,%20boolean)" class="external-link" rel="nofollow">importResultSet</a> method of the <a href="https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells" class="external-link" rel="nofollow">Cells</a> collection. There are many overloaded versions of the <a href="https://apireference.aspose.com/java/cells/com.aspose.cells/cells#importResultSet(java.sql.ResultSet,%20int,%20int,%20boolean)" class="external-link" rel="nofollow">importResultSet</a> method but a typical overload takes the following parameters:</p><ul><li><strong>Result set</strong>, the <em>ResultSet</em> object containing the data you're importing.</li><li><strong>Start cell</strong>, the name of the start cell (for example, &quot;A1&quot;) from which to import the contents of the <em>ResultSet</em>.</li><li><strong>Is field name shown</strong>, specifies whether the names of the columns of the <em>ResultSet</em> should be imported to the worksheet as a first row.</li></ul><p> </p><script src="https://gist.github.com/aspose-com-gists/a20e8fa273e7cfa37d032b8211fcf8bf.js?file=Examples-src-main-java-com-aspose-cells-examples-data-ImportingfromResultSet-ImportingfromResultSet.java">

#### Importing Data from JSON

Aspose.Cells provides a [JsonUtility](https://apireference.aspose.com/java/cells/com.aspose.cells/JsonUtility) class for processing JSON. [JsonUtility](https://apireference.aspose.com/java/cells/com.aspose.cells/JsonUtility) class has an [ImportData](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)) method for importing JSON data. Aspose.Cells also provides a [JsonLayoutOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/JsonLayoutOptions) class that represents the options of JSON layout. The [ImportData](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)) method accepts [JsonLayoutOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/JsonLayoutOptions) as a parameter. The [JsonLayoutOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/JsonLayoutOptions) class provides the following properties.

*   [ArrayAsTable](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Indicates in the array should be processed as a table or not.
*   [ConvertNumericOrDate](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Gets or sets a value that indicates whether the string in JSON is to be converted to numeric or date.
*   [DateFormat](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonlayoutoptions#DateFormat): Gets and sets the format of the date value.  
    
*   [IgnoreArrayTitle](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Indicates whether to ignore the title if the property of the object is an array  
    
*   [IgnoreNull](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Indicates whether the null value should be ignored or not.  
    
*   [IgnoreObjectTitle](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Indicates whether to ignore the title if the property of the object is an object.  
    
*   [NumberFormat](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonlayoutoptions#NumberFormat): Gets and sets the format of numeric value.  
    
*   [TitleStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/jsonlayoutoptions#TitleStyle): Gets and sets the style of the title.  
    

The sample code given below demonstrates the use of the [JsonUtility](https://apireference.aspose.com/java/cells/com.aspose.cells/JsonUtility) and [JsonLayoutOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/JsonLayoutOptions)classes to import JSON data.

## Export Data from Worksheet

Aspose.Cells not only lets its users import data to worksheets from external data sources but also allow them to export worksheet data to an array.

### Exporting Data Using Aspose.Cells - Exporting Data to Array

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook ](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook)class contains a [WorksheetCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#Worksheets) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/java/cells/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) collection.

Data can easily be exported to an *Array *object using the [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Cells) class' [exportArray](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) method.

#### Columns Containing Strongly Typed Data

Spreadsheets stores data as a sequence of rows and columns. Use the [exportArray](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) method to export the data from a worksheet to an array. [exportArray](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) takes the following parameters to export worksheet data as an *`Array`* object:

*   **Row number**, the row number of the first cell the data will be exported from.
*   **Column number**, the column number of the first cell from where the data will be exported
*   **Number of rows**, the number of rows to export.
*   **Number of columns**, the number of columns to export.

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleMergedTemplate.xlsx](https://docs2.aspose.com/cells/java/attachments/5276213/90112035.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleMergedTemplate\_out.xlsx](https://docs2.aspose.com/cells/java/attachments/5276213/90112036.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

