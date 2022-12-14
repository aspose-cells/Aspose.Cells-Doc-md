---
title: تحويل ملفات Excel إلى ملفات PDF في PHP
type: docs
weight: 30
url: /ar/java/converting-excel-to-pdf-files-in-php/
---
## **Aspose.Cells - تحويل ملفات Excel إلى ملفات PDF**
لتحويل ملف Excel إلى Pdf باستخدام Aspose.Cells for Java في PHP ، ما عليك سوى استدعاء Excel_إلى_pdf () طريقة وحدة المحول.

**كود PHP**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
تحميل**تحويل ملفات Excel إلى ملفات PDF (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
