---
title: فتح الملفات في PHP
type: docs
weight: 10
url: /ar/net/opening-files-in-php/
---
## **Aspose.Cells - فتح ملفات Excel**
### **فتح من خلال المسار**
ما عليك سوى فتح ملف Microsoft Excel بالرجوع إلى مسار الملف

**كود PHP**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**فتح الملفات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
