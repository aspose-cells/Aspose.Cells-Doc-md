---
title: 检查工作簿是否包含隐藏的外部链接
type: docs
weight: 950
url: /zh/java/check-if-workbook-contains-hidden-external-links/
---

## **可能的使用场景**
有时，工作簿包含无法在Microsoft Excel中查看的隐藏外部链接。Aspose.Cells检索所有外部链接，无论它们是可见的还是隐藏的。但是，您可以检查 [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) 属性以检查外部链接是否可见。
## **检查工作簿是否包含隐藏的外部链接**
以下示例代码加载包含隐藏外部链接的 [源excel文件](5472525.xlsx)。这些链接在Microsoft Excel中无法查看，但它们存在于工作簿中。在打印 [ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) 和 [ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred) 属性之后，它会打印 [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) 属性。下面的控制台输出显示，所有外部链接都不可见。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **控制台输出**
以下是执行给定的 [示例excel文件](5472525.xlsx) 时上述示例代码的控制台输出。



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
