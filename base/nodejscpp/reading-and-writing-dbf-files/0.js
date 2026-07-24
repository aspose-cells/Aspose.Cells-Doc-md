const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "Data/";
const filePath = path.join(dataDir, "example.dbf");

const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Dbf);

const workbook = new AsposeCells.Workbook(filePath, loadOptions);

const worksheet = workbook.getWorksheets().get(0);

const cells = worksheet.getCells();

const sb = [];

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

for (let i = 0; i <= maxRow; i++)
{
    for (let j = 0; j <= maxCol; j++)
    {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        sb.push("|");
        sb.push(value);
    }
    sb.push("|");
    sb.push("\n");
}

console.log(sb.join(""));

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);