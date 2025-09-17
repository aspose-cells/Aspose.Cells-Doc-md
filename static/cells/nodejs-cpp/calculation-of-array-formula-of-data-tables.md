##Calculation of Array Formula of Data Tables with Node.js via C++
How to use the Aspose.Cells library to calculate array formulas for a data table in Microsoft Excel using Node.js via C++. Load or create an Excel file, calculate the array formula, and save the modified file.
You can create a Data Table in Microsoft Excel using Data > What-If Analysis > Data Table.... Aspose.Cells now allows you to calculate the array formula of a data table. Please use [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) as normal for calculating any type of formulas.
In the following sample code, we used the [source excel file](5115535.xlsx). If you change the value of cell B1 to 100, the values of the Data Table which are filled with Yellow color will become 120 as shown in the following images. The sample code generates the [output PDF](5115538.pdf).
![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)
![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)
Here is the sample code used to generate the [output PDF](5115538.pdf) from the [source excel file](5115535.xlsx). Please read the comments for more information.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);
// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);
// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();
// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```
