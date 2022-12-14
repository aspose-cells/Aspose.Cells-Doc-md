---
title: إنشاء تقارير Excel منسقة ديناميكيًا باستخدام رسم بياني أنيق
type: docs
weight: 130
url: /ar/net/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
---
{{% alert color="primary" %}} 

تم تصميم هذا المستند لتوفير المعلومات الضرورية حول كيفية استخلاص البيانات من بعض مصادر البيانات إلى شبكة رائعة مثل التحكم ، ولصق مخطط فيها وتصدير التقرير مع الرسم البياني إلى MS Excel لإجراء التحليل والمقارنات والطباعة.

{{% /alert %}} 
## **ملخص**
هناك سيناريوهات معينة على الويب تتطلب كلاً من إعداد التقارير والعروض التقديمية ، وهي مجموعة من الأجزاء أو العناصر التي يمكن أن تعمل معًا بشكل جيد. تشرح المقالة مدى سهولة تصميم وإنشاء تقارير Excel أنيقة ديناميكيًا بطريقة WYSIWYG. يقوم بتصدير البيانات من ملف XML (يمكنك أيضًا استخدام مصادر بيانات أخرى) إلى التحكم Aspose.Cells.GridWeb الذي يوفر لك البيئة الحقيقية التي تسمح لك بتطبيق تنسيق غني وجذاب على البيانات وحساب نتائج الصيغة مثل MS Excel. كما أنه ينشئ مخططًا معقدًا استنادًا إلى استخدام بيانات مصدر ورقة العمل[Aspose.Cells](https://products.aspose.com/cells/) المكون ولصق صورة المخطط في تقرير المبيعات. أخيرًا ، يتم حفظ تقرير Excel مع الرسم البياني المرفق على القرص باستخدام مكون Aspose.Cells.

تتضمن هذه المقالة الكود المصدري والمشروع التجريبي المميز بالكامل لمثل هذه الوظيفة.

يتيح للمستخدمين الذين لديهم تصور مفصل حول كيفية إنشاء تقرير أعمال لإدخال البيانات في ورقة عمل للشبكة وتطبيق بعض التنسيقات على الخلايا في الصفوف والأعمدة ، وتضمين رسمًا بيانيًا استنادًا إلى نطاق مصدر البيانات قبل حفظ اكسل تقرير الى القرص.
## **مكونات Aspose**
 أستخدم ثلاثة من[Aspose](http://www.aspose.com/) مكونات لأداء المهمة بسهولة.[Aspose](http://www.aspose.com/) يوفر الناشر المكون من .NET و Java مجموعة متنوعة من المكونات الغنية بالميزات.[Aspose](http://www.aspose.com/) يوفر خطًا رائعًا من مكونات .NET و Java. يحظى بثقة الآلاف من العملاء في جميع أنحاء العالم ، وتشمل المنتجات مكونات تنسيق الملف ومنتجات التقارير والمكونات المرئية ومكونات الأدوات التي تسمح بفتح وتعديل وإنشاء وحفظ ودمج وتحويل وما إلى ذلك من المستندات بتنسيقات مختلفة بما في ذلك DOC و RTF و WordML و HTML و PDF و XLS و SpreadsheetML و Tab Delimited و CSV و PPT و SWF و EMF و WMF و MPX و MPD وغيرها من التنسيقات.

أود أن أغتنم هذه الفرصة لأقدم لكم ثلاثة من هذه المكونات التي تم استخدامها في هذا المسعى.
## **Aspose.Cells ضوابط الشبكة**
 Aspose.Cells تعتبر ضوابط الشبكة حلاً شاملاً للشبكة. تأتي ضوابط الشبكة Aspose.Cells معبأة مع مكونين مختلفين من واجهة المستخدم الرسومية .NET (Aspose.Cells.GridDesktop و Aspose.Cells.GridWeb): أحدهما لدعم تطبيقات سطح المكتب والآخر لدعم تطبيقات الويب. كلا الإصدارين متطابقان بشكل متساوٍ لجعل التنفيذ في أي من النظامين أمرًا سريعًا. Aspose.Cells.GridWeb يوفر القدرة على الاستيراد من جداول بيانات Excel والتصدير إليها. لذلك يمكن لأي شخص على دراية ببرنامج Excel (حتى المستخدمين النهائيين) تصميم شكل ومظهر الشبكة. Aspose.Cells.GridWeb يوفر أيضًا API سهل الاستخدام وغني بالميزات والذي يوفر للمطورين تحكمًا كاملاً في شكل وملمس وسلوك شبكتهم. لمعرفة المزيد عن المنتج وميزاته ودليل المبرمجين ، يرجى مراجعة ملخص قائمة الميزات ، Aspose.Cells.[العروض](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells**هو أحد مكونات تقارير جداول بيانات Excel التي تمكنك من قراءة جداول بيانات Excel وكتابتها دون استخدام Microsoft Excel ليتم تثبيتها إما على جانب العميل أو الخادم.**Aspose.Cells** هو مكون غني بالميزات يقدم أكثر بكثير من مجرد تصدير أساسي للبيانات. مع**Aspose.Cells** يمكن للمطورين تصدير البيانات وتنسيق جداول البيانات بكل التفاصيل وعلى كل مستوى ، واستيراد الصور ، واستيراد المخططات ، وإنشاء المخططات ، ومعالجة المخططات ، ودفق بيانات Excel ، وحفظها بتنسيقات مختلفة بما في ذلك XLS ، و CSV ، و SpreadsheetML ، و TabDelimited ، و TXT ، و XML ([Aspose.Pdf](https://products.aspose.com/pdf/) متكامل) وغيرها الكثير.**Aspose.Cells** يقدم وسيلة سهلة الاستخدام وغنية بالميزات**API** للمبرمجين. لديها قائمة كبيرة من الميزات. لمعرفة المزيد عن المنتج ومميزاته وللحصول على دليل المبرمج ، يرجى مراجعة ملخص**قائمة الصور**, **Aspose.Cells التوثيق** وعروض توضيحية مميزة عبر الإنترنت. يمكنك[تحميل](https://downloads.aspose.com/cells) نسخته التقييمية مجانًا.
## **تصميم الواجهة**
بدأنا في إنشاء تطبيق ويب Asp.Net جديد في Visual Studio.Net.

 أنا**يضيف مرجعا**إلى المكونات الثلاثة ieAspose.Cells.GridWeb.dll و Aspose.Chart.dll و Aspose.Cells.dll للمشروع أولاً. أضع بعض التحكم في الصفحة وأضع خصائصها ، أي قائمة منسدلة وزر أمر وتسمية. ثم أضع**Aspose.Cells.GridWeb****مراقبة**(**شبكة**) إليها من صندوق الأدوات ، لأنه بعد إضافة مراجع إلى المكونات الثلاثة ، فإن**شبكة**ظهر التحكم في صندوق الأدوات. المكونان الآخران (**Aspose.Chart**و**Aspose.Cells**) هي مجرد مكتبات ، فقط يمكنك الرجوع إلى المشروع.

أقوم أيضًا بإنشاء مجلدين "ملف" و "صور" ، وأضف "Products.xml" و "chart.gif" إلى هذين المجلدين على التوالي. ملف xml هو ملف مصدر بيانات يتم استخراج البيانات منه لملء ملف**شبكة**ورقة عمل. سيوفر ملف الصورة صورة لزر مخصص يتم وضعه على ملف**شبكة**مراقبة.

أقوم الآن بإنشاء زر أمر مخصص. أنا ببساطة انقر بزر الماوس الأيمن فوق ملف**شبكة**السيطرة وانقر فوق خيار "أزرار الأوامر المخصصة ...".

سيقوم بتنشيط محرر Custom Command Button ، ويسمح لك المحرر بإنشاء أزرار صورة أوامر مخصصة مع إرفاق تلميح أداة. أحدد قيم بعض خصائص الزر ، على سبيل المثال ، الأمر (الاسم) -> "btnChart" ، ImageUrl -> أعط المسار إلى ملف الصورة ("chart.gif") وتلميح الأدوات -> أعط تلميح الأداة.

لذلك ، يتم إضافة زر الأمر المخصص كما قد تراه (محاطًا بدائرة باللون الأحمر) في لقطة الشاشة التالية.

|![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
|:- |


أخيرًا ، قمت بتعيين بعض سمات الخط (غامقة) للتسمية وزر الأمر. أقوم أيضًا بضبط حجم عناصر التحكم للحصول على المظهر النهائي.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **استرجاع البيانات من ملف XML**
فيما يلي هيكل ملف XML المستخدم في المشروع.
### **بنية ملف XML**
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
## **تعبئة ورقة عمل عنصر التحكم Aspose.Cells.GridWeb بالبيانات**
يمكنني استخدام بعض API من**شبكة**لتعبئة ورقة عمل ببيانات من ملف XML المصدر. أكتب التعليمات البرمجية في معالج حدث النقر فوق زر الأمر (المسمى "إظهار التقرير"). يتم تصفية تقرير البيانات بناءً على العنصر المحدد من القائمة المنسدلة.



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
## **تنسيق البيانات في Cells**
للتمييز بين أنواع المعلومات المختلفة في ورقة العمل ، وللحصول على العرض الأمثل للبيانات الموجودة في ورقة العمل ولجعل ورقة العمل أسهل في المسح الضوئي ، يمكنك تنسيق ورقة العمل. أ**شكل**يمثل نمطًا ويتم تعريفه على أنه مجموعة من الخصائص ، مثل الخطوط وأحجام الخطوط وتنسيقات الأرقام وحدود الخلية وتظليل الخلية بلون الخلفية الخالص أو نمط لون معين والمسافة البادئة والمحاذاة واتجاه النص في الخلايا.

أقوم بدمج المزيد من سطور التعليمات البرمجية أعلاه. أضع العنوان / العنوان الفرعي للتقرير ، وأقوم ببعض التنسيقات على خلايا العنوان والعنوان الفرعي والتفاصيل. أقوم أيضًا بتطبيق تنسيق الأرقام على الحقلين (تعيين تنسيق رقم العملة على حقلي سعر الوحدة والبيع) وضبط ارتفاع / عرض الصفوف والأعمدة باستخدام**Aspose.Cells.GridWeb**API.



{{< highlight "java" >}}

 // قم بإنشاء خلية العنوان (A1) في الورقة وطبق التنسيقات.

// تقوم الأسطر التالية بإدخال قيمة سلسلة إلى الخلية ، وتحديدها

// حجم الخط ، حدد إعدادات المحاذاة الأفقية والعمودية ، اضبط

// ألوان المقدمة والخلفية ودمج الخلايا (A1: E2).

ورقة WebWorksheet = GridWeb1.WebWorksheets [0] ؛

sheet.Cells ["A1"]. PutValue ("مبيعات المنتج حسب الفئة")؛

sheet.Cells ["A1"]. Style.Font.Size = new FontUnit ("20pt")؛

sheet.Cells ["A1"]. Style.HorizontalAlign = HorizontalAlign.Center؛

sheet.Cells ["A1"]. Style.VerticalAlign = VerticalAlign.Middle؛

sheet.Cells ["A1"]. Style.BackColor = Color.SkyBlue؛

sheet.Cells ["A1"]. Style.ForeColor = Color.Blue؛

ورقة Cells. دمج (0 ، 0 ، 2 ، 5) ؛

// أنشئ خلية الترجمة (A3) في الورقة وطبق التنسيقات.

// تقوم الأسطر التالية بإدخال قيمة سلسلة إلى الخلية ، وتحديدها

// حجم الخط مع السمات ، وتحديد المحاذاة الأفقية والعمودية

// الإعدادات ، قم بتعيين ألوان المقدمة والخلفية ودمج الخلايا

// (A3: E3).

sheet.Cells ["A3"]. PutValue (DropDownList1.SelectedItem.Text) ؛

sheet.Cells ["A3"]. Style.Font.Size = new FontUnit ("13pt")؛

sheet.Cells ["A3"]. Style.Font.Bold = true ؛

sheet.Cells ["A3"]. Style.Font.Italic = true ؛

sheet.Cells ["A3"]. Style.HorizontalAlign = HorizontalAlign.Left؛

sheet.Cells ["A3"]. Style.VerticalAlign = VerticalAlign.Middle؛

sheet.Cells ["A3"]. Style.BackColor = Color.SeaGreen؛

sheet.Cells ["A3"]. Style.ForeColor = Color.Yellow؛

ورقة Cells. دمج (2 ، 0 ، 1 ، 5) ؛

// احصل على فهارس الصف والعمود الأخير (التي تحتوي على بيانات).

int totalrow = ورقة .Cells.MaxRow +1 ؛

int totalcol = ورقة .Cells.MaxColumn ؛

// احصل على مجموعات الورقة Cells

خلايا WebCells = Sheet.Cells ؛

// تحديد كائن Cell.

خلية WebCell

// قم بالتكرار خلال البيانات الموجودة في الورقة وقم بتنسيق حقلين باستخدام

// نمط رقم العملة.

لـ (int i = 4 ؛ i<=totalrow;i++)

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
## **إنتاج التقرير المنسق (ملف XLS) باستخدام رسم بياني باستخدام مكون Aspose.Cells**
الآن ، سأكتب بعض التعليمات البرمجية لحفظ التقرير المنسق مع رسم بياني على القرص. أنا أستخدم**شبكة** 'س**يحفظ**زر ،**شبكة** 'س**SaveCommand**يتم تشغيل الحدث عند النقر فوق الزر حفظ ، لذلك سأتعامل معه. هنا ، أستخدم**Aspose.Cells**عنصر لتصدير التقرير المنسق إلى MS Excel ، وإنشاء مخطط وتضمينه في ملف Excel الناتج. لم أدرج صورة المخطط (تم إنشاؤها بواسطة**Aspose.Chart**المكون) بدلاً من ذلك قم بإنشاء مخطط مشابه باستخدام API من**Aspose.Cells**، بحيث يمكنك تعديل الرسم البياني في MS Excel حسب حاجتك.





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
## **تشغيل التطبيق**
الآن ، أقوم بتشغيل التطبيق. القائمة المنسدلة مليئة بالفئات المميزة.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

أحدد فئة أريد من خلالها إظهار تقرير المبيعات والنقر فوق الزر "إظهار التقرير".

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

لذلك ، يتم عرض التقرير في ملف**شبكة**على أساس الفئة المختارة. يتم تنسيق التقرير افتراضيًا بناءً على الكود (المكتوب مسبقًا).

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

إذا كنت ترغب في تنسيق البيانات في بعض الخلايا بطريقة WYSIWYG ، فيمكنك القيام بذلك بسهولة تامة.**Aspose.Cells.GridWeb**يوفر**شكل Cells**محرر ، حدد الخلية (الخلايا) التي تريدها وانقر عليها بزر الماوس الأيمن ، وانقر فوق الخيار "تنسيق Cell ...".

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

يظهر مربع حوار التنسيق Cell.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

أحدد بعض سمات الخط وانقر على موافق.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

واحصل على النتيجة.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

بصرف النظر عن تنسيق الخلايا ، يمكنك أيضًا تحرير قيم الخلية الخاصة بك. انقر نقرًا مزدوجًا فوق الخلية (الخلايا) التي تريدها وقم بتحرير القيمة.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

لإرسال نتيجة التحرير وإعادة حساب كل الصيغة ، أنقر فوق الزر ذي الصلة (المحاط بدائرة باللون الأحمر) لتحديث التقرير.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

الآن سوف أقوم بإنشاء المخطط ولصقه في عنصر التحكم. انقر فوق زر الأمر المخصص (المحاط بدائرة باللون الأحمر) لإنشاء مخطط دائري بناءً على نطاق البيانات.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

أخيرًا ، سأقوم بتصدير تقرير البيانات هذا مع رسم بياني إلى MS Excel. أنقر فوق ملف**يحفظ**زر (محاط باللون الأحمر). النقر فوق ملف**يحفظ**سيعرض الزر**تحميل الملف**الحوار ، يمكنك إما**فتح**التقرير الناتج (ملف اكسل الناتج مع رسم بياني) في MS Excel أو احفظه على القرص.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

عندما أنقر فوق الزر فتح (مربع حوار تنزيل الملف) ، يتم تصدير تقرير Excel مع الرسم البياني إلى MS Excel. يتم عرض الجزء العلوي من التقرير.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

يتم عرض الجزء السفلي من تقرير Excel.

![ما يجب القيام به: image_بديل_نص](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
