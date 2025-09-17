##Import and Export Data
This article discusses some data import and export techniques that developers have access to through Aspose.Cells.
## Import Data into Worksheet
Data represents the world as it is. To make sense of data, we analyze it and gain an understanding of the world. Data turns into information.
There are many ways of performing analysis: putting data into spreadsheets and manipulating it in different ways is one common method. With Aspose.Cells, it is easy to create spreadsheets that take data from a range of external sources and prepare them for analysis.
This article discusses some data import techniques that developers have access to through Aspose.Cells.
### Importing Data Using Aspose.Cells
When you open an Excel file with Aspose.Cells, all data in the file is automatically imported. Aspose.Cells can also import data from other data sources:
- [Array](https://docs.aspose.com/cells/java/import-and-export-data/).
- [Array list](https://docs.aspose.com/cells/java/import-and-export-data/).
- [Result set](https://docs.aspose.com/cells/java/import-and-export-data/).
- [JSON](https://docs.aspose.com/cells/java/import-and-export-data/)
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contains the collection [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) which allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collection. [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collection provides very useful methods for importing data from other data sources. This article explains how these methods can be used.
#### Importing from Array
To import data to a spreadsheet from an array, call the importArray method of the [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collection. There are many overloaded versions of the importArray method but a typical overload takes the following parameters:
- **Array**, the array object that you're importing content from.
- **Row number**, the row number of the first cell that the data will be imported to.
- **Column number**, the column number of the first cell that the data will be imported to.
- **Is vertical**, a Boolean value that specifies whether to import data vertically or horizontally.
#### Importing from Multi-dimensional Arrays
To import data to a spreadsheet from multi-dimensional arrays, call the relevant importArray overload of the [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collection:
#### Importing from an ArrayList
To import data from an *ArrayList* to worksheets, call the [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-) method of the [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collection. The [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-) method takes the following parameters:
- **ArrayList**, the *ArrayList* object whose contents will be imported.
- **Row Number**, the row number of the first cell of the cell range from which contents will be imported.
- **Column Number**, the column number of the first cell from which data will be imported.
- **Is Vertical**, is a Boolean value that specifies whether to import data vertically or horizontally.
#### Importing from Custom Objects to merged area
To import data from a collection of objects to a worksheet containing merged cells, use [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) property. If the Excel template has merged cells, set the value of [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) property to true. Pass the [**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions) object along with the list of columns/properties to the method to display your desired list of objects. The following code sample demonstrates the use of [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) property to import data from Custom Objects to merged cells. Please see the attached [source Excel](90112035.xlsx) file and the [output Excel](90112036.xlsx) file for reference.
#### Importing Data from JSON
Aspose.Cells provides a [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) class for processing JSON. [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) class has an [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-) method for importing JSON data. Aspose.Cells also provides a [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) class that represents the options of JSON layout. The [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-) method accepts [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) as a parameter. The [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) class provides the following properties.
- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Indicates in the array should be processed as a table or not.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Gets or sets a value that indicates whether the string in JSON is to be converted to numeric or date.
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Gets and sets the format of the date value.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Indicates whether to ignore the title if the property of the object is an array
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Indicates whether the null value should be ignored or not.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Indicates whether to ignore the title if the property of the object is an object.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Gets and sets the format of numeric value.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Gets and sets the style of the title.
The sample code given below demonstrates the use of the [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) and [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) classes to import JSON data.
## Export Data from Worksheet
Aspose.Cells not only lets its users import data to worksheets from external data sources but also allow them to export worksheet data to an array.
### Exporting Data Using Aspose.Cells - Exporting Data to Array
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collection.
Data can easily be exported to an Array object using the [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) class' [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) method.
#### Columns Containing Strongly Typed Data
Spreadsheets stores data as a sequence of rows and columns. Use the [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) method to export the data from a worksheet to an array. [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) takes the following parameters to export worksheet data as an *Array* object:
- Row number, the row number of the first cell the data will be exported from.
- Column number, the column number of the first cell from where the data will be exported
- Number of rows, the number of rows to export.
- Number of columns, the number of columns to export.
## **Advance topics**
- [Import Data from Microsoft Access Database ResultSet Object to the Worksheet](https://docs.aspose.com/cells/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Specify Formula Fields while Importing Data to Worksheet](https://docs.aspose.com/cells/java/specify-formula-fields-while-importing-data-to-worksheet/)
