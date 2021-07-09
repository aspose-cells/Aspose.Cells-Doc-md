---
title: Opening Files with Different Formats
type: docs
weight: 10
url: /java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

Developers use of Aspose.Cells to open files for different purposes. For example, open a file to retrieve data from it, or use a pre-defined designer spreadsheet file to speed up your development process. Aspose.Cells allows developers to open different kinds of source files. These source files can be Microsoft Excel reports, SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV) files. This article discusses opening these different source files using Aspose.Cells.

{{% /alert %}}

### **Simple Ways to Open Excel Files**

{{% alert color="primary" %}}

#### **Important to Know**

Aspose.Cells supports Excel file formats from Excel 97 to Excel 2007/2010. But, if you save your Excel file in the following format as shown below in the figure then your Excel file will fail to open using Aspose.Cells.

**Don't save your Excel files in this format**

![todo:image_alt_text](opening-files-with-different-formats_1.png)

If you do, the Excel file will contain data in Excel 5.0/95 format, which is not supported by Aspose.Cells. So, please save your Excel file as a Microsoft Excel Workbook as shown below. 

**Save your Excel files in this format**

![todo:image_alt_text](opening-files-with-different-formats_2.png)

{{% /alert %}}

#### **Opening through Path**

To open a Microsoft Excel file using the file path, pass the path of the file as a parameter while creating the instance of the **[Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook)** class. The following sample code demonstrates opening an Excel file using the file path.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

#### **Opening through Stream**

Sometimes, the Excel file that you want to open is stored as a stream. In that case, similar to opening a file using the file path, pass the stream as a parameter while instantiating the **[Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook)** class. The following sample code demonstrates opening an Excel file using stream.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

#### **Opening Files of Different Microsoft Excel Versions**

It's very common to believe that the Excel files that you're opening could be created by different versions of Microsoft Excel: Microsoft Excel 97, 2000, XP, 2003 and 2007/2010. When that's the case, use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class to specify the format of the Excel file using the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

The **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration contains many pre-defined file formats some of which are given below.

|**File Format Types**|**Description**|
| :- | :- |
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

#### **Opening Microsoft Excel 95/5.0 Files**

To open Microsoft Excel 95 files, use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class and select **[EXCEL_95](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#EXCEL_95)** value in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration. Sample file to test the code can be downloaded from the following link:

[Excel95_5.0.xls](Excel95_5.0.xls)

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

#### **Opening Microsoft Excel 97 Files**

To open Microsoft Excel 97 files, use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** method and select the **[EXCEL_97_TO_2003](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#EXCEL_97_TO_2003)** value in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

#### **Opening Microsoft Excel 2000 Files**

To open Microsoft Excel 2000 files, use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class and select the **[XLSX](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#XLSX)** value in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

#### **Opening Microsoft Excel 2003 Files**

To open Microsoft Excel 2003 files, use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class and select the **[EXCEL_97_TO_2003](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#EXCEL_97_TO_2003)** value, predefined in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

#### **Opening Microsoft Excel XP Files**

To open Microsoft Excel XP files, use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class and select the **[EXCEL_97_TO_2003](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#EXCEL_97_TO_2003)** value, predefined in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

#### **Opening Microsoft Excel 2007/2010 XLSX Files**

To open Microsoft Excel 2007/2010 XLSX files, use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class and select the **[XLSX](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#XLSX)** value, predefined in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

#### **Opening Files with Different Formats**

Aspose.Cells allows developers to open spreadsheet files with different formats such as SpreadsheetML, CSV, Tab Delimited files. To open such files, developers can use the same methodology as they use for opening files of different Microsoft Excel versions.

#### **Opening SpreadsheetML Files**

SpreadsheetML files are the XML representations of your spreadsheets including all information about the spreadsheet such as formatting, formulae, etc. Since Microsoft Excel XP, an XML export option is added to Microsoft Excel that exports your spreadsheets to SpreadsheetML files.

To open SpreadsheetML files, use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class and select the **[EXCEL_2003_XML](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#EXCEL_2003_XML)** value, predefined in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

#### **Opening CSV Files**

Comma Separated Values (CSV) files contain records whose values are delimited or separated by commas. In CSV files, data is stored in a tabular format that has fields separated by the comma character and quoted by the double-quote character. If a field's value contains a double quote character it is escaped with a pair of double-quote characters. You can also use Microsoft Excel to export your spreadsheet data to a CSV file.

To open CSV files, use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class and select the **[CSV](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#CSV)** value, predefined in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

#### **Opening CSV files and replacing invalid characters**

In Excel, when CSV file with special characters is opened, the characters are automatically replaced. The same is done by Aspose.Cells API which is demonstrated in the code example given below.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

#### **Opening CSV files using preferred parser**

This is not always necessary to use default parser settings for opening the CSV files. Sometimes importing CSV file does not create expected output like date format is not as expected or empty fields are handled differently. For this purpose **[TxtLoadOptions.PreferredParsers](https://apireference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)** is available to provide own preferred parser to parse different data types as per the requirement. Following sample code demonstrates the usage of the preferred parser.  

Sample source file and output files can be downloaded from the following links for testing this feature.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

#### **Opening Tab Delimited Files**

Tab-delimited files contain spreadsheet data but without any formatting. Data is arranged in rows and columns such as tables and spreadsheets. Shortly, a tab-delimited file is a special kind of plain text file with a tab between each column in the text.

To open tab-delimited files, developers should use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class and select the **[TAB_DELIMITED](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#TAB_DELIMITED)** value, predefined in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

#### **Opening Tab-Separated Values (TSV) Files**

TSV files are also used to contain spreadsheet data but without any formatting. The format is the same with Tab Delimited where data is arranged in rows and columns such as tables and spreadsheets.

To open tab-delimited files, developers should use the **[LoadOptions](https://apireference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class and select the **[TSV](https://apireference.aspose.com/cells/java/com.aspose.cells/fileformattype#TSV)** value, predefined in the **[FileFormatType](https://apireference.aspose.com/cells/java/com.aspose.cells/FileFormatType)** enumeration.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningTSVFiles-1.java" >}}

#### **Opening Encrypted Excel Files**

We know that it's possible to create encrypted Excel files using Microsoft Excel. To open such encrypted files, developers should call a special overloaded LoadOptions method and select the DEFAULT value, predefined in the FileFormatType enumeration. This method would also take the password for the encrypted file as shown below in the example.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells also supports opening password-protected MS Excel 2013 files.

{{% alert color="primary" %}}

There are fair chances that the Workbook constructor may throw System.OutOfMemoryException while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory, therefore, the spreadsheet has to be loaded while enabling the [Memory Preferences](https://docs.aspose.com/cells/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

#### **Opening SXC Files**

StarOffice Calc is similar to Microsoft Excel and supports formulas, charts, functions, and macros. The spreadsheets created with this software are saved with the SXC extension. The SXC file is also used for OpenOffice.org Calc spreadsheet files. Aspose.Cells can read SXC files as demonstrated by the following code sample.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

#### **Opening FODS Files**

FODS file is spreadsheet saved in OpenDocument XML without any compression. Aspose.Cells can read FODS files as demonstrated by the following code sample.

##### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}
