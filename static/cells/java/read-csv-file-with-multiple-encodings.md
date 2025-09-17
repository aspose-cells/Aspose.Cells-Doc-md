##Read CSV File With Multiple Encodings
## **Aspose.Cells - Read CSV File With Multiple Encodings**
Sometime, your CSV file contains multiple Encodings (Unicode, ANSI, UTF8, UTF7 etc). Aspose.Cells allows you to load such CSV files and converting them into other formats, for example PDF or XLSX.
**Java**
//Set Multi Encoded Property to True
TxtLoadOptions options = new TxtLoadOptions();
options.setMultiEncoded(true);
//Load the CSV file into Workbook
Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);
//Save it in XLSX format
workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)
For more details, visit [Reading CSV File with Multiple Encodings](https://docs.aspose.com/cells/java/reading-csv-file-with-multiple-encodings).
