---
title: 查找单元格值是否以单引号开始
type: docs
weight: 270
url: /zh/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: 学习如何通过 Aspose.Cells for Node.js via C++ API 判断单元格值是否以单引号开头。
keywords: 使用 C++ 搜索以单引号开头的单元格值
---

{{% alert color="primary" %}}

Aspose.Cells 现在提供了 [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) 方法，用于判断单元格值是否以单引号开头。在此之前，没有办法区分类似 sample 和 'sample 等字符串。

{{% /alert %}}

以下示例说明了用 [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) 方法无法区分类似 sample 和 'sample 的字符串。因此，我们必须使用 [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) 方法来区分它们。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
