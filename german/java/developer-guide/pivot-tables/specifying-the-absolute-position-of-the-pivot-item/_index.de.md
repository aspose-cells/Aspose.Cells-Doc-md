---
title: Angabe der absoluten Position des Pivot-Elements
type: docs
weight: 40
url: /de/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Manchmal muss der Benutzer die absolute Position der Pivot-Elemente angeben, Aspose.Cells API hat einige neue Eigenschaften und eine Methode zum Erreichen dieser Benutzeranforderung bereitgestellt.

-  Hinzugefügt[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) Eigenschaft, die verwendet werden kann, um den Positionsindex in allen PivotItems unabhängig vom übergeordneten Knoten anzugeben. Hinzugefügt[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) Eigenschaft, die verwendet werden kann, um den Positionsindex in den PivotItems unter demselben übergeordneten Knoten anzugeben.
-  Hinzugefügt[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean))-Methode, um das Element basierend auf dem Zählwert nach oben oder unten zu verschieben, wobei die Anzahl die Anzahl der Positionen ist, um die das PivotItem nach oben oder unten verschoben werden soll. Wenn der Zählwert kleiner als null ist, wird das Element nach oben verschoben, während, wenn der Zählwert größer als null ist, das PivotItem nach unten verschoben wird. Der isSameParent-Parameter vom booleschen Typ gibt an, ob der Verschiebevorgang im selben übergeordneten Knoten ausgeführt werden muss oder nicht.
-  Veraltet die*PivotItem.move(int count)* Methode, daher wird empfohlen, die neu hinzugefügte Methode zu verwenden[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) stattdessen.

 Bitte beachten Sie, dass ein Anruf erforderlich ist[**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) und[**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ) Methoden vor der Verwendung[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) Eigenschaften und[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) Methode.

{{% /alert %}}

## Beispielcode

Der folgende Beispielcode erstellt eine Pivot-Tabelle und gibt dann die Positionen der Pivot-Elemente in demselben übergeordneten Knoten an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
