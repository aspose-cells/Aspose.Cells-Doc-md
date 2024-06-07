---
title: 数据筛选
type: docs
weight: 60
url: /zh/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel提供了一些不错的功能来自动筛选工作表数据。 Aspose.Cells完全支持Microsoft Excel的自动筛选功能。 本文解释了如何在Microsoft Excel中使用这些功能以及如何使用Aspose.Cells对其进行编码。

{{% /alert %}}

## **自动筛选数据**

自动筛选是选择仅显示列表中希望显示的那些项目的最快方式。 自动筛选功能允许用户根据一组标准对列表中的项目进行筛选。 根据文本、数字或日期进行筛选。

### **Microsoft Excel中的自动筛选**

要在Microsoft Excel中激活自动筛选功能：

1.在工作表中点击标题行。
1. 从“数据”菜单中选择“筛选”，然后选择“自动筛选”。

当您在工作表上应用自动筛选时，筛选开关（黑色箭头）将显示在列标题右侧。

1.单击筛选箭头以查看筛选选项。

一些自动筛选选项包括：

|**选项**|**描述**|
| :- | :- |
|All|一次显示列表中的所有项目。|
|Custom|自定义过滤器标准，如包含/不包含|
|Filter by Color|基于填充颜色的筛选|
|Date Filters|根据不同的日期条件筛选行|
|Number Filters|不同类型的数字过滤，如比较、平均值和前10名等|
|Text Filters|不同类型的过滤器，如以...开头，以...结束，包含等|
|Blanks/Non Blanks|这些过滤器可通过文本过滤器空白实现|
用户可以使用这些选项手动筛选他们在Microsoft Excel中的工作表数据。

### **Aspose.Cells的自动筛选**

Aspose.Cells提供了一个表示Excel文件的类[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了一系列广泛的属性和方法来管理工作表。要创建自动筛选，请使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)属性。[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)属性是[**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)类的一个对象，它提供[**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)属性以指定构成标题行的单元格范围。自动筛选应用于构成标题行的单元格范围。

在每个工作表中，您只能指定一个筛选范围。这受到Microsoft Excel的限制。要进行自定义数据筛选，请使用[**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object))方法。

在下面的示例中，我们使用Aspose.Cells创建了与上一节中使用Microsoft Excel创建的相同的AutoFilter筛选。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **不同类型的筛选**

Aspose.Cells提供了多种选项来应用不同类型的筛选，如颜色筛选、日期筛选、数字筛选、文本筛选、空白筛选和非空白筛选。

##### **填充颜色**

Aspose.Cells提供了一个函数[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor))，根据单元格的填充颜色属性来筛选数据。在下面给出的示例中，使用具有工作表第一列中不同填充颜色的模板文件来测试颜色筛选功能。可以下载以下文件以检查功能。

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **日期**

可以实现不同类型的日期筛选，例如过滤所有具有2018年1月日期的行。以下示例代码演示了使用[**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int))函数进行此筛选。可以使用以下文件进行测试此功能。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **动态日期**

有时需要基于日期的动态筛选，例如显示所有在一月份的单元格，而不考虑年份。在这种情况下，使用如下示例代码中所述的[**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int))函数。可以使用以下文件进行测试。

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **数字**

可以使用Aspose.Cells应用自定义筛选，例如选择值在给定范围之间的单元格。以下示例演示了使用[**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object))函数筛选数字的用法。可以从以下链接下载示例文件。

1. [数字.xlsx](72417320.xlsx)
1. [过滤后的数字.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **文本**

如果一列包含文本，并且要选择包含特定文本的单元格，则可以使用[**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String))函数。在下面的示例中，模板文件包含一个国家列表，将选择包含特定国家名称的行。以下代码演示了使用以下示例文件进行文本筛选。

1. [文本.xlsx](72417322.xlsx)
1. [过滤后的文本.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **空白**

如果一列包含文本，其中有些单元格为空，并且需要选择仅在存在空单元格的行，则可以使用如下所示的[**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int))函数。可以从以下链接下载示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [过滤后的空白.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **非空白**

当需要筛选具有任何文本的单元格时，可以使用如下所示的[**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int))筛选函数。可以从以下链接下载示例文件。

1. [空白.xlsx](72417324.xlsx)
1. [过滤后的非空白.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **包含的自定义过滤器**

Excel提供自定义筛选功能，例如筛选包含某些特定字符串的行。Aspose.Cells中提供了此功能，并通过过滤示例文件中的名称来演示。可以从以下链接下载示例文件。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **不包含的自定义过滤器**

Excel提供了自定义过滤器，例如过滤不包含某个特定字符串的行。Aspose.Cells中提供此功能，并通过下面演示了在示例文件中过滤名称。下面提供了示例文件。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **以某字符串开始的自定义过滤器**

Excel提供了自定义过滤器，例如过滤以某个特定字符串开始的行。Aspose.Cells中提供此功能，并通过下面演示了在示例文件中过滤名称。下面提供了示例文件。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **以某字符串结束的自定义过滤器**

Excel提供了自定义筛选器，例如筛选以特定字符串结尾的行。Aspose.Cells提供了此功能，并通过下面的示例文件中的名称进行了演示。

1. [源示例国家名称.xlsx](sourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **高级主题**
- [应用Microsoft Excel的高级筛选以显示满足复杂条件的记录](/cells/zh/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [刷新AutoFilter后获取所有隐藏行索引](/cells/zh/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

