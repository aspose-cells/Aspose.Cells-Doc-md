---
title: Evita la notazione esponenziale di numeri grandi durante l'importazione da HTML
type: docs
weight: 600
url: /it/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

 volte il tuo HTML contiene numeri come 1234567890123456 che sono più lunghi di 15 cifre e quando importi il tuo HTML in un file excel, questi numeri vengono convertiti in notazione esponenziale come 1.23457E+15. Se lo desideri, il tuo numero dovrebbe essere importato così com'è e non convertito in notazione esponenziale, quindi utilizzalo[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) proprietà e impostarla**VERO** durante il caricamento del codice HTML.

{{% /alert %}} 
## **Evita la notazione esponenziale di numeri grandi durante l'importazione da HTML**
 Il seguente codice di esempio spiega l'utilizzo di[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)proprietà. Importerà il numero così com'è senza convertirlo in notazione esponenziale.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
