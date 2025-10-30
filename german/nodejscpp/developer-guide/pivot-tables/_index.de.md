---
title: Pivot Tabelle einfügen
linktitle: Pivot Tabellen
type: docs
weight: 160
url: /de/nodejs-cpp/create-pivot-table/
description: Erstellen und Formatieren von Pivot Tabellen in Excel Tabellendateien.
---

## **Pivot-Tabelle erstellen**

Es ist möglich, Aspose.Cells for Node.js via C++ zu verwenden, um Pivot-Tabellen programmatisch zu Arbeitsblättern hinzuzufügen.

### **Pivot-Tabellen-Objektmodell**

Aspose.Cells for Node.js via C++ stellt eine spezielle Gruppe von Klassen bereit, mit denen Pivot-Tabellen erstellt und gesteuert werden können. Diese Klassen werden verwendet, um [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-Objekte zu erstellen und zu setzen, die Bausteine einer Pivot-Tabelle sind. Die Objekte sind:

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) repräsentiert ein Feld in einer [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) repräsentiert eine Sammlung aller [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield)-Objekte im [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) repräsentiert eine Pivot-Tabelle auf einem Arbeitsblatt.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) repräsentiert eine Sammlung aller [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-Objekte auf einem Arbeitsblatt.

### **Erstellen einer einfachen Pivot-Tabelle mithilfe von Aspose.Cells**

1. Fügen Sie Daten zu einem Arbeitsblatt mithilfe der [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Methode des [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)-Objekts hinzu.
   Diese Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie der Arbeitsmappe eine Pivot-Tabelle hinzu, indem Sie die [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) Methode der [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection)-Sammlung aufrufen, die im Arbeitsblattobjekt gekapselt ist.
1. Greifen Sie auf das neue [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-Objekt aus der [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection)-Sammlung zu, indem Sie den PivotTable-Index übergeben.
1. Verwenden Sie eines der oben erklärten [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable)-Objekte, um die Pivot-Tabelle zu verwalten.

Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle zum Arbeitsblatt hinzugefügt.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

Beim Zuweisen eines Zellenbereichs als Datenquelle muss der Bereich von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, aber "C3:A1" ist es nicht.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
