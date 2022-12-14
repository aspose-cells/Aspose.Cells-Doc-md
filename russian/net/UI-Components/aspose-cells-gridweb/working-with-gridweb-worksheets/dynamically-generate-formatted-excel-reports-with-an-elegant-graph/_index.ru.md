---
title: Динамическое создание отформатированных отчетов Excel с элегантным графиком
type: docs
weight: 130
url: /ru/net/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
---
{{% alert color="primary" %}} 

Этот документ предназначен для предоставления необходимой информации о том, как мы можем извлечь данные из какого-либо источника данных в великолепную сетку, такую как контроль, вставить в нее диаграмму и экспортировать отчет с диаграммой в MS Excel для проведения анализа, сравнения и печати.

{{% /alert %}} 
## **Обзор**
Существуют определенные веб-сценарии, которые требуют как отчетов, так и презентаций, комбинации частей или объектов, которые могут хорошо работать вместе. В статье объясняется, как легко динамически разрабатывать и создавать стильные отчеты Excel в формате WYSIWYG. Он экспортирует данные из файла XML (вы также можете использовать другие источники данных) в элемент управления Aspose.Cells.GridWeb, который предоставляет вам реальную среду, позволяющую применять богатый и привлекательный формат к данным и вычислять результаты формул, такие как MS Excel. Он также создает сложную диаграмму на основе исходных данных рабочего листа, используя[Aspose.Cells](https://products.aspose.com/cells/) компонента и вставляет изображение диаграммы в отчет о продажах. Наконец, отчет Excel с прикрепленным графиком сохраняется на диск с помощью компонента Aspose.Cells.

Эта статья включает исходный код и полнофункциональный демонстрационный проект для такой функциональности.

Это позволяет пользователям с подробным пониманием того, как создать бизнес-отчет, вводить данные в рабочий лист сетки и применять некоторое форматирование к ячейкам в строках и столбцах, вставлять график на основе исходного диапазона данных перед сохранением отчет excel на диск.
## **Компоненты Aspose**
 Я использую три из[Aspose](http://www.aspose.com/) компоненты для выполнения задачи с легкостью.[Aspose](http://www.aspose.com/) , Издатель компонентов .NET и Java предоставляет множество многофункциональных компонентов.[Aspose](http://www.aspose.com/) предоставляет большую линейку компонентов .NET и Java. Продукты, которым доверяют тысячи клиентов по всему миру, включают компоненты форматов файлов, продукты для создания отчетов, визуальные компоненты и служебные компоненты, которые позволяют программно открывать, изменять, генерировать, сохранять, объединять, преобразовывать и т. д. документы в различных форматах, включая DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, Tab Delimited, CSV, PPT, SWF, EMF, WMF, MPX, MPD и другие форматы.

Я хотел бы воспользоваться этой возможностью, чтобы представить вам три из этих компонентов, которые использовались в этом квесте.
## **Aspose.Cells Элементы управления сетью**
 Aspose.Cells Grid Controls — комплексное решение для сетки. Aspose.Cells Элементы управления Grid поставляются в комплекте с двумя различными компонентами GUI .NET (Aspose.Cells.GridDesktop и Aspose.Cells.GridWeb): один для поддержки настольных приложений, а другой — для поддержки веб-приложений. Обе версии в равной степени согласованы, чтобы упростить внедрение на любой платформе. Aspose.Cells.GridWeb предоставляет возможность импорта и экспорта в электронные таблицы Excel. Таким образом, любой, кто знаком с Excel (даже конечные пользователи), может спроектировать внешний вид сетки. Aspose.Cells.GridWeb также предлагает простой в использовании, многофункциональный API, который предоставляет разработчикам полный контроль над внешним видом, поведением и поведением их сетки. Чтобы узнать больше о продукте, его функциях и получить руководство для программистов, ознакомьтесь с кратким описанием списка функций, Aspose.Cells. Документация по GridWeb и онлайн-реклама[Демо](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells**— это компонент отчетности по электронным таблицам Excel, который позволяет вам читать и писать электронные таблицы Excel без использования Microsoft Excel, устанавливаемого на клиентской или серверной стороне.**Aspose.Cells** — это многофункциональный компонент, который предлагает гораздо больше, чем просто экспорт данных. С**Aspose.Cells** разработчики могут экспортировать данные, форматировать электронные таблицы во всех деталях и на каждом уровне, импортировать изображения, импортировать диаграммы, создавать диаграммы, манипулировать диаграммами, передавать данные Excel в потоковом режиме, сохранять в различных форматах, включая XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) комплексные) и многое другое.**Aspose.Cells** предлагает простой в использовании, многофункциональный**API** для программистов. Он имеет огромный список функций. Чтобы узнать больше о продукте, его функциях и получить руководство программиста, ознакомьтесь с кратким описанием**Список функций**, **Aspose.Cells Документация** и онлайн-демонстрации. Вы можете[скачать](https://downloads.aspose.com/cells) его оценочная версия бесплатно.
## **Проектирование интерфейса**
Мы начинаем создавать новое веб-приложение Asp.Net в Visual Studio.Net.

 я**Добавить ссылку**к трем компонентам ieAspose.Cells.GridWeb.dll, Aspose.Chart.dll и Aspose.Cells.dll к проекту в первую очередь. Я помещаю некоторые элементы управления на страницу и устанавливаю их свойства, т.е. выпадающий список, командную кнопку и метку. затем я размещаю**Aspose.Cells.GridWeb****контроль**(**GridWeb**) к нему из панели инструментов, так как после добавления ссылок на три компонента**GridWeb**элемент управления появился на панели инструментов. Два других компонента (**Aspose.Chart**а также**Aspose.Cells**) — это просто библиотеки, которые ссылаются только на проект.

Также создаю две папки "file" и "images", добавляю в эти папки соответственно "Products.xml" и "chart.gif". Файл xml представляет собой файл источника данных, из которого будут извлекаться данные для заполнения**GridWeb**рабочий лист. Файл изображения предоставит изображение для пользовательской кнопки, размещенной на**GridWeb**контроль.

Теперь я создаю пользовательскую командную кнопку. Я просто щелкаю правой кнопкой мыши по**GridWeb**управления и нажмите «Пользовательские кнопки управления…».

Это активирует редактор пользовательских командных кнопок, редактор позволяет создавать пользовательские кнопки изображения команд с прикрепленной подсказкой. Я указываю значения для некоторых свойств кнопки, например, Command (Name) -> "btnChart", ImageUrl -> указать путь к файлу изображения ("chart.gif") и ToolTip -> дать всплывающую подсказку.

Итак, пользовательская командная кнопка добавлена, как вы можете видеть (обведена красным цветом) на следующем снимке экрана.

|![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
|:- |


Наконец, я установил некоторые атрибуты шрифта (выделены полужирным шрифтом) для метки и командной кнопки. Я также регулирую размер элементов управления, чтобы получить окончательный вид.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Получение данных из XML-файла**
Ниже приведена файловая структура XML, используемая в проекте.
### **Структура XML-файла**
**XML**

{{< highlight "csharp" >}}

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

{{< highlight "java" >}}

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

private object[]GetDistinctValues(DataTable dtable, string colName)

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
Я использую некоторые API из**GridWeb**для заполнения рабочего листа данными из исходного XML-файла. Я пишу код в обработчике кликов командной кнопки (с надписью «Показать отчет»). Отчет данных фильтруется на основе выбранного элемента из раскрывающегося списка.



{{< highlight "java" >}}

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
## **Форматирование данных в Cells**
Чтобы различать различные типы информации на рабочем листе, для оптимального отображения данных на вашем рабочем листе и для облегчения сканирования рабочего листа, вы форматируете рабочий лист. А**Формат**представляет собой стиль и определяется как набор характеристик, таких как шрифты и размеры шрифта, числовые форматы, границы ячеек, затенение ячеек сплошным цветом фона или определенным цветовым шаблоном, отступы, выравнивание и ориентация текста в ячейках.

Я объединяю еще несколько строк кода выше. Я размещаю заголовок/подзаголовок отчета, форматирую заголовок, подзаголовок и ячейки с подробностями. Я также применяю форматирование чисел к двум полям (устанавливаю числовой формат валюты в поля UnitPrice и Sale) и настраиваю высоту/ширину строк и столбцов, используя**Aspose.Cells.GridWeb**API.



{{< highlight "java" >}}

 //Создаем ячейку заголовка (A1) на листе и применяем форматирование.

//Следующие строки вводят в ячейку строковое значение, указываем

//размер шрифта, указать параметры горизонтального и вертикального выравнивания, установить

//цвета переднего плана и фона и объединение ячеек (A1:E2).

Лист WebWorksheet = GridWeb1.WebWorksheets[0];

лист.Cells["A1"].PutValue("Продажи товаров по категориям");

лист.Cells["A1"].Style.Font.Size = новый FontUnit("20pt");

лист.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

лист.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

лист.Cells["A1"].Style.BackColor = Color.SkyBlue;

лист.Cells["A1"].Style.ForeColor = Color.Blue;

лист.Cells.Объединить(0, 0, 2, 5);

//Создаем ячейку подзаголовка (A3) на листе и применяем форматирование.

//Следующие строки вводят в ячейку строковое значение, указываем

//размер шрифта с атрибутами, указать горизонтальное и вертикальное выравнивание

//настройки, установить цвета переднего плана и фона и объединить ячейки

//(А3:Е3).

лист.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

лист.Cells["A3"].Style.Font.Size = новый FontUnit("13pt");

лист.Cells["A3"].Style.Font.Bold = true;

лист.Cells["A3"].Style.Font.Italic = true;

лист.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

лист.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

лист.Cells["A3"].Style.BackColor = Color.SeaGreen;

лист.Cells["A3"].Style.ForeColor = Color.Yellow;

лист.Cells.Объединить(2, 0, 1, 5);

//Получить индексы последней строки и столбца (которые содержат данные).

int totalrow = лист.Cells.MaxRow +1;

int totalcol = лист.Cells.MaxColumn;

//Получить лист Cells collections

Ячейки WebCells = лист.Cells;

//Определяем объект Cell.

ячейка WebCell;

//Проходим по данным на листе и форматируем два поля с помощью

// Стиль номера валюты.

для (целое i = 4;i<=totalrow;i++)

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
## **Создание форматированного отчета (файл .XLS) с графиком с использованием компонента Aspose.Cells**
Теперь я напишу код для сохранения отформатированного отчета с графиком на диск. я использую**GridWeb** х**Сохранять**кнопка,**GridWeb** х**СохранитьКоманда**событие запускается, когда вы нажимаете кнопку «Сохранить», поэтому я справлюсь с этим. Здесь я использую**Aspose.Cells**компонент для экспорта отформатированного отчета в MS Excel, создания диаграммы и встраивания ее в выходной файл Excel. Я не вставил изображение диаграммы (созданный**Aspose.Chart**компонент), а создайте аналогичную диаграмму, используя API из**Aspose.Cells**так что вы можете редактировать диаграмму в MS Excel для ваших нужд.





{{< highlight "java" >}}

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
Теперь запускаю приложение. Выпадающий список заполнен отдельными категориями.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Я выбираю категорию, по которой хочу показать отчет о продажах и нажимаю кнопку "Показать отчет".

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Итак, отчет отображается в**GridWeb**в зависимости от выбранной категории. Отчет форматируется по умолчанию на основе кода (написанного ранее).

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Если вы хотите отформатировать данные в некоторых ячейках в режиме WYSIWYG, вы можете сделать это довольно легко.**Aspose.Cells.GridWeb**обеспечивает**Формат Cells**редакторе, выберите нужную ячейку (ячейки) и щелкните ее правой кнопкой мыши, выберите параметр «Формат Cell…».

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Появится диалоговое окно Формат Cell.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Я указываю некоторые атрибуты шрифта и нажимаю «ОК».

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

И получить результат.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Помимо форматирования ячеек, вы также можете редактировать значения ячеек. Дважды щелкните нужную ячейку (ячейки) и отредактируйте значение.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Для отправки результата редактирования и пересчета всей формулы я нажимаю соответствующую кнопку (обведенную красным цветом), чтобы обновить отчет.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Теперь я создам диаграмму и вставлю ее в элемент управления. Я нажимаю пользовательскую кнопку команды (обведенную красным цветом), чтобы создать круговую диаграмму на основе диапазона данных.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Наконец, я экспортирую этот отчет с графиком в MS Excel. я нажимаю**Сохранять**кнопка (обведена красным цветом). Нажав на**Сохранять**кнопка будет отображаться**Загрузка файла**диалог, вы можете либо**Открытым**полученный отчет (выходной файл excel с графиком) в MS Excel или сохранить на диск.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Когда я нажимаю кнопку «Открыть» (диалоговое окно «Загрузка файла»), отчет Excel с графиком экспортируется в MS Excel. Показана верхняя часть отчета.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Показана нижняя часть отчета Excel.

![дело:изображение_альтернативный_текст](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
