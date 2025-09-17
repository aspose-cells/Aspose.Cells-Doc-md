##Change the HTML Link Target Type with Node.js via C++
Learn how to change the HTML link target type using Aspose.Cells for Node.js via C++. Control the target attribute in your HTML links.
Aspose.Cells allows you to change the HTML link target type. HTML link looks like this
As you can see, the target attribute in the above HTML link is **_self**. You can control this target attribute using the [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--) property. This property takes the [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype) enum which has the following values.
- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top
The following code illustrates the usage of [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--) property. It changes the link target type to **blank**. By default, it is **parent**.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Sample1.xlsx");
const outputPath = path.join(dataDir, "Output.out.html");
const workbook = new AsposeCells.Workbook(inputPath);
const opts = new AsposeCells.HtmlSaveOptions();
opts.setLinkTargetType(AsposeCells.HtmlLinkTargetType.Self);
workbook.save(outputPath, opts);
console.log(`File saved: ${outputPath}`);
```
