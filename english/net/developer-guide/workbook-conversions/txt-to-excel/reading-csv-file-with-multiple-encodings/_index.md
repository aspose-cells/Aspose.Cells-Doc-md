---
title: Reading CSV File with Multiple Encodings
type: docs
weight: 200
url: /net/reading-csv-file-with-multiple-encodings/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, your CSV file contains multiple Encodings (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells allows you to load such CSV files and converting them into other formats, for example, PDF or XLSX.

{{% /alert %}}

Aspose.Cells provides the [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) property, which you need to set to **true** to load your CSV file with multiple encodings properly.

The following screenshot shows a sample CSV file that contains two lines. The first line is in **ANSI** encoding and the second line is in **Unicode** encoding

|**Input file**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

The following screenshot shows the XLSX file converted from the above CSV file without setting the [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) property to **true**. As you can see, the Unicode text was not converted properly.

|**Output file 1: no accommodation made for multiple encoding**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

The following screenshot shows the XSLX file converted from the above CSV file after setting the [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) property to **true**. As you can see, the Unicode text is now converted properly.

|**Output file 2: IsMultiEncoded is set to true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Below is the sample code that converts the above CSV file into XLSX format properly.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Related Articles

- [Opening CSV Files](/cells/net/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="csharp" >}}
