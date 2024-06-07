---
title: 检查工作簿是否包含隐藏的外部链接
type: docs
weight: 230
url: /zh/net/check-if-workbook-contains-hidden-external-links/
---

## **可能的使用场景**
有时，工作簿中包含无法在Microsoft Excel中查看的隐藏外部链接。 Aspose.Cells检索所有外部链接，无论它们是可见的还是隐藏的。 但是，您可以检查[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) 属性以检查外部链接是否可见。
## **检查工作簿是否包含隐藏的外部链接**
以下示例代码加载包含隐藏外部链接的[源Excel文件](5115413.xlsx)。 这些链接无法在Microsoft Excel中查看，但它们存在于工作簿内。 在打印[ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) 和[ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) 属性后，它打印[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) 属性。 在下面的控制台输出中，您会看到其所有外部链接都不可见。
### **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **控制台输出**
这是上述示例代码与给定的[示例Excel文件](5115413.xlsx)执行时的控制台输出。



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
