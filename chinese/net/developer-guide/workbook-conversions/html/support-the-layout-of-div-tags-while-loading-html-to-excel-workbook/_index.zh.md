---
title: 支持在加载 HTML 到 Excel 工作簿时 DIV 标签的布局
type: docs
weight: 50
url: /zh/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

通常，在将 HTML 加载到 Excel 工作簿对象时，会忽略 DIV 标签的布局。但是，如果您不希望忽略 DIV 标签的布局，请将 [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) 属性设置为 **true**。该属性的默认值为 **false**。

{{% /alert %}} 

以下示例代码说明了 [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) 属性的用法。请下载用于输入 HTML 的 [Aspose Logo](5115218.png) 和代码生成的 [输出 Excel 文件](5115220.xlsx)。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
