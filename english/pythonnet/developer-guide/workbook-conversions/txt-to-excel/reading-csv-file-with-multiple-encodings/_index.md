---
title: Reading CSV File with Multiple Encodings
type: docs
weight: 200
url: /python-net/reading-csv-file-with-multiple-encodings/
description: Reading CSV File with Multiple Encodings by using Aspose.Cells for Python via .NET API.
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---

{{% alert color="primary" %}}

Sometimes, your CSV file contains multiple Encodings (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells allows you to load such CSV files and converting them into other formats, for example, PDF or XLSX.

{{% /alert %}}

Aspose.Cells provides the [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) property, which you need to set to **true** to load your CSV file with multiple encodings properly.

The following screenshot shows a sample CSV file that contains two lines. The first line is in **ANSI** encoding and the second line is in **Unicode** encoding

|**Input file**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

The following screenshot shows the XLSX file converted from the above CSV file without setting the [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) property to **true**. As you can see, the Unicode text was not converted properly.

|**Output file 1: no accommodation made for multiple encoding**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

The following screenshot shows the XSLX file converted from the above CSV file after setting the [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) property to **true**. As you can see, the Unicode text is now converted properly.

|**Output file 2: IsMultiEncoded is set to true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Below is the sample code that converts the above CSV file into XLSX format properly.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
