---
title: تحويل Excel إلى ملفات PDF في PHP
type: docs
weight: 30
url: /ar/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - تحويل إكسل إلى ملفات PDF**
لتحويل Excel إلى ملف Pdf باستخدام Aspose.Cells for Java في PHP، ما عليك سوى استدعاء الأسلوب excel_to_pdf() من وحدة القوائم.

**كود PHP**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **تحويل إكسل إلى ملفات PDF (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
