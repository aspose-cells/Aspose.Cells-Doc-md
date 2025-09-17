##Public API Changes in Aspose.Cells 8.7.1
This document describes the changes to the Aspose.Cells API from version 8.7.0 to 8.7.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.
## **Added APIs**
### **Added LookInType.OriginalValues Property**
Aspose.Cells APIs already support the [Find or Search Data](https://docs.aspose.com/cells/net/find-or-search-data/) feature for spreadsheets in order to find some particular piece of contents in cell value & formula. However, this feature was lacking the aspect of formatting applied onto the cell that may change the appearance as well as the value of the contents, consequently make the text unsearchable using the original value. With this release of Aspose.Cells APIs, another constant by the name LookInType.OriginalValues has been exposed to the public API which allows to overcome the situation as discussed above.
For more details on this feature, please review the detailed article on [Search Data Using Original Values](https://docs.aspose.com/cells/net/search-data-using-original-values/)
Following is the simple usage scenario.
**C#**
//Create workbook object
Workbook workbook = new Workbook();
//Access first worksheet
Worksheet worksheet = workbook.Worksheets[0];
//Add 10 in cell A1 and A2
worksheet.Cells["A1"].PutValue(10);
worksheet.Cells["A2"].PutValue(10);
//Add Sum formula in cell D4 but customize it as ---
Cell cell = worksheet.Cells["D4"];
Style style = cell.GetStyle();
style.Custom = "---";
cell.SetStyle(style);
//The result of formula will be 20
//but 20 will not be visible because
//the cell is formatted as ---
cell.Formula = "=Sum(A1:A2)";
//Calculate the workbook
workbook.CalculateFormula();
//Create find options
FindOptions options = new FindOptions();
options.LookInType = LookInType.OriginalValues;
options.LookAtType = LookAtType.EntireContent;
Cell foundCell = null;
object obj = 20;
//Find 20 which is Sum(A1:A2) and formatted as ---
foundCell = worksheet.Cells.Find(obj, foundCell, options);
//Print the found cell
Console.WriteLine(foundCell);
### **Added OnBeforeColumnFilter Event for GridWeb**
Aspose.Cells.GridWeb for .NET 8.7.1 has exposed the OnBeforeColumnFilter event which serves as callback to the filtering mechanism done through the GridWeb UI. As the name suggests, the event is triggered before the column filtering is applied and can be used to get the filtering information such as column index and value on which filter has to be applied.
Simple usage scenario looks as follow.
**C#**
protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)
{
string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;
}
Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>
