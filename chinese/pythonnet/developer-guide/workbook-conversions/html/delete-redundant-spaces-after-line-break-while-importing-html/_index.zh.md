---
title: 在导入HTML时删除换行后多余的空格
type: docs
weight: 20
url: /zh/python-net/delete-redundant-spaces-after-line-break-while-importing/
description: 本主题展示了如何在导入HTML时使用Aspose.Cells for Python via NET删除换行后多余的空格。
keywords: 导入HTML时删除换行后多余的空格，导入HTML删除换行后多余的空格。
---

{{% alert color="primary" %}}

请使用[**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/)属性并将其设置为**true**，以删除换行标签后的所有多余空格。默认情况下，此属性为**false**，输出的excel文件中保留多余的空格。

{{% /alert %}}

将HTMLLoadOptions.delete_redundant_spaces属性的设置为false和true的影响

将此属性设置为**false**和**true**的效果如下所示。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## 在导入HTML时删除换行后多余的空格

### 编程示例

以下示例代码显示了[**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/)属性的用法。请将其设置为**true**或**false**，以获得以上截图中显示的输出。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DeleteRedundantSpacesWhileImportingFromHtml-1.py" >}}
