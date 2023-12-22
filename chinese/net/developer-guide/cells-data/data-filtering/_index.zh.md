---
title: 数据过滤
type: docs
weight: 85
url: /zh/net/data-filtering/
description: 了解如何使用 Aspose.Cells for .NET API 添加数据过滤器。
keywords: Add Filter by Color, Add Date Filters, Add Number Filters, Add Dynamic Filter, Add Text Filters, Add custom filter with Contains, Add custom filter with NotContains, Add custom filter with BeginsWith, Add custom filter with EndsWith
---
{{% alert color="primary" %}}

Microsoft Excel 提供了一些很好的功能来自动筛选工作表数据。 Aspose.Cells 完全支持Microsoft Excel 的自动筛选功能。本文介绍了如何使用 Microsoft Excel 中的功能，以及如何使用 Aspose.Cells 对其进行编码。

{{% /alert %}}

##  **自动过滤数据**

自动筛选是从工作表中仅选择要在列表中显示的项目的最快方法。自动过滤功能允许用户根据设定的条件过滤列表中的项目。根据文本、数字或日期进行过滤。

###  **Microsoft Excel 中的自动筛选**

要激活 Microsoft Excel 中的自动筛选功能：

1. 单击工作表中的标题行。
1. 来自**数据**菜单，选择**筛选**然后*自动过滤**。

当您将自动筛选器应用于工作表时，筛选器开关（黑色箭头）将出现在列标题的右侧。

1. 单击过滤器箭头可查看过滤器选项列表。

一些自动过滤器选项是：

|**选项**|**描述**|
| :- | :- |
|全部|显示列表中的所有项目一次。|
|风俗|自定义过滤条件，例如包含/不包含|
|按颜色过滤|基于填充颜色的过滤器|
|日期过滤器|根据日期的不同条件过滤行|
|数字过滤器|不同类型的数字过滤器，如比较、平均值和前 10 名等。|
|文本过滤器|不同的过滤器，如开头、结尾、包含等，|
|空白/非空白|这些过滤器可以通过 Text Filter Blank 来实现|

用户使用这些选项在 Microsoft Excel 中手动筛选工作表数据。

###  **自动过滤器 Aspose.Cells**

Aspose.Cells提供了一个代表Excel文件的类Workbook。 Workbook 类包含一个 Worksheets 集合，允许访问 Excel 文件中的每个工作表。

工作表由 Worksheet 类表示。 Worksheet 类提供了多种属性和方法来管理工作表。要创建自动筛选器，请使用 Worksheet 类的 AutoFilter 属性。 AutoFilter 属性是 AutoFilter 类的一个对象，它提供 Range 属性来指定组成标题行的单元格范围。自动筛选器应用于作为标题行的单元格范围。

在每个工作表中，您只能指定一个筛选范围。这受到 Microsoft Excel 的限制。对于自定义数据过滤，请使用 AutoFilter.Custom 方法。

在下面给出的示例中，我们使用 Aspose.Cells 创建了与上一节中使用 Microsoft Excel 创建的相同的自动筛选器。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

####  **不同类型的过滤器**

Aspose.Cells 提供了多个选项来应用不同类型的过滤器，如颜色过滤器、日期过滤器、数字过滤器、文本过滤器、空白过滤器和无空白过滤器。

#####  **填色**

Aspose.Cells提供了一个函数AddFillColorFilter来根据单元格的填充颜色属性过滤数据。在下面给出的示例中，使用工作表第一列中具有不同填充颜色的模板文件来测试颜色过滤功能。可以从以下链接下载示例文件。

1. [彩色细胞.xlsx](72417315.xlsx)
1. [过滤彩色细胞.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

#####  **日期**

可以实现不同类型的日期过滤器，例如过滤具有 2018 年 1 月日期的所有行。以下示例代码使用 AddDateFilter 函数演示了此过滤器。下面给出了示例文件。

1. [日期.xlsx](72417317.xlsx)
1. [过滤日期.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

#####  **动态日期**

有时需要基于日期的动态过滤器，例如所有单元格的日期都在一月份，无论年份如何。在这种情况下，将使用 DynamicFilter 函数，如以下示例代码所示。下面给出了示例文件。

1. [日期.xlsx](72417317.xlsx)
1. [过滤动态日期.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

#####  **数字**

可以使用 Aspose.Cells 应用自定义过滤器，例如选择具有给定范围之间的数字的单元格。以下示例演示了如何使用 Custom() 函数来过滤数字。下面给出了示例文件。

1. [编号.xlsx](72417320.xlsx)
1. [过滤数.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

#####  **文本**

如果列包含文本并且要选择包含特定文本的单元格，则可以使用 Filter() 函数。在以下示例中，模板文件包含国家/地区列表，并且要选择包含特定国家/地区名称的行。以下代码演示了过滤文本。下面给出了示例文件。

1. [文本.xlsx](72417322.xlsx)
1. [过滤文本.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

#####  **毛坯**

如果列中包含的文本很少有空白单元格，并且需要筛选来仅选择存在空白单元格的行，则可以使用 MatchBlanks() 函数，如下所示。下面给出了示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [过滤空白.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

#####  **非空白**

当要过滤包含任何文本的单元格时，请使用 MatchNonBlanks 过滤功能，如下所示。下面给出了示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [过滤非空白.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

#####  **自定义过滤器包含**

Excel 提供了自定义过滤器，例如包含某些特定字符串的过滤器行。此功能在 Aspose.Cells 中可用，并在下面通过过滤示例文件中的名称进行演示。下面给出了示例文件。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

#####  **使用 NotContains 自定义过滤器**

Excel 提供了自定义过滤器，例如过滤不包含某些特定字符串的行。此功能在 Aspose.Cells 中可用，并通过过滤下面给出的示例文件中的名称进行了演示。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

#####  **使用 BeginsWith 自定义过滤器**

Excel 提供了自定义过滤器，例如以某些特定字符串开头的过滤器行。此功能在 Aspose.Cells 中可用，并通过过滤下面给出的示例文件中的名称进行了演示。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

#####  **带有 EndsWith 的自定义过滤器**

Excel 提供了自定义过滤器，例如以某些特定字符串结尾的过滤器行。此功能在 Aspose.Cells 中可用，并通过过滤下面给出的示例文件中的名称进行了演示。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

##  **高级主题**
- [应用 Microsoft Excel 的高级筛选器显示满足复杂条件的记录](/cells/zh/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [刷新自动筛选后获取所有隐藏行索引](/cells/zh/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
