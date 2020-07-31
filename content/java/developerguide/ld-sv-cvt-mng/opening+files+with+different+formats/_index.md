---
title : "Opening Files with Different Formats" 
description : "" 
weight : 12049 
toc : false
type: docs
url: /java/developerguide/ld-sv-cvt-mng/opening+files+with+different+formats/
---

# Aspose.Cells for Java : Opening Files with Different Formats


Developers use of Aspose.Cells to open files for different purposes. For example, open a file to retrieve data from it, or use a pre-defined designer spreadsheet file to speed up your development process. Aspose.Cells allows developers to open different kinds of source files. These source files can be Microsoft Excel reports, SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV) files. This article discusses opening these different source files using Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Simple Ways to Open Excel Files](#simple-ways-to-open-excel-files)
    *   1.1 [Important to Know](#important-to-know)
    *   1.2 [Opening through Path](#opening-through-path)
        *   1.2.1 [Example](#example)
    *   1.3 [Opening through Stream](#opening-through-stream)
        *   1.3.1 [Example](#example)
    *   1.4 [Opening Files of Different Microsoft Excel Versions](#opening-files-of-different-microsoft-excel-versions)
    *   1.5 [Opening Microsoft Excel 95/5.0 Files](#opening-microsoft-excel-95/5.0-files)
        *   1.5.1 [Example](#example)
    *   1.6 [Opening Microsoft Excel 97 Files](#opening-microsoft-excel-97-files)
        *   1.6.1 [Example](#example)
    *   1.7 [Opening Microsoft Excel 2000 Files](#opening-microsoft-excel-2000-files)
        *   1.7.1 [Example](#example)
    *   1.8 [Opening Microsoft Excel 2003 Files](#opening-microsoft-excel-2003-files)
        *   1.8.1 [Example](#example)
    *   1.9 [Opening Microsoft Excel XP Files](#opening-microsoft-excel-xp-files)
        *   1.9.1 [Example](#example)
    *   1.10 [Opening Microsoft Excel 2007/2010 XLSX Files](#opening-microsoft-excel-2007/2010-xlsx-files)
        *   1.10.1 [Example](#example)
    *   1.11 [Opening Files with Different Formats](#opening-files-with-different-formats)
    *   1.12 [Opening SpreadsheetML Files](#opening-spreadsheetml-files)
        *   1.12.1 [Example](#example)
    *   1.13 [Opening CSV Files](#opening-csv-files)
        *   1.13.1 [Example](#example)
    *   1.14 [Opening CSV files and replacing invalid characters](#opening-csv-files-and-replacing-invalid-characters)
        *   1.14.1 [Example](#example)
    *   1.15 [Opening CSV files using preferred parser](#opening-csv-files-using-preferred-parser)
        *   1.15.1 [Example](#example)
    *   1.16 [Opening Tab Delimited Files](#opening-tab-delimited-files)
        *   1.16.1 [Example](#example)
    *   1.17 [Opening Tab-Separated Values (TSV) Files](#opening-tab-separated-values-(tsv)-files)Files)
        *   1.17.1 [Example](#example)
    *   1.18 [Opening Encrypted Excel Files](#opening-encrypted-excel-files)
        *   1.18.1 [Example](#example)
    *   1.19 [Opening SXC Files](#opening-sxc-files)
        *   1.19.1 [Example](#example)
    *   1.20 [Opening FODS Files](#opening-fods-files)
        *   1.20.1 [Example](#example)
{{< /panel >}}
 

### Simple Ways to Open Excel Files

#### Important to Know

Aspose.Cells supports Excel file formats from Excel 97 to Excel 2007/2010. But, if you save your Excel file in the following format as shown below in the figure then your Excel file will fail to open using Aspose.Cells.  
  
**Don't save your Excel files in this format**  
![](https://docs2.aspose.com/cells/java/attachments/5276272/5473257.png)

If you do, the Excel file will contain data in Excel 5.0/95 format, which is not supported by Aspose.Cells. So, please save your Excel file as a Microsoft Excel Workbook as shown below.  
  
**Save your Excel files in this format**  
![](https://docs2.aspose.com/cells/java/attachments/5276272/5473256.png)

#### Opening through Path

To open a Microsoft Excel file using the file path, pass the path of the file as a parameter while creating the instance of the [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) class. The following sample code demonstrates opening an Excel file using the file path.

##### Example


#### Opening through Stream

Sometimes, the Excel file that you want to open is stored as a stream. In that case, similar to opening a file using the file path, pass the stream as a parameter while instantiating the [Workbook](https://apireference.aspose.com/java/cells/com.aspose.cells/Workbook) class. The following sample code demonstrates opening an Excel file using stream.

##### Example

#### Opening Files of Different Microsoft Excel Versions

It's very common to believe that the Excel files that you're opening could be created by different versions of Microsoft Excel: Microsoft Excel 97, 2000, XP, 2003 and 2007/2010. When that's the case, use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class to specify the format of the Excel file using the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

The [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration contains many pre-defined file formats some of which are given below.

{{< table style="table-striped" >}}
|File Format Types|Description|
|:----|:----|
|AsposePdf|Specifies the spreadsheet in Aspose.Pdf.Xml format that can be read by Aspose.Pdf to produce a PDF file.|
|CSV|Represents a CSV file|
|Default|Represents an Excel 2003 file|
|Excel97|Represents an Excel 97 file|
|Excel2000|Represents an Excel 2000 file|
|ExcelXP|Represents an Excel XP file|
|Excel2003|Represents an Excel 2003 file|
|Excel2007Xlsx|Represents an Excel 2007 XLSX file|
|Excel2007Xlsm|Represents an Excel 2007 XLSM file|
|Excel2007Xltx|Represents an Excel 2007 template XLTX file|
|Excel2007Xltm|Represents an Excel 2007 macro-enabled XLTM file|
|Excel2007Xlsb|Represents an Excel 2007 binary XLSB file|
|SpreadsheetML|Represents a SpreadSheetML file|
|TSV|Represents a Tab-separated values file|
|TabDelimited|Represents a Tab Delimited text file|
|HTML|Represents an HTML file(s)|
|MHTML|Represents an MHTML file(s)|
|ODS|Represents an OpenDocument Spreadsheet file|
{{< /table >}}

#### Opening Microsoft Excel 95/5.0 Files

To open Microsoft Excel 95 files, use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class and select [EXCEL\_95](https://apireference.aspose.com/java/cells/com.aspose.cells/fileformattype#EXCEL_95) value in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration. Sample file to test the code can be downloaded from the following link:

[Excel95\_5.0.xls](https://docs2.aspose.com/cells/java/attachments/5276272/81920919.xls)

##### Example

#### Opening Microsoft Excel 97 Files

To open Microsoft Excel 97 files, use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) method and select the [EXCEL\_97\_TO\_2003](https://apireference.aspose.com/java/cells/com.aspose.cells/fileformattype#EXCEL_97_TO_2003) value in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

##### Example

#### Opening Microsoft Excel 2000 Files

To open Microsoft Excel 2000 files, use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class and select the EXCEL2000 value in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

##### Example

#### Opening Microsoft Excel 2003 Files

To open Microsoft Excel 2003 files, use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class and select the EXCEL2003 value, predefined in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

##### Example

#### Opening Microsoft Excel XP Files

To open Microsoft Excel XP files, use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class and select the EXCELlXP value, predefined in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

##### Example

#### Opening Microsoft Excel 2007/2010 XLSX Files

To open Microsoft Excel 2007/2010 XLSX files, use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class and select the EXCEL2007 value, predefined in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

##### Example

#### Opening Files with Different Formats

Aspose.Cells allows developers to open spreadsheet files with different formats such as SpreadsheetML, CSV, Tab Delimited files. To open such files, developers can use the same methodology as they use for opening files of different Microsoft Excel versions.

#### Opening SpreadsheetML Files

`SpreadsheetML` files are the XML representations of your spreadsheets including all information about the spreadsheet such as formatting, formulae, etc. Since Microsoft Excel XP, an XML export option is added to Microsoft Excel that exports your spreadsheets to SpreadsheetML files.

To open SpreadsheetML files, use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class and select the SPREADSHEETML value, predefined in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

##### Example

#### Opening CSV Files

Comma Separated Values (CSV) files contain records whose values are delimited or separated by commas. In CSV files, data is stored in a tabular format that has fields separated by the comma character and quoted by the double-quote character. If a field's value contains a double quote character it is escaped with a pair of double-quote characters. You can also use Microsoft Excel to export your spreadsheet data to a CSV file.

To open CSV files, use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class and select the [CSV](https://apireference.aspose.com/java/cells/com.aspose.cells/fileformattype#CSV) value, predefined in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

##### Example

#### Opening CSV files and replacing invalid characters

In Excel, when CSV file with special characters is opened, the characters are automatically replaced. The same is done by Aspose.Cells API which is demonstrated in the code example given below.

##### Example

#### Opening CSV files using preferred parser

This is not always necessary to use default parser settings for opening the CSV files. Sometimes importing CSV file does not create expected output like date format is not as expected or empty fields are handled differently. For this purpose [TxtLoadOptions.PreferredParsers](https://apireference.aspose.com/java/cells/com.aspose.cells/txtloadoptions#PreferredParsers)is available to provide own preferred parser to parse different data types as per the requirement. Following sample code demonstrates the usage of the preferred parser.  

Sample source file and output files can be downloaded from the following links for testing this feature.

[samplePreferredParser.csv](https://docs.aspose.com/download/attachments/5013529/samplePreferredParser.csv?version=1&modificationDate=1540829615013&api=v2)

[outputsamplePreferredParser.xlsx](https://docs.aspose.com/download/attachments/5013529/outputsamplePreferredParser.xlsx?version=1&modificationDate=1540829626105&api=v2)

##### Example

#### Opening Tab Delimited Files

Tab-delimited files contain spreadsheet data but without any formatting. Data is arranged in rows and columns such as tables and spreadsheets. Shortly, a tab-delimited file is a special kind of plain text file with a tab between each column in the text.

To open tab-delimited files, developers should use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class and select the [TAB\_DELIMITED](https://apireference.aspose.com/java/cells/com.aspose.cells/fileformattype#TAB_DELIMITED) value, predefined in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

##### Example

#### Opening Tab-Separated Values (TSV) Files

TSV files are also used to contain spreadsheet data but without any formatting. The format is the same with Tab Delimited where data is arranged in rows and columns such as tables and spreadsheets.

To open tab-delimited files, developers should use the [LoadOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/LoadOptions) class and select the [TSV](https://apireference.aspose.com/java/cells/com.aspose.cells/fileformattype#TSV) value, predefined in the [FileFormatType](https://apireference.aspose.com/java/cells/com.aspose.cells/FileFormatType) enumeration.

##### Example

#### Opening Encrypted Excel Files

We know that it's possible to create encrypted Excel files using Microsoft Excel. To open such encrypted files, developers should call a special overloaded `LoadOptions` method and select the DEFAULT value, predefined in the `FileFormatType` enumeration. This method would also take the password for the encrypted file as shown below in the example.

##### Example

  
Aspose.Cells also supports opening password-protected MS Excel 2013 files.

There are fair chances that the `Workbook` constructor may throw `System.OutOfMemoryException` while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory, therefore, the spreadsheet has to be loaded while enabling the [Memory Preferences](http://www.aspose.com/docs/display/cellsjava/Optimizing+Memory+Usage+while+Working+with+Big+Files+having+Large+Datasets).

#### Opening SXC Files

StarOffice Calc is similar to Microsoft Excel and supports formulas, charts, functions, and macros. The spreadsheets created with this software are saved with the SXCextension. The SXC file is also used for OpenOffice.org Calc spreadsheet files. Aspose.Cells can read SXC files as demonstrated by the following code sample.

##### Example

#### Opening FODS Files

FODS file is spreadsheet saved in OpenDocument XML without any compression. Aspose.Cells can read FODS files as demonstrated by the following code sample.

##### Example

