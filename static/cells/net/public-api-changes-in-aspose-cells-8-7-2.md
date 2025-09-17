##Public API Changes in Aspose.Cells 8.7.2
This document describes the changes to the Aspose.Cells API from version 8.7.1 to 8.7.2 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.
## **Added APIs**
### **Extended the Default Calculation Engine**
Aspose.Cells APIs have powerful calculation engine that can calculate almost all of the Microsoft Excel functions. Moreover, the Aspose.Cells APIs now allow to extend the default calculation engine to meet custom calculation requirements of any application.
Following APIs have been added with the release of Aspose.Cells for .NET 8.7.2.
1. AbstractCalculationEngine Class
1. CalculationData Class
1. CalculationOptions.CustomEngine Property
Above mentioned APIs allow to implement custom calculation engine for all functions (including Excel's native functions) with more flexibility.
For more details on this feature, please review the detailed article on [Implementing Custom Calculation Engine](https://docs.aspose.com/cells/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
Following is the simple usage scenario.
**C#**
public class MyEngine : AbstractCalculationEngine
{
public override void Calculate(CalculationData data)
{
string funcName = data.FunctionName.ToUpper();
if ("MYFUNC".Equals(funcName))
{
//do calculation for MYFUNC here
int count = data.ParamCount;
object res = null;
for (int i = 0; i < count; i++)
{
object pv = data.GetParamValue(i);
if (pv is ReferredArea)
{
ReferredArea ra = (ReferredArea)pv;
pv = ra.GetValue(0, 0);
}
//process the parameter here
//res = ...;
}
data.CalculatedValue = res;
}
}
}
### **Added Overloaded Indexer for TextBoxCollection**
Aspose.Cells for .NET 8.7.2 has exposed the overloaded indexed for the TextBoxCollection class in order to access the instance of TextBox using its name as string.
For more details on this feature, please review the detailed article on [Accessing the TextBox via its Name](https://docs.aspose.com/cells/net/access-the-text-box-by-the-name/)
Simple usage scenario looks as follow.
**C#**
//Create an instance of Workbook
Workbook workbook = new Workbook();
//Access the first Worksheet from the collection
Worksheet sheet = workbook.Worksheets[0];
//Add a TextBox to the collection
int idx = sheet.TextBoxes.Add(10, 10, 10, 10);
//Access the TextBox using its index
TextBox box = sheet.TextBoxes[idx];
//Set the name for the TextBox
box.Name = "MyTextBox";
//Access the same TextBox via its name
box = sheet.TextBoxes["MyTextBox"];
### **Added OnAfterColumnFilter Event for GridWeb**
Aspose.Cells.GridWeb for .NET 8.7.2 has exposed the OnAfterColumnFilter event which serves as callback to the filtering mechanism done through the Aspose.Cells.GridWeb UI. As the name suggests, the event is triggered after the column filtering is applied and can be used to get the filtering information such as column index on which filter was applied and selected filter value.
Simple usage scenario looks as follow.
**C#**
protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)
{
string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;
}
Do not forget to register the event to GridWeb control <acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>
