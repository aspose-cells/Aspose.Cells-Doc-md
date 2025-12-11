---
title: Convert CSV, TSV, and TXT to Excel with Golang via C++
linktitle: Convert CSV, TSV, and TXT to Excel
type: docs
weight: 30
url: /go-cpp/convert-csv-tsv-and-txt-to-excel/
description: Learn how to convert CSV, TSV, and TXT files to Excel using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Using Aspose.Cells for C++, you can convert CSV files to Excel, OpenOffice, PDF, JSON, and many other formats.

{{% /alert %}}

## **Opening CSV Files**

Comma‑Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double‑quote character. If a field value contains a double‑quote character, it is escaped with a pair of double‑quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **Opening CSV Files and Replacing Invalid Characters**

In Excel, when a CSV file with special characters is opened, the characters are automatically replaced. The same is done by the Aspose.Cells API, as demonstrated in the code example below.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **Using Preferred Parser**

It is not always necessary to use default parser settings for opening CSV files. Sometimes, importing a CSV file does not create the expected output, such as when the date format is not as expected or empty fields are handled differently. For this purpose, **TxtLoadOptions.PreferredParsers** is available to provide your own preferred parser to parse different data types as per your requirements. The following sample code demonstrates the usage of a preferred parser.

Sample source file and output files can be downloaded from the following links for testing this feature.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **Opening Text Files with a Custom Separator**

Text files are used to hold spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **Opening Tab-Delimited Files**

Tab‑delimited (Text) files contain spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab‑delimited file is a special kind of plain text file with a tab between each column.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **Opening Tab-Separated Values (TSV) Files**

Tab‑separated values (TSV) files contain spreadsheet data but without any formatting. They are the same as a tab‑delimited file, where data is arranged in rows and columns like in tables and spreadsheets.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## **Advanced Topics**
- [Load or Import CSV File with Formulas](/cells/cpp/load-or-import-csv-file-with-formulas/)
- [Reading CSV File with Multiple Encodings](/cells/cpp/reading-csv-file-with-multiple-encodings/)