---
title: Erstellen von Pivot Tabellen und Pivot Diagrammen
type: docs
weight: 20
url: /de/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

Eine Pivot-Tabelle ist eine interaktive Zusammenfassung von Datensätzen. Sie können beispielsweise Hunderte von Rechnungseinträgen in einer Liste in einem Arbeitsblatt haben. Eine Pivot-Tabelle kann die Rechnungen nach Kunden, Produkt oder Datum zusammenfassen. Mit Microsoft Excel ist es möglich, die Informationen in der Pivot-Tabelle schnell neu anzuordnen, indem Sie Schaltflächen an eine neue Position ziehen.

Ein Pivot-Diagramm ist eine interaktive grafische Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme wurden in Excel 2000 eingeführt. Durch die Verwendung eines Pivot-Diagramms wird es noch einfacher, die Daten zu verstehen, da die Pivot-Tabelle automatisch Teil- und Gesamtsummen erstellt.

Aspose.Cells unterstützt [Pivot-Tabellen](/cells/de/net/create-pivot-tables-and-pivot-charts/) und [Pivot-Diagramme](/cells/de/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Hinzufügen von Pivot-Tabellen und -Diagrammen**

Aspose.Cells bietet eine spezielle Reihe von Klassen zur Erstellung von Pivot-Tabellen. Diese Klassen werden verwendet, um PivotTable-Objekte zu erstellen und zu setzen, die als grundlegende Bausteine eines PivotTable-Objekts dienen:

- PivotField, ein Feld in einem Pivot-Tabellenbericht.
- PivotFields, eine Sammlung aller PivotField-Objekte in einer Pivot-Tabelle.
- PivotTable, ein Pivot-Tabellenbericht auf einem Arbeitsblatt.
- PivotTables, eine Sammlung aller PivotTable-Objekte auf dem Arbeitsblatt.

### **Vorbereitung zur Verwendung von Aspose.Cells**

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Aspose.Cells herunterladen](https://downloads.aspose.com/cells/net).
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.
      Alle [Aspose](http://www.aspose.com/) Komponenten, wenn sie installiert sind, arbeiten im Evaluierungsmodus. Der Evaluierungsmodus hat keine zeitliche Begrenzung und fügt nur Wasserzeichen in erstellte Dokumente ein. Um mit der Komponente in vollem Umfang zu arbeiten, benötigen Sie eine gültige Lizenz.
1. Ein Projekt erstellen:
   1. Starten Sie Visual Studio.Net.
   1. Erstellen Sie eine neue Konsolenanwendung.
1. Fügen Sie Verweise hinzu:
   Fügen Sie einen Verweis auf das Aspose.Cells-Komponent in Ihr Projekt ein, beispielsweise ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Hinzufügen einer Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen:

1. Fügen Sie einige Daten in Zellen eines Arbeitsblatts mit der PutValue/setValue-Methode eines Cell-Objekts ein. Sie können auch eine Vorlagendatei verwenden, die bereits mit Daten gefüllt ist. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Methode add der PivotTables-Sammlung aufrufen (die im Arbeitsblatt-Objekt gekapselt ist).
1. Greifen Sie auf das neue PivotTable-Objekt aus der PivotTables-Sammlung zu, indem Sie seinen Index übergeben. # Verwenden Sie eines der in dem PivotTable-Objekt gekapselten Pivot-Tabellenobjekte, um die Tabelle zu verwalten.

Codebeispiele finden Sie unten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Hinzufügen eines Pivot-Diagramms**

Um ein PivotChart mit Aspose.Cells zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie den PivotSource des Diagramms so, dass er auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Setzen Sie andere Attribute.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
