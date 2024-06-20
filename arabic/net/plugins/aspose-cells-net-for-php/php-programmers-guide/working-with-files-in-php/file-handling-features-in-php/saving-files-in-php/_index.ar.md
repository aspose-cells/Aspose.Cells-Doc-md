---
title: حفظ الملفات في PHP
type: docs
weight: 20
url: /ar/net/saving-files-in-php/
---

## **Aspose.Cells - حفظ ملفات الإكسل**
### **الفتح عبر المسار**
حفظ ملف Excel لمايكروسوفت عن طريق الإشارة إلى مسار الملف

**كود PHP**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array());

        //Your Code goes here for any workbook related operations

        $ptr->Call($workbook,"Save",array($dataDir.'/book1.xls'));

        print "File saved successfully!" . PHP_EOL;

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **حفظ الملفات (Aspose.Cells)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
