---
title: Evita la notazione esponenziale dei grandi numeri durante l importazione da HTML
type: docs
weight: 10
url: /it/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

A volte il tuo Html contiene numeri come 1234567890123456 che sono più lunghi di 15 cifre e quando importi il tuo HTML nel file di Excel, questi numeri vengono convertiti in notazione esponenziale come 1.23457E+15. Se vuoi, il tuo numero dovrebbe essere importato com'è e non convertito in notazione esponenziale, allora si prega di utilizzare la proprietà [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) e impostarla su **true** durante il caricamento del tuo HTML.

{{% /alert %}}

Il seguente codice di esempio spiega l'uso della proprietà [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision). L'API importerà il numero così com'è senza convertirlo in notazione esponenziale.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
