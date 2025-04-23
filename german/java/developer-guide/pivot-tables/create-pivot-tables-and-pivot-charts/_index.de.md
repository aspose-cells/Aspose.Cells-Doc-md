---
title: Erstellen von Pivot Tabellen und Pivot Diagrammen
type: docs
weight: 10
url: /de/java/create-pivot-tables-and-pivot-charts/
description: Erstellen von Pivot Tabellen und Pivot Charts mit der Aspose.Cells for Java API.
keywords: excel pivot tabelle java erstellen, excel pivot diagramm java erstellen, excel pivot tabelle und pivot diagramm java erstellen, erstellen von excel pivot tabelle java, erstellen von excel pivot diagramm java, erstellen von excel pivot tabelle und pivot diagramm java, java erstellen von excel pivot tabelle und pivot diagramm, wie man excel pivot tabelle und pivot diagramm java erstellt
---

{{% alert color="primary" %}}

Eine Pivot-Tabelle ist eine interaktive Zusammenfassung von Datensätzen. Sie können beispielsweise Hunderte von Rechnungseinträgen in einer Liste in einem Arbeitsblatt haben. Eine Pivot-Tabelle kann die Rechnungen nach Kunden, Produkt oder Datum zusammenfassen. Mit Microsoft Excel ist es möglich, die Informationen in der Pivot-Tabelle schnell neu anzuordnen, indem Sie Schaltflächen an eine neue Position ziehen.

Ein Pivot-Diagramm ist eine interaktive grafische Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme wurden in Excel 2000 eingeführt. Durch die Verwendung eines Pivot-Diagramms wird es noch einfacher, die Daten zu verstehen, da die Pivot-Tabelle automatisch Teil- und Gesamtsummen erstellt.

Aspose.Cells unterstützt [Pivot-Tabellen](/cells/de/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) und [Pivot-Diagramme](/cells/de/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Hinzufügen von Pivot-Tabellen und -Diagrammen**

Aspose.Cells bietet eine spezielle Reihe von Klassen zur Erstellung von Pivot-Tabellen. Diese Klassen werden verwendet, um PivotTable-Objekte zu erstellen und zu setzen, die als grundlegende Bausteine eines PivotTable-Objekts dienen:

- PivotField, ein Feld in einem Pivot-Tabellenbericht.
- PivotFields, eine Sammlung aller PivotField-Objekte in einer Pivot-Tabelle.
- PivotTable, ein Pivot-Tabellenbericht auf einem Arbeitsblatt.
- PivotTables, eine Sammlung aller PivotTable-Objekte auf dem Arbeitsblatt.

### **Vorbereitung zur Verwendung von Aspose.Cells**

1. Laden Sie Aspose.Cells.Zip herunter und installieren Sie es:
   1. [Aspose.Cells for Java herunterladen](https://downloads.aspose.com/cells/java).
   1. Entpacken Sie es auf Ihrem Entwicklungscomputer.
      Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren nach der Installation im Evaluierungsmodus. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. Erstellen Sie ein Projekt
   1. Sie können entweder ein Projekt mit einem Java-Editor wie z.B. Eclipse erstellen oder ein einfaches Programm mit einem Notepad erstellen.
1. Fügen Sie den Klassenpfad hinzu:
   Um den Klassenpfad in Eclipse zu setzen:
   1. Extrahieren Sie die Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
   1. Setzen Sie den Klassenpfad des Projekts in Eclipse:
   1. Wählen Sie Ihr Projekt in Eclipse und klicken Sie dann auf Menüs Projekt-Eigenschaften.
   1. Wählen Sie im linken Bereich des Popup-Fensters "Java Build Path" aus, wählen Sie dann die Registerkarte "Bibliotheken" aus, klicken Sie auf "JARs hinzufügen" oder "Externe JARs hinzufügen", um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und fügen Sie sie zu den Erstellungspfaden hinzu.
   1. Schreiben Sie eine Anwendung, um die APIs der Aspose-Komponenten aufzurufen.
      Oder Sie können es auch zur Laufzeit im DOS-Prompt unter Windows festlegen.

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Erstellen einer Pivot-Tabelle**

Um eine Pivot-Tabelle mit Aspose.Cells zu erstellen:

1. Fügen Sie einige Daten in Zellen eines Arbeitsblatts mit der PutValue/setValue-Methode eines Cell-Objekts ein. Sie können auch eine Vorlagendatei verwenden, die bereits mit Daten gefüllt ist. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die Methode add der PivotTables-Sammlung aufrufen (die im Arbeitsblatt-Objekt gekapselt ist).
1. Greifen Sie auf das neue PivotTable-Objekt aus der PivotTables-Sammlung zu, indem Sie seinen Index übergeben.
1. Verwenden Sie eines der im PivotTable-Objekt gekapselten Pivot-Table-Objekte, um das Table zu verwalten.

Ein Codebeispiel wird unten gegeben. Wenn der Code ausgeführt wird, wird eine neue Datei generiert: pivotTable_test.xls.

**Eingangsdaten** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Das Output-Pivot-Table**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Erstellen eines Pivot-Diagramms basierend auf dem Pivot-Table**

Um ein Pivot-Diagramm mit Aspose.Cells zu erstellen:

1. Fügen Sie ein Diagramm hinzu.
1. Setzen Sie den PivotSource des Diagramms so, dass er auf eine vorhandene Pivot-Tabelle in der Tabelle verweist.
1. Setzen Sie andere Attribute.

Unten ist der Code, den das Bauteil verwendet, um die Aufgabe zu erfüllen. Wenn der Code ausgeführt wird, wird eine neue Datei generiert: pivotChart_test.xls.

**Das Pivot-Diagrammblatt**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie man Pivot-Tabellen und Pivot-Diagramme mit Aspose.Cells erstellt. Hoffentlich wird es Ihnen helfen, diese Funktionen in Ihren eigenen Szenarien zu verwenden.

Aspose.Cells hat jahrelange Forschung, Design und sorgfältige Abstimmung genossen.

Wir begrüßen Ihre Anfragen, Kommentare und Vorschläge im [Aspose.Cells-Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine schnelle Antwort.

{{% /alert %}}

## Verwandte Artikel

- [Benutzerdefiniertes Sortieren in der Pivot-Tabelle](/cells/de/java/custom-sorting-in-pivot-table/)
- [Pivot-Tabelle formatieren](/cells/de/java/formatting-pivot-table/)
- [Pivot-Tabelle aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen](/cells/de/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Pivot-Tabellen-Ribbons deaktivieren](/cells/de/java/disable-pivot-table-ribbons/)

{{< app/cells/assistant language="java" >}}
