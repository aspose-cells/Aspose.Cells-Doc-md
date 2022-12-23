---
title: فتح الملفات في PHP
type: docs
weight: 10
url: /ar/java/opening-files-in-php/
---
## **Aspose.Cells - طرق بسيطة لفتح ملفات Excel**
### **فتح طريق**
ما عليك سوى فتح ملف Microsoft Excel بالرجوع إلى مسار الملف

**كود PHP**

{{< highlight "ruby" >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **فتح من خلال تيار**
في بعض الأحيان ، يتم تخزين ملف Excel الذي تريد فتحه كتدفق. في هذه الحالة ، استخدم إصدارًا محملاً بشكل زائد من الأسلوب Open الذي يأخذ كائن Stream الذي يحتوي على ملف Excel لفتح الملف.

**كود PHP**

{{< highlight "ruby" >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**فتح الملفات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
