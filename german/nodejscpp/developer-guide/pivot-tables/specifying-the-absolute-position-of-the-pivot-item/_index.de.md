---
title: Angabe der absoluten Position des Pivot Elements
type: docs
weight: 50
url: /de/nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Manchmal muss der Benutzer die absolute Position der Pivot-Elemente angeben, die API von Aspose.Cells for Node.js via C++ hat einige neue Eigenschaften und eine Methode freigegeben, um die Benutzeranforderung zu erfüllen.

- Hinzugefügte [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-) Eigenschaft, die verwendet werden kann, um den Position-Index in allen Pivot-Elementen unabhängig vom übergeordneten Knoten anzugeben. Hinzugefügte [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) Eigenschaft, die verwendet werden kann, um den Position-Index in den Pivot-Elementen unter dem gleichen übergeordneten Knoten anzugeben.
- Hinzugefügte [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) Methode, um das Element basierend auf dem Zählwert nach oben oder unten zu bewegen, wobei der Zählwert die Anzahl der Positionen angibt, um das Pivot-Element nach oben oder unten zu bewegen. Wenn der Zählwert kleiner als null ist, wird das Element nach oben verschoben, wenn der Zählwert größer als null ist, wird das Pivot-Element nach unten verschoben. Der boolesche Typ-Parameter isSameParent gibt an, ob die Verschiebungsoperation im gleichen übergeordneten Knoten durchgeführt werden soll oder nicht.
- Die *PivotItem.move(int count)* Methode ist veraltet, daher wird empfohlen, stattdessen die neu hinzugefügte Methode [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) zu verwenden.

{{% /alert %}}

Der folgende Beispielcode erstellt ein Pivot-Table und legt dann die Positionen der Pivot-Elemente im gleichen übergeordneten Knoten fest. Sie können die [Quell-Excel-Datei](5112632.xlsx) und die [Ausgabe-Excel-Datei](5112619.xlsx) für Ihre Referenz herunterladen. Wenn Sie die Ausgabe-Excel-Datei öffnen, sehen Sie, dass das Pivot-Element "4H12" sich an der 0. Position im übergeordneten Knoten "K11" befindet und "DIF400" sich an der 3. Position befindet. Ebenso befindet sich CA32 an Position 1 und AAA3 an Position 2.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

Bitte beachten Sie, dass es notwendig ist, die Methoden PivotTable.RefreshData und PivotTable.CalculateData aufzurufen, bevor Sie die [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-), [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) Eigenschaften und [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) Methode verwenden.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
