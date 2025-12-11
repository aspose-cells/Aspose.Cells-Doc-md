---
title: Find if the cell value starts with single quote mark with Golang via C++
linktitle: Find if the cell value starts with single quote mark
type: docs
weight: 270
url: /go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Learn how to find if the cell value starts with a single quote mark through the Aspose.Cells for C++ API.
keywords: Find cell value starts with a single quote mark, Search cell value starts with a single quote mark
---

{{% alert color="primary" %}}

Aspose.Cells now provides the [**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) property to determine whether a cell value starts with a single quote mark. Before this property, there was no way to distinguish between strings such as sample and 'sample, etc.

{{% /alert %}}

The following sample code demonstrates that strings such as sample and 'sample cannot be differentiated using the [**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) property. Therefore, we must use the [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) property to distinguish them.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}