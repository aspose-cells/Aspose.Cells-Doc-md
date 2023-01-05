---
title: Php 中的分页预览
type: docs
weight: 60
url: /zh/java/page-break-preview-in-php/
---
## **Aspose.Cells - 分页预览**
将工作表设置为分页预览使用**Aspose.Cells Java for PHP** 只需调用**分页预览**模块。

**PHP代码**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Displaying the worksheet in page break preview

$worksheet->setPageBreakPreview(true);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **下载运行代码**
下载**分页预览 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
