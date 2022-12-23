---
title: حفظ الملفات في PHP
type: docs
weight: 20
url: /ar/java/saving-files-in-php/
---
## **Aspose.Cells - حفظ الملفات**
### **حفظ الملف في بعض المواقع**
 إذا احتاج المطورون إلى حفظ ملفاتهم باستخدام**Aspose.Cells Java for PHP** إلى بعض مواقع التخزين ، يمكنهم ببساطة تحديد اسم الملف (بمسار التخزين الكامل) وتنسيق الملف المطلوب (باستخدام امتداد**نوع الملف**تعداد) أثناء استدعاء**حفظ**طريقة**دفتر العمل**موضوع.

**كود PHP**

{{< highlight "php" >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**حفظ الملفات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
