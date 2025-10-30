---
title: Encontrar si el valor de la celda comienza con una comilla simple con Golang a través de C++
linktitle: Encontrar si el valor de la celda comienza con un signo de comilla simple
type: docs
weight: 270
url: /es/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aprende cómo encontrar si el valor de la celda comienza con una comilla simple mediante la API Aspose.Cells for C++.
keywords: Encontrar valor de celda que comienza con un signo de comilla simple, Buscar valor de celda que comienza con un signo de comilla simple
---

{{% alert color="primary" %}}

Ahora Aspose.Cells proporciona la propiedad [**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) para encontrar si el valor de la celda comienza con un signo de comilla simple. Antes de esta propiedad, no había forma de distinguir entre cadenas como ejemplo y 'ejemplo, etc.

{{% /alert %}}

El siguiente código de muestra explica que las cadenas como ejemplo y 'ejemplo no se pueden diferenciar con la propiedad [**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). Por lo tanto, debemos usar la propiedad [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) para distinguirlas.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}
