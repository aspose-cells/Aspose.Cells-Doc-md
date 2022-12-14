---
title: 检查工作簿是否包含隐藏的外部链接
type: docs
weight: 230
url: /zh/net/check-if-workbook-contains-hidden-external-links/
---
## **可能的使用场景**
有时，工作簿包含隐藏的外部链接，无法在 Microsoft Excel 中查看。 Aspose.Cells 检索所有外部链接，无论它们是可见的还是隐藏的。但是，您可以检查[外部链接.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)检查外部链接是否可见的属性
## **检查工作簿是否包含隐藏的外部链接**
下面的示例代码加载[源文件](5115413.xlsx)其中包含隐藏的外部链接。这些链接无法在 Microsoft Excel 中查看，但它们存在于工作簿中。印刷后[外部链接.数据源](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource)和[外部链接.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred)财产，它打印[外部链接.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)财产。在下面的控制台输出中，您会看到，它的所有外部链接都不可见。
### **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **控制台输出**
这是使用给定的执行时上述示例代码的控制台输出[示例 excel 文件](5115413.xlsx).



{{< highlight "java" >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
