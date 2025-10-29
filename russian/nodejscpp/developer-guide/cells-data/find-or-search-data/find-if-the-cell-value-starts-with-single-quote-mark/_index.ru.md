---
title: Узнайте, начинается ли значение ячейки с одинарной кавычки через Aspose.Cells для API Python via .NET.
type: docs
weight: 270
url: /ru/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Узнайте, как определить, начинается ли значение ячейки с кавычки, через API Aspose.Cells for Node.js via C++.
keywords: Найти значение ячейки, начинающееся с кавычки, Node.js через C++, поиск значения ячейки, начинающегося с кавычки, Node.js через C++
---

{{% alert color="primary" %}}

Теперь Aspose.Cells предоставляет метод [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) для определения, начинается ли значение ячейки с кавычки. До этого свойства не было способа различить строки вроде sample и 'sample' и т.д.

{{% /alert %}}

Следующий пример показывает, что строки вроде sample и 'sample' нельзя отличить с помощью метода [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). Поэтому необходимо использовать метод [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) для их различения.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
