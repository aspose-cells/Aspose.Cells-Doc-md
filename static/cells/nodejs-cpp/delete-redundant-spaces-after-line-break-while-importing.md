##Delete redundant spaces after line break while importing HTML with Node.js via C++
Learn how to delete redundant spaces after line breaks while importing HTML using Aspose.Cells for Node.js via C++.
Please use [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) property and set it **true** to delete all the redundant spaces coming after the line break tag. By default, this property is **false** and redundant spaces are preserved in the output Excel files.
## Effect of setting the HTMLLoadOptions.deleteRedundantSpaces property to false and true
The following screenshot shows the effect of setting this property to **false** and **true**.
![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## Delete redundant spaces after line break while importing HTML
### Programming Sample
The following sample code shows the usage of the [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) property. Please set it **true** or **false** to get the output as shown in the above screenshot.
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// Sample Html containing redundant spaces after <br> tag
const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";
// Convert Html to byte array
const byteArray = Buffer.from(html, 'utf-8');
// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setDeleteRedundantSpaces(true);
// Convert byte array into stream
const stream = Uint8Array.from(byteArray);
// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Auto fit the sheet columns
sheet.autoFitColumns();
// Save the workbook
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
