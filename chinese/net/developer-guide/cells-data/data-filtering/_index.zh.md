---
title: 数据筛选
type: docs
weight: 85
url: /zh/net/data-filtering/
description: 学习如何通过 Aspose.Cells for .NET API 添加数据筛选。
keywords: 按颜色添加筛选器，添加日期筛选器，添加数字筛选器，添加动态筛选器，添加文本筛选器，添加包含的自定义筛选器，添加不包含的自定义筛选器，使用以开头的自定义筛选器，使用以结尾的自定义筛选器
---

{{% alert color="primary" %}}

Microsoft Excel 提供了一些很好的自动筛选工作表数据的功能。Aspose.Cells 完全支持 Microsoft Excel 的自动筛选功能。本文介绍了如何在 Microsoft Excel 中使用这些功能，以及如何使用 Aspose.Cells 对其进行编码。

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

### **Aspose.Cells 自动筛选**

Aspose.Cells提供了一个表示Excel文件的类Workbook。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。

工作表由Worksheet类表示。Worksheet类提供了广泛的属性和方法来管理工作表。要创建自动筛选，请使用Worksheet类的AutoFilter属性。AutoFilter属性是AutoFilter类的对象，该类提供了Range属性，用于指定构成标题行的单元格范围。自动筛选应用于构成标题行的单元格范围。

在每个工作表中，您只能指定一个筛选范围。这是由Microsoft Excel限制的。要进行自定义数据过滤，请使用AutoFilter.Custom方法。

在下面的示例中，我们使用 Aspose.Cells 创建了与上一节中使用 Microsoft Excel 创建的相同的自动筛选。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **不同类型的筛选**

Aspose.Cells 提供了多种选项，应用不同类型的筛选，如颜色筛选、日期筛选、数字筛选、文本筛选、空白筛选和非空白筛选。

##### **填充色**

Aspose.Cells 提供了 AddFillColorFilter 函数，用于根据单元格的填充颜色属性筛选数据。在下面的示例中，使用具有工作表第一列中不同填充颜色的模板文件来测试颜色筛选功能。示例文件可从以下链接下载。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **日期**

可实现不同类型的日期过滤，例如筛选所有包含 2018 年 1 月的日期的行。以下示例代码演示了如何使用 AddDateFilter 函数进行此筛选。示例文件如下。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **动态日期**

有时需要基于日期进行动态过滤，例如筛选所有在一月份的日期，而不考虑年份。在这种情况下，可以使用 DynamicFilter 函数，如以下示例代码所示。示例文件如下。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **数字**

可以使用 Aspose.Cells 应用自定义筛选，例如选择在给定范围内的数字的单元格。以下示例演示了使用 Custom() 函数筛选数字的用法。示例文件如下。

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **文本**

如果某一列包含文本，并且需要选择包含特定文本的单元格，可以使用 Filter() 函数。在以下示例中，模板文件包含国家列表，要选择包含特定国家名称的行。以下代码演示了文本过滤。示例文件如下。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **空白**

如果某一列包含文本，有一些单元格为空白，并且需要筛选出只包含空白单元格的行，则可以使用 MatchBlanks() 函数，如下所示。示例文件如下。

1. [空白.xlsx](72417324.xlsx)
1. [筛选空白.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **非空白**

当需要过滤带有任何文本的单元格时，可以使用 MatchNonBlanks 过滤函数，如下所示。示例文件如下。

1. [空白.xlsx](72417324.xlsx)
1. [筛选非空白.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **包含自定义筛选**

Excel 提供了自定义筛选功能，例如筛选包含特定字符串的行。Aspose.Cells 中也提供了此功能，并且通过下面的示例演示了对样本文件中的名称进行筛选。示例文件如下。

1. [源样本国家名称.xlsx](源样本国家名称.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **不包含特定字符串的自定义筛选**

Excel提供了自定义筛选功能，例如筛选不包含特定字符串的行。这一功能在Aspose.Cells中可用，并通过以下演示在示例文件中筛选名称。示例文件可从以下链接下载。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **以指定字符串开头的自定义筛选**

Excel提供了自定义筛选功能，例如筛选以特定字符串开头的行。这一功能在Aspose.Cells中可用，并通过以下演示在示例文件中筛选名称。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **以指定字符串结尾的自定义筛选**

Excel 提供了自定义筛选功能，例如筛选以特定字符串结尾的行。Aspose.Cells 中也提供了此功能，并且通过下面的示例演示了对下面给出的样本文件中的名称进行筛选。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **高级主题**
- [将 Microsoft Excel 的高级筛选应用于显示符合复杂条件的记录](/cells/zh/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [在刷新自动筛选后获取所有隐藏行索引](/cells/zh/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
