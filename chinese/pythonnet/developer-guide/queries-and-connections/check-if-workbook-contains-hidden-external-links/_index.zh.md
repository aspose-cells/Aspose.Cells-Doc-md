---
title: 检查工作簿是否包含隐藏的外部链接
type: docs
weight: 230
url: /zh/python-net/check-if-workbook-contains-hidden-external-links/
---

## **可能的使用场景**
有时，工作簿中包含隐藏外部链接，不能在Microsoft Excel中查看。Aspose.Cells for Python via .NET 可以检索所有外部链接，无论它们是隐藏还是可见。你还可以检查[ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible)属性，了解外部链接是否可见。

## **检查工作簿是否包含隐藏的外部链接**
以下示例代码加载包含隐藏外部链接的[源Excel文件](5115413.xlsx)。这些链接在Microsoft Excel中无法查看，但它们存在于工作簿内。在打印[ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source)和[ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred)属性后，会打印[ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible)属性。在下方的控制台输出中，您会看到，它的所有外部链接都不可见。

### **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

### **控制台输出**
这是执行给定[源Excel文件](5115413.xlsx)时上述示例代码的控制台输出。



{{< highlight java >}}

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

