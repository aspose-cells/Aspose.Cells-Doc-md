---
title: إزالة أوراق العمل باستخدام اسم الورقة في PHP
type: docs
weight: 40
url: /ar/net/removing-worksheets-using-sheet-name-in-php/
---
## **إزالة أوراق العمل باستخدام اسم الورقة**
إزالة أوراق العمل باستخدام اسم الورقة

**كود PHP**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $ptr->Call($worksheets,"RemoveAt_2",array("Sheet1"));

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

        print "Completed." . PHP_EOL;

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**إزالة أوراق العمل باستخدام اسم الورقة (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetName.php)
