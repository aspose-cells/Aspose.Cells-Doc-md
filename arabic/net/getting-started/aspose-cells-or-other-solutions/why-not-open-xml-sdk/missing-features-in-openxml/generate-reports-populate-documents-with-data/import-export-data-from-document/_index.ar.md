---
title: استيراد بيانات التصدير من المستند
type: docs
weight: 10
url: /ar/net/import-export-data-from-document/
---
## **استيراد البيانات من المستند**

البيانات عبارة عن مجموعة من الحقائق الأولية ونقوم بإنشاء جداول بيانات أو تقارير لتقديم هذه الحقائق الأولية بطريقة أكثر وضوحا. عادة ، نضيف البيانات إلى جداول البيانات بأنفسنا ولكن في بعض الأحيان ، نحتاج إلى إعادة استخدام موارد البيانات الحالية وهنا تأتي الحاجة إلى استيراد البيانات إلى جداول البيانات من مصادر بيانات مختلفة. في هذا الموضوع ، سنناقش بعض الأساليب لاستيراد البيانات إلى أوراق العمل من مصادر بيانات مختلفة.

## **استيراد البيانات باستخدام Aspose.Cells**

 عندما تستخدم ملفات**Aspose.Cells** لفتح ملف Excel ، يتم استيراد جميع البيانات الموجودة في الملف تلقائيًا ولكن Aspose.Cells يدعم أيضًا استيراد البيانات من مصادر بيانات مختلفة. يتم سرد عدد قليل من مصادر البيانات هذه أدناه:

- **مجموعة مصفوفة**
- **ArrayList**
- **جدول البيانات**
- **عمود البيانات**
- **عرض البيانات**
- **شبكة بيانات**
- **داتاريدر**
- **عرض شبكي**

 Aspose.Cells يوفر فصل دراسي ،**دفتر العمل** يمثل ملف Excel. تحتوي فئة المصنف على مجموعة أوراق العمل التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة ورقة العمل. توفر فئة ورقة العمل مجموعة Cells.

توفر المجموعة Cells طرقًا مفيدة جدًا لاستيراد البيانات من مصادر البيانات المختلفة.

### **الاستيراد من Array**

 يمكن للمطورين استيراد البيانات من مصفوفة إلى أوراق العمل الخاصة بهم عن طريق استدعاء**ImportArray** طريقة جمع Cells. هناك العديد من الإصدارات المحملة بشكل زائد من طريقة ImportArray ولكن الحمل الزائد النموذجي يأخذ المعلمات التالية:

- Array ، يمثل كائن المصفوفة الذي تحتاج محتوياته إلى الاستيراد
- رقم الصف ، يمثل رقم الصف للخلية الأولى حيث سيتم استيراد البيانات
- رقم العمود ، يمثل رقم العمود للخلية الأولى حيث سيتم استيراد البيانات
- هو عمودي ، قيمة منطقية تحدد استيراد البيانات عموديًا أو أفقيًا

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **الاستيراد من ArrayList**

 يمكن للمطورين استيراد البيانات من ArrayList إلى أوراق العمل الخاصة بهم عن طريق استدعاء**ImportArrayList** طريقة جمع Cells. تأخذ طريقة ImportArray المعلمات التالية:**ArrayList** ، يمثل كائن ArrayList الذي تحتاج محتوياته إلى الاستيراد

- رقم الصف ، يمثل رقم الصف للخلية الأولى حيث سيتم استيراد البيانات
- رقم العمود ، يمثل رقم العمود للخلية الأولى حيث سيتم استيراد البيانات
- هو عمودي ، قيمة منطقية تحدد استيراد البيانات عموديًا أو أفقيًا

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir + "DataImport from Array List.xls");

{{< /highlight >}}

### **الاستيراد من كائنات مخصصة**

 يمكن للمطورين استيراد البيانات من مجموعة الكائنات إلى ورقة العمل باستخدام**ImportCustomObjects**. يمكنك تقديم قائمة بالأعمدة / الخصائص للطريقة لعرض قائمة الكائنات التي تريدها.

{{< highlight "csharp" >}}

//Instantiate a new Workbook

Workbook book = new Workbook();

//Clear all the worksheets

book.Worksheets.Clear();

//Add a new Sheet "Data";

Worksheet sheet = book.Worksheets.Add("Data");

//Define List

List<WeeklyItem> list = new List<WeeklyItem>();

//Add data to the list of objects

list.Add(new WeeklyItem() { AtYarnStage = 1, InWIPStage = 2, Payment = 3, Shipment = 4, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 5, InWIPStage = 9, Payment = 7, Shipment = 2, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 7, InWIPStage = 3, Payment = 3, Shipment = 8, Shipment2 = 3 });

//We pick a few columns not all to import to the worksheet

