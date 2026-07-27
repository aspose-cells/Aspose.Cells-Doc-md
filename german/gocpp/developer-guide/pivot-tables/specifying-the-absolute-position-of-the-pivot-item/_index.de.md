---
title: Festlegung der absoluten Position des Pivot Elements mit Golang über C++
linktitle: Angabe der absoluten Position des Pivot Elements
type: docs
weight: 50
url: /de/go-cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Erfahren Sie, wie Sie die absolute Position von Pivot Elementen in C++ mit Aspose.Cells festlegen.
---

{{% alert color="primary" %}}

Manchmal müssen Benutzer die absolute Position der Pivot-Elemente angeben. Die Aspose.Cells API hat einige neue Eigenschaften und eine Methode bereitgestellt, um diese Anforderung zu erfüllen.

- Hinzugefügte [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/) Eigenschaft, die verwendet werden kann, um den Position-Index in allen Pivot-Elementen unabhängig vom übergeordneten Knoten anzugeben. Hinzugefügte [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) Eigenschaft, die verwendet werden kann, um den Position-Index in den Pivot-Elementen unter dem gleichen übergeordneten Knoten anzugeben.
- Die Methode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) wurde hinzugefügt, um das Element basierend auf dem Zählwert nach oben oder unten zu verschieben, wobei der Zählwert die Anzahl der Positionen ist, um die das Pivot-Element nach oben oder unten verschoben werden soll. Wenn der Zählwert kleiner als null ist, wird das Element nach oben verschoben, während bei einem Zählwert größer als null das Pivot-Element nach unten verschoben wird. Der Boolesche Parameter `isSameParent` gibt an, ob die Verschiebung im selben Elternknoten erfolgen soll.
- Der veraltete `PivotItem.Move(int count)`-Methode; es wird empfohlen, stattdessen die neu hinzugefügte Methode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) zu verwenden.

{{% /alert %}}

Der folgende Beispielcode erstellt eine Pivot-Tabelle und gibt dann die Positionen der Pivot-Elemente im selben Elternknoten an. Sie können die [Quelldatei Excel](5112632.xlsx) und die [Ausgabedatei Excel](5112619.xlsx) herunterladen. Wenn Sie die Ausgabedatei öffnen, sehen Sie, dass das Pivot-Element "4H12" an Position 0 im Elternknoten "K11" ist und "DIF400" an Position 3. Ebenso befindet sich CA32 an Position 1 und AAA3 an Position 2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingTheAbsolutePositionOfThePivotItem.go" >}}
{{% alert color="primary" %}}

Bitte beachten Sie, dass es erforderlich ist, die Methoden `PivotTable.RefreshData` und `PivotTable.CalculateData` aufzurufen, bevor Sie die Eigenschaften [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) und die Methode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) verwenden.

{{% /alert %}}
