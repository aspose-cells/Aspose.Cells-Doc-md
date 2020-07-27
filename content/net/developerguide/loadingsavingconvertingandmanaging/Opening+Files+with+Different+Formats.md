+++
title = "Opening Files with Different Formats" 
description = "" 
weight = 12062 
+++

Aspose.Cells for .NET : Opening Files with Different Formats  

# Aspose.Cells for .NET : Opening Files with Different Formats



Using `Aspose.Cells` you can open files with different formats. **`Aspose.Cells`** can open a range of file formats such as Microsoft Excel spreadsheets (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Comma\-separated values (CSV), Tab Delimited or Tab-separated values (TSV) files etc.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Opening Files with Different Formats](#OpeningFileswithDifferentFormats-OpeningFileswithDifferentFormats)
    *   1.1 [Opening SpreadsheetML Files](#OpeningFileswithDifferentFormats-OpeningSpreadsheetMLFiles)
    *   1.2 [Opening HTML Files](#OpeningFileswithDifferentFormats-OpeningHTMLFiles)
    *   1.3 [Opening CSV Files](#OpeningFileswithDifferentFormats-OpeningCSVFiles)
        *   1.3.1 [Opening CSV files and replacing invalid characters](#OpeningFileswithDifferentFormats-OpeningCSVfilesandreplacinginvalidcharacters)
        *   1.3.2 [Using preferred parser](#OpeningFileswithDifferentFormats-Usingpreferredparser)
    *   1.4 [Opening Text Files with Custom Separator](#OpeningFileswithDifferentFormats-OpeningTextFileswithCustomSeparator)
    *   1.5 [Opening Tab Delimited Files](#OpeningFileswithDifferentFormats-OpeningTabDelimitedFiles)
    *   1.6 [Opening Tab-Separated Values (TSV) Files](#OpeningFileswithDifferentFormats-OpeningTab-SeparatedValues(TSV)Files)
    *   1.7 [Opening SXC Files](#OpeningFileswithDifferentFormats-OpeningSXCFiles)
    *   1.8 [Opening FODS Files](#OpeningFileswithDifferentFormats-OpeningFODSFiles)
{{< /panel >}}
 

## Opening Files with Different Formats

Aspose.Cells allows developers to open spreadsheet files with different formats such as SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV), ODS files. To open such files, developers can use the same methodology as they use for opening files of different Microsoft Excel versions.

### Opening SpreadsheetML Files

SpreadsheetML files are XML representations of spreadsheets including all information about it, such as formatting, formulae etc. Since Microsoft Excel XP, an XML export option is added to Microsoft Excel that exports your spreadsheets to SpreadsheetML files.

### Opening HTML Files

Aspose.Cells allows you to open HTML file into Workbook object. The HTML file should Microsoft Excel oriented i.e MS-Excel should be able to open it.

### Opening CSV Files

Comma Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double quote character. If a field value contains a double quote character it is escaped with a pair of double quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

#### Opening CSV files and replacing invalid characters

In Excel, when CSV file with special characters is opened, the characters are automatically replaced. The same is done by Aspose.Cells API which is demonstrated in the code example given below.

#### Using preferred parser

This is not always necessary to use default parser settings for opening the CSV files. Sometimes importing CSV file does not create expected output like date format is not as expected or empty fields are handled differently. For this purpose **TxtLoadOptions.PreferredParsers**is available to provide own preferred parser to parse different data types as per the requirement. Following sample code demonstrates the usage of preferred parser.  

Sample source file and output files can be downloaded from the following links for testing this feature.

[samplePreferredParser.csv](https://docs2.aspose.com/cells/net/attachments/5013529/73990157.csv)

[outputsamplePreferredParser.xlsx](https://docs2.aspose.com/cells/net/attachments/5013529/73990158.xlsx)  

### Opening Text Files with Custom Separator

Text files are used to hold spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters.

### Opening Tab Delimited Files

Tab delimited (Text) file contains spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab delimited file is a special kind of plain text file with a tab between each column.

### Opening Tab-Separated Values (TSV) Files

Tab-separated values (TSV) file contains spreadsheet data but without any formatting. It is the same with Tab Delimited file where data is arranged in rows and columns like in tables and spreadsheets.

### Opening SXC Files

StarOffice Calc is similar to Microsoft Excel and supports formulas, charts, functions, and macros. The spreadsheets created with this software are saved with the SXCextension. The SXC file is also used for OpenOffice.org Calc spreadsheet files. Aspose.Cells can read SXC files as demonstrated by the following code sample.

### Opening FODS Files

FODS file is spreadsheet saved in OpenDocument XML without any compression. Aspose.Cells can read FODS files as demonstrated by the following code sample.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [samplePreferredParser.csv](https://docs2.aspose.com/cells/net/attachments/5013529/73990157.csv) (text/csv)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [outputsamplePreferredParser.xlsx](https://docs2.aspose.com/cells/net/attachments/5013529/73990158.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

