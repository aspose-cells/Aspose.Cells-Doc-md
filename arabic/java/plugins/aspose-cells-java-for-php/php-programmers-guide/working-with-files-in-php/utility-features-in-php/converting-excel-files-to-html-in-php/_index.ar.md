---
title: تحويل ملفات Excel إلى HTML في PHP
type: docs
weight: 20
url: /ar/java/converting-excel-files-to-html-in-php/
---
## **Aspose.Cells - تحويل ملفات Excel إلى HTML**
لتحويل Excel إلى HTML باستخدام Aspose.Cells for Java في PHP ، ما عليك سوى استدعاء ورقة العمل_إلى_html () طريقة وحدة المحول.

**كود PHP**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**تحويل ملفات Excel إلى HTML (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
