---
title: Erstellen Sie Pivot-Tabellen und Pivot-Diagramme
type: docs
weight: 20
url: /de/python-net/create-pivot-tables-and-pivot-charts/
description: So fügen Sie Pivot-Tabellen und Pivot-Diagramme mit Aspose.Cells for Python via .NET hinzu.
keywords: Add Pivot Tables and Pivot Charts.
---
{{% alert color="primary" %}}

Eine Pivot-Tabelle ist eine interaktive Zusammenfassung von Datensätzen. Sie können beispielsweise Hunderte von Rechnungseinträgen in einer Liste in einem Arbeitsblatt haben. Eine Pivot-Tabelle kann die Rechnungen nach Kunde, Produkt oder Datum summieren. Mit Microsoft Excel ist es möglich, die Informationen in der Pivot-Tabelle schnell neu anzuordnen, indem Sie Schaltflächen an eine neue Position ziehen.

Ein Pivot-Diagramm ist eine interaktive grafische Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme wurden in Excel 2000 eingeführt. Die Verwendung eines Pivot-Diagramms macht es noch einfacher, die Daten zu verstehen, da die Pivot-Tabelle Zwischensummen und Summen automatisch erstellt.

 Aspose.Cells for Python via .NET unterstützt[Pivot-Tabellen](/cells/de/python-net/create-pivot-tables-and-pivot-charts/) Und[Pivot-Diagramme](/cells/de/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

##  **Hinzufügen von Pivot-Tabellen und Diagrammen**

Aspose.Cells for Python via .NET bietet einen speziellen Satz von Klassen, die zum Erstellen von Pivot-Tabellen verwendet werden. Diese Klassen werden zum Erstellen und Festlegen von PivotTable-Objekten verwendet, die als Grundbausteine eines PivotTable-Objekts fungieren:

- PivotField, ein Feld in einem Pivot-Tabellenbericht.
- PivotFields, eine Sammlung aller PivotField-Objekte in einer Pivot-Tabelle.
- PivotTable, ein PivotTable-Bericht auf einem Arbeitsblatt.
- PivotTables, eine Sammlung aller PivotTable-Objekte im Arbeitsblatt.

###  **Vorbereitung zur Verwendung von Aspose.Cells for Python via .NET**
1.  Installieren Sie Aspose.Cells for Python via .NET von[Pypi](https://pypi.org/project/aspose-cells-python/)verwenden Sie den Befehl als: $ pip install aspose-cells-python.
1. Sie können auch die Schritt-für-Schritt-Anleitung zur Installation von „Aspose.Cells for Python via .NET“ in Ihrer Entwicklerumgebung befolgen.


###  **Hinzufügen einer Pivot-Tabelle**

So erstellen Sie eine Pivot-Tabelle mit Aspose.Cells for Python via .NET:

1. Fügen Sie mithilfe der put_value-Methode eines Cell-Objekts einige Daten zu den Zellen eines Arbeitsblatts hinzu. Sie verwenden auch eine bereits mit Daten gefüllte Vorlagendatei. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Add-Methode der PivotTables-Sammlung aufrufen (gekapselt im Worksheet-Objekt).
1. Greifen Sie über die PivotTables-Auflistung auf das neue PivotTable-Objekt zu, indem Sie dessen Index übergeben. # Verwenden Sie eines der im PivotTable-Objekt gekapselten Pivot-Tabellenobjekte, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

###  **Hinzufügen eines Pivot-Diagramms**

So erstellen Sie ein PivotChart mit Aspose.Cells for Python via .NET:

1. Fügen Sie ein Diagramm hinzu.
1. Legen Sie die PivotSource des Diagramms so fest, dass sie auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Legen Sie andere Attribute fest.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

