---
title: 在导入HTML时删除换行后多余的空格
type: docs
weight: 20
url: /zh/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

请使用[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces)属性并将其设置为**true**，以删除换行标签后的所有多余空格。默认情况下，此属性为**false**，输出的excel文件中保留多余的空格。

{{% /alert %}}

## 将HTMLLoadOptions.DeleteRedundantSpaces属性设置为false和true的效果

将此属性设置为**false**和**true**的效果如下所示。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## 在导入HTML时删除换行后多余的空格

### 编程示例

以下示例代码显示了[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces)属性的用法。请将其设置为**true**或**false**，以获得以上截图中显示的输出。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
