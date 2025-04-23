---
title: Angabe der absoluten Position des Pivot Elements
type: docs
weight: 40
url: /de/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Manchmal muss der Benutzer die absolute Position der Pivot-Elemente angeben. Die Aspose.Cells-API hat einige neue Eigenschaften und eine Methode zur Erfüllung dieses Benutzerwunsches freigegeben.

- Hinzugefügte [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) Eigenschaft, die verwendet werden kann, um den Position-Index in allen Pivot-Elementen unabhängig vom übergeordneten Knoten anzugeben. Hinzugefügte [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) Eigenschaft, die verwendet werden kann, um den Position-Index in den Pivot-Elementen unter dem gleichen übergeordneten Knoten anzugeben.
- Hinzugefügte Methode [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-), um das Element basierend auf dem Zählwert nach oben oder unten zu bewegen, wobei der Zählwert die Anzahl der Positionen ist, um das Pivot-Element nach oben oder unten zu bewegen. Wenn der Zählwert kleiner als Null ist, wird das Element nach oben verschoben, während wenn der Zählwert größer als Null ist, das Pivot-Element nach unten verschoben wird, Boolean type isSameParent-Parameter, der angibt, ob die Verschiebung in den gleichen Elternknoten durchgeführt werden soll oder nicht.
- Die Methode *PivotItem.move(int count)* ist veraltet, daher wird vorgeschlagen, stattdessen die neu hinzugefügte Methode [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) zu verwenden.

Bitte beachten Sie, dass es notwendig ist, die Methoden [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) und [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) vor der Verwendung von [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) Eigenschaften und [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) Methode aufzurufen.

{{% /alert %}}

## Beispielcode

Der folgende Beispielcode erstellt eine Pivot-Tabelle und gibt dann die Positions der Pivot-Elemente im gleichen Elternknoten an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
{{< app/cells/assistant language="java" >}}
