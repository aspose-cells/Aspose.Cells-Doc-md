---
title: 导入时删除换行后的多余空格 HTML
type: docs
weight: 20
url: /zh/net/delete-redundant-spaces-after-line-break-while-importing/
---
{{% alert color="primary" %}}

请用[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces)属性并设置它**真的**删除换行标记后的所有冗余空格。默认情况下，此属性是**错误的**并且在输出的 excel 文件中保留了多余的空格。

{{% /alert %}}

## 将 HTMLLoadOptions.DeleteRedundantSpaces 属性设置为 false 和 true 的效果

下面的截图展示了将这个属性设置为的效果**错误的**和**真的**.

![待办事项：图片_替代_文本](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## 导入时删除换行后的多余空格 HTML

### 编程范例

下面的示例代码显示了[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces)财产。请设定**真的**要么**错误的**获得如上图所示的输出。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
