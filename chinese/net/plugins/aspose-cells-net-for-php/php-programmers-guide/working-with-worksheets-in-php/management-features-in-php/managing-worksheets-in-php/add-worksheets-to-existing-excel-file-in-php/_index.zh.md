---
title: 在 PHP 中将工作表添加到现有的 Excel 文件
type: docs
weight: 10
url: /zh/net/add-worksheets-to-existing-excel-file-in-php/
---
将工作表添加到现有 Excel 文件

将工作表添加到现有 Excel 文件

**PHP代码**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $worksheet_index = $ptr->Call($worksheets,"Add_2",array());

        $worksheet = $ptr->Get($worksheets,"Item",array($worksheet_index));

        $ptr->Set($worksheet,"Name","My Worksheet",array());

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

        print "Completed." . PHP_EOL;

{{< /highlight >}}
## **下载运行代码**
下载**将工作表添加到现有 Excel 文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/AddWorksheetsToExistingExcelFile.php)
