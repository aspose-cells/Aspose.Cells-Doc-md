##Add XML Map inside the Workbook using XmlMapCollection.Add method with Node.js via C++
Learn how to add XML Map inside the workbook using XmlMapCollection.Add method with Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
Aspose.Cells provides [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) method which you can use to import your XML Map inside the workbook.
## **Add XML Map inside the Workbook using XmlMapCollection.Add method**
The following sample code adds XML Map inside the workbook using the [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) method and saves it as [output excel file](5115434.xlsx). The screenshot shows the XML Map that has been imported from the [sample.xml](5115433.xml) inside the output excel file.
![add-xml-map](add-xml-map.png)
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const wb = new AsposeCells.Workbook();
// Add xml map found inside the sample.xml inside the workbook
wb.getWorksheets().getXmlMaps().add(path.join(dataDir, "sample.xml"));
// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
