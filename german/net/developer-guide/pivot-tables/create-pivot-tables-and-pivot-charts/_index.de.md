---
title: Erstellen Sie Pivot-Tabellen und Pivot-Diagramme
type: docs
weight: 20
url: /de/net/create-pivot-tables-and-pivot-charts/
---
{{% alert color="primary" %}}

Eine Pivot-Tabelle ist eine interaktive Zusammenfassung von Datensätzen. Beispielsweise können Sie Hunderte von Rechnungseinträgen in einer Liste in einem Arbeitsblatt haben. Eine Pivot-Tabelle kann die Rechnungen nach Kunde, Produkt oder Datum summieren. Mit Microsoft Excel ist es möglich, die Informationen in der Pivot-Tabelle schnell neu anzuordnen, indem Sie Schaltflächen an eine neue Position ziehen.

Ein Pivot-Diagramm ist eine interaktive grafische Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme wurden in Excel 2000 eingeführt. Die Verwendung eines Pivot-Diagramms macht es noch einfacher, die Daten zu verstehen, da die Pivot-Tabelle Zwischensummen und Summen automatisch erstellt.

 Aspose.Cells unterstützt[Pivot-Tabellen](/cells/de/net/create-pivot-tables-and-pivot-charts/) und[Pivot-Diagramme](/cells/de/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Hinzufügen von Pivot-Tabellen und Diagrammen**

Aspose.Cells stellt einen speziellen Satz von Klassen bereit, die zum Erstellen von Pivot-Tabellen verwendet werden. Diese Klassen werden zum Erstellen und Festlegen von PivotTable-Objekten verwendet, die als grundlegende Bausteine eines PivotTable-Objekts fungieren:

- PivotField, ein Feld in einem Pivot-Tabellenbericht.
- PivotFields, eine Sammlung aller PivotField-Objekte in einer Pivot-Tabelle.
- PivotTable, ein PivotTable-Bericht auf einem Arbeitsblatt.
- PivotTables, eine Auflistung aller PivotTable-Objekte auf dem Arbeitsblatt.

### **Vorbereitung zur Verwendung von Aspose.Cells**

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Aspose.Cells herunterladen](https://downloads.aspose.com/cells/net).
 1. Installieren Sie es auf Ihrem Entwicklungscomputer.
 Alle[Aspose](http://www.aspose.com/) Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein. Um mit der Komponente in vollem Umfang arbeiten zu können, benötigen Sie eine gültige Lizenz.
1. Erstellen Sie ein Projekt:
 1. Starten Sie Visual Studio.Net.
 1. Erstellen Sie eine neue Konsolenanwendung.
1. Referenzen hinzufügen:
 Fügen Sie Ihrem Projekt einen Verweis auf die Komponente Aspose.Cells hinzu, z. B. ...\Programme\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Hinzufügen einer Pivot-Tabelle**

So erstellen Sie eine Pivot-Tabelle mit Aspose.Cells:

1. Fügen Sie mithilfe der PutValue/setValue-Methode eines Cell-Objekts einige Daten zu Arbeitsblattzellen hinzu. Sie verwenden auch eine bereits mit Daten gefüllte Vorlagendatei. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die add-Methode der PivotTables-Auflistung aufrufen (eingekapselt im Worksheet-Objekt).
1. Greifen Sie auf das neue PivotTable-Objekt aus der PivotTables-Auflistung zu, indem Sie seinen Index übergeben. # Verwenden Sie eines der im PivotTable-Objekt gekapselten PivotTable-Objekte, um die Tabelle zu verwalten.

Codebeispiele sind unten angegeben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Hinzufügen eines Pivot-Diagramms**

So erstellen Sie ein PivotChart mit Aspose.Cells:

1. Fügen Sie ein Diagramm hinzu.
1. Legen Sie die PivotSource des Diagramms fest, um auf eine vorhandene Pivot-Tabelle in der Tabelle zu verweisen.
1. Legen Sie andere Attribute fest.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

