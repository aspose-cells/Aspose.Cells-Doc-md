---
title: Trova la posizione assoluta della forma all interno del foglio di lavoro
type: docs
weight: 7000
url: /it/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Scopri come trovare la posizione assoluta della forma all interno del foglio di lavoro attraverso le API Aspose.Cells for Java.
keywords: Come trovare la posizione assoluta della forma in Java, Ottenere la posizione assoluta della forma utilizzando Java, Ottenere la posizione assoluta della forma all interno del foglio di lavoro via Java, Misurare la posizione assoluta della forma con Java.
---

{{% alert color="primary" %}}

A volte devi conoscere la posizione assoluta di una forma su un foglio di lavoro. Aspose.Cells fornisce le proprietà [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) e [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) a questo scopo. Queste proprietà restituiscono la posizione assoluta di una forma in un foglio di lavoro in pixel.

{{% /alert %}}

## **Spiegazione delle proprietà Shape.getLeftToCorner() e Shape.getTopToCorner()**

Questa schermata spiega quali distanze misurano le proprietà [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) e [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner).

**Come misurare la posizione assoluta**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

Il seguente codice di esempio visualizza la posizione assoluta della prima forma in un foglio di lavoro in pixel. Il codice visualizza il seguente output nella console:

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
