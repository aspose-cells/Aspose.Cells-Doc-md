---
title: Pivot Tabelle einfügen
description: Erstellen und Formatieren einer Pivot Tabelle mit Aspose.Cells für Python via .NET.
linktitle: Pivot Tabellen
url: /de/python-net/pivot-tables/
type: docs
weight: 160
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
keywords: Pivot Tabelle erstellen, Pivot Tabelle einfügen, Pivot Tabelle formatieren.
---

## **Pivot-Tabelle erstellen**
Es ist möglich, mithilfe von Aspose.Cells für Python via .NET Pivot-Tabellen programmatisch zu Arbeitsmappen hinzuzufügen.

### **Pivot-Tabellen-Objektmodell**
Aspose.Cells für Python via .NET bietet eine spezielle Reihe von Klassen im [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/)-Namespace, die verwendet werden, um Pivot-Tabellen zu erstellen und zu steuern. Diese Klassen werden verwendet, um [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)-Objekte zu erstellen und zu setzen, die die Bausteine einer Pivot-Tabelle sind. Die Objekte sind:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) repräsentiert ein Feld in einer [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) repräsentiert eine Sammlung aller [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield)-Objekte im [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) repräsentiert eine Pivot-Tabelle auf einem Arbeitsblatt.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) repräsentiert eine Sammlung aller [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-Objekte auf einem Arbeitsblatt.

### **Erstellen einer einfachen Pivot-Tabelle mithilfe von Aspose.Cells**
1. Fügen Sie Daten zu einem Arbeitsblatt mithilfe der [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Methode des [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str)-Objekts hinzu.
   Diese Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie der Arbeitsmappe eine Pivot-Tabelle hinzu, indem Sie die [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) Methode der [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)-Sammlung aufrufen, die im Arbeitsblattobjekt gekapselt ist.
1. Greifen Sie auf das neue [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-Objekt aus der [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)-Sammlung zu, indem Sie den PivotTable-Index übergeben.
1. Verwenden Sie eines der oben erklärten [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-Objekte, um die Pivot-Tabelle zu verwalten.
Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle zum Arbeitsblatt hinzugefügt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}
Beim Zuweisen eines Zellenbereichs als Datenquelle muss der Bereich von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, aber "C3:A1" ist es nicht.
{{% /alert %}}

## **Erweiterte Themen**

{{< app/cells/assistant language="python-net" >}}