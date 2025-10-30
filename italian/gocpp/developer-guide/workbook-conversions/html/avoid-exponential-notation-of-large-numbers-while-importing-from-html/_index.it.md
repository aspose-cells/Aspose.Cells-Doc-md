---
title: Evita la notazione esponenziale di numeri grandi durante l importazione da HTML con Golang via C++
linktitle: Evita la notazione esponenziale dei grandi numeri durante l importazione da HTML
type: docs
weight: 10
url: /it/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Impara come evitare la notazione esponenziale di numeri grandi durante l’importazione da HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte il tuo HTML contiene numeri come 1234567890123456 che sono più lunghi di 15 cifre, e quando importi il tuo HTML in un file Excel, questi numeri vengono convertiti in notazione esponenziale come 1.23457E+15. Se desideri che il numero venga importato così com’è e non convertito in notazione esponenziale, utilizza la proprietà [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/) e impostala su **true** durante il caricamento del tuo HTML.

{{% /alert %}}

Il seguente esempio di codice spiega l’uso della proprietà [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/). L’API importerà il numero così com’è senza convertirlo in notazione esponenziale.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
