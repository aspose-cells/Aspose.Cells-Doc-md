---
title: Encontrar si el valor de la celda comienza con un signo de comilla simple
type: docs
weight: 270
url: /es/python-net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aprenda cómo encontrar si el valor de la celda comienza con comilla simple a través de la API de Aspose.Cells for Python via .NET.
keywords: Biblioteca de Excel de Python, Encontrar valor de celda que comienza con comilla simple en Python, Buscar valor de celda que comienza con comilla simple en Python
---

{{% alert color="primary" %}}

Ahora, Aspose.Cells para Python via .NET proporciona la propiedad [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) para encontrar si el valor de la celda comienza con una comilla simple. Antes de esta propiedad, no había forma de distinguir entre cadenas como muestra y 'muestra, etc.

{{% /alert %}}

El siguiente código de muestra explica que las cadenas como ejemplo y 'ejemplo no se pueden diferenciar con la propiedad [**Cell.string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/). Por lo tanto, debemos usar la propiedad [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix/) para distinguirlas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FindIfCellValueStartsWithSingleQuote.py" >}}
