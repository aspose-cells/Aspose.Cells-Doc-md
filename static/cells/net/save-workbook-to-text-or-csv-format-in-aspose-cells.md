##Save Workbook to Text or CSV Format in Aspose.Cells
Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.
The following code example explains how to save an entire workbook into text format. Load the source workbook which could be any Microsoft Excel or OpenOffice spreadsheet file (so XLS, XLSX, XLSM, XLSB, ODS and so on) with any number of worksheets.
When the code is executed, it converts the data of all sheets in the workbook to TXT format.
You can modify the same example to save your file to CSV. By default, TxtSaveOptions.Separator is comma, so do not specify a separator if saving to CSV format.
**C#**
string filePath = "source.xlsx";
//Load your source workbook
Workbook workbook = new Workbook(filePath);
//0-byte array
byte[] workbookData = new byte[0];
//Text save options. You can use any type of separator
TxtSaveOptions opts = new TxtSaveOptions();
opts.Separator = '\t';
//Copy each worksheet data in text format inside workbook data array
for (int idx = 0; idx < workbook.Worksheets.Count; idx++)
{
//Save the active worksheet into text format
MemoryStream ms = new MemoryStream();
workbook.Worksheets.ActiveSheetIndex = idx;
workbook.Save(ms, opts);
//Save the worksheet data into sheet data array
ms.Position = 0;
byte[] sheetData = ms.ToArray();
//Combine this worksheet data into workbook data array
byte[] combinedArray = new byte[workbookData.Length + sheetData.Length];
Array.Copy(workbookData, 0, combinedArray, 0, workbookData.Length);
Array.Copy(sheetData, 0, combinedArray, workbookData.Length, sheetData.Length);
workbookData = combinedArray;
}
//Save entire workbook data into file
File.WriteAllBytes(filePath + ".out.txt", workbookData);
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
