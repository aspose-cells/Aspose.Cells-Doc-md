---
title: 通过C++用Golang访问文本框名称
linktitle: 按名称访问文本框
type: docs
weight: 230
url: /zh/go-cpp/access-the-text-box-by-the-name/
description: 了解如何使用Aspose.Cells for C++按名称访问文本框。
---

## 按名称访问文本框

早先，可以通过索引访问[**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/go-cpp/worksheet/gettextboxes/)集合中的文本框，但现在也可以通过名称访问此集合中的文本框。如果你已知其名称，这是一种方便快捷的访问方式。

以下示例代码首先创建一个文本框并赋予其一些文本和名称，然后通过名称访问该文本框并打印其文本。

### 使用C++按名称访问文本框的代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessTheTextBoxByTheName.go" >}}
### 样本代码生成的控制台输出

这是上面示例代码的控制台输出。

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
