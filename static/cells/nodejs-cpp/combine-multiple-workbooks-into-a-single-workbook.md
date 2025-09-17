##Combine Multiple Workbooks into a Single Workbook with Node.js via C++
Learn how to combine multiple workbooks into a single workbook using Aspose.Cells for Node.js via C++.
Sometimes, you need to combine workbooks with various content like images, charts and data into a single workbook. Aspose.Cells for Node.js via C++ supports this feature. This article shows how to create a console application and combine workbooks with a few, simple lines of code using Aspose.Cells.
## **Combining Workbooks with Images and Charts**
The example code combines two workbooks into a single workbook using Aspose.Cells for Node.js via C++. The code loads the source workbooks, uses the [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) method to combine them, and saves the output workbook.
### **Source Workbooks**
- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)
### **Output Workbooks**
- [combined.xlsx](5473095.xlsx)
### **Screenshots**
Below are screenshots of the source and output workbooks.
You can use any source workbooks. These images are just for illustration purposes.
**The first worksheet of the charts workbook - stacked**
![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)
**Second worksheet of charts workbook - line**
![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)
**First worksheet of the picture workbook - picture**
![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)
**All three worksheets in the combined workbook - stacked, line, picture**
![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));
// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));
// Combining the two workbooks
sourceBook1.combine(sourceBook2);
const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```
## **Advance topics**
- [Combine Multiple Worksheets into a Single Worksheet](https://docs.aspose.com/cells/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Merge Files](https://docs.aspose.com/cells/nodejs-cpp/merge-files/)
