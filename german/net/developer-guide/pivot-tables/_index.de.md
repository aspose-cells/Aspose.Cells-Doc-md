---
title: Pivot Tabelle einfügen
description: Erstellen und Formatieren von Pivot Tabellen in Excel Tabellendateien.
linktitle: Pivot Tabellen
url: /de/net/create-pivot-table/
type: docs
weight: 160
keywords: Pivot Tabelle erstellen, Pivot Tabelle einfügen, Pivot Tabelle formatieren.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Pivot-Tabelle erstellen**
Es ist möglich, Aspose.Cells zu verwenden, um programmgesteuert Pivot-Tabellen zu Tabellenkalkulationen hinzuzufügen.

### **Pivot-Tabellen-Objektmodell**
Aspose.Cells stellt eine spezielle Gruppe von Klassen im [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot)-Namespace bereit, die verwendet werden, um Pivot-Tabellen zu erstellen und zu steuern. Diese Klassen dienen zur Erstellung und Einstellung von [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-Objekten, den Bausteinen einer Pivot-Tabelle. Die Objekte sind:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) repräsentiert ein Feld in einer [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) repräsentiert eine Sammlung aller [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)-Objekte im [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) repräsentiert eine Pivot-Tabelle auf einem Arbeitsblatt.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) repräsentiert eine Sammlung aller [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-Objekte auf einem Arbeitsblatt.

### **Erstellen einer einfachen Pivot-Tabelle mithilfe von Aspose.Cells**
1. Fügen Sie Daten zu einem Arbeitsblatt mithilfe der [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-Methode des [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)-Objekts hinzu.
   Diese Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie der Arbeitsmappe eine Pivot-Tabelle hinzu, indem Sie die [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) Methode der [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)-Sammlung aufrufen, die im Arbeitsblattobjekt gekapselt ist.
1. Greifen Sie auf das neue [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-Objekt aus der [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)-Sammlung zu, indem Sie den PivotTable-Index übergeben.
1. Verwenden Sie eines der oben erklärten [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)-Objekte, um die Pivot-Tabelle zu verwalten.
Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle zum Arbeitsblatt hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}
Beim Zuweisen eines Zellenbereichs als Datenquelle muss der Bereich von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, aber "C3:A1" ist es nicht.
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}