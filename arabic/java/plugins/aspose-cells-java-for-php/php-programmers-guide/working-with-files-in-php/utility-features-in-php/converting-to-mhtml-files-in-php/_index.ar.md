---
title: تحويل إلى ملفات MHTML في PHP
type: docs
weight: 40
url: /ar/java/converting-to-mhtml-files-in-php/
---

## **Aspose.Cells - تحويل ملفات MHTML**
لتحويل ورقة العمل إلى ملف MHTML باستخدام رمز Aspose.Cells for Java في PHP، قم ببساطة باستدعاء طريقة worksheet_to_mhtml() من وحدة Converter.

**كود PHP**

{{< highlight php >}}

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
## **تحميل رمز التشغيل**
تحميل **تحويل ملفات MHTML (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
