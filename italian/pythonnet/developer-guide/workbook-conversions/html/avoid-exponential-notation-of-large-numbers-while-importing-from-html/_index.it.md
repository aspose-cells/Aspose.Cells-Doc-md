---
title: Evita la notazione esponenziale dei grandi numeri durante l importazione da HTML
type: docs
weight: 10
url: /it/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Questo argomento mostra come evitare la notazione esponenziale dei numeri grandi durante l importazione dall HTML utilizzando Aspose.Cells per Python via NET.
keywords: Evitare la notazione esponenziale dei numeri grandi durante l importazione dall HTML, mantenere la precisione durante l importazione dell html.
---

{{% alert color="primary" %}}

A volte il tuo Html contiene numeri come 1234567890123456 che sono più lunghi di 15 cifre e quando importi il tuo HTML nel file di Excel, questi numeri vengono convertiti in notazione esponenziale come 1.23457E+15. Se vuoi, il tuo numero dovrebbe essere importato com'è e non convertito in notazione esponenziale, allora si prega di utilizzare la proprietà [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) e impostarla su **true** durante il caricamento del tuo HTML.

{{% /alert %}}

Il seguente codice di esempio spiega l'uso della proprietà [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/). L'API importerà il numero così com'è senza convertirlo in notazione esponenziale.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
