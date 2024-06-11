---
title: 查找单元格值是否以单引号开始
type: docs
weight: 270
url: /zh/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: 学习如何通过Aspose.Cells for Python via .NET API查找单元格值是否以单引号标记开始。
keywords: Python Excel库，Python查找单元格值以单引号标记开始，Python搜索单元格值以单引号标记开始
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET现在提供了[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/)属性，以查找单元格值是否以单引号标记开始。在使用此属性之前，无法区分“sample”和“'sample”等字符串。

{{% /alert %}}

下面的示例代码解释了像“sample”和“'sample”这样的字符串不能通过[**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/)属性进行区分。因此，我们必须使用[**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/)属性对它们进行区分。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
