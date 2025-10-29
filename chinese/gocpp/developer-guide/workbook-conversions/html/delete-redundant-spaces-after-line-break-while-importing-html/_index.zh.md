---
title: 用 Golang 通过 C++ 导入 HTML 时删除换行后的多余空格
linktitle: 导入HTML时删除换行后多余空格
type: docs
weight: 20
url: /zh/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: 了解如何在导入HTML时删除换行后的多余空格（使用Aspose.Cells for C++）。
---

{{% alert color="primary" %}}

 请使用[**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/)属性，并将其设置为**true**，以删除换行标签后的所有多余空格。默认情况下，此属性为**false**，在输出Excel文件时会保留多余空格。

{{% /alert %}}

## 将HTMLLoadOptions.DeleteRedundantSpaces属性设置为false和true的效果

以下截图显示了将此属性设置为**false**和**true**的效果。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

在导入HTML时删除换行后的多余空格

###编程示例

以下示例代码展示了[**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/)属性的用法。请将其设置为**true**或**false**以获得上面截图中显示的输出。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}
