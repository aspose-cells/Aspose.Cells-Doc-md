---
title: 数据筛选
type: docs
weight: 85
url: /zh/net/data-filtering/
description: 通过使用Aspose.Cells for .NET API学习如何添加数据筛选。
keywords: 通过颜色添加筛选、添加日期筛选、添加数字筛选、添加动态筛选、添加文本筛选、使用包含添加自定义筛选、使用不包含添加自定义筛选、使用以...开头添加自定义筛选、使用以...结束添加自定义筛选
---

{{% alert color="primary" %}}

Microsoft Excel提供了一些不错的功能来自动筛选工作表数据。 Aspose.Cells完全支持Microsoft Excel的自动筛选功能。 本文解释了如何在Microsoft Excel中使用这些功能以及如何使用Aspose.Cells对其进行编码。

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

### **Aspose.Cells的自动筛选**

Aspose.Cells提供了一个类，Workbook代表一个Excel文件。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。

工作表由Worksheet类表示。Worksheet类提供了一系列属性和方法来管理工作表。要创建自动筛选，请使用Worksheet类的AutoFilter属性。AutoFilter属性是AutoFilter类的对象，它提供了用于指定构成标题行的单元格范围的Range属性。自动筛选应用于标题行构成的单元格范围。

在每个工作表中，您只能指定一个筛选范围。这受到Microsoft Excel的限制。对于自定义数据筛选，请使用AutoFilter.Custom方法。

在下面的示例中，我们使用Aspose.Cells创建了与上一节中使用Microsoft Excel创建的相同的AutoFilter筛选。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **不同类型的筛选**

Aspose.Cells提供了多种选项来应用不同类型的筛选，如颜色筛选、日期筛选、数字筛选、文本筛选、空白筛选和非空白筛选。

##### **填充颜色**

Aspose.Cells提供了一个AddFillColorFilter函数，根据单元格的填充颜色属性对数据进行筛选。在下面给出的示例中，使用表格文件中的第一列中的不同填充颜色来测试颜色筛选功能。示例文件可以从以下链接下载。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **日期**

可以实现不同类型的日期筛选，如筛选所有包含2018年1月日期的行。以下示例代码演示了使用AddDateFilter函数进行此筛选。示例文件如下所示。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **动态日期**

有时需要根据日期动态筛选，例如所有包含1月日期的单元格，而不管年份如何。在这种情况下，使用DynamicFilter函数，如下面示例代码所示。示例文件如下所示。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **数字**

使用Aspose.Cells可以应用自定义过滤器，例如选择在给定范围内具有数字的单元格。以下示例演示了使用Custom()函数过滤数字的用法。下面提供了示例文件。

1. [数字.xlsx](72417320.xlsx)
1. [过滤后的数字.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **文本**

如果一列包含文本，并且需要选择包含特定文本的单元格，则可以使用Filter()函数。在下面的示例中，模板文件包含国家列表，并且要选择包含特定国家名称的行。以下代码演示了过滤文本的方法。下面提供了示例文件。

1. [文本.xlsx](72417322.xlsx)
1. [过滤后的文本.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **空白**

如果一列包含文本，其中有一些单元格为空白，并且需要仅选择那些存在空白单元格的行，则可以使用MatchBlanks()函数，如下所示。下面提供了示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [过滤后的空白.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **非空白**

当需要过滤具有任何文本的单元格时，请使用MatchNonBlanks过滤函数，如下所示。下面提供了示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [过滤后的非空白.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **包含的自定义过滤器**

Excel提供了自定义过滤器，例如过滤包含某个特定字符串的行。Aspose.Cells中提供此功能，并通过下面演示了在示例文件中过滤名称。下面提供了示例文件。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)
1. [输出源示例国家名称.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **不包含的自定义过滤器**

Excel提供了自定义过滤器，例如过滤不包含某个特定字符串的行。Aspose.Cells中提供此功能，并通过下面演示了在示例文件中过滤名称。下面提供了示例文件。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **以某字符串开始的自定义过滤器**

Excel提供了自定义过滤器，例如过滤以某个特定字符串开始的行。Aspose.Cells中提供此功能，并通过下面演示了在示例文件中过滤名称。下面提供了示例文件。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **以某字符串结束的自定义过滤器**

Excel提供了自定义过滤器，例如过滤以某个特定字符串结尾的行。Aspose.Cells中提供此功能，并通过下面演示了在示例文件中过滤名称。下面提供了示例文件。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **高级主题**
- [应用Microsoft Excel的高级筛选以显示满足复杂条件的记录](/cells/zh/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [刷新AutoFilter后获取所有隐藏行索引](/cells/zh/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
