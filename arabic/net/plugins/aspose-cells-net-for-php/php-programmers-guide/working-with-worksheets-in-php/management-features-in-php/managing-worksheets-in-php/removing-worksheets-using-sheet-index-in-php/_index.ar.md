---
title: إزالة أوراق العمل باستخدام فهرس الورقة في البي إتش بي
type: docs
weight: 30
url: /ar/net/removing-worksheets-using-sheet-index-in-php/
---

## **إزالة أوراق العمل باستخدام فهرس الورقة**
إزالة أوراق العمل باستخدام فهرس الورقة

**كود PHP**

{{< highlight php >}}

         $dataDir = '';

        / Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $ptr->Call($worksheets,"RemoveAt",array(0));

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **إزالة الأوراق باستخدام مؤشر الورقة (Aspose.Cells)** من أي من المواقع الاجتماعية البرمجية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetIndex.php)
