---
title: Reading CSV File with Multiple Encodings using Node.js via C++
linktitle: Reading CSV File with Multiple Encodings
type: docs
weight: 200
url: /nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: Learn how to read CSV files with multiple encodings using Aspose.Cells for Node.js via C++.
---


{{% alert color="primary" %}}

Sometimes, your CSV file contains multiple Encodings (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells allows you to load such CSV files and convert them into other formats, for example, PDF or XLSX.

{{% /alert %}}

Aspose.Cells provides the [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) property, which you need to set to **true** to load your CSV file with multiple encodings properly.

The following screenshot shows a sample CSV file that contains two lines. The first line is in **ANSI** encoding and the second line is in **Unicode** encoding

|**Input file**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

The following screenshot shows the XLSX file converted from the above CSV file without setting the [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) property to **true**. As you can see, the Unicode text was not converted properly.

|**Output file 1: no accommodation made for multiple encoding**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

The following screenshot shows the XSLX file converted from the above CSV file after setting the [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) property to **true**. As you can see, the Unicode text is now converted properly.

|**Output file 2: IsMultiEncoded is set to true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Below is the sample code that converts the above CSV file into XLSX format properly.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## Related Articles

- [Opening CSV Files](/cells/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
