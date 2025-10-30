---
title: Trova la posizione assoluta della forma all interno del foglio di lavoro con Golang tramite C++
linktitle: Trova la posizione assoluta della forma all interno del foglio di lavoro
type: docs
weight: 8000
url: /it/go-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Determina la posizione assoluta di una forma in un foglio di lavoro usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

A volte è necessario conoscere la posizione assoluta di una forma in un foglio di lavoro. Aspose.Cells fornisce le proprietà [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/go-cpp/shape/getlefttocorner/) e [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) a questo scopo. Queste proprietà restituiscono la posizione assoluta della forma all'interno del foglio di lavoro in pixel.

{{% /alert %}}

Il codice di esempio seguente visualizza la posizione assoluta della prima forma nel foglio di lavoro in pixel. Il codice di esempio visualizza l'output della console seguente:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindingAbsolutePositionOfShapeInsideTheWorksheet.go" >}}
