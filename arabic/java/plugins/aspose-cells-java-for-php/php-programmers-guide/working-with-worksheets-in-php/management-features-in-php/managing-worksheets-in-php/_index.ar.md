---
title: إدارة أوراق العمل في Php
type: docs
weight: 10
url: /ar/java/managing-worksheets-in-php/
---
## **Aspose.Cells - إدارة أوراق العمل**
### **إضافة أوراق عمل إلى ملف Excel جديد**
لإضافة ورقة عمل إلى ملف Excel جديد باستخدام**Aspose.Cells Java لـ PHP** ، ببساطة اتصل**add_worksheet** طريقة**أوراق العمل** وحدة.

**كود PHP**

{{< highlight "php" >}}

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
### **إزالة أوراق العمل باستخدام اسم الورقة**
 لإزالة ورقة العمل حسب اسم الورقة باستخدام**Aspose.Cells Java لـ PHP** ، ببساطة اتصل**remove_worksheet_by_name** طريقة**أوراق العمل** وحدة.

**كود PHP**

{{< highlight "php" >}}

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
### **إزالة أوراق العمل باستخدام فهرس الورقة**
 لإزالة ورقة العمل عن طريق فهرس الورقة باستخدام**Aspose.Cells Java لـ PHP** ، ببساطة اتصل**remove_worksheet_by_index** طريقة**أوراق العمل** وحدة.

**كود PHP**

{{< highlight "php" >}}

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
## **قم بتنزيل كود التشغيل**
تحميل**إدارة أوراق العمل (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
