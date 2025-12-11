---
title: Convert CSV, TSV and TXT to Excel
type: docs
weight: 30
url: /net/convert-csv-tsv-and-txt-to-excel/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Using Aspose.Cells, you can convert a CSV file to Excel, OpenOffice, PDF, JSON and many different formats.

{{% /alert %}}


## **Opening CSV Files**

Comma-Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double quote character. If a field value contains a double quote character it is escaped with a pair of double quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Opening CSV files and replacing invalid characters**

In Excel, when a CSV file with special characters is opened, the characters are automatically replaced. The same is done by the Aspose.Cells API, as demonstrated in the code example given below.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Using preferred parser**

It is not always necessary to use the default parser settings when opening CSV files. Sometimes importing a CSV file does not create the expected output, such as the date format being incorrect or empty fields being handled differently. For this purpose, **TxtLoadOptions.PreferredParsers** is available to provide a custom parser to parse different data types as required. The following sample code demonstrates the usage of the preferred parser.

Sample source file and output files can be downloaded from the following links for testing this feature.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Opening Text Files with Custom Separator**

Text files are used to hold spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Opening Tab Delimited Files**

A tab-delimited (text) file contains spreadsheet data but without any formatting. Data is arranged in rows and columns, like in tables and spreadsheets. Basically, a tab-delimited file is a special kind of plain text file with a tab between each column.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Opening Tab-Separated Values (TSV) Files**

A tab-separated values (TSV) file contains spreadsheet data but without any formatting. It is the same as a tab-delimited file, where data is arranged in rows and columns like in tables and spreadsheets.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Advanced topics**
- [Load or Import CSV file with Formulas](/cells/net/load-or-import-csv-file-with-formulas/)
- [Reading CSV File with Multiple Encodings](/cells/net/reading-csv-file-with-multiple-encodings/)

{{< app/cells/assistant language="csharp" >}}
