---
title : "Display or Hide Tabs in Aspose.Cells" 
description : "" 
weight : 16824 
toc : false
type: docs
url: /net/plugins/vsto/missingfeaturesinvsto/display+or+hide+tabs+in+aspose.cells/
---

# Aspose.Cells for .NET : Display or Hide Tabs in Aspose.Cells


If you closely look at the bottom of a Microsoft Excel file, you will see a number of controls. These include:

*   Sheet tabs.
*   Tab scrolling buttons.

Sheet tabs represent the worksheets in the Excel file. Click any tab to switch to that worksheet. The more worksheets in the workbook, the more sheet tabs there are. If the Excel file has a good number of worksheets you need buttons to navigate through them. So, Microsoft Excel provides tab scrolling buttons for scrolling through the sheet tabs.

**Sheet tabs & tab scrolling buttons**  
![](https://docs2.aspose.com/cells/net/attachments/5020764/5115069.png)

Using Aspose.Cells, developers can control the visibility of sheet tabs and tabs scrolling buttons in Excel files.

Below is a complete example that opens an Excel file (book1.xls), hides its tabs and saves the modified file as output.xls.

You can see that Book1.xls file contains tabs in the figure below. After the example code is executed, the tabs are hidden, as you can see from the screenshot of the output.xls file below.

**book1.xls: Excel file before any modification**  
![](https://docs2.aspose.com/cells/net/attachments/5020764/5115072.png)

**output.xls: Excel file after modification**  
![](https://docs2.aspose.com/cells/net/attachments/5020764/5115074.png)

**C#**

{{< code lang="c#" >}}
//Instantiating a Workbook object
//Opening the Excel file
Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file
workbook.Settings.ShowTabs = false;

//Saving the modified Excel file
workbook.Save("output.xls");
 
{{< /code >}}

#### Controlling the Tab Bar Width

**C#**

{{< code lang="c#" >}}
//Adjusting the sheet tab bar width
workbook.Worksheets.SheetTabBarWidth = 800;
 
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsnet.codeplex.com/SourceControl/latest#Plugins/Aspose For VSTO/Aspose.Cells Features missing in VSTO/Display or Hide Tabs/)
*   [CodePlex](https://asposevsto.codeplex.com/SourceControl/latest#Aspose Only features Unavailable in VSTO/Aspose.Cells/Display or Hide Tabs/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
*   [Code.MSDN](https://code.msdn.microsoft.com/Missing-features-in-VSTO-ac9ea836/view/SourceCode#content)

## Download Sample Code

*   [CodePlex](https://asposecellsnet.codeplex.com/releases/view/618484)
*   [CodePlex](https://asposevsto.codeplex.com/releases/view/618289)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/Missing-features-in-VSTO-ac9ea836#content)

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Display or Hide Tabs-001.png](https://docs2.aspose.com/cells/net/attachments/5020764/5115069.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Display or Hide Tabs-002.png](https://docs2.aspose.com/cells/net/attachments/5020764/5115072.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Display or Hide Tabs-003.png](https://docs2.aspose.com/cells/net/attachments/5020764/5115074.png) (image/png)  

