---
title: Динамическая генерация отформатированных отчетов Excel с элегантным графиком
type: docs
weight: 130
url: /ru/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb, генерация отчета, отчет
description: Эта статья представляет, как сгенерировать отчет в GridWeb.
---

{{% alert color="primary" %}} 

Этот документ предназначен для предоставления необходимой информации о том, как мы можем извлекать данные из некоторого источника данных в замечательное сетчатое подобие управления, вставлять график в него и экспортировать отчет с графиком в MS Excel для анализа, сравнений и печати.

{{% /alert %}} 
## **Обзор**
Существуют определенные веб-сценарии, которые требуют как Отчетности, так и Презентаций, комбинацию частей или объектов, которые могут хорошо взаимодействовать. В статье объясняется, насколько легко создавать и генерировать стильные отчеты Excel динамически в режиме WYSIWYG. Он экспортирует данные из файла XML (вы также можете использовать другие источники данных) в управление Aspose.Cells.GridWeb, которое предоставляет вам реальную среду, позволяющую применять богатый и привлекательный формат данных и рассчитывать результаты формул, как в MS Excel. Он также генерирует сложный график на основе данных исходного рабочего листа с помощью [Aspose.Cells](https://products.aspose.com/cells/) и вставляет изображение графика в Отчет по продажам. Наконец, отчет Excel с прикрепленным графиком сохраняется на диск с использованием компонента Aspose.Cells.

Эта статья включает в себя исходный код и полностью оснащенный демонстрационный проект для такой функциональности.

Он предоставляет пользователям подробное понимание того, как создать бизнес-отчет для ввода данных в рабочий лист сетки и применить некоторое форматирование к ячейкам в строках и столбцах, вставить график на основе исходного диапазона данных перед сохранением отчета Excel на диск.
## **Компоненты Aspose**
Для выполнения задачи я использую три компонента [Aspose](http://www.aspose.com/), издателя компонентов .NET и Java, предоставляющего различные компоненты с богатым набором функций. Aspose предоставляет отличный ряд компонентов .NET и Java. Доверенные тысячами клиентов по всему миру, продукты включают Компоненты формата файла, Продукты отчетности, Визуальные компоненты и Утилитарные компоненты, которые позволяют программно открывать, изменять, генерировать, сохранять, объединять, преобразовывать и т.д. документы в различных форматах, включая DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, разделенные табуляциями, CSV, PPT, SWF, EMF, WMF, MPX, MPD и другие форматы.

Я хотел бы воспользоваться этой возможностью, чтобы представить вам три из этих компонентов, которые были использованы в этом квесте.
## **Управление сетчатыми контролями Aspose.Cells**
Управление сетчатыми контролями Aspose.Cells является полным решением для сетки. Управление сетчатыми контролями Aspose.Cells поставляется вместе с двумя различными графическими интерфейсами .NET (Aspose.Cells.GridDesktop и Aspose.Cells.GridWeb): один для поддержки настольных приложений, другой для поддержки веб-приложений. Обе версии одинаково хороши для удобной реализации в любой платформе. Aspose.Cells.GridWeb предоставляет возможность импорта и экспорта в электронные таблицы Excel. Так что любой, знакомый с Excel (даже конечные пользователи), может создать внешний вид и ощущения сетки. Aspose.Cells.GridWeb также предлагает простой в использовании, богатый набор функций API, который предоставляет разработчикам полный контроль над внешним видом, ощущениями и поведением их сетки. Чтобы узнать больше о продукте, его функциях и для руководства программиста, пожалуйста, проверьте резюме списка функций, Документацию Aspose.Cells.GridWeb и онлайн-представленные [демонстрации](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells** - это компонент отчетности электронных таблиц Excel, который позволяет читать и записывать электронные таблицы Excel без установки Microsoft Excel на стороне клиента или сервера. **Aspose.Cells** - это компонент с богатым набором функций, предлагающий гораздо больше, чем простое экспортирование данных. С помощью **Aspose.Cells** разработчики могут экспортировать данные, форматировать электронные таблицы в самых мельчайших деталях и на каждом уровне, импортировать изображения, импортировать графики, создавать графики, управлять графиками, передавать данные Excel, сохранять в различных форматах, включая XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) интегрирован) и многие другие. **Aspose.Cells** предлагает простой в использовании, богатый набор функций **API** для программистов. У него огромный список функций. Чтобы узнать больше о продукте, его функциях и для руководства программиста, пожалуйста, проверьте резюме **списка функций**, **Документацию Aspose.Cells** и онлайн-представленные демонстрации. Вы можете [скачать](https://downloads.aspose.com/cells) его оценочную версию бесплатно.
## **Создание интерфейса**
Начинаем создание нового веб-приложения Asp.Net в Visual Studio.Net.

Я **Добавляю ссылку** на три компонента, т.е. Aspose.Cells.GridWeb.dll, Aspose.Chart.dll и Aspose.Cells.dll в проект сначала. Я размещаю на странице некоторые элементы управления и задаю их свойства, например, раскрывающийся список, кнопку команды и метку. Затем я добавляю**контрол Aspose.Cells.GridWeb**(**GridWeb**) на него из панели инструментов, поскольку после добавления ссылок на три компонента, контрол**GridWeb**появляется на панели инструментов. Другие два компонента (**Aspose.Chart**и**Aspose.Cells**) - только библиотеки, просто добавляются в проект.

Также я создаю две папки "file" и "images", добавляю в них "Products.xml" и "chart.gif" соответственно. Файл xml - это файл источника данных, из которого будут извлечены данные для заполнения рабочего листа**GridWeb**. Файл изображения предоставит изображение для настраиваемой кнопки, размещенной на управлении**GridWeb**.

Теперь я создаю настраиваемую кнопку команды. Просто щелкаю правой кнопкой мыши на управлении**GridWeb**и нажимаю опцию"Настраиваемые кнопки команд...".

Это активирует редактор настраиваемых кнопок команд, который позволяет создавать настраиваемые изображения кнопок команд с прикрепленной подсказкой. Я указываю значения для некоторых свойств кнопки, например, Команда (Имя) ->"btnChart", ImageUrl -> укажите путь к файлу изображения ("chart.gif") и ToolTip -> дайте подсказку.

Таким образом, настраиваемая кнопка команды добавлена, как вы можете видеть (ограниченная красным цветом) на следующем снимке экрана.

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


Наконец, я задаю некоторые атрибуты шрифта (жирный) для метки и кнопки команды. Я также корректирую размер элементов управления, чтобы получить окончательный вид.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Извлечение данных из файла XML**
Ниже приведена структура файла XML, используемая в проекте.
### **Структура файла XML**
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
## **Заполнение рабочего листа элемента управления Aspose.Cells.GridWeb данными**
Я использую некоторые API элемента управления **GridWeb**, чтобы заполнить рабочий лист данными из исходного файла XML. Я пишу код в обработчике события щелчка кнопки команды (помеченной как "Показать отчет"). Отчет о данных фильтруется на основе выбранного элемента из раскрывающегося списка.



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
## **Форматирование данных в ячейках**
Чтобы различать различные типы информации на рабочем листе, для оптимального отображения данных на вашем рабочем листе и для удобства сканирования рабочего листа, вы форматируете рабочий лист. **Формат** представляет собой стиль и определяется как набор характеристик, таких как шрифты и их размеры, числовые форматы, границы ячеек, заливка ячеек цветом фона или определенным цветовым узором, отступ, выравнивание и ориентация текста в ячейках.

Я добавляю еще несколько строк кода выше. Я размещаю заголовок / подзаголовок отчета, выполняю форматирование заголовка, подзаголовка и детальных ячеек. Я также применяю числовое форматирование к двум полям (устанавливаю числовой формат валюты для полей UnitPrice и Sale) и настраиваю высоту/ширину строк и столбцов с использованием API **Aspose.Cells.GridWeb**.



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
## **Создание отформатированного отчета (.XLS-файла) с графиком с использованием компонента Aspose.Cells**
Теперь, я напишу некоторый код для сохранения отформатированного отчета с графиком на диск. Я использую кнопку **Save** элемента управления **GridWeb**, событие **SaveCommand** элемента управления **GridWeb** вызывается при нажатии на кнопку Сохранить, так что я буду обрабатывать его. Здесь я использую компонент **Aspose.Cells** для экспорта отформатированного отчета в MS Excel, создаю диаграмму и встраиваю её в выходной файл Excel. Я не вставляю изображение диаграммы (созданной компонентом **Aspose.Chart**), а создаю аналогичную диаграмму с использованием API **Aspose.Cells**, чтобы вы могли редактировать диаграмму в MS Excel по своему усмотрению.





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
## **Запуск приложения**
Теперь я запускаю приложение. Список раскрывающегося списка заполняется отдельными категориями.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Я выбираю категорию, по которой хочу показать отчет о продажах, и нажимаю кнопку "Показать отчет".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Теперь, отчет показан в элементе управления **GridWeb** на основе выбранной категории. Отчет отформатирован по умолчанию на основе ранее написанного кода.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Если вы хотите форматировать данные в некоторых ячейках интуитивно понятным образом, вы можете сделать это довольно легко. **Aspose.Cells.GridWeb**предоставляет редактор **Format Cells**, выберите нужные ячейки и щелкните правой кнопкой мыши, затем выберите опцию "Формат ячейки...".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Показан диалоговое окно "Формат ячейки".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Я указываю некоторые атрибуты шрифта и нажимаю OK.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

И получаю результат.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Помимо форматирования ячеек, вы также можете редактировать значения ячеек. Дважды щелкните на выбранной ячейке(ках) и отредактируйте значение.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Чтобы отправить результат редактирования и пересчитать все формулы, я нажимаю на соответствующую кнопку (закруженную красным цветом), чтобы обновить отчет.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Теперь я создам диаграмму и вставлю ее в контроль. Я нажимаю на пользовательскую командную кнопку (закруженную красным цветом), чтобы создать круговую диаграмму на основе диапазона данных.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Наконец, я экспортирую этот отчет с данными и графиком в MS Excel. Я нажимаю кнопку**Сохранить** (закруженную красным цветом). Нажатие на кнопку**Сохранить** отобразит диалоговое окно**Скачать файл**, вы можете либо**Открыть**получившийся отчет (файл Excel с графиком) в MS Excel, либо сохранить его на диск.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Когда я нажимаю кнопку Открыть (диалоговое окно Скачать файл), отчет Excel с графиком экспортируется в MS Excel. Показано верхнее отображение отчета.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Показано нижнее отображение отчета Excel.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
