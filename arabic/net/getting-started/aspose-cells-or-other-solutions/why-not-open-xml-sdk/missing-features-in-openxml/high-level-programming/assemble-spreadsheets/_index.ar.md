---
title: تجميع جداول البيانات
type: docs
weight: 10
url: /ar/net/assemble-spreadsheets/
---
يصف هذا القسم كيفية:

قم بإنشاء ملف Excel جديد من البداية وأضف ورقة عمل إليه.

- أضف أوراق العمل إلى جداول بيانات المصمم.
- قم بالوصول إلى أوراق العمل باستخدام اسم الورقة.
- قم بإزالة ورقة عمل من ملف Excel باستخدام اسم الورقة الخاص بها.
- قم بإزالة ورقة عمل من ملف Excel باستخدام فهرس الورقة الخاص بها.
- يوفر Aspose.Cells فئة ، مصنف يمثل ملف Excel. تحتوي فئة المصنف على مجموعة أوراق عمل تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة ورقة العمل. توفر فئة ورقة العمل نطاقًا واسعًا من الخصائص والأساليب لإدارة أوراق العمل.
## **إضافة أوراق عمل إلى ملف Excel جديد**
لإنشاء ملف Excel جديد برمجيًا:

- قم بإنشاء كائن من فئة المصنف.
- قم باستدعاء طريقة الإضافة لمجموعة أوراق العمل. تتم إضافة ورقة عمل فارغة إلى ملف Excel * تلقائيًا. يمكن الرجوع إليها عن طريق تمرير فهرس ورقة ورقة العمل الجديدة إلى مجموعة أوراق العمل.
- الحصول على مرجع ورقة العمل.
- أداء العمل على أوراق العمل.
- احفظ ملف Excel الجديد بأوراق عمل جديدة عن طريق استدعاء طريقة Save لفئة المصنف.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **إضافة أوراق عمل إلى جدول بيانات المصمم**
عملية إضافة أوراق العمل إلى جدول بيانات المصمم مماثلة لعملية إضافة ورقة عمل جديدة ، باستثناء أن ملف Excel موجود بالفعل ، لذا يجب فتحه قبل إضافة أوراق العمل. يمكن فتح جدول بيانات المصمم بواسطة فئة المصنف.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **الوصول إلى أوراق العمل باستخدام اسم الورقة**
قم بالوصول إلى أي ورقة عمل أو احصل عليها عن طريق تحديد اسمها أو فهرسها.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **إزالة أوراق العمل باستخدام اسم الورقة**
لإزالة أوراق العمل من ملف ، قم باستدعاء أسلوب RemoveAt الخاص بمجموعة أوراق العمل. قم بتمرير اسم الورقة إلى أسلوب RemoveAt لإزالة ورقة عمل معينة.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **إزالة أوراق العمل باستخدام فهرس الورقة**
تعمل إزالة أوراق العمل حسب الاسم بشكل جيد عندما يكون اسم ورقة العمل معروفًا. إذا كنت لا تعرف اسم ورقة العمل ، فاستخدم إصدارًا محملاً بشكل زائد من أسلوب RemoveAt الذي يأخذ فهرس ورقة العمل بدلاً من اسم الورقة الخاص بها.

{{< highlight "csharp" >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
