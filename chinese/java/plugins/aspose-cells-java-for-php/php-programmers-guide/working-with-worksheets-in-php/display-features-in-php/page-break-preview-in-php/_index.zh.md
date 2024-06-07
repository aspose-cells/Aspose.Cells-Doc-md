---
title: 在Php中分页预览
type: docs
weight: 60
url: /zh/java/page-break-preview-in-php/
---

## **Aspose.Cells - 分页预览**
要使用**Aspose.Cells Java for PHP**设置工作表以分页预览，简单调用**PageBreakPreview**模块。

**PHP代码**

{{< highlight php >}}

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
从下面列出的任何社交编码站点下载**页面分隔预览（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
