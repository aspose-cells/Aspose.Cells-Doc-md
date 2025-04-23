---
title: Wie man mit Aspose.Cells für Python via .NET ein PivotChart hinzufügt
linktitle: Pivot Diagramm
type: docs
weight: 100
url: /de/python-net/how-to-add-pivot-chart/
description: Wie man mit Aspose.Cells für Python via .NET ein PivotChart hinzufügt.
keywords: PivotChart
---
## Was ist ein PivotChart

Ein Pivot-Chart ist eine visuelle Darstellung der Daten in einer Pivot-Tabelle. Pivot-Charts bieten eine Möglichkeit, Zusammenfassungen zu erstellen, zu analysieren, zu erkunden und präsentabel zu machen. Hier sind einige wichtige Funktionen und Aspekte von Pivot-Charts:

1. Dynamische Datenrepräsentation: Pivot-Charts aktualisieren sich automatisch, um Änderungen an der Pivot-Tabelle widerzuspiegeln. Wenn Felder in der Pivot-Tabelle hinzugefügt oder entfernt werden, wird das Pivot-Chart entsprechend aktualisiert.

1. Interaktiv: Pivot-Charts sind interaktiv, ermöglichen es Benutzern, Daten zu filtern, zu sortieren und zu vertiefen. Dadurch ist es einfach, verschiedene Aspekte des Datensatzes zu erkunden.

1. Flexibles Layout: Benutzer können das Layout des Pivot-Diagrams durch Ziehen und Ablegen von Feldern ändern, was Flexibilität bei der Visualisierung von Daten bietet.

1. Verschiedene Diagrammtypen: Pivot-Diagramme können mit verschiedenen Diagrammtypen wie Säulendiagrammen, Liniendiagrammen, Kreisdiagrammen und mehr erstellt werden, je nach Art der Daten und den gewünschten Erkenntnissen.

1. Zusammenfassung: Pivot-Diagramme fassen große Datenmengen zusammen und können Summen, Durchschnitte, Zählen oder andere Zusammenfassungsstatistiken anzeigen.

1. Filtern: Sie bieten Filterfunktionen, mit denen nur Daten angezeigt werden, die bestimmte Kriterien erfüllen.

<br>
Pivot-Diagramme werden häufig in Business Intelligence und Datenanalyse verwendet, um eine klare und prägnante visuelle Zusammenfassung komplexer Datensätze zu bieten. Sie sind ein mächtiges Werkzeug, um datengetriebene Entscheidungen zu treffen.

## Wie man mit Aspose.Cells für Python Excel-Library ein PivotChart hinzufügt

### **Hinzufügen einer Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells für Python via .NET zu erstellen:

1. Fügen Sie einige Daten in Zellen eines Arbeitsblatts mit der PutValue/setValue-Methode eines Cell-Objekts ein. Sie können auch eine Vorlagendatei verwenden, die bereits mit Daten gefüllt ist. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Methode add der PivotTables-Sammlung aufrufen (die im Arbeitsblatt-Objekt gekapselt ist).
1. Greifen Sie auf das neue PivotTable-Objekt aus der PivotTables-Sammlung zu, indem Sie seinen Index übergeben. # Verwenden Sie eines der in dem PivotTable-Objekt gekapselten Pivot-Tabellenobjekte, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotTable-1.py" >}}

### **Hinzufügen eines Pivot-Diagramms**

Um ein PivotChart mit Aspose.Cells für Python via .NET zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie den PivotSource des Diagramms so, dass er auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Setzen Sie andere Attribute.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotChart-1.py" >}}

