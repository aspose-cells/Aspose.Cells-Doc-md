---
title: Erstellen von Pivot Tabellen und Pivot Diagrammen
type: docs
weight: 20
url: /de/python-net/create-pivot-tables-and-pivot-charts/
description: Wie man Pivot Tabellen und Pivot Charts mit Aspose.Cells für Python via .NET hinzufügt.
keywords: Aspose.Cells für Python Excel, Excel Python Bibliothek, Pivot Tabellen und Pivot Charts hinzufügen mit der Aspose.Cells für Python Excel Bibliothek.
---

{{% alert color="primary" %}}

Eine Pivot-Tabelle ist eine interaktive Zusammenfassung von Datensätzen. Sie können beispielsweise Hunderte von Rechnungseinträgen in einer Liste in einem Arbeitsblatt haben. Eine Pivot-Tabelle kann die Rechnungen nach Kunden, Produkt oder Datum zusammenfassen. Mit Microsoft Excel ist es möglich, die Informationen in der Pivot-Tabelle schnell neu anzuordnen, indem Sie Schaltflächen an eine neue Position ziehen.

Ein Pivot-Diagramm ist eine interaktive grafische Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme wurden in Excel 2000 eingeführt. Durch die Verwendung eines Pivot-Diagramms wird es noch einfacher, die Daten zu verstehen, da die Pivot-Tabelle automatisch Teil- und Gesamtsummen erstellt.

Aspose.Cells für Python via .NET unterstützt [Pivot-Tabellen](/cells/de/python-net/create-pivot-tables-and-pivot-charts/) und [Pivot-Charts](/cells/de/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Pivot-Tabellen und -Diagramme mit der Aspose.Cells für Python Excel-Bibliothek hinzufügen**

Aspose.Cells für Python via .NET bietet eine spezielle Reihe von Klassen zur Erstellung von Pivot-Tabellen. Diese Klassen werden verwendet, um PivotTable-Objekte zu erstellen und zu setzen, die als grundlegende Bausteine eines PivotTable-Objekts dienen:

- PivotField, ein Feld in einem Pivot-Tabellenbericht.
- PivotFields, eine Sammlung aller PivotField-Objekte in einer Pivot-Tabelle.
- PivotTable, ein Pivot-Tabellenbericht auf einem Arbeitsblatt.
- PivotTables, eine Sammlung aller PivotTable-Objekte auf dem Arbeitsblatt.

### **Bereiten Sie sich darauf vor, Aspose.Cells für Python via .NET zu verwenden**
1. Installieren Sie Aspose.Cells für Python via .NET von [pypi](https://pypi.org/project/aspose-cells-python/) mit dem Befehl: $ pip install aspose-cells-python.
1. Sie können auch die schrittweisen Anweisungen zur Installation von "Aspose.Cells für Python via .NET" in Ihrer Entwicklerumgebung befolgen.


### **Wie man ein Pivot-Table mit der Aspose.Cells for Python Excel-Bibliothek hinzufügt**

Um eine Pivot-Tabelle mit Aspose.Cells für Python via .NET zu erstellen:

1. Fügen Sie einige Daten zu Zellen auf einem Arbeitsblatt hinzu, indem Sie die put_value-Methode eines Cell-Objekts verwenden. Sie verwenden auch eine Vorlagendatei, die bereits mit Daten gefüllt ist. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Methode add der PivotTables-Sammlung aufrufen (die im Arbeitsblatt-Objekt gekapselt ist).
1. Greifen Sie auf das neue PivotTable-Objekt aus der PivotTables-Sammlung zu, indem Sie seinen Index übergeben. # Verwenden Sie eines der in dem PivotTable-Objekt gekapselten Pivot-Tabellenobjekte, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **Wie man ein Pivot-Diagramm mit Aspose.Cells für Python Excel-Bibliothek hinzufügt**

Um ein PivotChart mit Aspose.Cells für Python via .NET zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie den PivotSource des Diagramms so, dass er auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Setzen Sie andere Attribute.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

