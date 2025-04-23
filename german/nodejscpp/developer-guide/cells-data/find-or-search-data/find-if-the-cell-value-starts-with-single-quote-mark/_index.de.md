---
title: Überprüfen Sie, ob der Zellenwert mit einem einfachen Anführungszeichen beginnt
type: docs
weight: 270
url: /de/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Lernen Sie, wie Sie mit der API Aspose.Cells for Node.js via C++ prüfen, ob der Zellwert mit einem einzelnen Anführungszeichen beginnt.
keywords: Zellwert, der mit einem einzelnen Anführungszeichen beginnt, finden Node.js via C++, Zellwert, der mit einem einzelnen Anführungszeichen beginnt, durchsuchen Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells bietet jetzt die Methode [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) an, um zu prüfen, ob der Zellwert mit einem einzelnen Anführungszeichen beginnt. Vor dieser Eigenschaft gab es keine Möglichkeit, Strings wie sample und 'sample' zu unterscheiden.

{{% /alert %}}

Der folgende Beispielcode erklärt, dass Strings wie sample und 'sample' mit der Methode [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) nicht unterschieden werden können. Daher müssen wir die Methode [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) verwenden, um sie zu unterscheiden.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

