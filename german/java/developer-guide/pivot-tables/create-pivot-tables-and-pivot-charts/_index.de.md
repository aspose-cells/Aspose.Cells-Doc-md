---
title: Erstellen Sie Pivot-Tabellen und Pivot-Diagramme
type: docs
weight: 10
url: /de/java/create-pivot-tables-and-pivot-charts/
description: Erstellen Sie Pivot-Tabellen und Pivot-Diagramme mit Aspose.Cells for Java API.
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

Eine Pivot-Tabelle ist eine interaktive Zusammenfassung von Datensätzen. Beispielsweise können Sie Hunderte von Rechnungseinträgen in einer Liste in einem Arbeitsblatt haben. Eine Pivot-Tabelle kann die Rechnungen nach Kunde, Produkt oder Datum summieren. Mit Microsoft Excel ist es möglich, die Informationen in der Pivot-Tabelle schnell neu anzuordnen, indem Sie Schaltflächen an eine neue Position ziehen.

Ein Pivot-Diagramm ist eine interaktive grafische Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme wurden in Excel 2000 eingeführt. Die Verwendung eines Pivot-Diagramms macht es noch einfacher, die Daten zu verstehen, da die Pivot-Tabelle Zwischensummen und Summen automatisch erstellt.

 Aspose.Cells unterstützt[Pivot-Tabellen](/cells/de/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) und[Pivot-Diagramme](/cells/de/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **Hinzufügen von Pivot-Tabellen und Diagrammen**

Aspose.Cells stellt einen speziellen Satz von Klassen bereit, die zum Erstellen von Pivot-Tabellen verwendet werden. Diese Klassen werden zum Erstellen und Festlegen von PivotTable-Objekten verwendet, die als grundlegende Bausteine eines PivotTable-Objekts fungieren:

- PivotField, ein Feld in einem Pivot-Tabellenbericht.
- PivotFields, eine Sammlung aller PivotField-Objekte in einer Pivot-Tabelle.
- PivotTable, ein PivotTable-Bericht auf einem Arbeitsblatt.
- PivotTables, eine Auflistung aller PivotTable-Objekte auf dem Arbeitsblatt.

### **Vorbereitung zur Verwendung von Aspose.Cells**

1. Laden Sie Aspose.Cells.Zip herunter und installieren Sie es:
   1. [Herunterladen Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Entpacken Sie es auf Ihrem Entwicklungscomputer.
 Alles[Aspose](http://www.aspose.com/) Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.
1. Erstellen Sie ein Projekt
 1. Sie können entweder ein Projekt mit einem Java-Editor erstellen, z. B. Eclipse, oder ein einfaches Programm mit einem NotePad erstellen.
1. Klassenpfad hinzufügen:
 So legen Sie einen Klassenpfad mit Eclipse fest:
1. Extrahieren Sie Aspose.Cells.jar und dom4j_1.6.1.jar aus Aspose.Cells.zip.
 1. Legen Sie den Klassenpfad des Projekts in Eclipse fest:
1. Wählen Sie Ihr Projekt in Eclipse aus und klicken Sie dann auf Menüs Projekt-Eigenschaften.
 1. Wählen Sie „Java Build Path“ auf der linken Seite des Popup-Fensters, wählen Sie dann die Registerkarte „Bibliotheken“, klicken Sie auf „JARs hinzufügen“ oder „Externe JARs hinzufügen“, um Aspose.Cells.jar und dom4j_1.6.1.jar auszuwählen und hinzuzufügen in Baupfade.
 1. Anwendung schreiben, um APIs der Komponenten von Aspose aufzurufen.
 Oder Sie können es zur Laufzeit an der DOS-Eingabeaufforderung in Windows festlegen.

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **Erstellen einer Pivot-Tabelle**

So erstellen Sie eine Pivot-Tabelle mit Aspose.Cells:

1. Fügen Sie mithilfe der PutValue/setValue-Methode eines Cell-Objekts einige Daten zu Arbeitsblattzellen hinzu. Sie verwenden auch eine bereits mit Daten gefüllte Vorlagendatei. Die Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die add-Methode der PivotTables-Auflistung aufrufen (eingekapselt im Worksheet-Objekt).
1. Greifen Sie auf das neue PivotTable-Objekt aus der PivotTables-Auflistung zu, indem Sie seinen Index übergeben.
1. Verwenden Sie eines der im PivotTable-Objekt gekapselten PivotTable-Objekte, um die Tabelle zu verwalten.

Ein Codebeispiel ist unten angegeben. Das Ausführen des Codes generiert eine neue Datei: pivotTable_test.xls.

**Eingabedaten** 

![todo: Bild_alt_Text](create-pivot-tables-and-pivot-charts_1.png)

**Die Ausgabe-Pivot-Tabelle**

![todo: Bild_alt_Text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Erstellen eines Pivot-Diagramms basierend auf der Pivot-Tabelle**

So erstellen Sie ein Pivot-Diagramm mit Aspose.Cells:

1. Fügen Sie ein Diagramm hinzu.
1. Legen Sie die PivotSource des Diagramms fest, um auf eine vorhandene Pivot-Tabelle in der Tabelle zu verweisen.
1. Legen Sie andere Attribute fest.

Unten ist der Code, der von der Komponente verwendet wird, um die Aufgabe auszuführen. Das Ausführen des Codes generiert eine neue Datei: pivotChart_test.xls.

**Das Pivot-Chart-Blatt**

![todo: Bild_alt_Text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie Sie Pivot-Tabellen und Pivot-Diagramme mit Aspose.Cells erstellen. Hoffentlich hilft er Ihnen bei der Verwendung dieser Funktionen in Ihren eigenen Szenarien.

Aspose.Cells hat von jahrelanger Forschung, Design und sorgfältiger Abstimmung profitiert.

 Wir freuen uns über Ihre Fragen, Kommentare und Anregungen unter[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Wir garantieren eine zeitnahe Antwort.

{{% /alert %}}

## Zum Thema passende Artikel

- [Benutzerdefinierte Sortierung in der Pivot-Tabelle](/cells/de/java/custom-sorting-in-pivot-table/)
- [Pivot-Tabelle formatieren](/cells/de/java/formatting-pivot-table/)
- [Pivot-Tabelle mit berechneten Elementen aktualisieren und berechnen](/cells/de/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Pivot-Tabellen-Menübänder deaktivieren](/cells/de/java/disable-pivot-table-ribbons/)

