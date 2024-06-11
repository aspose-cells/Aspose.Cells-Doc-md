---
title: 通过 Aspose.Cells for .NET API 学习如何查找单元格值是否以单引号标记开头。
type: docs
weight: 270
url: /zh/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: 通过Aspose.Cells for Python通过.NET API学习如何查找单元格值是否以单引号标记开头。
keywords: Python Excel库，Python查找以单引号标记开头的单元格值，Python查找以单引号标记开头的单元格值
---

{{% alert color="primary" %}}

Aspose.Cells for Python通过.NET现在提供了[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/)属性，用于查找单元格值是否以单引号标记开头。 在此属性之前，没有办法区分如样本和'样本等字符串。

{{% /alert %}}

以下示例代码解释了类似 sample 和 'sample 无法通过 [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/) 属性区分的情况。因此，我们必须使用 [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) 属性来区分它们。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
