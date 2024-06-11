---
title: 数据筛选
type: docs
weight: 85
url: /zh/python-net/data-filtering/
description: 通过使用Aspose.Cells for Python通过.NET API学习如何添加数据筛选。
keywords: Python Excel库，Python按颜色添加筛选，Python添加日期筛选，Python添加数字筛选，Python添加动态筛选，Python添加文本筛选，Python使用包含的自定义筛选，Python使用不包含的自定义筛选，Python使用以...开始的自定义筛选，Python使用以...结束的自定义筛选
---

{{% alert color="primary" %}}

Microsoft Excel提供了一些很好的功能来对工作表数据进行自动筛选。Aspose.Cells for Python通过.NET完全支持Microsoft Excel的自动筛选功能。本文说明了如何在Microsoft Excel中使用这些功能，并如何使用Aspose.Cells for Python通过.NET对其进行编码。

{{% /alert %}}

## **自动筛选数据**

自动筛选是选择仅显示列表中希望显示的那些项目的最快方式。 自动筛选功能允许用户根据一组标准对列表中的项目进行筛选。 根据文本、数字或日期进行筛选。

### **Microsoft Excel中的自动筛选**

要在Microsoft Excel中激活自动筛选功能：

1.在工作表中点击标题行。
1.从**数据**菜单中选择**筛选**，然后选择**自动筛选**。

当您在工作表上应用自动筛选时，筛选开关（黑色箭头）将显示在列标题右侧。

1.单击筛选箭头以查看筛选选项。

一些自动筛选选项包括：

|**选项**|**描述**|
| :- | :- |
|All|一次显示列表中的所有项目。|
|Custom|自定义过滤器标准，如包含/不包含|
|Filter by Color|基于填充颜色的筛选|
|Date Filters|根据不同的日期条件筛选行|
|Number Filters|不同类型的数字过滤，如比较，平均值和前10等|
|Text Filters|不同类型的过滤器，如以...开头，以...结束，包含等|
|Blanks/Non Blanks|这些过滤器可通过文本过滤器空白实现|

用户可以使用这些选项手动筛选他们在Microsoft Excel中的工作表数据。

### **使用Aspose.Cells for Python Excel库进行自动筛选**

Aspose.Cells for Python通过.NET提供了一个类Workbook，用于表示Excel文件。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。

工作表由Worksheet类表示。Worksheet类提供了一系列属性和方法来管理工作表。要创建自动筛选，请使用Worksheet类的AutoFilter属性。AutoFilter属性是AutoFilter类的对象，它提供了用于指定构成标题行的单元格范围的Range属性。自动筛选应用于标题行构成的单元格范围。

在每个工作表中，您只能指定一个筛选范围。这受到Microsoft Excel的限制。对于自定义数据筛选，请使用AutoFilter.Custom方法。

在下面给出的示例中，我们使用Aspose.Cells for Python通过.NET创建了与上一节中使用Microsoft Excel创建的相同的AutoFilter。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **不同类型的筛选**

Aspose.Cells for Python通过.NET提供多个选项来应用不同类型的筛选，如颜色筛选，日期筛选，数字筛选，文本筛选，空白筛选和非空白筛选。

##### **填充颜色**

Aspose.Cells for Python通过.NET提供了一个AddFillColorFilter函数，可根据单元格的填充颜色属性对数据进行筛选。在下面给出的示例中，使用包含工作表第一列中不同填充颜色的模板文件来测试颜色筛选功能。示例文件可从以下链接下载。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **日期**

可以实现不同类型的日期筛选，如筛选所有包含2018年1月日期的行。以下示例代码演示了使用AddDateFilter函数进行此筛选。示例文件如下所示。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **动态日期**

有时需要根据日期动态筛选，例如所有包含1月日期的单元格，而不管年份如何。在这种情况下，使用DynamicFilter函数，如下面示例代码所示。示例文件如下所示。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **数字**

可以使用Aspose.Cells for Python通过.NET应用自定义筛选，例如选择具有给定范围内数字的单元格。以下示例演示了如何使用Custom()函数来筛选数字。给出了示例文件。

1. [数字.xlsx](72417320.xlsx)
1. [过滤后的数字.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **文本**

如果一列包含文本，并且需要选择包含特定文本的单元格，则可以使用Filter()函数。在下面的示例中，模板文件包含国家列表，并且要选择包含特定国家名称的行。以下代码演示了过滤文本的方法。下面提供了示例文件。

1. [文本.xlsx](72417322.xlsx)
1. [过滤后的文本.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **空白**

如果一列包含文本，其中有一些单元格为空白，并且需要仅选择那些存在空白单元格的行，则可以使用MatchBlanks()函数，如下所示。下面提供了示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [过滤后的空白.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **非空白**

当需要过滤具有任何文本的单元格时，请使用MatchNonBlanks过滤函数，如下所示。下面提供了示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [过滤后的非空白.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **包含的自定义过滤器**

Excel提供了自定义筛选，如筛选包含特定字符串的行。这个功能在Aspose.Cells for Python通过.NET中是可用的，并通过过滤样本文件中的名称来进行下面的演示。给出了示例文件。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)
1. [输出源示例国家名称.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **不包含的自定义过滤器**

Excel提供了自定义筛选功能，如筛选不包含特定字符串的行。这个功能在Aspose.Cells for Python通过.NET中是可用的，并通过过滤下面给出的样本文件中的名称来进行演示。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **以某字符串开始的自定义过滤器**

Excel提供了自定义筛选功能，如筛选以特定字符串开始的行。这个功能在Aspose.Cells for Python通过.NET中是可用的，并通过过滤下面给出的样本文件中的名称来进行演示。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **以某字符串结束的自定义过滤器**

Excel提供了自定义筛选功能，如筛选以特定字符串结束的行。这个功能在Aspose.Cells for Python通过.NET中是可用的，并通过过滤下面给出的样本文件中的名称来进行演示。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **高级主题**
- [应用Microsoft Excel的高级筛选以显示满足复杂条件的记录](/cells/zh/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [刷新AutoFilter后获取所有隐藏行索引](/cells/zh/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
