---
title: 数据筛选
type: docs
weight: 85
url: /zh/python-net/data-filtering/
description: 学习如何使用Aspose.Cells for Python via .NET API添加数据筛选。
keywords: Python Excel库，Python按颜色添加筛选器，Python添加日期筛选，Python添加数字筛选器，Python添加动态筛选器，Python添加文本筛选器，Python使用包含添加自定义筛选器，Python使用不包含添加自定义筛选器，Python使用以...开头添加自定义筛选器，Python使用以...结尾添加自定义筛选器。
---

{{% alert color="primary" %}}

Microsoft Excel提供了自动筛选工作表数据的一些良好功能。Aspose.Cells for Python via .NET完全支持Microsoft Excel的自动筛选功能。本文解释了如何在Microsoft Excel中使用这些功能，以及如何使用Aspose.Cells for Python via .NET进行编码。

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

### **使用Aspose.Cells for Python Excel库进行自动筛选**

Aspose.Cells for Python via .NET提供的类Workbook代表Excel文件。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。

工作表由Worksheet类表示。Worksheet类提供了广泛的属性和方法来管理工作表。要创建自动筛选，请使用Worksheet类的AutoFilter属性。AutoFilter属性是AutoFilter类的对象，该类提供了Range属性，用于指定构成标题行的单元格范围。自动筛选应用于构成标题行的单元格范围。

在每个工作表中，您只能指定一个筛选范围。这是由Microsoft Excel限制的。要进行自定义数据过滤，请使用AutoFilter.Custom方法。

在下面的示例中，我们使用Aspose.Cells for Python via .NET创建了与上述在Microsoft Excel中创建的相同的自动筛选。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **不同类型的筛选**

Aspose.Cells for Python via .NET提供了多种选项来应用不同类型的筛选，如颜色筛选，日期筛选，数字筛选，文本筛选，空白筛选和非空白筛选。

##### **填充色**

Aspose.Cells for Python via .NET 提供了 AddFillColorFilter 功能，可以根据单元格的填充颜色属性来过滤数据。在下面给出的示例中，使用了一个模板文件，该文件的工作表的第一列具有不同的填充颜色，用于测试颜色过滤功能。示例文件可以从以下链接下载。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **日期**

可实现不同类型的日期过滤，例如筛选所有包含 2018 年 1 月的日期的行。以下示例代码演示了如何使用 AddDateFilter 函数进行此筛选。示例文件如下。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **动态日期**

有时需要基于日期进行动态过滤，例如筛选所有在一月份的日期，而不考虑年份。在这种情况下，可以使用 DynamicFilter 函数，如以下示例代码所示。示例文件如下。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **数字**

可使用 Aspose.Cells for Python via .NET 应用自定义过滤，比如选择介于给定范围内的数字的单元格。以下示例演示了使用 Custom() 函数筛选数字的用法。示例文件如下。

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **文本**

如果某一列包含文本，并且需要选择包含特定文本的单元格，可以使用 Filter() 函数。在以下示例中，模板文件包含国家列表，要选择包含特定国家名称的行。以下代码演示了文本过滤。示例文件如下。

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **空白**

如果某一列包含文本，有一些单元格为空白，并且需要筛选出只包含空白单元格的行，则可以使用 MatchBlanks() 函数，如下所示。示例文件如下。

1. [空白.xlsx](72417324.xlsx)
1. [筛选空白.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **非空白**

当需要过滤带有任何文本的单元格时，可以使用 MatchNonBlanks 过滤函数，如下所示。示例文件如下。

1. [空白.xlsx](72417324.xlsx)
1. [筛选非空白.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **包含自定义筛选**

Excel 提供了自定义过滤功能，可以筛选包含特定字符串的行。Aspose.Cells for Python via .NET 也提供了此功能，并通过示例文件中的名称进行了演示。示例文件如下。

1. [源样本国家名称.xlsx](源样本国家名称.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **不包含特定字符串的自定义筛选**

Excel 提供了自定义过滤功能，可以筛选不包含特定字符串的行。Aspose.Cells for Python via .NET 也提供了此功能，并通过示例文件中的名称进行了演示。示例文件如下。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **以指定字符串开头的自定义筛选**

Excel 提供了自定义过滤功能，可以筛选以特定字符串开头的行。Aspose.Cells for Python via .NET 也提供了此功能，并通过示例文件中的名称进行了演示。示例文件如下。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **以指定字符串结尾的自定义筛选**

Excel 提供了自定义过滤功能，可以筛选以特定字符串结尾的行。Aspose.Cells for Python via .NET 也提供了此功能，并通过示例文件中的名称进行了演示。示例文件如下。

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **高级主题**
- [将 Microsoft Excel 的高级筛选应用于显示符合复杂条件的记录](/cells/zh/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [在刷新自动筛选后获取所有隐藏行索引](/cells/zh/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
