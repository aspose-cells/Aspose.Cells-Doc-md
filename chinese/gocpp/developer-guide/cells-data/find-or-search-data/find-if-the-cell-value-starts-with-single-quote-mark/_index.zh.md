---
title: 判断单元格值是否以单引号开头（用Golang via C++）
linktitle: 查找单元格值是否以单引号开始
type: docs
weight: 270
url: /zh/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: 学习如何使用Aspose.Cells for C++ API查找单元格值是否以单引号开始。
keywords: 查找单元格值是否以单引号标记开始，搜索单元格值是否以单引号标记开始
---

{{% alert color="primary" %}}

Aspose.Cells 现在提供了属性 [**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) 来查找单元格值是否以单引号标记开始。在此属性之前，无法区分类似 sample 和 'sample 等字符串。

{{% /alert %}}

下面的示例代码解释了像“sample”和“'sample”这样的字符串不能通过[**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/)属性进行区分。因此，我们必须使用[**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)属性对它们进行区分。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}
