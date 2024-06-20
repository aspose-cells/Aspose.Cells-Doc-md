---
title: تحويل ملفات Excel إلى HTML في PHP
type: docs
weight: 20
url: /ar/java/converting-excel-files-to-html-in-php/
---

## **Aspose.Cells - تحويل ملفات إكسل إلى HTML**
لتحويل Excel إلى HTML باستخدام Aspose.Cells for Java في PHP، ما عليك سوى استدعاء الأسلوب worksheet_to_html() من وحدة القوائم.

**كود PHP**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **تحويل ملفات إكسل إلى HTML (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
