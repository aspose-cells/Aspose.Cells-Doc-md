---
title: تجميع جداول البيانات
type: docs
weight: 10
url: /ar/net/assemble-spreadsheets/
---

يصف هذا القسم كيفية:

إنشاء ملف Excel جديد من البداية وإضافة ورق العمل إليه.

- إضافة أوراق العمل إلى جداول البيانات.
- الوصول إلى أوراق العمل باستخدام اسم الورقة.
- إزالة ورقة عمل من ملف Excel باستخدام اسمها.
- إزالة ورقة عمل من ملف Excel باستخدام فهرسها.
- توفر Aspose.Cells فئة تُسمى Workbook التي تمثل ملف Excel. تحتوي فئة Workbook على مجموعة Worksheets التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بفئة Worksheet. توفر فئة Worksheet مجموعة واسعة من الخصائص والأساليب لإدارة ورقات العمل.
## **إضافة ورقات العمل إلى ملف Excel جديد**
لإنشاء ملف Excel جديد برمجياً:

- إنشاء كائن من فئة Workbook.
- استدعاء الطريقة Add من مجموعة Worksheets. يتم إضافة ورقة عمل فارغة إلى ملف Excel * تلقائياً. يمكن الإشارة إليها عن طريق تمرير فهرس الورقة الجديدة إلى مجموعة Worksheets.
- الحصول على مرجع لورقة العمل.
- أداء العمل على الأوراق العمل.
- حفظ ملف Excel الجديد مع أوراق عمل جديدة عن طريق استدعاء طريقة Save من فئة Workbook.

{{< highlight csharp >}}

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
## **إضافة ورقات عمل إلى جدول التصميم**
يكون عملية إضافة ورقات عمل إلى جدول التصميم نفسها كإضافة ورقة عمل جديدة، باستثناء أن ملف Excel موجود بالفعل وبالتالي يجب فتحه قبل إضافة الأوراق العمل. يمكن فتح جدول التصميم باستخدام فئة Workbook.

{{< highlight csharp >}}

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
## **الوصول إلى الأوراق العمل باستخدام اسم الورقة**
الوصول أو الحصول على أي ورقة عمل عن طريق تحديد اسمها أو فهرسها.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **إزالة الأوراق العمل باستخدام اسم الورقة**
لإزالة الأوراق العمل من ملف، استدعاء طريقة RemoveAt لمجموعة Worksheets. قم بتمرير اسم الورقة إلى طريقة RemoveAt لإزالة ورقة عمل معينة.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **إزالة الأوراق العمل باستخدام فهرس الورقة**
يعمل إزالة الأوراق العمل باستخدام الاسم بشكل جيد عندما يكون اسم الورقة معروفاً. إذا لم تكن تعرف اسم الورقة العمل، استخدم نسخة معدلة من طريقة RemoveAt التي تأخذ فهرس ورقة العمل بدلاً من اسم الورقة.

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
