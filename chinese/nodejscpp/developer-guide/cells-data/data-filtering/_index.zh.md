---
title: 数据筛选
type: docs
weight: 85
url: /zh/nodejs-cpp/data-filtering/
description: 学习如何使用Aspose.Cells for Node.js via C++ API添加数据筛选。
keywords: 通过C++在Node.js中添加颜色筛选，在Node.js中添加日期筛选，在Node.js中添加数字筛选，在Node.js中添加动态筛选，在Node.js中添加文本筛选，通过C++在Node.js中添加包含筛选，通过C++在Node.js中添加不包含筛选，通过C++在Node.js中添加以某字母开头的筛选，通过C++在Node.js中添加以某字母结尾的筛选
---

{{% alert color="primary" %}}
微软Excel提供一些很好的自动筛选功能。Aspose.Cells完全支持微软Excel的自动筛选功能。本文解释如何在微软Excel中使用这些功能，以及如何使用Aspose.Cells for Node.js via C++编写代码实现这些功能。
{{% /alert %}}

## **自动筛选数据**

自动筛选是选择仅显示列表中您想要显示的项的最快方法。自动筛选功能允许用户根据一组标准过滤列表中的项目。根据文本、数字或日期进行筛选。

### **Microsoft Excel 中的自动筛选**

要在 Microsoft Excel 中启用自动筛选功能：

1. 单击工作表中的标题行。
1. 从**数据**菜单中选择**筛选**，然后选择**自动筛选**。

在工作表上应用自动筛选时，过滤开关 (黑色箭头) 会出现在列标题右侧。

1. 单击筛选箭头，以查看筛选选项列表。

一些自动筛选选项包括：

|**选项**|**描述**|
| :- | :- |
|All|在列表中显示所有项目一次。
|Custom|自定义包含/不包含等筛选条件
|Filter by Color|基于填充颜色的筛选
|Date Filters|基于不同日期标准的行筛选
|Number Filters|在数字上应用不同类型的筛选，例如比较，平均值和前10名等。
|Text Filters|不同的筛选，如以...开始、以...结束、包含等。
|Blanks/Non Blanks|这些筛选可以通过文本筛选空白值实现。

用户可以使用这些选项手动筛选其 Microsoft Excel 工作表中的数据。

### **使用Aspose.Cells for Node.js via C++的自动筛选**

Aspose.Cells提供了一个表示Excel文件的类Workbook。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。

工作表由Worksheet类表示。Worksheet类提供了广泛的属性和方法来管理工作表。要创建自动筛选，请使用Worksheet类的AutoFilter属性。AutoFilter属性是AutoFilter类的对象，该类提供了Range属性，用于指定构成标题行的单元格范围。自动筛选应用于构成标题行的单元格范围。

在每个工作表中，您只能指定一个筛选范围。这是由Microsoft Excel限制的。要进行自定义数据过滤，请使用AutoFilter.Custom方法。

下例中，我们使用Aspose.Cells for Node.js via C++创建了与上文微软Excel中相同的自动筛选。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter.js" >}}

#### **不同类型的筛选**

Aspose.Cells 提供了多种选项，应用不同类型的筛选，如颜色筛选、日期筛选、数字筛选、文本筛选、空白筛选和非空白筛选。

##### **填充色**

Aspose.Cells 提供了 AddFillColorFilter 函数，用于根据单元格的填充颜色属性筛选数据。在下面的示例中，使用具有工作表第一列中不同填充颜色的模板文件来测试颜色筛选功能。示例文件可从以下链接下载。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FillColor.js" >}}


##### **日期**

可以实现不同类型的日期筛选，例如筛选所有2018年1月的日期。以下示例代码演示了如何使用AddDateFilter函数完成此筛选。提供的样例文件如下。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Date.js" >}}


##### **动态日期**

有时需要基于日期进行动态过滤，例如筛选所有在一月份的日期，而不考虑年份。在这种情况下，可以使用 DynamicFilter 函数，如以下示例代码所示。示例文件如下。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-DynamicFilter.js" >}}


##### **数字**

可以使用 Aspose.Cells 应用自定义筛选，例如选择在给定范围内的数字的单元格。以下示例演示了使用 Custom() 函数筛选数字的用法。示例文件如下。

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Number.js" >}}


##### **文本**

如果某列包含文本，且欲筛选包含特定文本的单元格，可以使用Filter()函数。以下示例中，模板文件包含国家名单，要筛选包含某个国家名的行。以下代码演示文本筛选。样例文件如下。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Text.js" >}}


##### **空白**

如果某一列包含文本，有一些单元格为空白，并且需要筛选出只包含空白单元格的行，则可以使用 MatchBlanks() 函数，如下所示。示例文件如下。

1. [空白.xlsx](72417324.xlsx)
1. [筛选空白.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Blanks.js" >}}


##### **非空白**

当需要过滤带有任何文本的单元格时，可以使用 MatchNonBlanks 过滤函数，如下所示。示例文件如下。

1. [空白.xlsx](72417324.xlsx)
1. [筛选非空白.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-NonBlanks.js" >}}


##### **包含自定义筛选**

Excel 提供了自定义筛选功能，例如筛选包含特定字符串的行。Aspose.Cells 中也提供了此功能，并且通过下面的示例演示了对样本文件中的名称进行筛选。示例文件如下。

1. [源样本国家名称.xlsx](源样本国家名称.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-Contains.js" >}}


##### **不包含特定字符串的自定义筛选**

Excel提供自定义筛选，例如筛选不包含某些特定字符串的行。此功能在Aspose.Cells中可用，以下示例通过筛选样本中的姓名演示。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-NotContains.js" >}}


##### **以指定字符串开头的自定义筛选**

Excel还提供以某些字符串开头的自定义筛选。此功能在Aspose.Cells中可用，以下示例通过筛选样本中的姓名进行演示。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-BeginsWith.js" >}}


##### **以指定字符串结尾的自定义筛选**

Excel提供了自定义筛选功能，例如筛选以特定字符串结尾的行。这一功能在Aspose.Cells中可用，并通过以下演示在示例文件中筛选名称。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-EndsWith.js" >}}


## **高级主题**
- [将 Microsoft Excel 的高级筛选应用于显示符合复杂条件的记录](/cells/zh/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [在刷新自动筛选后获取所有隐藏行索引](/cells/zh/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="nodejs-cpp" >}}
