---
title: فتح الملفات في PHP
type: docs
weight: 10
url: /ar/java/opening-files-in-php/
---

## **Aspose.Cells - طرق بسيطة لفتح ملفات إكسل**
### **الفتح عبر المسار**
فقط قم بفتح ملف Microsoft Excel عن طريق الإشارة إلى مسار الملف

**كود PHP**

{{< highlight ruby >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **الفتح عبر التيار**
في بعض الأحيان، يتم تخزين ملف إكسل الذي ترغب في فتحه كتيار. في هذه الحالة، استخدم الإصدار المحمل من طريقة الفتح التي تأخذ كائن التيار الذي يحتوي على ملف إكسل لفتح الملف.

**كود PHP**

{{< highlight ruby >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **فتح الملفات (Aspose.Cells)** من أي من المواقع الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
