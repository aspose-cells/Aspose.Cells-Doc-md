##Render Unicode Supplementary characters in output PDF by Aspose.Cells for Node.js via C++
Learn how to render Unicode Supplementary characters in output PDF using Aspose.Cells for Node.js via C++.
Normal Unicode characters are 2-bytes long while Unicode Supplementary characters are 4-bytes long. Aspose.Cells now supports rendering of these 4-bytes Unicode characters.
In the Unicode Character Standard, Supplementary Characters are the characters assigned code points from U+10000 to U+10FFFF. In other words, these are the Unicode characters greater than U+FFFF.
- In UTF-8 these characters are each 4 bytes long.
- In UTF-16 these characters require 2 surrogates (16-bit units).
## Render Unicode Supplementary characters in output PDF by Aspose.Cells for Node.js via C++
The following screenshot shows how Aspose.Cells rendered the [source excel file](5115563.xlsx) into the [output PDF](5115564.pdf). As you can see all three Unicode Supplementary characters have been rendered exactly the same as done by Microsoft Excel.
![todo:image_alt_text](output.png)
## Sample Code
You can use this sample code to convert [source excel file](5115563.xlsx) into [output PDF](5115564.pdf).
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source excel file containing Unicode Supplementary characters
const workbook = new AsposeCells.Workbook(path.join(dataDir, "unicode-supplementary-characters.xlsx"));
// Save the workbook
workbook.save(path.join(dataDir, "RenderUnicodeInOutput_out.pdf"));
```
