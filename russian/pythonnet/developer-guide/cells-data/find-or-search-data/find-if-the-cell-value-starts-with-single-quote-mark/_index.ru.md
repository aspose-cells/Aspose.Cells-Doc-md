---
title: Узнайте, начинается ли значение ячейки с одинарной кавычки через Aspose.Cells для API Python via .NET.
type: docs
weight: 270
url: /ru/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Узнайте, начинается ли значение ячейки с одного знака кавычки через API Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python via .NET теперь предоставляет свойство {0}, чтобы узнать, начинается ли значение ячейки с одиночной кавычки. До появления этого свойства не было способа отличить строки, такие как пример и пример и т. д.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET теперь предоставляет свойство [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/), чтобы определить, начинается ли значение ячейки с одного знака кавычки. До появления этого свойства не было способа различить строки, такие как пример и 'пример' и т. д.

{{% /alert %}}

В следующем образце кода объясняется, что строки как пример и 'пример не могут быть различены с помощью свойства [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/). Поэтому мы должны использовать свойство [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/), чтобы различать их.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
