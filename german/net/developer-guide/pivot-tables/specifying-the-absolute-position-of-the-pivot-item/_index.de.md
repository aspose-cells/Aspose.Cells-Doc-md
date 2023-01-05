---
title: Festlegen der absoluten Position des Pivot-Elements
type: docs
weight: 50
url: /de/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Manchmal muss der Benutzer die absolute Position der Pivot-Elemente angeben, Aspose.Cells API hat einige neue Eigenschaften und eine Methode zum Erreichen der Benutzeranforderungen offengelegt.

-  Hinzugefügt[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) Eigenschaft, die verwendet werden kann, um den Positionsindex in allen PivotItems unabhängig vom übergeordneten Knoten anzugeben. Hinzugefügt[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) Eigenschaft, die verwendet werden kann, um den Positionsindex in den PivotItems unter demselben übergeordneten Knoten anzugeben.
-  Hinzugefügt[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)-Methode, um das Element basierend auf dem count-Wert nach oben oder unten zu verschieben, wobei count die Nummer der Position ist, um das PivotItem nach oben oder unten zu verschieben. Wenn der Zählwert kleiner als null ist, wird das Element nach oben verschoben, während das PivotItem nach unten verschoben wird, wenn der Zählwert größer als null ist. Der isSameParent-Parameter vom booleschen Typ gibt an, ob der Verschiebevorgang im selben übergeordneten Knoten ausgeführt werden muss oder nicht.
-  Veraltet die*PivotItem.Move(int count)* Methode daher wird empfohlen, die neu hinzugefügte Methode zu verwenden[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) stattdessen.

{{% /alert %}}

 Der folgende Beispielcode erstellt eine Pivot-Tabelle und gibt dann die Positionen der Pivot-Elemente in demselben übergeordneten Knoten an. Sie können die herunterladen[Quelle Excel](5112632.xlsx) und[Excel ausgeben](5112619.xlsx) Dateien für Ihre Referenz. Wenn Sie die Excel-Ausgabedatei öffnen, sehen Sie, dass sich das Pivot-Element „4H12“ an Position 0 im übergeordneten Element „K11“ und „DIF400“ an Position 3 befindet. Ebenso befindet sich CA32 an Position 1 und AAA3 an Position 2

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Bitte beachten Sie, dass die Methoden PivotTable.RefreshData und PivotTable.CalculateData vor der Verwendung aufgerufen werden müssen[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) Eigenschaften und[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) Methode.

{{% /alert %}}
