---
title: إدراج أو حذف صفوف أو أعمدة
type: docs
weight: 20
url: /ar/net/insert-or-delete-rows-or-columns/
---
سواء كنا بصدد إنشاء ورقة عمل جديدة من البداية أو كنا نعمل على ورقة عمل موجودة ، فقد نحتاج إلى إضافة صفوف أو أعمدة إضافية إلى ورقة العمل لاستيعاب المزيد من البيانات أو لسبب آخر. بشكل عكسي ، قد يُطلب أيضًا حذف الصفوف أو الأعمدة من المواضع المحددة في ورقة العمل.
## **إدارة الصفوف / الأعمدة**
**Aspose.Cells** يوفر فئة ، مصنف يمثل ملف Excel. تحتوي فئة المصنف على مجموعة أوراق العمل التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة ورقة العمل. توفر فئة ورقة العمل مجموعة Cells تمثل كافة الخلايا في ورقة العمل.

**Cells**توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل ، وقد تمت مناقشة القليل منها أدناه بمزيد من التفصيل.
## **إدخال صف**
 يمكن للمطورين إدراج صف في ورقة العمل في أي مكان عن طريق استدعاء الأسلوب InsertRow للمجموعة Cells.**الصف إدراج** تأخذ الطريقة فهرس الصف حيث سيتم إدراج الصف الجديد.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a row into the worksheet at 3rd position

worksheet.Cells.InsertRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Row.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **إدراج صفوف متعددة**
في بعض الأحيان ، قد يحتاج المطورون إلى إدراج عدة صفوف في ورقة العمل. يمكن القيام بذلك عن طريق استدعاء طريقة InsertRows لمجموعة Cells. تأخذ طريقة InsertRows معلمتين:

- **فهرس الصف**، فهرس الصف حيث سيتم إدراج الصفوف الجديدة
- **عدد الصفوف**، إجمالي عدد الصفوف التي يجب إدراجها

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting 10 rows into the worksheet starting from 3rd row

worksheet.Cells.InsertRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **حذف صف**
 يمكن للمطورين حذف صف من ورقة العمل في أي مكان عن طريق استدعاء**احذف صف** طريقة جمع Cells.**احذف صف** تأخذ الطريقة فهرس الصف الذي يجب حذفه.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 3rd row from the worksheet

worksheet.Cells.DeleteRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **حذف عدة صفوف**
إذا احتاج المطورون إلى حذف عدة صفوف من ورقة العمل ، فيمكن القيام بذلك أيضًا عن طريق استدعاء طريقة DeleteRows للمجموعة Cells. تأخذ طريقة DeleteRows معلمتين:

- **فهرس الصف**، فهرس الصف الذي سيتم حذف الصفوف منه.
- **عدد الصفوف**، إجمالي عدد الصفوف التي يجب حذفها.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 10 rows from the worksheet starting from 3rd row

worksheet.Cells.DeleteRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **إدخال عمود**
يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء طريقة InsertColumn لمجموعة Cells. تأخذ طريقة InsertColumn فهرس العمود حيث سيتم إدراج العمود الجديد.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a column into the worksheet at 2nd position

worksheet.Cells.InsertColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **حذف عمود**
لحذف عمود من ورقة العمل في أي مكان ، يمكن للمطورين استدعاء طريقة DeleteColumn لمجموعة Cells. تأخذ طريقة DeleteColumn فهرس العمود لحذفه.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting a column from the worksheet at 2nd position

worksheet.Cells.DeleteColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
