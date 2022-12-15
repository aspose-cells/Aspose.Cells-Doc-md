---
title: Interruzioni di riga e ritorno a capo del testo
type: docs
weight: 10
url: /it/java/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Per garantire che il testo in una cella possa essere letto, è possibile applicare interruzioni di riga esplicite e ritorno a capo automatico. Il ritorno a capo trasforma una riga in più righe in una cella, che le interruzioni di riga esplicite inseriscono nelle interruzioni esattamente dove le desideri.

{{% /alert %}}

## **Per avvolgere il testo in un Cell**

 Per disporre il testo in una cella, utilizzare il[**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)proprietà.

Il codice di esempio seguente mostra come utilizzare la disposizione del testo e le interruzioni di riga esplicite in una cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **Per utilizzare interruzioni di riga esplicite**

Puoi usare '\n' in Java per inserire le interruzioni di riga esplicite in una cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}
