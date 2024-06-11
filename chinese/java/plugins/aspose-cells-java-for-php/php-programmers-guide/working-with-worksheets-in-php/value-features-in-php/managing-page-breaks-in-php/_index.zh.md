---
title: 在Php中管理分页符
type: docs
weight: 20
url: /zh/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - 管理分页符**
### **添加分页**
要使用**Aspose.Cells Java for PHP**添加分页符，请调用**pagebreaks**模块的**add_page_breaks**方法。下面是代码示例。

**PHP 代码**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **清除所有分页符**
要使用**Aspose.Cells Java for PHP**清除所有分页符，请调用**pagebreaks**模块的**clear_all_page_breaks**方法。下面是代码示例。

**PHP 代码**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **移除特定分页符**
要使用**Aspose.Cells Java for PHP**移除特定的分页符，请调用**pagebreaks** 模块的 **remove_page_break** 方法。以下是代码示例。

**PHP 代码**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编程网站下载**管理分页符（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
