---
title: إدارة أوراق العمل في PHP
type: docs
weight: 10
url: /ar/java/managing-worksheets-in-php/
---

## **Aspose.Cells - إدارة ورق العمل**
### **إضافة ورقات العمل إلى ملف Excel جديد**
لإضافة صفحة عمل إلى ملف إكسل جديد باستخدام **Aspose.Cells Java for PHP**، ما عليك سوى استدعاء طريقة **add_worksheet** من وحدة **MangingWorksheets**.

**كود PHP**

{{< highlight php >}}

 //Instantiating a Workbook object

$workbook = new Workbook();

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$sheetIndex = $worksheets->add();

$worksheet = $worksheets->get($sheetIndex);

//Setting the name of the newly added worksheet

$worksheet->setName("My Worksheet");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
### **إزالة الأوراق العمل باستخدام اسم الورقة**
لإزالة الصفحة عن طريق اسم الورقة باستخدام **Aspose.Cells Java for PHP**، ما عليك سوى استدعاء طريقة **remove_worksheet_by_name** من وحدة **MangingWorksheets**.

**كود PHP**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet name

$workbook->getWorksheets()->removeAt("Sheet1");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
### **إزالة الأوراق العمل باستخدام فهرس الورقة**
لإزالة الصفحة عن طريق فهرس الصفحة باستخدام **Aspose.Cells Java for PHP**، ما عليك سوى استدعاء طريقة **remove_worksheet_by_index** من وحدة **MangingWorksheets**.

**كود PHP**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream=new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet index

$workbook->getWorksheets()->removeAt(0);

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
## **تحميل رمز التشغيل**
قم بتنزيل  **إدارة الورقة (Aspose.Cells)**  من أي من مواقع التعاون البرمجي الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
