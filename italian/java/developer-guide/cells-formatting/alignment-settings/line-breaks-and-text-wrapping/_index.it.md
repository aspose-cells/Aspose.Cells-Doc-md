---
title: Interruzioni di riga e a capo automatico del testo
type: docs
weight: 10
url: /it/java/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Per garantire che il testo in una cella possa essere letto, possono essere applicati ritorni a capo espliciti e a capo automatico del testo. Il ritorno a capo del testo trasforma una riga in più in una cella, mentre i ritorni a capo espliciti inseriscono spazi esattamente dove si desidera.

{{% /alert %}}

## **Per incapsulare il testo in una cella**

Per incapsulare il testo in una cella, utilizzare la proprietà [**Aspose.Cells.Style.setTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped).

Il seguente codice di esempio mostra come utilizzare il ritorno a capo del testo e gli a capo espliciti in una cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WrapTextinCell-1.java" >}}

## **Per utilizzare ritorni a capo espliciti**

Puoi usare '\n' in Java per inserire a capo espliciti in una cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseExplicitLineBreaks-UseExplicitLineBreaks.java" >}}
