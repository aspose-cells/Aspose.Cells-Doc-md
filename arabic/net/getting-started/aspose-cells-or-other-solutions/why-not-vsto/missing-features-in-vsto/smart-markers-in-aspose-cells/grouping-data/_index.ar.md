---
title: تجميع البيانات
type: docs
weight: 10
url: /ar/net/grouping-data/
---
في بعض تقارير Excel ، قد تحتاج إلى تقسيم البيانات إلى مجموعات لتسهيل قراءتها وتحليلها. أحد الأغراض الأساسية لتقسيم البيانات إلى مجموعات هو إجراء العمليات الحسابية (إجراء عمليات موجزة) على كل مجموعة من السجلات.

تسمح لك العلامات الذكية Aspose.Cells بتجميع البيانات الخاصة بك حسب المجال (المجالات) ووضع صفوف التلخيص بين مجموعات البيانات أو مجموعات البيانات. على سبيل المثال ، في حالة تجميع البيانات حسب Customer.CustomerID ، يمكنك إضافة سجل ملخص في كل مرة تتغير فيها المجموعة.

يوضح المثال مقتطفات التعليمات البرمجية التي تلي كيفية تجميع البيانات في تقرير Excel باستخدام العلامات الذكية.
## **المعلمات**
فيما يلي بعض معلمات العلامات الذكية المستخدمة لتجميع البيانات.
**المجموعة: عادي / دمج / كرر**

نحن ندعم ثلاثة أنواع من المجموعات يمكنك الاختيار من بينها.

- عادي - لا تتكرر قيمة المجموعة حسب الحقل (الحقول) للسجلات المقابلة في العمود ؛ بدلاً من ذلك يتم طباعتها مرة واحدة لكل مجموعة بيانات.
- دمج - نفس سلوك المعلمة العادية ، باستثناء أنها تدمج الخلايا في المجموعة حسب الحقل (الحقول) لكل مجموعة مجموعة.
- تكرار - تتكرر قيمة المجموعة حسب الحقل (الحقول) للسجلات المقابلة.

إذا كان لديك العديد من المعلمات ، فافصل بينها بفاصلات ، ولكن بدون مسافة: معلمة A ، معلمة B ، معلمة ج
### **مثال**
يوضح هذا المثال بعض معلمات التجميع قيد التنفيذ. يستخدم قاعدة بيانات Northwind.mdb Microsoft Access ويستخرج البيانات من الجدول المسمى "تفاصيل الطلب". نقوم بإنشاء ملف مصمم يسمى SmartMarker_Designer.xls في Microsoft Excel ووضع علامات ذكية في خلايا مختلفة في أوراق العمل. تتم معالجة العلامات لتعبئة أوراق العمل. يتم وضع البيانات وتنظيمها بواسطة حقل المجموعة.

يحتوي ملف المصمم على ورقتي عمل. في البداية ، وضعنا علامات ذكية مع معلمات تجميع كما هو موضح في لقطة الشاشة أدناه. يتم وضع ثلاث علامات ذكية (مع معلمات التجميع):
& = تفاصيل الطلب. معرف الطلب (المجموعة: دمج ، تخطي: 1) ،
& = تفاصيل الطلب الكمية (الإجمالي الفرعي 9: تفاصيل الطلب. معرف الطلب) ، و
& = تفاصيل الطلب.سعر الوحدة (الإجمالي الفرعي 9: تفاصيل الطلب. معرف الطلب) انتقل إلى A5 و B5 و C5 على التوالي.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Grouping Data OLE DB.xlsx";

//Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=~\\..\\..\\..\\Data\\Northwind.mdb");

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

wd.Workbook = new Workbook(FileName);

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save(FileName);

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
