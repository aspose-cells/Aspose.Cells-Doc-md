---
title: 使用优雅图表动态生成格式化的Excel报表
type: docs
weight: 130
url: /zh/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb, 生成报表, 报表
description: 本文介绍了如何在GridWeb中生成报表。
---

{{% alert color="primary" %}} 

本文旨在提供必要的信息，以便从某个数据源提取数据到类似电子表格的控件中，将图表粘贴到其中，并导出附有图表的报表到MS Excel，以进行分析、比较和打印。有些网页场景需要同时进行报表和演示，需要可以很好地共同工作的部件或对象的组合。该文章解释了设计和动态生成时尚excel报表的简易程度。它将数据从一个XML文件导出（也可以利用其他数据源），到Aspose.Cells.GridWeb控件，该控件为您提供了真实的环境，允许您对数据应用丰富和吸引人的格式，以及像MS Excel一样计算公式结果。它还使用[Aspose.Cells](https://products.aspose.com/cells/)组件根据工作表源数据生成复杂的图表，并将图表图像粘贴到销售报表中。最后，使用Aspose.Cells组件，将包含图表的Excel报表保存到磁盘。

{{% /alert %}} 
## **概述**
本文包括了这种功能的源码和全功能演示项目。

它使用户全面了解如何创建业务报告，将数据输入到网格的工作表中并对行和列中的单元格应用一些格式化，在保存Excel报表到磁盘之前根据数据源范围嵌入图表。

我使用[Aspose](http://www.aspose.com/)的三个组件来轻松完成任务。[Aspose](http://www.aspose.com/)是.NET和Java组件发布商，提供各种功能丰富的组件。[Aspose](http://www.aspose.com/)提供了一系列优秀的.NET和Java组件。作为一款备受全球数千客户信赖的产品，其产品包括文件格式组件、报告产品、可视化组件和实用程序组件，允许以编程方式在各种格式的文档中进行打开、修改、生成、保存、合并、转换等操作，包括DOC、RTF、WordML、HTML、PDF、XLS、SpreadsheetML、Tab Delimited、CSV、PPT、SWF、EMF、WMF、MPX、MPD和其他各种格式。
## **Aspose组件**
我使用了三个[Aspose](http://www.aspose.com/)组件来轻松完成任务。[Aspose](http://www.aspose.com/)是.NET和Java组件发布商，提供各种功能丰富的组件。[Aspose](http://www.aspose.com/)提供了一系列出色的.NET和Java组件，受到全球成千上万的客户的信任，其产品包括文件格式组件、报告产品、可视化组件和实用程序组件，可以以编程方式打开、修改、生成、保存、合并、转换等各种格式的文档，包括DOC、RTF、WordML、HTML、PDF、XLS、SpreadsheetML、Tab Delimited、CSV、PPT、SWF、EMF、WMF、MPX、MPD和其他格式。

我想借此机会向您介绍其中三个组件，这些组件已经在这个任务中被使用。
## **Aspose.Cells网格控件**
Aspose.Cells网格控件是一个完整的网格解决方案。Aspose.Cells网格控件包含两个不同的GUI .NET组件（Aspose.Cells.GridDesktop和Aspose.Cells.GridWeb）：一个用于支持桌面应用程序，另一个用于支持Web应用程序。两个版本均能够轻松实现在任何一个平台上的应用。Aspose.Cells.GridWeb提供了从Excel电子表格中导入和导出的功能。因此，任何熟悉Excel的人（甚至是最终用户）都可以设计网格的外观和功能。Aspose.Cells.GridWeb还提供了一个易于使用、功能丰富的API，为开发人员提供了对其网格外观、功能和行为的完全控制。如需了解更多关于产品、其功能和程序员指南的信息，请查看功能摘要、Aspose.Cells.GridWeb文档和在线特色[演示](https://aspose.github.io/)。
## **Aspose.Cells**
**Aspose.Cells**是一种Excel电子表格报告组件，可以让您在客户端或服务器端不需安装Microsoft Excel的情况下读取和写入Excel电子表格。**Aspose.Cells**是一个功能丰富的组件，不仅提供基本的数据导出。使用**Aspose.Cells**，开发人员可以导出数据、以任何细节和级别对电子表格进行格式设置、导入图像、导入图表、创建图表、操纵图表、流式传输Excel数据、保存为各种格式（包括XLS、CSV、SpreadsheetML、TabDelimited、TXT、XML（与[Aspose.Pdf](https://products.aspose.com/pdf/)集成）等等。**Aspose.Cells**为程序员提供了一个易于使用、功能丰富的**API**。它拥有大量功能。如需了解更多关于产品、其功能和程序员指南的信息，请查看功能摘要、**Aspose.Cells文档**和在线特色演示。您可以免费[下载](https://downloads.aspose.com/cells)其评估版本。
## **设计界面**
我们在Visual Studio.Net中开始创建一个新的Asp.Net web应用程序。

我首先为项目**添加引用**，即Aspose.Cells.GridWeb.dll、Aspose.Chart.dll和Aspose.Cells.dll。我在页面上放置一些控件并设置它们的属性，如下拉列表、命令按钮和标签。然后，我从工具箱中将**Aspose.Cells.GridWeb控件**（**GridWeb**）放置到页面中，因为在添加三个组件的引用后，**GridWeb**控件将出现在工具箱中。另外两个组件（**Aspose.Chart**和**Aspose.Cells**）只是库，只需将其引用到项目中。

我还创建了两个文件夹"文件"和"图片"，分别添加了"Products.xml"和"chart.gif"。XML文件是一个数据源文件，从中可以提取数据以填充**GridWeb**工作表。图像文件将为**GridWeb控件**上放置的自定义按钮提供图像。

我现在创建了一个自定义命令按钮。我简单地右键单击**GridWeb**控件，然后选择"自定义命令按钮..."选项。

这将激活自定义命令按钮编辑器，编辑器允许您创建带有工具提示的自定义命令图像按钮。我为按钮的一些属性指定了值，例如命令（名称）->"btnChart"、ImageUrl->给出图像文件的路径（"chart.gif"）和ToolTip->给出工具提示。

因此，如下截图所示，自定义命令按钮已添加（用红色圈出）。

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


最后，我为标签和命令按钮设置了一些字体属性（加粗）。我还调整了控件的大小，获得了最终的外观。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **从XML文件检索数据**
以下是项目中使用的XML文件结构。
### **XML文件结构**
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
## **填充Aspose.Cells.GridWeb控件的工作表数据**
我使用了**GridWeb**控件的一些API来从源XML文件中填充工作表数据。我在命令按钮（标记为“显示报告”）的点击事件处理程序中编写代码。数据报告是根据下拉列表中的选择项目进行筛选的。



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
为了区分工作表上不同类型的信息，在工作表中最佳显示数据并使工作表更易扫描，您需要对工作表进行格式化。**格式**表示一种样式，并定义为一组特征，如字体和字体大小、数字格式、单元格边框、纯背景色或特定颜色模式的单元格着色、缩进、单元格内的对齐和文本方向。

我将一些代码行与上述代码合并。我放置了报告的标题/子标题，对标题、子标题和详细单元格进行了一些格式化。我还对两个字段应用了数字格式化（将货币数字格式设置为UnitPrice和Sale字段），并使用**Aspose.Cells.GridWeb**API调整的行和列的高度/宽度。



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
## **使用Aspose.Cells组件生成带有图表的格式化报告（.XLS文件）**
现在，我将编写一些代码将带有图表的格式化报告保存到磁盘。我利用**GridWeb**的**Save**按钮，当单击保存按钮时，**GridWeb**的**SaveCommand**事件被触发，因此，我将处理它。在这里，我使用**Aspose.Cells**组件将格式化报告导出到MS Excel，并生成图表并将其嵌入到输出的Excel文件中。我没有插入由**Aspose.Chart**组件创建的图表图像，而是使用**Aspose.Cells**的API创建类似的图表，以便您可以根据自己的需求在MS Excel中编辑图表。





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

我通过选择一个分类来显示销售报告，并单击“显示报告”按钮。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

因此，根据所选的类别，报告被显示在**GridWeb**中。报告根据先前编写的代码默认格式化。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

如果您想以所见即所得的方式格式化一些单元格中的数据，您可以轻松地进行。**Aspose.Cells.GridWeb**提供**格式单元格**编辑器，选择您需要的单元格，右键单击它，单击“格式单元格...”选项。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

显示格式单元格对话框。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

指定一些字体属性，然后单击“确定”。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

然后得到结果。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

除了单元格格式化外，您还可以编辑单元格值。双击您所需的单元格并编辑值。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

为提交编辑结果和重新计算所有公式，我单击相关按钮（用红色圈起）以更新报告。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

现在，我将创建图表并将其粘贴到控件中。我单击自定义命令按钮（用红色圈起）以根据数据范围创建饼图。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

最后，我将通过图形将此数据报告导出到 MS Excel。我点击**保存**按钮（用红色圈出）。点击**保存**按钮将显示**文件下载**对话框，您可以选择要么**打开**生成的报告（带图形的输出 Excel 文件）到 MS Excel，要么保存到磁盘。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

当我点击**打开**按钮（文件下载对话框）时，带图形的 Excel 报告将被导出到 MS Excel。报告的上部分显示。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

显示 Excel 报告的下部分。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
