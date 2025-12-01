---
title: Convert CSV, TSV and TXT to Excel
type: docs
weight: 50
url: /java/convert-csv-tsv-and-txt-to-excel/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Opening CSV Files**

Comma Separated Values (CSV) files contain records whose values are delimited or separated by commas. In CSV files, data is stored in a tabular format that has fields separated by the comma character and quoted by the double-quote character. If a field's value contains a double quote character it is escaped with a pair of double-quote characters. You can also use Microsoft Excel to export your spreadsheet data to a CSV file.

To open CSV files, use the [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) class and select the [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV) value, predefined in the [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) enumeration.

## **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Opening CSV files and replacing invalid characters**

In Excel, when CSV file with special characters is opened, the characters are automatically replaced. The same is done by Aspose.Cells API which is demonstrated in the code example given below.

#### **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Opening CSV files using preferred parser**

This is not always necessary to use default parser settings for opening the CSV files. Sometimes importing CSV file does not create expected output like date format is not as expected or empty fields are handled differently. For this purpose [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) is available to provide own preferred parser to parse different data types as per the requirement. Following sample code demonstrates the usage of the preferred parser.  

Sample source file and output files can be downloaded from the following links for testing this feature.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Opening TSV(Tab Delimited) Files**

Tab-delimited files contain spreadsheet data but without any formatting. Data is arranged in rows and columns such as tables and spreadsheets. Shortly, a tab-delimited file is a special kind of plain text file with a tab between each column in the text.

To open tab-delimited files, developers should use the [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) class and select the [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV) value, predefined in the [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) enumeration.

## **Example**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Advance topics**
- [Load or Import CSV file with Formulas](/cells/java/load-or-import-csv-file-with-formulas/)
- [Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format](/cells/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

{{< app/cells/assistant language="java" >}}
