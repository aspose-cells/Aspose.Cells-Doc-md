---
title: التحويل إلى ملفات MHTML في PHP
type: docs
weight: 40
url: /ar/java/converting-to-mhtml-files-in-php/
---
## **Aspose.Cells - التحويل إلى ملفات MHTML**
لتحويل ورقة العمل إلى ملف MHTML باستخدام Aspose.Cells for Java في PHP ، ما عليك سوى استدعاء ورقة العمل_إلى_mhtml () طريقة وحدة المحول.

**كود PHP**

{{< highlight "php" >}}

 $sveFormat = new SaveFormat();

//Specify the file path

$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options

$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file

$wb = new Workbook($filePath);

//Save the MHT file

$wb->save($filePath . ".out.mht", $sv);

{{< /highlight >}}
## **تحميل كود الجري**
تحميل**التحويل إلى ملفات MHTML (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
