const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "data/";
const workbook = new AsposeCells.Workbook(dataDir + "book1.xls");

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
    const sourceSheet = workbook.getWorksheets().get(i);
    const sheetName = sourceSheet.getName();
    
    const destWorkbook = new AsposeCells.Workbook();
    const destIndex = destWorkbook.getWorksheets().add();
    const destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    const destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, AsposeCells.SaveFormat.Excel97To2003);
}