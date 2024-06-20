---
title: تجميع البيانات في Aspose.Cells
type: docs
weight: 10
url: /ar/net/grouping-data-in-aspose-cells/
---

في بعض تقارير Excel قد تحتاج إلى تقسيم البيانات إلى مجموعات لجعلها أسهل قراءة وتحليل. أحد الأغراض الرئيسية لتقسيم البيانات إلى مجموعات هو تشغيل الحسابات (أداء عمليات ملخصية) على كل مجموعة من السجلات.

تسمح علامات Aspose.Cells الذكية لك بتجميع بياناتك حسب الحقل(الحقول) ووضع صفوف ملخصية بين مجموعات البيانات أو السجلات. على سبيل المثال، إذا كنت تقوم بتجميع البيانات حسب Customers.CustomerID، يمكنك إضافة سجل ملخصي في كل مرة يتغير فيها المجموعة.

توضح مقاطع الكود المثالية التالية كيفية تجميع البيانات في تقرير Excel باستخدام علامات Aspose.Cells الذكية.
## **معلمات**
فيما يلي بعض معلمات العلامات الذكية المستخدمة لتجميع البيانات.
**group:normal/merge/repeat**

نحن ندعم ثلاثة أنواع من التجميع يمكنك الاختيار بينها.

- عادي - قيمة حقل (حقول) التجميع لا تكرر للسجلات المقابلة في العمود؛ بدلاً من ذلك يتم طباعتهم مرة واحدة لكل مجموعة بيانات.
- دمج - نفس السلوك كما هو الحال بالنسبة للمعلمة العادية، باستثناء أنه يدمج الخلايا في حقول التجميع لكل مجموعة محددة.
- تكرار - يتم تكرار قيمة حقل (حقول) التجميع للسجلات المقابلة.

إذا كان لديك عدة معلمات، فاسمح بفصلها بفواصل، ولكن بدون مسافة: معلمة أ، معلمة ب، معلمة ج
### **مثال**
يظهر هذا المثال بعض معلمات التجميع في العمل. يستخدم قاعدة بيانات Microsoft Access بمسمى Northwind.mdb ويستخرج البيانات من الجدول الذي يحمل اسم "تفاصيل الطلب". ننشئ ملف مصمم يسمى SmartMarker_Designer.xls في Microsoft Excel ونضع علامات ذكية في الخلايا المختلفة في ورقات العمل. يتم معالجة العلامات لملء ورقات العمل. يتم وضع البيانات وتنظيمها حسب حقل تجميع.

يحتوي الملف المصمم على ورقتي عمل. في الأولى نضع علامات ذكية مع معلمات التجميع كما هو مبين في اللقطة أدناه. يتم وضع ثلاث علامات ذكية (بمعلمات تجميع) كما يلي:
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(subtotal9:Order Details.OrderID)، و
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID) يذهب إلى A5، B5 و C5 على التوالي.

{{< highlight csharp >}}

 //Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=Northwind.mdb");

//Open the connection object.

con.Open();

//Create a command object and specify the SQL query.

OleDbCommand cmd = new OleDbCommand("Select * from [Order Details]", con);

//Create a data adapter object.

OleDbDataAdapter da = new OleDbDataAdapter();

//Specify the command.

da.SelectCommand = cmd;

//Create a dataset object.

DataSet ds = new DataSet();

//Fill the dataset with the table records.

da.Fill(ds, "Order Details");

//Create a datatable with respect to dataset table.

DataTable dt = ds.Tables["Order Details"];

//Create WorkbookDesigner object.

WorkbookDesigner wd = new WorkbookDesigner();

//Open the template file (which contains smart markers).

wd.Workbook = new Workbook("SmartMarkerDesigner.xls");

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save("outSmartMarker_Designer.xls");

{{< /highlight >}}
## **تحميل رمز عينة**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
