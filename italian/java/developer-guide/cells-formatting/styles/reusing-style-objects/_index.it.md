---
title: Riutilizzo degli oggetti stile
type: docs
weight: 60
url: /it/java/reusing-style-objects/
---

{{% alert color="primary" %}}

Riutilizzare gli oggetti stile può risparmiare memoria e rendere l'esecuzione del programma più veloce.

{{% /alert %}}

Per applicare una formattazione a un'ampia gamma di celle in un foglio di lavoro:

1. Creare un oggetto stile.
1. Specificare gli attributi.
1. Applicare lo stile alle celle nell'intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Lo stesso processo discusso in precedenza potrebbe essere realizzato anche come segue.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

Poiché i metodi [**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) e [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-) utilizzano molto meno memoria ed sono efficienti, la vecchia proprietà *Cell.getStyle()* che consumava molta memoria superflua, è stata rimossa con il rilascio di *Aspose.Cells 7.1.0*.

{{% /alert %}}
