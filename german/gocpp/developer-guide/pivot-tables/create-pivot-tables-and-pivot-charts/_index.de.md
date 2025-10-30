---
title: Pivot Tabellen und Pivot Diagramme mit Golang via C++ erstellen
linktitle: Erstellen von Pivot Tabellen und Pivot Diagrammen
type: docs
weight: 20
url: /de/go-cpp/create-pivot-tables-and-pivot-charts/
description: Erfahren Sie, wie Sie Pivot Tabellen und Pivot Diagramme in Excel Dateien mit Aspose.Cells und Golang via C++ erstellen.
---

{{% alert color="primary" %}}

Eine Pivot-Tabelle ist eine interaktive Zusammenfassung von Datensätzen. Zum Beispiel haben Sie vielleicht Hunderte von Rechnungsdatensätzen in einer Liste auf einem Arbeitsblatt. Eine Pivot-Tabelle kann die Rechnungen nach Kunde, Produkt oder Datum zusammenfassen. Mit Microsoft Excel ist es möglich, die Informationen in der Pivot-Tabelle durch Drag & Drop schnell neu anzuordnen.

Ein Pivot-Diagramm ist eine interaktive grafische Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme wurden in Excel 2000 eingeführt. Durch die Verwendung eines Pivot-Diagramms wird es noch einfacher, die Daten zu verstehen, da die Pivot-Tabelle automatisch Teil- und Gesamtsummen erstellt.

Aspose.Cells unterstützt [Pivot-Tabellen](/cells/de/cpp/create-pivot-tables-and-pivot-charts/) und [Pivot-Diagramme](/cells/de/cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Hinzufügen von Pivot-Tabellen und -Diagrammen**

Aspose.Cells bietet eine spezielle Reihe von Klassen zur Erstellung von Pivot-Tabellen. Diese Klassen werden verwendet, um PivotTable-Objekte zu erstellen und zu setzen, die als grundlegende Bausteine eines PivotTable-Objekts dienen:

- **PivotFeld**, ein Feld in einem Pivot-Tabellenbericht.
- **PivotFelder**, eine Sammlung aller PivotFeld-Objekte in einer Pivot-Tabelle.
- **PivotTabelle**, ein Pivot-Tabellenbericht auf einem Arbeitsblatt.
- **PivotTabellen**, eine Sammlung aller PivotTable-Objekte auf dem Arbeitsblatt.

### **Vorbereitung zur Verwendung von Aspose.Cells**

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Aspose.Cells herunterladen](https://downloads.aspose.com/cells/go-cpp/).
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.
      Alle [Aspose](http://www.aspose.com/) Komponenten, wenn sie installiert sind, arbeiten im Bewertungmodus. Der Bewertungmodus hat keine Zeitbegrenzung und fügt nur Wasserzeichen in die erstellten Dokumente ein. Um die Komponente vollständig zu nutzen, benötigen Sie eine gültige Lizenz.
1. Ein Projekt erstellen:
   1. Starten Sie Ihre C++-IDE (z.B. Visual Studio).
   1. Erstellen Sie eine neue Konsolenanwendung.
1. Fügen Sie Verweise hinzu:
   Fügen Sie einen Verweis auf die Aspose.Cells-Komponente in Ihr Projekt ein, z.B. `...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Hinzufügen einer Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen:

1. Fügen Sie Daten zu den Zellen eines Arbeitsblatts mit der Methode `PutValue` eines `Cell`-Objekts hinzu. Sie können auch eine bereits mit Daten gefüllte Vorlage verwenden. Die Daten werden als Datenquelle für die Pivot-Tabelle verwendet.
1. Fügen Sie eine Pivot-Tabelle zum Arbeitsblatt hinzu, indem Sie die Methode `Add` der `PivotTables`-Sammlung aufrufen (eingeschlossen im `Worksheet`-Objekt).
1. Greifen Sie auf das neue `PivotTable`-Objekt aus der `PivotTables`-Sammlung durch Angabe seines Index zu. Verwenden Sie eines der Pivot-Tabellen-Objekte, die im `PivotTable`-Objekt eingeschlossen sind, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts.go" >}}
### **Hinzufügen eines Pivot-Diagramms**

Um ein PivotChart mit Aspose.Cells zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie die `PivotSource` des Diagramms so, dass sie sich auf eine vorhandene Pivot-Tabelle im Spreadsheet bezieht.
1. Setzen Sie andere Attribute.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts-1.go" >}}
