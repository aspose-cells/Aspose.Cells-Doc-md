---
title: Evita la notazione esponenziale dei grandi numeri durante l importazione da HTML
type: docs
weight: 600
url: /it/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

A volte il tuo HTML contiene numeri come 1234567890123456 che sono più lunghi di 15 cifre e quando importi il tuo HTML nel file excel, questi numeri si convertono in notazione esponenziale come 1.23457E+15. Se desideri che il tuo numero venga importato così com'è e non convertito in notazione esponenziale, allora si prega di utilizzare la proprietà [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) e impostarla su **true** durante il caricamento del tuo HTML.

{{% /alert %}} 
## **Evita la notazione esponenziale dei grandi numeri durante l'importazione da HTML**
Il seguente codice di esempio spiega l'uso della proprietà [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision). Importerà il numero così com'è senza convertirlo in notazione esponenziale.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
