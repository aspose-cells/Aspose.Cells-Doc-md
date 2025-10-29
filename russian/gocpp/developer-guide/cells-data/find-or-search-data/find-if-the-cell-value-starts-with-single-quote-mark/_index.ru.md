---
title: Определите, начинается ли значение ячейки с одинарной кавычки, с помощью Golang через C++
linktitle: Узнайте, начинается ли значение ячейки с одинарной кавычки через Aspose.Cells для API Python via .NET.
type: docs
weight: 270
url: /ru/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Узнайте, как определить начинается ли значение ячейки с одинарной кавычки через API Aspose.Cells for C++.
keywords: Найти значение ячейки, начинающееся с одинарного символа кавычки, Поиск значения ячейки, начинающегося с одинарного символа кавычки
---

{{% alert color="primary" %}}

Aspose.Cells теперь предоставляет свойство [**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) для проверки, начинается ли значение ячейки с одинарного символа кавычки. До этого свойства не было способа отличить строки, такие как образец и 'образец и т. д.

{{% /alert %}}

В следующем образце кода объясняется, что строки как пример и 'пример не могут быть различены с помощью свойства [**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). Поэтому мы должны использовать свойство [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/), чтобы различать их.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}
