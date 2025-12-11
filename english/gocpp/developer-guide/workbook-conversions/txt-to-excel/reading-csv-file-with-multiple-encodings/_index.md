---
title: Reading CSV File with Multiple Encodings with Golang via C++
linktitle: Reading CSV File with Multiple Encodings
type: docs
weight: 200
url: /go-cpp/reading-csv-file-with-multiple-encodings/
description: Learn how to read CSV files with multiple encodings using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Sometimes, your CSV file contains multiple encodings (Unicode, ANSI, UTF‑8, UTF‑7, etc). Aspose.Cells allows you to load such CSV files and convert them into other formats, for example, PDF or XLSX.

{{% /alert %}}

Aspose.Cells provides the [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) property, which you need to set to **true** to load your CSV file with multiple encodings properly.

The following screenshot shows a sample CSV file that contains two lines. The first line is in **ANSI** encoding and the second line is in **Unicode** encoding.

|**Input file**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

The following screenshot shows the XLSX file converted from the above CSV file without setting the [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) property to **true**. As you can see, the Unicode text was not converted properly.

|**Output file 1: no accommodation made for multiple encoding**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

The following screenshot shows the XLSX file converted from the above CSV file after setting the [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) property to **true**. As you can see, the Unicode text is now converted properly.

|**Output file 2: IsMultiEncoded is set to true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Below is the sample code that converts the above CSV file into XLSX format properly.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadingCsvFileWithMultipleEncodings.go" >}}

## Related Articles

- [Opening CSV Files](/cells/cpp/opening-files-with-different-formats/#opening-csv-files)