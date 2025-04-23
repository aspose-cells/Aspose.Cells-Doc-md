---
title: 支持加载HTML到Excel工作簿时的DIV标签布局
type: docs
weight: 50
url: /zh/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

通常，加载HTML到Excel工作簿对象时会忽略div标签的布局。但是，如果希望保留div标签的布局，则请将[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag)属性设置为**true**。此属性的默认值为**false**。

{{% /alert %}} 

以下示例代码演示了[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) 属性的用法。请下载用于输入HTML的[Aspose Logo](5115218.png)和代码生成的[output excel file](5115220.xlsx)。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
