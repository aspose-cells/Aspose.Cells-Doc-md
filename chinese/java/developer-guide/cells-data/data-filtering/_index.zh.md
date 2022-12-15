---
title: 数据过滤
type: docs
weight: 60
url: /zh/java/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel 提供了一些很好的功能来自动筛选工作表数据。 Aspose.Cells 完全支持 Microsoft Excel 的自动筛选功能。本文介绍如何使用 Microsoft Excel 中的功能，以及如何使用 Aspose.Cells 对其进行编码。

{{% /alert %}}

## **自动过滤数据**

自动筛选是从工作表中仅选择要在列表中显示的项目的最快方法。自动筛选功能允许用户根据设定的标准筛选列表中的项目。根据文本、数字或日期进行过滤。

### **Microsoft Excel 中的自动筛选器**

要激活 Microsoft Excel 中的自动筛选功能：

1. 单击工作表中的标题行。
1. 来自**数据**菜单，选择**筛选**接着**自动过滤**.

当您将自动过滤器应用于工作表时，过滤器开关（黑色箭头）出现在列标题的右侧。

1. 单击过滤器箭头可查看过滤器选项列表。

一些自动过滤器选项是：

|**选项**|**描述**|
|:- |:- |
|全部|一次显示列表中的所有项目。|
|风俗|自定义过滤条件，如包含/不包含|
|按颜色过滤|基于填充颜色的过滤器|
|日期过滤器|根据日期的不同标准过滤行|
|数字过滤器|不同类型的数字过滤器，如比较、平均值和前 10 名等。|
|文本过滤器|不同的过滤器，如开头、结尾、包含等，|
|空白/非空白|这些过滤器可以通过 Text Filter Blank 来实现|
用户使用这些选项手动筛选 Microsoft Excel 中的工作表数据。

### **带 Aspose.Cells 的自动过滤器**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示一个 Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。

工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要创建自动过滤器，请使用[**自动过滤**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)的财产[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[**自动过滤**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)属性是[**自动过滤**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)类，它提供了[**范围**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)用于指定构成标题行的单元格范围的属性。自动过滤器应用于作为标题行的单元格范围。

在每个工作表中，您只能指定一个过滤范围。这是受 Microsoft Excel 的限制。对于自定义数据过滤，使用[**自动过滤器.自定义**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)） 方法。

在下面给出的示例中，我们使用 Aspose.Cells 创建了与上一节中使用 Microsoft Excel 创建的相同的自动筛选器。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **不同类型的过滤器**

Aspose.Cells 提供了多个选项来应用不同类型的过滤器，如颜色过滤器、日期过滤器、数字过滤器、文本过滤器、空白过滤器和无空白过滤器。

##### **填色**

Aspose.Cells提供了一个功能[**添加填充颜色过滤器**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)根据单元格的填充颜色属性过滤数据。在下面给出的示例中，使用工作表第一列具有不同填充颜色的模板文件来测试颜色过滤功能。可以下载以下文件来检查功能。

1. [彩色细胞.xlsx](72417315.xlsx)
1. [过滤彩色单元格.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **日期**

可以实现不同类型的日期过滤器，例如过滤所有具有 2018 年 1 月日期的行。以下示例代码演示了此过滤器使用[**添加日期过滤器**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)） 功能。以下文件可用于测试此功能。

1. [日期.xlsx](72417317.xlsx)
1. [过滤日期.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **动态日期**

有时需要基于日期的动态过滤器，例如所有单元格的日期都在一月份，而不管年份如何。在这种情况下，[**动态过滤器**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)函数按以下示例代码中给出的方式使用。以下文件可用于测试。

1. [日期.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **数字**

可以使用 Aspose.Cells 应用自定义过滤器，例如选择数字在给定范围之间的单元格。以下示例演示了[**风俗（）**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) 函数过滤数字。示例文件可以从以下链接下载。

1. [数字.xlsx](72417320.xlsx)
1. [筛选编号.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **文本**

如果一列包含文本并且要选择包含特定文本的单元格，[**筛选（）**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) 函数可以使用。在以下示例中，模板文件包含一个国家列表，要选择的行包含特定国家/地区名称。以下代码演示了使用以下示例文件过滤文本。

1. [文本.xlsx](72417322.xlsx)
1. [过滤文本.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **毛坯**

如果一列包含的文本很少有单元格是空白的，并且需要过滤器以仅选择那些存在空白单元格的行，[**匹配空白()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) 函数可以如下所示使用。示例文件可以从以下链接下载。

1. [空白.xlsx](72417324.xlsx)
1. [筛选空白.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **非空白**

当要过滤包含任何文本的单元格时，使用[**匹配非空白**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)过滤功能如下所示。示例文件可以从以下链接下载。

1. [空白.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **使用包含的自定义过滤器**

Excel 提供自定义过滤器，例如包含某些特定字符串的过滤器行。此功能在 Aspose.Cells 中可用，并在下面通过过滤示例文件中的名称进行了演示。示例文件可以从以下链接下载。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **使用 NotContains 的自定义过滤器**

Excel 提供自定义过滤器，例如不包含某些特定字符串的过滤器行。此功能在 Aspose.Cells 中可用，并在下面通过过滤下面给出的示例文件中的名称进行了演示。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **使用 BeginsWith 自定义过滤器**

Excel 提供自定义过滤器，例如以特定字符串开头的过滤器行。此功能在 Aspose.Cells 中可用，并在下面通过过滤下面给出的示例文件中的名称进行了演示。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **使用 EndsWith 自定义过滤器**

Excel 提供自定义过滤器，例如以特定字符串结尾的过滤器行。此功能在 Aspose.Cells 中可用，并在下面通过过滤下面给出的示例文件中的名称进行了演示。

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **推进主题**
- [应用 Microsoft Excel 的高级筛选器显示满足复杂条件的记录](/cells/zh/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [刷新自动筛选后获取所有隐藏行索引](/cells/zh/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

