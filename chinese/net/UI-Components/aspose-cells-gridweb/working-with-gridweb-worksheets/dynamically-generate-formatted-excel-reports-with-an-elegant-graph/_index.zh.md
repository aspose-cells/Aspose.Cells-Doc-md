---
title: 使用优雅的图表动态生成格式化的Excel报告
type: docs
weight: 130
url: /zh/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb,生成报告,报告
description: 本文介绍了如何在GridWeb中生成报告。
---

{{% alert color="primary" %}} 

本文旨在提供有关如何从某个数据源提取数据以填充类似电子表格的精彩网格控件，粘贴图表并将带有图形的报告导出到MS Excel以进行分析、比较和打印的必要信息。

{{% /alert %}} 
## **概览**
某些Web场景要求同时进行报表和演示，这就需要部分或对象的组合。本文解释了在所见即所得的方式中设计和动态生成时尚的Excel报告有多容易。它将数据从XML文件（您也可以使用其他数据源）导出到Aspose.Cells.GridWeb控件，该控件为您提供了真实环境，允许您为数据应用丰富并引人注目的格式，并计算像MS Excel一样的公式结果。它还基于工作表源数据使用[Aspose.Cells](https://products.aspose.com/cells/)组件生成复杂的图表，并将图表图像粘贴到销售报告中。最后，使用Aspose.Cells组件将附有图形的Excel报告保存到磁盘。

本文包括此功能的源代码和功能齐全的演示项目。

它使用户对如何创建业务报告将数据输入到网格工作表中并在保存Excel报告到磁盘之前对行和列中的单元格应用一些格式以及根据数据源范围嵌入图表有了详细的了解。
## **Aspose组件**
我使用了[Aspose](http://www.aspose.com/)的三个组件执行此任务。 [Aspose](http://www.aspose.com/)是.NET和Java组件发行商，提供多种功能丰富的组件。 [Aspose](http://www.aspose.com/)提供了一系列优秀的.NET和Java组件。受全球数千客户信赖，产品包括文件格式组件、报表产品、可视化组件和实用程序组件，可用于以编程方式打开、修改、生成、保存、合并、转换等各种格式的文档，包括DOC、RTF、WordML、HTML、PDF、XLS、SpreadsheetML、制表符分隔的、CSV、PPT、SWF、EMF、WMF、MPX、MPD和其他格式。

我要借此机会向您介绍这三个组件，它们在这个任务中已被使用。
## **Aspose.Cells网格控件**
Aspose.Cells网格控件是全面的网格解决方案。Aspose.Cells网格控件打包了两种不同的GUI .NET组件（Aspose.Cells.GridDesktop和Aspose.Cells.GridWeb）：一个用于支持桌面应用程序，另一个用于支持Web应用程序。两个版本同样出色，以使在任一平台上的实施变得轻而易举。Aspose.Cells.GridWeb提供从Excel电子表格导入和导出的功能。因此，任何熟悉Excel的人（甚至是最终用户）都可以设计网格的外观和感觉。Aspose.Cells.GridWeb还提供了易于使用、功能丰富的API，为开发人员提供了对其网格的外观、感觉和行为的完全控制。要了解有关产品、其功能以及程序员指南的更多信息，请查看特性列表摘要、Aspose.Cells.GridWeb文档和在线特色[演示](https://aspose.github.io/)。
## **Aspose.Cells**
**Aspose.Cells**是一款Excel电子表格报告组件，使您可以在客户端或服务器端不需要安装Microsoft Excel的情况下读取和写入Excel电子表格。**Aspose.Cells**是一个功能丰富的组件，提供的功能远不止基本的数据导出。使用**Aspose.Cells**，开发人员可以导出数据、以各种细节和层次格式化电子表格、导入图片、导入图表、创建图表、操作图表、流式传输Excel数据、以各种格式保存，包括XLS、CSV、SpreadsheetML、TabDelimited、TXT、XML（集成了[Aspose.Pdf](https://products.aspose.com/pdf/)）等等。**Aspose.Cells**为程序员提供了易于使用的、功能丰富的**API**。它具有大量的功能。要了解产品、其功能并获得程序员指南，请查看**功能列表**摘要、**Aspose.Cells**文档和在线功能齐备的演示。您可以免费[下载](https://downloads.aspose.com/cells)其评估版。
## **设计界面**
我们开始在Visual Studio.Net中创建一个新的Asp.Net Web应用。

首先，我向项目添加了对Aspose.Cells.GridWeb.dll、Aspose.Chart.dll和Aspose.Cells.dll三个组件的引用。我在页面上放置一些控件并设置它们的属性，即一个下拉列表、一个命令按钮和一个标签。然后，我从工具箱中将**Aspose.Cells.GridWeb控件**(**GridWeb**)放置到其中，因为在添加对这三个组件的引用后，**GridWeb**控件出现在工具箱中。另外两个组件（**Aspose.Chart** 和 **Aspose.Cells**）只是库，只需添加到项目的引用中。

我还创建了两个文件夹"file"和"images"，并分别将"Products.xml"和"chart.gif"添加到这些文件夹中。XML文件是一个数据源文件，将从中提取数据以填充**GridWeb**工作表单。图像文件将为放置在**GridWeb**控件上的自定义按钮提供图像。

现在，我创建了一个自定义命令按钮。我只需右键单击**GridWeb**控件，然后点击"自定义命令按钮..."选项。

它将激活自定义命令按钮编辑器，该编辑器允许您创建带有工具提示的自定义命令图像按钮。我指定按钮的某些属性的值，例如 Command（Name）->"btnChart"，ImageUrl -> 给出图片文件的路径（"chart.gif"）和 ToolTip -> 给出工具提示。

因此，自定义命令按钮被添加，您可以在下面的截图中看到它（用红色圈起来）。

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


最后，我设置了标签和命令按钮的一些字体属性（加粗）。我还调整了控件的大小以获得最终外观。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **从 XML 文件中检索数据**
以下是项目中使用的 XML 文件结构。
### **XML 文件结构**
**XML**

{{< highlight csharp >}}

 <?xml version="1.0" standalone="yes"?>

<SalesData>

  <Products>

    <ProductName>Data</ProductName>

    <QuantityPerUnit>Data</QuantityPerUnit>

    <CategoryName>Data</CategoryName>

    <UnitPrice>Data</UnitPrice>

    <Sale>Data</Sale>

  </Products>

 .........

</SalesData>



{{< /highlight >}}

{{< highlight java >}}

 private void Page_Load(object sender, System.EventArgs e)

{

if (!IsPostBack)

{

	// Uncomment the code below when you have purchased license

	// for Aspose.Cells.GridWeb, Aspose.Chart and Aspose.Cells. You need

	// to deploy the licenses in the same folder as your executable,

      // alternatively you can add the license files as an embedded

      // resource to your project.

	//

	// Set the license for Aspose.Cells.GridWeb

	// Aspose.Cells.GridWeb.License gridwebLicense = new

	// Aspose.Cells.GridWeb.License();

	// gridwebLicense.SetLicense("Aspose.Grid.lic");

	//

	// // Set the license for Aspose.Chart

	// Aspose.Chart.License chartLicense = new

	// Aspose.Chart.License();

	// chartLicense.SetLicense("Aspose.Chart.lic");

	//

	// // Set the license for Aspose.Cells

	// Aspose.Cells.License cellsLicense = new

	// Aspose.Cells.License();

	// cellsLicense.SetLicense("Aspose.Cells.lic");

	//Create a DataSet object.

	DataSet ds = new DataSet();

	//Get the Virtual Folder Path.

	string path = MapPath(".");

	//Reads XML data from xml file into DataSet object.

	ds.ReadXml(path + "\\file\\Products.xml");

	//Call the custom method to obtain distinct values from

	//CategoryName field and store data into an object array.

	object [] drs = GetDistinctValues(ds.Tables[0],"CategoryName");

	//Fill the drop down list with distinct field items.

	for(int i = 0;i<drs.Length;i++)

	{

		DropDownList1.Items.Add(drs[i].ToString());

	}

}

}

//This method is used to filter distinct values from CategoryName field in the datatable.

private object[] GetDistinctValues(DataTable dtable, string colName)

{

	// Create a Hashtable object.

	Hashtable hTable = new Hashtable();

	// Loop through the datatable rows and add distinct values to

	// Hashtable object minimizing the duplicates in the field.

	foreach (DataRow drow in dtable.Rows)

	if(!hTable.ContainsKey(drow[colName]))

	hTable.Add(drow[colName], string.Empty);

	// Create an object array based on the distinct key values of the Hashtable object.

	object[] objArray = new object[hTable.Keys.Count];

	// Copy the disctinct values to fill the array.

	hTable.Keys.CopyTo(objArray, 0);

	// Return the array object.

	return objArray;

}

{{< /highlight >}}
## **在 Aspose.Cells.GridWeb 控件的工作表中填充数据**
我使用**GridWeb**控件的一些 API 从源 XML 文件中填充工作表的数据。我在命令按钮（标记为"Show Report"）的单击事件处理程序中编写代码。数据报告是基于下拉列表中选定项目进行筛选的。



{{< highlight java >}}

 //Clears datasheets of the GridWeb control.

GridWeb1.WebWorksheets.Clear();

//Create a DataSet object.

DataSet ds = new DataSet();

//Get the Virtual Folder path.

string path = MapPath(".");

//Reads XML data from xml file into DataSet object.

ds.ReadXml(path + "\\file\\Products.xml");

//Create a DataView based on the datatable.

DataView dv = new DataView(ds.Tables[0]);

//Filter data in the DataView object based on the selected drop down list item.

dv.RowFilter = "CategoryName ='" + DropDownList1.SelectedItem.Text + "'";

//Importing data from the filtered DataView object to create and

//fill "Products" Worksheet start from A4 cell.

GridWeb1.WebWorksheets.ImportDataView(dv, null, null,"Products",3,0);

{{< /highlight >}}
## **在单元格中格式化数据**
为了区分工作表上不同类型的信息，以便在工作表上以最佳方式显示数据，并且使工作表更易于扫描，您需要对工作表进行格式化。**Format**表示一个样式，并被定义为一组特性，如字体和字体大小、数字格式、单元格边框、用纯色或特定颜色模式填充单元格、缩进、对齐和单元格中的文本方向。

我将一些更多的代码行合并到上面。我为报告的标题/副标题做了布局，对标题、副标题和详细单元格进行了一些格式化。我还对两个字段应用了数字格式化（为UnitPrice和Sale字段设置货币数字格式），并使用**Aspose.Cells.GridWeb**API调整了行和列的高度/宽度。



{{< highlight java >}}

 //Create the title cell (A1) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size, specify horizontal and vertical align settings, set

//foreground and background colors and merge cells (A1:E2).

WebWorksheet sheet = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Product Sales By Category");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

sheet.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

sheet.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A1"].Style.BackColor = Color.SkyBlue;

sheet.Cells["A1"].Style.ForeColor = Color.Blue;

sheet.Cells.Merge(0, 0, 2, 5);

//Create the subtitle cell (A3) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size with attributes, specify horizontal and vertical align

//settings, set foreground and background colors and merge cells

//(A3:E3).

sheet.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

sheet.Cells["A3"].Style.Font.Bold = true;

sheet.Cells["A3"].Style.Font.Italic = true;

sheet.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

sheet.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A3"].Style.BackColor = Color.SeaGreen;

sheet.Cells["A3"].Style.ForeColor = Color.Yellow;

sheet.Cells.Merge(2, 0, 1, 5);

//Obtain the last row and column (which contain data) indexes.

int totalrow = sheet.Cells.MaxRow +1;

int totalcol = sheet.Cells.MaxColumn;

//Get the sheet Cells collections

WebCells cells = sheet.Cells;

//Define the Cell object.

WebCell cell;

//Loop through the data in the sheet and format two fields with

//Currency number style.

for (int i = 4;i<=totalrow;i++)

{

	//Format the Sale Column.

	cell = cells[i,totalcol];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

	//Format the UnitPrice Column.

	cell = cells[i,totalcol-1];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

}

//Insert the Total row with data, formula and formatting style.

//It will calculate the total Sales of a Category.

cells[totalrow,0].PutValue( DropDownList1.SelectedItem.Text + " Total" );

cells[totalrow,0].Style.Font.Bold = true;

cells[totalrow,totalcol].Formula = "=SUM(E5:E" + totalrow.ToString() + ")";

cells[totalrow,totalcol].Style.Font.Bold = true;

//Specify some Row and Column formattings. It will set row height

//and column width accordingly.

cells.SetRowHeight(2, new Unit("17pt"));

cells.SetColumnWidth(0, new Unit("157pt"));

cells.SetColumnWidth(1, new Unit("106pt"));

cells.SetColumnWidth(2, new Unit("87pt"));

cells.SetColumnWidth(3, new Unit("56pt"));

cells.SetColumnWidth(4, new Unit("50pt"));



{{< /highlight >}}
## **使用 Aspose.Cells 组件生成带图形的格式化报告（.XLS 文件）**
现在，我将编写一些代码来将带有图形的格式化报告保存到磁盘。我利用**GridWeb**的**Save**按钮，当单击保存按钮时，**GridWeb**的**SaveCommand**事件被触发，因此，我将处理它。在这里，我使用**Aspose.Cells**组件将格式化报告导出到 MS Excel，并生成图表并嵌入到输出的 Excel 文件中。我没有插入由**Aspose.Chart**组件创建的图表图像，而是使用**Aspose.Cells**的 API 创建类似的图表，这样您就可以根据需要在 MS Excel 中编辑图表。





{{< highlight java >}}

 //This GridWeb control event is fired when you click on the "Save" button

//of the control. After Clicking this button "File Download" dialog is

//displayed and you may open into MS Excel / save the output excel file //with graph to disk.

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

	//Create MemoryStream object.

	System.IO.MemoryStream ms = new System.IO.MemoryStream();

	//Save the GridWeb's Report to the stream.

	this.GridWeb1.WebWorksheets.SaveToExcelFile(ms);

	//Create a new Workbook.

	Workbook workbook = new Workbook();

	//Open the stream into the Workbook.

	workbook.Open(ms);

	//Call the custom method which creates Chart.

	Workbook book = CellsChart(workbook);

	//Save the excel file displaying "File Download" dialog box.

	book.Save(ms, FileFormatType.Default);

	this.Response.ContentType = "application/vnd.ms-excel";

	this.Response.AddHeader("content-disposition", "attachment; filename=Export.xls");

	this.Response.BinaryWrite(ms.ToArray());

}

//This custom method is used to create the Chart based on the data source

//range in the GridWeb control. In this method we will use Aspose.Cells

//APIs to create the graph which will be saved later into the output //excel file.

private Workbook CellsChart(Workbook workbook)

{

	//Get the first Worksheet.

	Aspose.Cells.Worksheet sheet = workbook.Worksheets[0];

	//Get the Cells collection in the sheet.

	Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

	//Get the last row index.

	int maxrow = sheet.Cells.MaxDataRow;

	//Unmerge the cells.

	sheet.Cells.UnMerge(maxrow,0,15,10);

	int chartIndex = 0;

	//Add a new Chart into the sheet's Chart Collection.

chartIndex = sheet.Charts.Add(Aspose.Cells.ChartType.Pie,maxrow,0,maxrow+28,5);

	//Get the Chart object.

	Aspose.Cells.Chart chart = sheet.Charts[chartIndex];

	//Set the Chart Area.

	Aspose.Cells.ChartArea chartarea = chart.ChartArea;

	chartarea.Area.Formatting = FormattingType.Custom;

	chartarea.Border.IsVisible = false;

		chartarea.Area.FillFormat.SetTwoColorGradient(Color.PowderBlue, Color.LightSkyBlue, GradientStyleType.FromCenter,1);

	//Set some properties of Chart Plot Area.

	chart.PlotArea.Area.Formatting = FormattingType.None;

	chart.PlotArea.Border.IsVisible = false;

	//Set properties of Chart Title.

	chart.Title.Text = DropDownList1.SelectedItem.Text + " Sales";

	chart.Title.TextFont.Size = 20;

	//Set properties of NSeries

	int lastdatarow = maxrow-1;

	chart.NSeries.Add("E5:E" + lastdatarow.ToString(), true);

	chart.NSeries.CategoryData = "A5:A" + lastdatarow.ToString();

	//Set the Data Labels in the chart

	Aspose.Cells.DataLabels datalabels;

	for ( int i = 0; i < chart.NSeries.Count ;i ++ )

	{

		datalabels = chart.NSeries[i].DataLabels;

		datalabels.Postion = Aspose.Cells.LabelPositionType.Center;

		datalabels.IsPercentageShown = true;

	}

	//Set the Legend settings.

	Aspose.Cells.Legend legend = chart.Legend;

	legend.Position = Aspose.Cells.LegendPositionType.Bottom;

	legend.Height = 85;

	legend.Width = 330;

	legend.AutoScaleFont = true;

	legend.Border.Color = Color.Blue;

	legend.Area.Formatting = FormattingType.Custom;

	FillFormat fillformat = legend.Area.FillFormat;

	legend.Area.Formatting = FormattingType.None;

	legend.Border.IsVisible = false;

	//Autofit the first column.

	sheet.AutoFitColumn(0);

	//Return the Workbook.

	return workbook;

}



{{< /highlight >}}
## **运行应用程序**
现在，我运行应用程序。下拉列表被填充了不同的类别。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

我选择一个要显示销售报告的类别，然后单击"Show Report"按钮。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

因此，报告根据所选类别显示在**GridWeb**中。报告默认根据先前编写的代码进行了格式化。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

如果您想以所见即所得的方式对一些单元格进行格式化，您可以很容易地完成。**Aspose.Cells.GridWeb**提供**格式化单元格**编辑器，选择您所需的单元格，并右键单击，然后单击"格式化单元格..."选项。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

显示格式化单元格对话框。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

我指定了一些字体属性，然后单击确定。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

然后得到结果。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

除了单元格格式化，您还可以编辑单元格的值。双击您所需的单元格，然后编辑值。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

要提交编辑结果并重新计算所有公式，我单击相关按钮（用红色圈起来）来更新报告。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

现在，我将创建图表并将其粘贴到控件中。我单击自定义命令按钮（红色圈起来）以基于数据范围创建饼图。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

最后，我将此数据报告与图形导出到 MS Excel。我单击**Save**按钮（红色圈起来）。单击**Save**按钮将显示**文件下载**对话框，您可以要么**打开**结果报告（带图形的输出 excel 文件），要么将其保存到磁盘。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

当我单击“打开”按钮（文件下载对话框）时，带图形的 Excel 报告被导出到了 MS Excel。报告的上部分被显示。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

报告的下部分被显示。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
