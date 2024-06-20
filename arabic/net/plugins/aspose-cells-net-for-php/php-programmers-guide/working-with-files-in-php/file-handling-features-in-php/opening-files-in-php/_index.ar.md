---
title: فتح الملفات في PHP
type: docs
weight: 10
url: /ar/net/opening-files-in-php/
---

## **Aspose.Cells - فتح ملفات Excel**
### **الفتح عبر المسار**
فقط قم بفتح ملف Microsoft Excel عن طريق الإشارة إلى مسار الملف

**كود PHP**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **تحميل رمز التشغيل**
تنزيل **فتح الملفات (Aspose.Cells)** من أي من المواقع الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
