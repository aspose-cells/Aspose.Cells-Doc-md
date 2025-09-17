##Use Custom XML Parts in Aspose.Cells with Node.js via C++
Learn how to use custom XML parts in Aspose.Cells for Node.js via C++. Integrate external XML data within Excel files seamlessly.
## Using Custom XML Parts in Aspose.Cells
Custom XML Parts are the XML data that is stored by different applications like SharePoint etc. inside the Excel file. This data is consumed by different applications that need it. Microsoft Excel does not make use of this data so there is no GUI to add it. You can view this data by changing the extension of **.xlsx** into **.zip** and then by opening it using **WinZip**. You can also open the ZIP file using any third-party Windows zip utility such as WinRAR or WinZip etc. The data is present inside the **customXml** folder.
You can add custom XML parts using Aspose.Cells via the [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) method.
The following sample code makes use of [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) method and adds the **Book Catalog XML** and its name is **BookStore**. The following image shows the result of this code. As you can see, Book Catalog XML is added inside the BookStore node which is the name of this property.
![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)
![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)
## Node.js code to use custom XML parts
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");
// The sample XML that will be injected to Workbook
const booksXML = `<catalog>
// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();
// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);
// Save the resultant spreadsheet
workbook.save(filePath);
```
## Related Article
- [Adding Custom Properties visible inside Document Information Panel](https://docs.aspose.com/cells/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
