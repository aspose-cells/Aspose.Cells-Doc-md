---
title: إضافة أوراق العمل إلى ملف إكسل جديد باستخدام البي إتش بي
type: docs
weight: 20
url: /ar/net/add-worksheets-to-new-excel-file-in-php/
---

## **إضافة أوراق العمل إلى ملف إكسل جديد**
إضافة أوراق العمل إلى ملف إكسل جديد

**كود PHP**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array());

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $worksheet_index = $ptr->Call($worksheets,"Add_2",array());

        $worksheet = $ptr->Get($worksheets,"Item",array($worksheet_index));

        $ptr->Set($worksheet,"Name","My Worksheet",array());

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

        print "Completed." . PHP_EOL;

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **إضافة أوراق العمل إلى ملف إكسل جديد (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/AddingWorksheetsToNewExcelFile.php)
