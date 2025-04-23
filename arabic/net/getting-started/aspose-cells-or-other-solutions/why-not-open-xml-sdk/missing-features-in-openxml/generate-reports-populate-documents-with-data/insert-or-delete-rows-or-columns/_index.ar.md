---
title: إدراج أو حذف الصفوف أو الأعمدة
type: docs
weight: 20
url: /ar/net/insert-or-delete-rows-or-columns/
---

سواء كنا نقوم بإنشاء ورقة عمل جديدة من الصفر أو نعمل على ورقة عمل موجودة، قد نحتاج إلى إضافة صفوف أو أعمدة إضافية إلى الورقة العمل لاستيعاب المزيد من البيانات أو لسبب آخر. بالقدر المعاكس، قد يكون من الضروري أيضًا حذف الصفوف أو الأعمدة من مواقع محددة في الورقة العمل.
## **إدارة الصفوف / الأعمدة**
**Aspose.Cells** توفر فئة، Workbook التي تمثل ملف Excel. فئة Workbook تحتوي على مجموعة من Worksheets التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة Worksheet. توفر فئة Worksheet مجموعة من الخلايا التي تمثل جميع الخلايا في ورقة العمل.

مجموعة **Cells** توفر العديد من الأساليب لإدارة الصفوف أو الأعمدة في ورقة العمل، ويتم مناقشة بعضها أدناه بمزيد من التفاصيل.
## **إدراج صف**
يمكن للمطورين إدراج صف في ورقة العمل في أي موقع عن طريق استدعاء أسلوب InsertRow من مجموعة الخلايا. يأخذ أسلوب **InsertRow** الفهرس للصف الذي سيتم إدراج الصف الجديد فيه.

{{< highlight csharp >}}

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
في بعض الأحيان، قد يحتاج المطورون إلى إدراج صفوف متعددة في ورقة العمل. يمكن أن يتم ذلك عن طريق استدعاء أسلوب InsertRows من مجموعة الخلايا. يأخذ أسلوب InsertRows معهدان:

- **مؤشر الصف**، فهرس الصف الذي سيتم إدراج الصفوف الجديدة فيه
- **عدد الصفوف**, إجمالي عدد الصفوف التي تحتاج إلى الإدراج

{{< highlight csharp >}}

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
يمكن للمطورين حذف صف من ورقة العمل في أي موقع عن طريق استدعاء أسلوب **DeleteRow** من مجموعة الخلايا. يأخذ أسلوب **DeleteRow** الفهرس للصف الذي يحتاج إلى الحذف.

{{< highlight csharp >}}

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
## **حذف صفوف متعددة**
إذا كان المطورون بحاجة إلى حذف صفوف متعددة من ورقة العمل، يمكن أيضًا القيام بذلك عن طريق استدعاء أسلوب DeleteRows من مجموعة الخلايا. يأخذ أسلوب DeleteRows معهدان:

- **مؤشر الصف**، فهرس الصف من حيث سيتم حذف الصفوف
- **عدد الصفوف**, إجمالي عدد الصفوف التي تحتاج إلى الحذف

{{< highlight csharp >}}

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
## **إدراج عمود**
يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي موقع عن طريق استدعاء أسلوب InsertColumn من مجموعة الخلايا. يأخذ أسلوب InsertColumn الفهرس للعمود الذي سيتم إدراج العمود الجديد فيه.

{{< highlight csharp >}}

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
لحذف عمود من ورقة العمل في أي موقع، يمكن للمطورين استدعاء طريقة DeleteColumn من مجموعة Cells. تأخذ طريقة DeleteColumn الفهرس الذي يتم تحديد عموده.

{{< highlight csharp >}}

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
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