sheet.Cells.ImportCustomObjects((System.Collections.ICollection)list,

new string[]{ "Date", "InWIPStage", "Shipment", "Payment" },

true,

0,

0,

list.Count,

true,

"dd/mm/yyyy",

false);

//Auto-fit all the columns

book.Worksheets[0].AutoFitColumns();

//Save the Excel file

book.Save(MyDir+"ImportedCustomObjects.xls");

{{< /highlight >}}

### **الاستيراد من DataTable**

 يمكن للمطورين استيراد البيانات من ملف**جدول البيانات** إلى أوراق العمل الخاصة بهم عن طريق استدعاء**إيمبورداتاتابلي** طريقة جمع Cells. هناك العديد من الإصدارات المحملة بشكل زائد من**إيمبورداتاتابلي** طريقة ولكن الحمل الزائد النموذجي يأخذ المعلمات التالية:**جدول البيانات** ، يمثل**جدول البيانات** الكائن الذي يجب استيراد محتوياته

- **هل اسم الحقل معروض**، يحدد ما إذا كان يجب استيراد أسماء أعمدة DataTable إلى ورقة العمل كصف أول أم لا
- **ابدأ Cell**، يمثل اسم خلية البداية (أي "A1") من مكان استيراد محتويات DataTable

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating a "Products" DataTable object

DataTable dataTable = new DataTable("Products");

//Adding columns to the DataTable object

dataTable.Columns.Add("Product ID", typeof(Int32));

dataTable.Columns.Add("Product Name", typeof(string));

dataTable.Columns.Add("Units In Stock", typeof(Int32));

//Creating an empty row in the DataTable object

DataRow dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **تنزيل نموذج التعليمات البرمجية**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **تصدير البيانات من المستند**

 لا يسهّل Aspose.Cells المستخدمين فقط لاستيراد البيانات إلى أوراق العمل من مصادر البيانات الخارجية ولكن أيضًا يسمح لهم بتصدير بيانات ورقة العمل الخاصة بهم إلى**جدول البيانات** . كما نعلم ذلك**جدول البيانات** هو جزء من ADO.NET ويستخدم للاحتفاظ بالبيانات. بمجرد تخزين البيانات في ملف**جدول البيانات**يمكن استخدامه بأي طريقة حسب متطلبات المستخدمين.

## **تصدير البيانات إلى DataTable (.NET) باستخدام Aspose.Cells**

يمكن للمطورين بسهولة تصدير بيانات ورقة العمل الخاصة بهم إلى كائن DataTable عن طريق استدعاء طريقة ExportDataTable أو ExportDataTableAsString للفئة Cells. يتم استخدام كلتا الطريقتين في سيناريوهات مختلفة ، والتي تمت مناقشتها أدناه بمزيد من التفصيل.

### **الأعمدة التي تحتوي على بيانات مكتوبة بقوة**

نعلم أن جدول البيانات يخزن البيانات على شكل سلسلة من الصفوف والأعمدة. إذا كانت جميع القيم في أعمدة ورقة العمل مكتوبة بقوة (وهذا يعني أن جميع القيم في عمود يجب أن تحتوي على نفس نوع البيانات) ، فيمكننا تصدير محتوى ورقة العمل عن طريق استدعاء**ExportDataTable** طريقة الفئة Cells.**ExportDataTable** تأخذ الطريقة المعلمات التالية لتصدير بيانات ورقة العمل كملف**جدول البيانات** موضوع:**رقم الصف** ، يمثل رقم صف الخلية الأولى التي سيتم تصدير البيانات منها

- **رقم العمود** ، يمثل رقم عمود الخلية الأولى التي سيتم تصدير البيانات منها
- **عدد الصفوف** ، يمثل عدد الصفوف المراد تصديرها
- **عدد الأعمدة**، يمثل عدد الأعمدة المطلوب تصديرها
- **تصدير أسماء الأعمدة** ، مشروع منطقي يشير إلى ما إذا كان يجب تصدير البيانات الموجودة في الصف الأول من ورقة العمل كأسماء أعمدة في DataTable أم لا

{{< highlight "csharp" >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

### **الأعمدة التي تحتوي على بيانات غير مكتوبة بشدة**

 إذا لم يتم كتابة جميع القيم في أعمدة ورقة العمل بشكل قوي (وهذا يعني أن القيم الموجودة في عمود قد تحتوي على أنواع بيانات مختلفة) ، فيمكننا تصدير محتوى ورقة العمل عن طريق استدعاء**ExportDataTableAsString** طريقة الفئة Cells.**ExportDataTableAsString** تأخذ الطريقة نفس مجموعة المعلمات مثل تلك الخاصة بـ**ExportDataTable** طريقة لتصدير بيانات ورقة العمل كملف**جدول البيانات** موضوع.

{{< highlight "csharp" >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
