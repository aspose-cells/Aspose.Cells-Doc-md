##Set Worksheet Tab Color in Aspose.Cells
## **Aspose.Cells - Set Worksheet Tab Color**
Aspose.Cells allows you to change the color of individual worksheet tabs to make them prominent from the rest. For example, you can make Expenses red, Sales green, Assets blue, etc.
### **Setting Worksheet Tab Color with Microsoft Excel**
1. Right-click a tab in the tab-sheet at the bottom of the current worksheet.
1. Select **Tab color**.
1. Select a color from the palette.
1. Click **OK**.
**C#**
//Instantiate a new Workbook
Workbook workbook = new Workbook("../../data/test.xlsx");
//Get the first worksheet in the book
Worksheet worksheet = workbook.Worksheets[0];
//Set the tab color
worksheet.TabColor = Color.Red;
//Save the Excel file
workbook.Save("AsposeColoredTab_Out.xls");
## **Download Running Code**
Download **Set Worksheet Tab Color** form any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)
For more details, visit [Set Worksheet Tab Color](https://docs.aspose.com/cells/net/set-worksheet-tab-color/).
