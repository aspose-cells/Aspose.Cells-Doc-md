##Avoid exponential notation of large numbers while importing from HTML
Learn how to prevent large numbers from being converted to exponential notation while importing from HTML using Aspose.Cells for Node.js via C++.
Sometimes your HTML contains numbers like 1234567890123456, which are longer than 15 digits, and when you import your HTML to an Excel file, these numbers convert to exponential notation like 1.23457E+15. If you want your number to be imported as it is and not converted to exponential notation, then please use [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) property and set it **true** while loading your HTML.
The following sample code explains the usage of [**HtmlLoadOptions.getKeepPrecision()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getKeepPrecision--) property. The API will import the number as it is without converting it to exponential notation.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// Sample Html containing large number with digits greater than 15
const html = "<html><body><p>1234567890123456</p></body></html>";
// Convert Html to byte array
const byteArray = new TextEncoder().encode(html);
// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setKeepPrecision(true);
// Convert byte array into stream
const stream = byteArray;
// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Auto fit the sheet columns
sheet.autoFitColumns();
// Save the workbook
const outputDir = path.join(__dirname, "output/");
workbook.save(path.join(outputDir, "outputAvoidExponentialNotationWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
