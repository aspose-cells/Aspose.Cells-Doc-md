##Opening Files with Different Formats
Developers use of Aspose.Cells to open files for different purposes. For example, open a file to retrieve data from it, or use a pre-defined designer spreadsheet file to speed up your development process. Aspose.Cells allows developers to open different kinds of source files. These source files can be Microsoft Excel reports, SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV) files. This article discusses opening these different source files using Aspose.Cells.
If you need to know all supported file formats, please refer to the following pages:
[Supported File Formats](https://docs.aspose.com/cells/java/supported-file-formats/)
## **Simple Ways to Open Excel Files**
### **Opening through Path**
To open a Microsoft Excel file using the file path, pass the path of the file as a parameter while creating the instance of the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) class. The following sample code demonstrates opening an Excel file using the file path.
#### **Example**
### **Opening through Stream**
Sometimes, the Excel file that you want to open is stored as a stream. In that case, similar to opening a file using the file path, pass the stream as a parameter while instantiating the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) class. The following sample code demonstrates opening an Excel file using stream.
#### **Example**
### **Opening Files of Different Microsoft Excel Versions**
User may use the [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) class to specify the format of the Excel file using the [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) enumeration.
The [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) enumeration contains many pre-defined file formats some of which are given below.
|**Format Types**|**Description**|
| :- | :- |
|Csv|Represents a CSV file|
|Excel97To2003|Represents an Excel 97 - 2003 file|
|Xlsx|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSX file|
|Xlsm|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSM file|
|Xltx|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 template XLTX file|
|Xltm|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 macro-enabled XLTM file|
|Xlsb|Represents an Excel 2007/2010/2013/2016/2019 and Office 365 binary XLSB file|
|SpreadsheetML|Represents a SpreadsheetML file|
|Tsv|Represents a Tab-separated values file|
|TabDelimited|Represents a Tab Delimited text file|
|Ods|Represents an ODS file|
|Html|Represents an HTML file|
|Mhtml|Represents an MHTML file|
### **Opening Microsoft Excel 95/5.0 Files**
To open Microsoft Excel 95 files, instantiate the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) instance with the path or stream of the template file. Sample file to test the code can be downloaded from the following link:
[Excel95_5.0.xls](Excel95_5.0.xls)
#### **Example**
### **Opening Microsoft Excel 97 or later versions XLS Files**
To open XLS files of Microsoft Excel XLS 97 or later versions, instantiate the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) instance with the path or stream of the template file. Or use the [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) method and select the [**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL-97-TO-2003) value in the [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) enumeration.
#### **Example**
### **Opening Microsoft Excel 2007 or later versions XLSX Files**
To open XLSX files of Microsoft Excel 2007 or later versions, instantiate the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) instance with the path or stream of the template file. Or use the [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) class and select the [**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX) value in the [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) enumeration.
#### **Example**
### **Opening Files with Different Formats**
Aspose.Cells allows developers to open spreadsheet files with different formats such as SpreadsheetML, CSV, Tab Delimited files. To open such files, developers can use the same methodology as they use for opening files of different Microsoft Excel versions.
### **Opening SpreadsheetML Files**
SpreadsheetML files are the XML representations of your spreadsheets including all information about the spreadsheet such as formatting, formulae, etc. Since Microsoft Excel XP, an XML export option is added to Microsoft Excel that exports your spreadsheets to SpreadsheetML files.
To open SpreadsheetML files, use the [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) class and select the [**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET-ML) value in the [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) enumeration.
#### **Example**
### **Opening CSV Files**
Comma Separated Values (CSV) files contain records whose values are delimited or separated by commas. In CSV files, data is stored in a tabular format that has fields separated by the comma character and quoted by the double-quote character. If a field's value contains a double quote character it is escaped with a pair of double-quote characters. You can also use Microsoft Excel to export your spreadsheet data to a CSV file.
To open CSV files, use the [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) class and select the [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) value, predefined in the [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) enumeration.
#### **Example**
### **Opening CSV files and replacing invalid characters**
In Excel, when CSV file with special characters is opened, the characters are automatically replaced. The same is done by Aspose.Cells API which is demonstrated in the code example given below.
#### **Example**
### **Opening CSV files using preferred parser**
This is not always necessary to use default parser settings for opening the CSV files. Sometimes importing CSV file does not create expected output like date format is not as expected or empty fields are handled differently. For this purpose [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) is available to provide own preferred parser to parse different data types as per the requirement. Following sample code demonstrates the usage of the preferred parser.
Sample source file and output files can be downloaded from the following links for testing this feature.
[samplePreferredParser.csv](samplePreferredParser.csv)
[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)
#### **Example**
### **Opening TSV(Tab Delimited) Files**
Tab-delimited files contain spreadsheet data but without any formatting. Data is arranged in rows and columns such as tables and spreadsheets. Shortly, a tab-delimited file is a special kind of plain text file with a tab between each column in the text.
To open tab-delimited files, developers should use the [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) class and select the [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) value, predefined in the [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) enumeration.
#### **Example**
### **Opening Encrypted Excel Files**
We know that it's possible to create encrypted Excel files using Microsoft Excel. To open such encrypted files, developers should call a special overloaded LoadOptions method and select the DEFAULT value, predefined in the FileFormatType enumeration. This method would also take the password for the encrypted file as shown below in the example.
#### **Example**
Aspose.Cells also supports opening password-protected MS Excel 2013 files.
There are fair chances that the Workbook constructor may throw System.OutOfMemoryException while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory, therefore, the spreadsheet has to be loaded while enabling the [Memory Preferences](https://docs.aspose.com/cells/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).
### **Opening SXC Files**
StarOffice Calc is similar to Microsoft Excel and supports formulas, charts, functions, and macros. The spreadsheets created with this software are saved with the SXC extension. The SXC file is also used for OpenOffice.org Calc spreadsheet files. Aspose.Cells can read SXC files as demonstrated by the following code sample.
#### **Example**
### **Opening FODS Files**
FODS file is spreadsheet saved in OpenDocument XML without any compression. Aspose.Cells can read FODS files as demonstrated by the following code sample.
#### **Example**
## **Advance topics**
- [Filter Defined Names while loading Workbook](https://docs.aspose.com/cells/java/filter-defined-names-while-loading-workbook/)
- [Filter Objects while loading Workbook or Worksheet](https://docs.aspose.com/cells/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Get Warnings while Loading Excel File](https://docs.aspose.com/cells/java/get-warnings-while-loading-excel-file/)
- [Keep Separators for Blank Rows while exporting spreadsheets to CSV format](https://docs.aspose.com/cells/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Load Workbook with specified Printer Paper Size](https://docs.aspose.com/cells/java/load-workbook-with-specified-printer-paper-size/)
- [Opening Different Microsoft Excel Versions Files](https://docs.aspose.com/cells/java/opening-different-microsoft-excel-versions-files/)
- [Optimizing Memory Usage while Working with Big Files having Large Datasets](https://docs.aspose.com/cells/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells](https://docs.aspose.com/cells/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Reading CSV File with Multiple Encodings](https://docs.aspose.com/cells/java/reading-csv-file-with-multiple-encodings/)
- [Stop conversion or loading using InterruptMonitor when it is taking too long](https://docs.aspose.com/cells/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Using LightCells API](https://docs.aspose.com/cells/java/using-lightcells-api/)
