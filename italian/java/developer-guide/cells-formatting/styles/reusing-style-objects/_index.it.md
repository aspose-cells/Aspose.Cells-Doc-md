---
title: Riutilizzo degli oggetti di stile
type: docs
weight: 60
url: /it/java/reusing-style-objects/
---
{{% alert color="primary" %}}

Il riutilizzo degli oggetti di stile può risparmiare memoria e velocizzare l'esecuzione del programma.

{{% /alert %}}

Per applicare una formattazione a un'ampia gamma di celle in un foglio di lavoro:

1. Crea un oggetto di stile.
1. Specificare gli attributi.
1. Applicare lo stile alle celle nell'intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Lo stesso processo discusso sopra potrebbe anche essere realizzato come segue.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

 Perché il[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle() ) e[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style) ) usano molta meno memoria e sono efficienti, più vecchi*Cell.getStyle()* proprietà che consumava molta memoria non necessaria, è stata rimossa con il rilascio di*Aspose.Cells 7.1.0*.

{{% /alert %}}
