---
title: 数据筛选
type: docs
weight: 60
url: /zh/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel 提供了一些很好的自动筛选工作表数据的功能。Aspose.Cells 完全支持 Microsoft Excel 的自动筛选功能。本文介绍了如何在 Microsoft Excel 中使用这些功能，以及如何使用 Aspose.Cells 对其进行编码。

{{% /alert %}}

## **自动筛选数据**

自动筛选是选择仅显示列表中您想要显示的项的最快方法。自动筛选功能允许用户根据一组标准过滤列表中的项目。根据文本、数字或日期进行筛选。

### **Microsoft Excel 中的自动筛选**

要在 Microsoft Excel 中启用自动筛选功能：

1. 单击工作表中的标题行。
1. 从“数据”菜单中，选择“筛选”，然后选择“自动筛选”。

在工作表上应用自动筛选时，过滤开关 (黑色箭头) 会出现在列标题右侧。

1. 单击筛选箭头，以查看筛选选项列表。

一些自动筛选选项包括：

|**选项**|**描述**|
| :- | :- |
|All|在列表中显示所有项目一次。
|Custom|自定义包含/不包含等筛选条件
|Filter by Color|基于填充颜色的筛选
|Date Filters|基于不同日期标准的行筛选
|Number Filters|数字类型的不同筛选，如比较、平均值和前 10 等。
|Text Filters|不同的筛选，如以...开始、以...结束、包含等。
|Blanks/Non Blanks|这些筛选可以通过文本筛选空白值实现。
用户可以使用这些选项手动筛选其 Microsoft Excel 工作表中的数据。

### **Aspose.Cells 自动筛选**

Aspose.Cells 提供了一个代表 Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问 Excel 文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要创建自动筛选，使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)属性。[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)属性是[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) 类的对象，为指定组成标题行的单元格范围提供了[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)属性。自动筛选应用于组成标题行的单元格范围。

在每个工作表中，您只能指定一个筛选范围。这受到Microsoft Excel的限制。对于自定义数据筛选，使用[**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-)方法。

在下面的示例中，我们使用 Aspose.Cells 创建了与上一节中使用 Microsoft Excel 创建的相同的自动筛选。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **不同类型的筛选**

Aspose.Cells 提供了多种选项，应用不同类型的筛选，如颜色筛选、日期筛选、数字筛选、文本筛选、空白筛选和非空白筛选。

##### **填充色**

Aspose.Cells提供了一个函数[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter-int-int-com.aspose.cells.CellsColor-com.aspose.cells.CellsColor-)，根据单元格的填充颜色属性对数据进行筛选。在下面给出的示例中，使用具有表格第一列中不同填充颜色的模板文件来测试颜色筛选功能。可以下载以下文件来检查功能。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **日期**

可以实现不同类型的日期过滤，比如过滤所有包含2018年1月日期的行。以下示例代码演示了使用[**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter-int-int-int-int-int-int-int-int-)函数来实现此过滤。以下文件可用于测试此功能。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **动态日期**

有时需要基于日期的动态过滤，例如筛选出所有包含一月日期的单元格，不考虑年份。在这种情况下，可以使用[**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter-int-int-)函数，如下示例代码中所示。以下文件可用于测试。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **数字**

可以使用Aspose.Cells应用自定义过滤，比如选择数值在给定范围之间的单元格。以下示例演示了使用[**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-)函数来过滤数字的用法。示例文件可从以下链接下载。

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **文本**

如果某列包含文本并且需要选择包含特定文本的单元格，可以使用[**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter-int-java.lang.String-)函数。在下面的示例中，模板文件包含一组国家，需要选择包含特定国家名称的行。以下代码演示了使用以下示例文件来过滤文本。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **空白**

如果某列包含文本，有一些单元格为空白，并且需要只选择存在空白单元格的行，可以使用[**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks-int-)函数，如下所示。可以从以下链接下载示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [筛选空白.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **非空白**

当需要过滤包含任何文本的单元格时，可以使用以下演示以下[**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks-int-)过滤函数。可以从以下链接下载示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [筛选非空白.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **包含自定义筛选**

Excel提供了自定义筛选功能，例如筛选包含特定字符串的行。这一功能在Aspose.Cells中可用，并通过以下演示在示例文件中筛选名称。示例文件可从以下链接下载。

1. [源样本国家名称.xlsx](源样本国家名称.xlsx)
1. [输出源样本国家名称.xlsx](输出源样本国家名称.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **不包含特定字符串的自定义筛选**

Excel提供了自定义筛选功能，例如筛选不包含特定字符串的行。这一功能在Aspose.Cells中可用，并通过以下演示在示例文件中筛选名称。示例文件可从以下链接下载。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **以指定字符串开头的自定义筛选**

Excel提供了自定义筛选功能，例如筛选以特定字符串开头的行。这一功能在Aspose.Cells中可用，并通过以下演示在示例文件中筛选名称。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **以指定字符串结尾的自定义筛选**

Excel提供了自定义筛选功能，例如筛选以特定字符串结尾的行。这一功能在Aspose.Cells中可用，并通过以下演示在示例文件中筛选名称。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **高级主题**
- [将 Microsoft Excel 的高级筛选应用于显示符合复杂条件的记录](/cells/zh/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [在刷新自动筛选后获取所有隐藏行索引](/cells/zh/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

{{< app/cells/assistant language="java" >}}
