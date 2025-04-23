---
title: استيراد تصدير البيانات من المستند
type: docs
weight: 10
url: /ar/net/import-export-data-from-document/
---

## **استيراد البيانات من المستند**

البيانات هي مجموعة من الحقائق الخام ونقوم بإنشاء مستند جداول بيانات أو تقارير لعرض هذه الحقائق الخام بطريقة أكثر معنى. عادةً ما نضيف البيانات إلى جداول بيانات بأنفسنا ولكن في بعض الأحيان، نحتاج إلى إعادة استخدام مصادر البيانات الموجودة وهنا يأتي دور استيراد البيانات إلى جداول البيانات من مصادر بيانات مختلفة. في هذا الموضوع، سنناقش بعض التقنيات لاستيراد البيانات إلى أوراق العمل من مصادر بيانات مختلفة.

## **استيراد البيانات باستخدام Aspose.Cells**

عند استخدام **Aspose.Cells** لفتح ملف Excel، يتم استيراد جميع البيانات في الملف تلقائيًا ولكن Aspose.Cells يدعم أيضًا استيراد البيانات من مصادر البيانات المختلفة. يُذكر بعض هذه المصادر أدناه:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells توفر فئة، **Workbook** التي تمثل ملف Excel. تحتوي فئة Workbook على مجموعة Worksheets تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة Worksheet. توفر فئة Worksheet مجموعة Cells.

توفر مجموعة Cells طرقًا مفيدة جدًا لاستيراد البيانات من مصادر بيانات مختلفة.

### **استيراد من مصفوفة**

يمكن للمطورين استيراد البيانات من مصفوفة إلى ورقة العمل الخاصة بهم من خلال استدعاء الأسلوب **ImportArray** من مجموعة الخلايا. هناك العديد من الإصدارات المتعددة لأسلوب ImportArray ولكن الإصدار النموذجي يأخذ المعلمات التالية:

- مصفوفة, يمثل كائن المصفوفة التي تحتاج إلى استيراد محتوياتها
- رقم الصف, يمثل رقم الصف لأول خلية حيث سيتم استيراد البيانات
- رقم العمود, يمثل رقم العمود لأول خلية حيث سيتم استيراد البيانات
- هل هو عمودي, قيمة منطقية تحدد استيراد البيانات عموديا أم أفقيا

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **استيراد من ArrayList**

يمكن للمطورين استيراد البيانات من ArrayList إلى ورقة العمل الخاصة بهم من خلال استدعاء الأسلوب **ImportArrayList** من مجموعة الخلايا. يأخذ أسلوب ImportArray المعلمات التالية: **ArrayList** , يمثل كائن ArrayList الذي تحتاج إلى استيراد محتوياته

- رقم الصف , يمثل رقم الصف لأول خلية حيث سيتم استيراد البيانات
- رقم العمود , يمثل رقم العمود لأول خلية حيث سيتم استيراد البيانات
- هل هو عمودي , قيمة منطقية تحدد استيراد البيانات عموديا أم أفقيا

{{< highlight csharp >}}

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

### **استيراد من الكائنات المخصصة**

يمكن للمطورين استيراد البيانات من مجموعة من الكائنات إلى ورقة العمل باستخدام **ImportCustomObjects**. يمكنك تقديم قائمة من الأعمدة/الخصائص للأسلوب لعرض القائمة المرغوبة من الكائنات الخاصة بك.

{{< highlight csharp >}}

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

new string[] { "Date", "InWIPStage", "Shipment", "Payment" },

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

### **استيراد من DataTable**

يمكن للمطورين استيراد البيانات من **DataTable** إلى ورقة العمل الخاصة بهم من خلال استدعاء الأسلوب **ImportDataTable** من مجموعة الخلايا. هناك العديد من الإصدارات المتعددة لأسلوب **ImportDataTable** ولكن الإصدار النموذجي يأخذ المعلمات التالية:**DataTable** , يمثل كائن **DataTable** التي تحتاج إلى استيراد محتوياتها

- **هل يتم عرض اسم الحقل**, يحدد ما إذا كانت أسماء أعمدة DataTable يجب استيرادها إلى ورقة العمل كصف أول أم لا
- **الخلية البدء** , يمثل اسم الخلية البداية (مثل "A1") من حيث يتم استيراد محتويات **DataTable**

{{< highlight csharp >}}

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

dr[0] = 1;

dr[1] = "Aniseed Syrup";

dr[2] = 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **تحميل رمز عينة**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **تصدير البيانات من المستند**

Aspose.Cells لا تسهل فقط على مستخدميها استيراد البيانات إلى أوراق العمل من مصادر بيانات خارجية ولكن تسمح لهم أيضًا بتصدير بيانات ورقة العمل الخاصة بهم إلى **DataTable**. كما نعلم أن **DataTable** هي جزء من ADO.NET وتستخدم لاحتواء البيانات. بمجرد تخزين البيانات في **DataTable**، يمكن استخدامها بأي طريقة وفقًا لمتطلبات المستخدمين.

## **تصدير البيانات إلى DataTable (.NET) باستخدام Aspose.Cells**

يمكن للمطورين تصدير بيانات جدول العمل الخاص بهم إلى كائن DataTable عن طريق استدعاء إما طريقة ExportDataTable أو ExportDataTableAsString من فئة Cells. تُستخدم كلتا الطريقتين في سيناريوهات مختلفة، والتي سيتم مناقشتها أدناه بمزيد من التفصيل.

### **الأعمدة التي تحتوي على بيانات مكونة من نوع واحد**

نحن نعلم أن جدول البيانات يخزن البيانات كتسلسل من الصفوف والأعمدة. إذا كانت جميع القيم في أعمدة ورقة عمل من النوع المقيد (وهذا يعني أن جميع القيم في العمود يجب أن تكون لها نفس نوع البيانات) ثم يمكننا تصدير محتوى الورقة العمل باستدعاء طريقة **ExportDataTable** من فئة الخلايا. طريقة **ExportDataTable** تأخذ المعاملات التالية لتصدير بيانات ورقة العمل ككائن **DataTable**: **رقم الصف**، يمثل رقم الصف الأول من حيث سيتم تصدير البيانات.

- **رقم العمود**، يمثل رقم العمود الأول من حيث سيتم تصدير البيانات
- عدد الصفوف , يمثل عدد الصفوف المراد تصديرها
- عدد الأعمدة , يمثل عدد الأعمدة المراد تصديرها
- تصدير أسماء الأعمدة , خاصية منطقية تشير ما إذا كان يجب تصدير البيانات في الصف الأول من ورقة العمل كأسماء أعمدة DataTable أم لا

{{< highlight csharp >}}

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

### **الأعمدة التي تحتوي على بيانات غير مكونة من نوع واحد**

إذا كانت جميع القيم في أعمدة ورقة عمل ليست من النوع المقيد (وهذا يعني أن القيم في العمود قد تكون لها أنواع بيانات مختلفة) ثم يمكننا تصدير محتوى الورقة العمل باستدعاء طريقة **ExportDataTableAsString** من فئة الخلايا. طريقة **ExportDataTableAsString** تأخذ نفس مجموعة المعاملات كطريقة **ExportDataTable** لتصدير بيانات ورقة العمل ككائن **DataTable**.

{{< highlight csharp >}}

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

## **تحميل رمز عينة**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
