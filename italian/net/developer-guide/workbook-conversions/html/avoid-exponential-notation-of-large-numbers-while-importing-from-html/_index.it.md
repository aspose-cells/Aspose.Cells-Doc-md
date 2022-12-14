---
title: Evita la notazione esponenziale di numeri grandi durante l'importazione da HTML
type: docs
weight: 10
url: /it/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

 A volte il tuo Html contiene numeri come 1234567890123456 che sono più lunghi di 15 cifre e quando importi il tuo HTML in un file Excel, questi numeri vengono convertiti in notazione esponenziale come 1.23457E+15. Se lo desideri, il tuo numero dovrebbe essere importato così com'è e non convertito in notazione esponenziale, quindi utilizzalo[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) proprietà e impostarla**VERO** durante il caricamento del codice HTML.

{{% /alert %}}

 Il seguente codice di esempio spiega l'utilizzo di[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)proprietà. Lo API importerà il numero così com'è senza convertirlo in notazione esponenziale.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
