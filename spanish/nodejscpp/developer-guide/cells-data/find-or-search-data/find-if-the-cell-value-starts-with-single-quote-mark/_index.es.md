---
title: Encontrar si el valor de la celda comienza con un signo de comilla simple
type: docs
weight: 270
url: /es/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aprender cómo encontrar si el valor de la celda comienza con una comilla única a través de la API Aspose.Cells for Node.js via C++.
keywords: Buscar valor de celda que comienza con una comilla única Node.js a través de C++, Buscar valor de celda que comienza con una comilla única Node.js a través de C++
---

{{% alert color="primary" %}}

Aspose.Cells ahora proporciona el método [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) para encontrar si el valor de la celda comienza con una comilla única. Antes de esta propiedad, no había forma de distinguir entre cadenas como sample y 'sample' etc.

{{% /alert %}}

El siguiente código ejemplo explica que las cadenas como sample y 'sample no pueden diferenciarse con el método [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). Por lo tanto, debemos usar el método [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) para diferenciarlas.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
