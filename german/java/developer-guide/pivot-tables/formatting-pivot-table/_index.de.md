---
title: Formatieren der Pivot Tabelle
type: docs
weight: 60
url: /de/java/formatting-pivot-table/
---

## **Aussehen der Pivot-Tabelle**

[Wie man eine Pivot-Tabelle erstellt](/cells/de/java/create-pivot-table/) zeigt, wie man eine einfache Pivot-Tabelle erstellt. Dieser Artikel geht weiter und erörtert, wie das Erscheinungsbild einer Pivot-Tabelle durch das Festlegen von Eigenschaften angepasst werden kann.

### **Einstellen der Pivot-Tabellenformatoptionen**

Die Klasse [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) ermöglicht das Einstellen verschiedener Formatierungsoptionen für eine Pivot-Tabelle.

#### **Einstellen der AutoFormat- und PivotTableStyle-Typen**

Das folgende Codebeispiel veranschaulicht, wie man den Autoformat-Typ und den Pivot-Tabellenstil-Typ unter Verwendung der Eigenschaften [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) und [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) festlegt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Einstellen von Formatoptionen**

Das folgende Codebeispiel zeigt, wie eine Reihe von Formatierungsoptionen für einen Pivot-Tabellenbericht eingestellt werden können, einschließlich dem Hinzufügen von Gesamtsummen für Zeilen und Spalten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Formatierungsoptionen für PivotFields einstellen**

Neben der Steuerung der Formatierung der Gesamtpivottabelle ermöglicht Aspose.Cells for Java eine feinabgestimmte Steuerung der Formatierung für Zeilenfelder, Spaltenfelder und Seitenelemente.

#### **Formatierung für Zeilen-, Spalten- und Seitenelemente einstellen**

Das folgende Codebeispiel zeigt, wie auf Zeilenfelder zugegriffen, eine bestimmte Zeile festgelegt, Teilergebnisse festgelegt, eine automatische Sortierung angewendet und die autoShow-Option verwendet werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Formatierungsoptionen für Datenfelder einstellen**

Die folgenden Codezeilen veranschaulichen, wie Datenfelder formatiert werden können.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Ein Schnellformat für eine Pivot-Tabelle bearbeiten**

Die folgenden Codebeispiele zeigen, wie das Schnellformat, das auf eine Pivot-Tabelle angewendet wird, geändert werden kann.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Löschen von Pivot-Feldern**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) hat eine Methode namens [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--), die die Pivot-Felder löscht. Verwenden Sie sie, um zum Beispiel Seiten-, Spalten-, Zeilen- oder Daten-Pivot-Felder zu löschen.
Das unten stehende Code-Beispiel zeigt, wie alle Pivot-Felder im Datenbereich gelöscht werden können.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Konsolidierungsfunktion**

### **Anwendung von ConsolidationFunction auf Datenfelder des Pivot-Tabellen**

Aspose.Cells kann verwendet werden, um die Konsolidierungsfunktion auf Datenfelder (oder Wertefelder) des Pivot-Tables anzuwenden. In Microsoft Excel können Sie mit der rechten Maustaste auf das Wertefeld klicken und dann die Option **Feldwerteinstellungen...** auswählen und dann den Tab **Werte zusammenfassen nach** wählen. Von dort aus können Sie eine beliebige Konsolidierungsfunktion Ihrer Wahl wie Summe, Anzahl, Durchschnitt, Max, Min, Produkt, Unterschiedliche Anzahl usw. auswählen.

Aspose.Cells bietet die Aufzählung [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction), um die folgenden Konsolidierungsfunktionen zu unterstützen.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT-NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT-COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

Der folgende Code wendet die Konsolidierungsfunktion **Durchschnitt** auf das erste Datenfeld (oder Wertfeld) und die Konsolidierungsfunktion **Unterschiedliche Anzahl** auf das zweite Datenfeld (oder Wertfeld) an.

{{% alert color="primary" %}}

Die Konsolidierungsfunktion DistinctCount wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
{{< app/cells/assistant language="java" >}}
