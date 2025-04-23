---
title: Узнайте, начинается ли значение ячейки с одинарной кавычки через Aspose.Cells для API Python via .NET.
type: docs
weight: 270
url: /ru/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Узнайте, как найти, начинается ли значение ячейки с одинарного символа кавычки через API Aspose.Cells for .NET.
keywords: Найти значение ячейки, начинающееся с одинарного символа кавычки, Поиск значения ячейки, начинающегося с одинарного символа кавычки
---

{{% alert color="primary" %}}

Aspose.Cells теперь предоставляет свойство [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) для проверки, начинается ли значение ячейки с одинарного символа кавычки. До этого свойства не было способа отличить строки, такие как образец и 'образец и т. д.

{{% /alert %}}

В следующем образце кода объясняется, что строки как пример и 'пример не могут быть различены с помощью свойства [**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue). Поэтому мы должны использовать свойство [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix), чтобы различать их.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
{{< app/cells/assistant language="csharp" >}}
