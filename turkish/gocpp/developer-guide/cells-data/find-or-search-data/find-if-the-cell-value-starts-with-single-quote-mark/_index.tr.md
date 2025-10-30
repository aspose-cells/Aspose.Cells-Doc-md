---
title: C++ ile Golang kullanarak hücre değeri tek tırnak işaretiyle başlayıp başlamadığını bulun
linktitle: Hücre değerinin tek tek tırnak işaretiyle başlayıp başlamadığını bul
type: docs
weight: 270
url: /tr/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aspose.Cells for C++ API’sini kullanarak hücre değeri tek tırnakla başlıyor mu, diye nasıl bakacağınızı öğrenin.
keywords: Hücre değerinin tek tek tırnak işaretiyle başlayıp başlamadığını bulmak için şimdi Aspose.Cells {0} özelliğini sağlar. Bu özelliğin öncesinde, örnek ve örnek gibi örneğin gibi stringler arasında ayrım yapmanın bir yolu yoktu.
---

{{% alert color="primary" %}}

Aşağıdaki örnek kod, 'örnek' ve 'örnek gibi örneğin' gibi stringler arasında ayrım yapmanın {0} özelliği ile mümkün olamayacağını açıklar. Bu nedenle, onları ayırt etmek için {1} özelliğini kullanmalıyız.

{{% /alert %}}

Aşağıdaki örnek kod, örnek ve 'örnek gibi dizilerin [**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) özelliği ile ayırt edilemeyeceğini açıklar. Bu nedenle onları ayırt etmek için [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) özelliğini kullanmamız gerekir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}
