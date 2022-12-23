---
title: Trovare la posizione assoluta della forma all'interno del foglio di lavoro
type: docs
weight: 7000
url: /it/java/finding-absolute-position-of-shape-inside-the-worksheet/
---
{{% alert color="primary" %}}

 A volte è necessario conoscere la posizione assoluta di una forma su un foglio di lavoro. Aspose.Cells fornisce il[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) e[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) proprietà a questo scopo. Queste proprietà restituiscono la posizione assoluta di una forma in un foglio di lavoro in pixel.

{{% /alert %}}

## **Spiegazione delle proprietà Shape.getLeftToCorner() e Shape.getTopToCorner()**

Questo screenshot spiega quali distanze il[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) e[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)misura delle proprietà.

**Misurazione della posizione assoluta**

![cose da fare:immagine_alt_testo](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

Il codice di esempio seguente visualizza la posizione assoluta della prima forma in un foglio di lavoro in pixel. Il codice visualizza il seguente output nella console:

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
