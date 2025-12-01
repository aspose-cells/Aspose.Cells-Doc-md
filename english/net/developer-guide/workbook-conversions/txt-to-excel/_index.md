---
title: Convert CSV, TSV and TXT to Excel
type: docs
weight: 30
url: /net/convert-csv-tsv-and-txt-to-excel/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Using Aspose.Cells, you can convert CSV file to Excel , OpenOffice, Pdf, Json and many different formats.

{{% /alert %}}


## **Opening CSV Files**

Comma Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double quote character. If a field value contains a double quote character it is escaped with a pair of double quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Opening CSV files and replacing invalid characters**

In Excel, when CSV file with special characters is opened, the characters are automatically replaced. The same is done by Aspose.Cells API which is demonstrated in the code example given below.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Using preferred parser**

This is not always necessary to use default parser settings for opening the CSV files. Sometimes importing CSV file does not create expected output like date format is not as expected or empty fields are handled differently. For this purpose **TxtLoadOptions.PreferredParsers** is available to provide own preferred parser to parse different data types as per the requirement. Following sample code demonstrates the usage of preferred parser.  

Sample source file and output files can be downloaded from the following links for testing this feature.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Opening Text Files with Custom Separator**

Text files are used to hold spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Opening Tab Delimited Files**

Tab delimited (Text) file contains spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab delimited file is a special kind of plain text file with a tab between each column.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Opening Tab-Separated Values (TSV) Files**

Tab-separated values (TSV) file contains spreadsheet data but without any formatting. It is the same with Tab Delimited file where data is arranged in rows and columns like in tables and spreadsheets.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Advance topics**
- [Load or Import CSV file with Formulas](/cells/net/load-or-import-csv-file-with-formulas/)
- [Reading CSV File with Multiple Encodings](/cells/net/reading-csv-file-with-multiple-encodings/)

{{< app/cells/assistant language="csharp" >}}
