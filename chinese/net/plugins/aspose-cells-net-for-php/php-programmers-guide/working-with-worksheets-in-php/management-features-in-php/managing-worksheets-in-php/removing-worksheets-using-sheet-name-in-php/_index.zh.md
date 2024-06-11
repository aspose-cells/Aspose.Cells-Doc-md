---
title: 在 PHP 中使用工作表名称移除工作表
type: docs
weight: 40
url: /zh/net/removing-worksheets-using-sheet-name-in-php/
---

## **使用工作表名称移除工作表**
使用工作表名称移除工作表

**PHP 代码**

{{< highlight php >}}

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
## **下载运行代码**
从以下任一社交编程网站下载 **使用工作表名称移除工作表 (Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetName.php)
