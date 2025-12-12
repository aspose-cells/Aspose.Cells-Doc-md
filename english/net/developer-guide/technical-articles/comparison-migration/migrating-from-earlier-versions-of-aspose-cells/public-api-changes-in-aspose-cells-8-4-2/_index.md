---  
title: Public API Changes in Aspose.Cells 8.4.2  
type: docs  
weight: 150  
url: /net/public-api-changes-in-aspose-cells-8-4-2/  
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

This document describes the changes to the Aspose.Cells API from version 8.4.1 to 8.4.2 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/net/public-api-changes-in-aspose-cells-8-4-2/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.  

{{% /alert %}}  

## **Added APIs**  

### **Improved Chart Creation Mechanism**  
The Aspose.Cells.Charts.Chart class has exposed the `SetChartDataRange` method to ease the task of chart creation. The `SetChartDataRange` method accepts two parameters, where the first parameter is of type **string** that specifies the cell area from which to plot the data series. The second parameter is of type **Boolean** that specifies the plot orientation, that is, whether to plot the chart data series from a range of cell values by row or by columns.  

The following code snippet shows how to create a column chart with a few lines of code, assuming the chart's plot series data is present on the same worksheet from cell **A1** to **D4**.  

**C#**  

{{< highlight csharp >}}  

 //Add a new chart of type Column to chart collection  

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);  

//Retrieve the newly added chart instance  

Chart chart = worksheet.Charts[idx];  

//Specify the chart's data series from cell A1 to D4  

chart.SetChartDataRange("A1:D4", true);  

{{< /highlight >}}  

### **Added VbaModuleCollection.Add Method**  
Aspose.Cells for .NET 8.4.2 has exposed the `VbaModuleCollection.Add` method to add a new VBA module to the instance of **Workbook**. The `VbaModuleCollection.Add` method accepts a parameter of type [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) to add a worksheet‑specific module.  

The following code snippet shows how to use the `VbaModuleCollection.Add` method.  

**C#**  

{{< highlight csharp >}}  

 //Create new workbook  

Workbook workbook = new Workbook();  

//Access first worksheet  

Worksheet worksheet = workbook.Worksheets[0];  

//Add VBA module for first worksheet  

int idx = workbook.VbaProject.Modules.Add(worksheet);  

//Access the VBA Module, set its name and code  

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];  

module.Name = "TestModule";  

module.Codes = "Sub ShowMessage()" + "\r\n" +  

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +  

"End Sub";  

//Save the workbook  

workbook.Save(output, SaveFormat.Xlsm);  

{{< /highlight >}}  

### **Overloaded Method Cells.CopyColumns Added**  
Aspose.Cells for .NET 8.4.2 has exposed an overloaded version of the `Cells.CopyColumns` method to repeat the source columns onto the destination. The newly exposed method accepts five parameters in total, where the first four parameters are the same as those of the common `Cells.CopyColumns` method. However, the last parameter of type **int** specifies the number of destination columns onto which the source columns have to be repeated.  

The following code snippet shows how to use the newly exposed `Cells.CopyColumns` method.  

**C#**  

{{< highlight csharp >}}  

 //Load an existing workbook  

Workbook workbook = new Workbook(input);  

//Access first worksheet  

Worksheet worksheet = workbook.Worksheets[0];  

//Access cells of first worksheet  

Cells cells = worksheet.Cells;  

//Copy the first two columns (A & B) along with formatting  

//to columns G, H & I.  

//Please note, the columns G & H will be replaced by A & B respectively  

//whereas column I will be replaced by column A  

cells.CopyColumns(cells, 0, 2, 6, 3);  

//Save the workbook  

workbook.Save(output);  

{{< /highlight >}}  

### **Enumeration Fields PasteType.Default & PasteType.DefaultExceptBorders Added**  
With the release of v8.4.2, the Aspose.Cells API has added two new enumeration fields for **PasteType** as detailed below.  

- **PasteType.Default** – Works similar to Excel's “All” functionality for pasting a range of cells.  
- **PasteType.DefaultExceptBorders** – Works similar to Excel's “All except borders” functionality for pasting a range of cells.  

The following sample code demonstrates the use of the **PasteType.Default** field.  

**C#**  

{{< highlight csharp >}}  

 //Load an existing workbook  

Workbook workbook = new Workbook(input);  

//Access first worksheet  

Worksheet worksheet = workbook.Worksheets[0];  

//Access cells of first worksheet  

Cells cells = worksheet.Cells;  

//Create source & destination ranges  

Range source = cells.CreateRange("A1:B6");  

Range destination = cells.CreateRange("D1:E6");  

//Copy the source range onto the destination range with everything except column widths  

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });  

//Save the workbook  

workbook.Save(output);  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Starting from the release of Aspose.Cells for .NET 8.4.2, the enumeration field **PasteType.All** behaves differently compared to Excel's “All” functionality for pasting a range of cells. Now, **PasteType.All** also copies the column widths onto the destination range, as opposed to Excel's “All” functionality. In order to mimic Excel's “All” behavior, please use **PasteType.Default**.  

{{% /alert %}}  

{{< app/cells/assistant language="csharp" >}}
