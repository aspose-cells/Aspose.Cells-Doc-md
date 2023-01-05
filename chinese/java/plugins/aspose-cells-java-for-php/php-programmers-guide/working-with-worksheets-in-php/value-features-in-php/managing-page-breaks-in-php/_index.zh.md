---
title: 在 Php 中管理分页符
type: docs
weight: 20
url: /zh/java/managing-page-breaks-in-php/
---
## **Aspose.Cells - 管理分页符**
### **添加分页符**
添加分页符使用**Aspose.Cells Java for PHP**， 称呼**添加分页符**的方法**分页符**模块。您可以在下面看到代码示例。

**PHP代码**

{{< highlight "php" >}}

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
使用清除所有分页符**Aspose.Cells Java for PHP**， 称呼**clear_all_page_breaks**的方法**分页符**模块。您可以在下面看到代码示例。

**PHP代码**

{{< highlight "php" >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **删除特定分页符**
使用删除特定分页符**Aspose.Cells Java for PHP**， 称呼**删除分页符**的方法**分页符**模块。您可以在下面看到代码示例。

**PHP代码**

{{< highlight "php" >}}

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
下载**管理分页符 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
